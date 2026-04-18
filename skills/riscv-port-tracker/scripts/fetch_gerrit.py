#!/usr/bin/env python3
"""
Fetch Gerrit commits for a specific owner and extract upstream port hashes.

Usage:
    python3 fetch_gerrit.py --owner mfarazma@ibm.com --n 10

Output: JSON array of commits with upstream_hash extracted from commit messages.
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.request

GERRIT_URL = "https://chromium-review.googlesource.com"


def fetch_commits(owner: str, n: int) -> list:
    """Fetch Gerrit commits for owner and return parsed data."""
    url = f"{GERRIT_URL}/changes/?q=owner:{owner}&n={n}&o=CURRENT_COMMIT&o=CURRENT_REVISION"
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8")
    
    # Skip Gerrit's anti-XSSI prefix ")]}'"
    if raw.startswith(")]}'"):
        raw = raw[4:]
    
    data = json.loads(raw)
    return data


def extract_upstream_hash(message: str) -> str | None:
    """Extract upstream commit hash from 'Port <hash>' line in commit message."""
    # Pattern: "Port <40-char hex hash>" or "Port commit <hash>"
    pattern = r"Port\s+(?:commit\s+)?([a-f0-9]{40})"
    match = re.search(pattern, message, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def extract_keyword_from_subject(subject: str) -> str:
    """Extract core keyword from subject for fallback search."""
    # Remove architecture prefix like "PPC:", "s390:", "PPC/s390:"
    cleaned = re.sub(r"^(PPC|s390|PPC/s390|Merged):\s*", "", subject)
    # Remove "[xxx]" tags
    cleaned = re.sub(r"\[[^\]]+\]\s*", "", cleaned)
    # Remove "Reland" prefix
    cleaned = re.sub(r"^Reland\s+\"[^\"]+\"\s*", "", cleaned)
    cleaned = re.sub(r"^Reland\s+", "", cleaned)
    return cleaned.strip()


def parse_commits(commits: list) -> list:
    """Parse commits and extract relevant info."""
    result = []
    for c in commits:
        # Skip ABANDONED and NEW commits
        status = c.get("status", "")
        if status not in ("MERGED",):
            continue
        
        # Get commit message
        current_rev = c.get("current_revision", "")
        revisions = c.get("revisions", {})
        commit = {}
        if current_rev and current_rev in revisions:
            commit = revisions[current_rev].get("commit", {})
        elif revisions:
            commit = list(revisions.values())[0].get("commit", {})
        
        message = commit.get("message", "")
        subject = c.get("subject", "")
        
        upstream_hash = extract_upstream_hash(message)
        keyword = extract_keyword_from_subject(subject)
        
        result.append({
            "subject": subject,
            "status": status,
            "upstream_hash": upstream_hash,
            "keyword": keyword,
            "change_number": c.get("_number"),
            "project": c.get("project"),
            "updated": c.get("updated"),
            "message": message,
        })
    
    return result


def main():
    parser = argparse.ArgumentParser(description="Fetch Gerrit commits and extract port hashes")
    parser.add_argument("--owner", default="mfarazma@ibm.com", help="Owner email to query")
    parser.add_argument("--n", type=int, default=5, help="Number of commits to fetch")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of formatted")
    args = parser.parse_args()
    
    commits = fetch_commits(args.owner, args.n)
    parsed = parse_commits(commits)
    
    if args.json:
        print(json.dumps(parsed, indent=2))
    else:
        for i, c in enumerate(parsed, 1):
            print(f"[{i}] {c['subject']}")
            print(f"    Status: {c['status']} | Updated: {c['updated'][:10]}")
            if c['upstream_hash']:
                print(f"    Upstream: {c['upstream_hash'][:12]}...")
            else:
                print(f"    Upstream: N/A (keyword: {c['keyword'][:40]}...")
            print()


if __name__ == "__main__":
    main()