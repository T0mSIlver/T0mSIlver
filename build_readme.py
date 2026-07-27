#!/usr/bin/env python3
"""Rebuild the "Recently in other projects" section of README.md.

Pulls my recent public PRs and issues in repos I don't own from the GitHub
search API and rewrites the block between the marker comments. Run daily by
.github/workflows/update-readme.yml; run manually with `python3 build_readme.py`.

Deliberately unauthenticated: with no token, private repo titles can never
leak into this public README. Unauthenticated search allows 10 requests/min
and this makes one request a day.

Pattern from simonw/simonw (replace_chunk, Apache-2.0) and
nickcharlton/nickcharlton (search query shape).
"""

import json
import pathlib
import re
import urllib.parse
import urllib.request

USER = "T0mSIlver"
MAX_ITEMS = 8
MARKER = "recent_contributions"
# Issues search uses advanced syntax (GitHub default since 2025): multiple
# negative qualifiers AND together, so -user: excludes all my own repos.
QUERY = f"author:{USER} -user:{USER} is:public sort:updated-desc"


def fetch_items():
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": QUERY, "per_page": 30}
    )
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-profile-readme",
        },
    )
    with urllib.request.urlopen(request) as response:
        return json.load(response)["items"]


def label(item):
    if "pull_request" in item:
        if item["pull_request"].get("merged_at"):
            return "merged"
        return "open PR" if item["state"] == "open" else "closed PR"
    return f"{item['state']} issue"


def render(item):
    repo = item["repository_url"].split("/repos/")[-1]
    title = item["title"].replace("[", r"\[").replace("]", r"\]")
    return (
        f"- **{label(item)}** [{title}]({item['html_url']}) — "
        f"[{repo}](https://github.com/{repo})"
    )


def replace_chunk(content, marker, chunk):
    pattern = re.compile(
        rf"<!-- {marker} starts -->.*<!-- {marker} ends -->", re.DOTALL
    )
    replacement = f"<!-- {marker} starts -->\n{chunk}\n<!-- {marker} ends -->"
    if not pattern.search(content):
        raise SystemExit(f"marker {marker!r} not found in README.md")
    return pattern.sub(replacement, content)


def main():
    items = fetch_items()[:MAX_ITEMS]
    chunk = "\n".join(render(item) for item in items)
    readme = pathlib.Path(__file__).parent / "README.md"
    readme.write_text(replace_chunk(readme.read_text(), MARKER, chunk))
    print(f"wrote {len(items)} items")


if __name__ == "__main__":
    main()
