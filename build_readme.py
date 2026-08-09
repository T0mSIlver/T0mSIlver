#!/usr/bin/env python3
"""Rebuild the "Recently in other projects" section of README.md.

Pulls my recent public PRs, issues and discussions in repos I don't own and
rewrites the block between the marker comments. Run daily by
.github/workflows/update-readme.yml; run manually with
`GITHUB_TOKEN=$(gh auth token) python3 build_readme.py`.

Two APIs, because they don't overlap: REST /search/issues covers PRs and
issues and needs no token, while discussions exist only in GraphQL, which
always requires one. Some upstreams (starlette, for one) route bug reports to
Discussions instead of Issues, so leaving them out drops real contributions.

`is:public` on both queries is what keeps private repo titles out of this
public README, and it is the only layer that holds everywhere: a manual run
authenticates with a personal token that can read every private repo I own.
CI adds a second layer that covers CI alone -- GITHUB_TOKEN is an
installation token scoped to this repo and cannot read my private repos in
the first place -- so don't drop `is:public` on the assumption that the
token scoping has it covered.

An unset GITHUB_TOKEN is the local-run case and simply skips discussions. A
token that is set but fails is a real error, and in CI one is always set, so
it aborts loudly rather than committing a README with the discussions
silently dropped.

Pattern from simonw/simonw (replace_chunk, Apache-2.0) and
nickcharlton/nickcharlton (search query shape). State icons in icons/ are
Octicons (primer/octicons, MIT) recolored with Primer's state colors; the
media query inside each SVG handles dark mode.
"""

import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

USER = "T0mSIlver"
MAX_ITEMS = 8
MARKER = "recent_contributions"
# Issues search uses advanced syntax (GitHub default since 2025): multiple
# negative qualifiers AND together, so -user: excludes all my own repos.
# GraphQL discussion search accepts the same qualifiers unchanged.
QUERY = f"author:{USER} -user:{USER} is:public sort:updated-desc"

DISCUSSION_QUERY = """
query($q: String!) {
  search(query: $q, type: DISCUSSION, first: 30) {
    nodes {
      ... on Discussion {
        title
        url
        updatedAt
        isAnswered
        repository { nameWithOwner }
      }
    }
  }
}
"""


def get_json(url, data=None, headers=None):
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-profile-readme",
            **(headers or {}),
        },
    )
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def fetch_issues():
    """Recent public PRs and issues, via the unauthenticated REST search API."""
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": QUERY, "per_page": 30}
    )
    return get_json(url)["items"]


def fetch_discussions():
    """Recent public discussions, via GraphQL. Empty list if unauthenticated."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN unset: skipping discussions", file=sys.stderr)
        return []
    body = json.dumps({"query": DISCUSSION_QUERY, "variables": {"q": QUERY}})
    try:
        payload = get_json(
            "https://api.github.com/graphql",
            data=body.encode(),
            headers={"Authorization": f"Bearer {token}"},
        )
    # ValueError covers json.JSONDecodeError: a 200 whose body isn't JSON.
    except (urllib.error.URLError, ValueError) as error:
        raise SystemExit(f"discussion search failed: {error}")
    if payload.get("errors"):
        raise SystemExit(f"discussion search failed: {payload['errors']}")
    return payload["data"]["search"]["nodes"]


def issue_icon(item):
    """Icon name in icons/ (recolored Octicons) and its alt text."""
    if "pull_request" in item:
        if item["pull_request"].get("merged_at"):
            return "pr_merged", "Merged pull request"
        if item.get("draft"):
            return "pr_draft", "Draft pull request"
        if item["state"] == "open":
            return "pr_open", "Open pull request"
        return "pr_closed", "Closed pull request"
    if item["state"] == "open":
        return "issue_open", "Open issue"
    return "issue_closed", "Closed issue"


def from_issue(item):
    return {
        "updated": item["updated_at"],
        "title": item["title"],
        "url": item["html_url"],
        "repo": item["repository_url"].split("/repos/")[-1],
        "icon": issue_icon(item),
    }


def from_discussion(node):
    return {
        "updated": node["updatedAt"],
        "title": node["title"],
        "url": node["url"],
        "repo": node["repository"]["nameWithOwner"],
        "icon": ("discussion_answered", "Answered discussion")
        if node["isAnswered"]
        else ("discussion", "Discussion"),
    }


def render(entry):
    title = entry["title"].replace("[", r"\[").replace("]", r"\]")
    name, alt = entry["icon"]
    return f"- ![{alt}](icons/{name}.svg) [{title}]({entry['url']}) `{entry['repo']}`"


def replace_chunk(content, marker, chunk):
    pattern = re.compile(
        rf"<!-- {marker} starts -->.*<!-- {marker} ends -->", re.DOTALL
    )
    replacement = f"<!-- {marker} starts -->\n{chunk}\n<!-- {marker} ends -->"
    if not pattern.search(content):
        raise SystemExit(f"marker {marker!r} not found in README.md")
    return pattern.sub(replacement, content)


def main():
    entries = [from_issue(item) for item in fetch_issues()]
    entries += [from_discussion(node) for node in fetch_discussions()]
    # Both APIs return ISO-8601 UTC timestamps, which sort lexicographically.
    entries.sort(key=lambda entry: entry["updated"], reverse=True)
    entries = entries[:MAX_ITEMS]
    chunk = "\n".join(render(entry) for entry in entries)
    readme = pathlib.Path(__file__).parent / "README.md"
    readme.write_text(replace_chunk(readme.read_text(), MARKER, chunk))
    print(f"wrote {len(entries)} items")


if __name__ == "__main__":
    main()
