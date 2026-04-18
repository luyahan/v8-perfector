---
name: riscv-port-tracker
description: Track PPC/s390 upstream ports and check RISC-V port status. This skill should be used when checking if commits from other architectures (PPC/s390) have been ported to RISC-V. Triggers for requests like "check RISC-V port status", "track upstream ports", "查看 RISC-V port 情况", or "检查 mfarazma@ibm.com 的提交".
---

# RISC-V Port Tracker

Track upstream commits from PPC/s390 and check if they have been ported to RISC-V.

## Purpose

Help identify which upstream PPC/s390 commits need to be ported to RISC-V by:
1. Fetching recent Gerrit commits from IBM contributors
2. Extracting upstream commit hashes from port commit messages
3. Checking RISC-V git history for corresponding ports

## When to Use

Use this skill when:
- Checking if PPC/s390 upstream ports have been applied to RISC-V
- Tracking port status of commits from specific contributors
- Identifying commits that need RISC-V porting

## Workflow

### Step 1: Update Local Repository

Always fetch latest changes before checking:

```bash
cd ~/v8/v8 && git fetch origin
```

### Step 2: Fetch Gerrit Commits

Use the script to get recent commits:

```bash
python3 <skill_path>/scripts/fetch_gerrit.py --owner mfarazma@ibm.com --n 5 --json
```

The script outputs JSON with:
- `subject`: Commit title
- `status`: MERGED/ABANDONED
- `upstream_hash`: Hash extracted from `Port <hash>` line
- `keyword`: Fallback search term from subject
- `change_number`: Gerrit change number

### Step 3: Check RISC-V Port Status

For each commit with an upstream hash, search RISC-V history:

```bash
git log origin/main --oneline --grep="<upstream_hash>" -- "*riscv*"
```

If hash search yields nothing, try keyword search:

```bash
git log origin/main --oneline --grep="<keyword>" -- "*riscv*"
```

### Step 4: Output Analysis

Report findings in two categories:

**Already Ported:**
| Subject | Upstream Hash | RISC-V Commit | Files Changed |
|---------|---------------|---------------|---------------|
| ... | abc123... | def456... | src/.../riscv/... |

**Not Yet Ported:**
| Subject | Upstream Hash | Gerrit Link | Suggested Action |
|---------|---------------|-------------|------------------|
| ... | abc123... | https://chromium-review.../c/<number> | Port needed |

## Commit Message Patterns

### PPC/s390 Port Format

```
PPC/s390: [component] Description

Port <40-char-upstream-hash>

Original Commit Message:
    ...
```

### RISC-V Port Format

```
[riscv][component] Description

Port commit <40-char-upstream-hash>
```

**Key difference:** RISC-V uses `[riscv]` prefix and `Port commit` format.

## Special Cases and Insights

### Bidirectional Port Flow

Not all "Port" commits flow from x64/ARM to other architectures. Some features are authored by RISC-V contributors first, then ported to PPC/s390:

**Examples:**
- CPU detection refactor (`89ad1535`) — RISC-V authored, ported to PPC/s390
- Liftoff FP/SIMD separation (`bbdf6953`) — RISC-V authored, ported to PPC/s390

This indicates RISC-V port maturity. When PPC/s390 ports a hash, check if RISC-V is already **upstream author** rather than needing to port.

**Detection:**
```bash
# Check if RISC-V is the original author
git log --oneline <upstream_hash>^..<upstream_hash> --format="%an %ae"
```

### Multi-Hash Port Pattern

RISC-V committers sometimes batch multiple upstream ports into a single commit, while PPC/s390 typically ports one hash per commit.

**Example:**
- `023bbe3a249` ports both wasmfx trap (`68126fa4`) and arg_buffer preserve (`96be7867`)

**Detection:**
```bash
# A single RISC-V commit may match multiple upstream hashes
git log origin/main --grep="<hash1>" --grep="<hash2>" --all-match -- "*riscv*"
```

When a PPC/s390 port appears "not ported", check if it was batched with other ports in a RISC-V commit.

### Revert and Reland Cycles

Some RISC-V ports go through revert cycles before final landing. Track these for quality assurance.

**Example:**
- Superspread: first committed (`95cc42e5cef`), then reverted (`3458733472d`), then relanded (`00c7579b537`)

**Detection:**
```bash
# Check for reverts related to a feature
git log origin/main --oneline --grep="Revert" --grep="<keyword>" --all-match
```

When analyzing port status, report if a feature was previously reverted and relanded.

## Quick Reference

### Search Commands

```bash
# Search by upstream hash
git log origin/main --oneline --grep="<hash>" -- "*riscv*"

# Search by keyword
git log origin/main --oneline --grep="<keyword>" -- "*riscv*"

# Check if hash exists anywhere
git log --oneline --all --grep="<hash>"
```

### Gerrit Review Links

```
https://chromium-review.googlesource.com/c/v8/v8/+/<change_number>
```

## Resources

### scripts/

- `fetch_gerrit.py` - Fetch and parse Gerrit commits from chromium-review.googlesource.com