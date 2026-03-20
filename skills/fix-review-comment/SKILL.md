---
name: fix-review-comment
description: Guide for addressing upstream Gerrit review comments. This skill should be used when the user wants to fix code review feedback, address reviewer comments, or respond to upstream PR/CL feedback. Triggers for requests like "fix review comment", "address reviewer feedback", "回应 reviewer 的 comment", or "修复上游 review".
---

# Fix Review Comment

This skill guides the process of addressing upstream Gerrit review comments with a structured, plan-first approach.

## Purpose

Ensure review comments are addressed correctly by:
1. Understanding the comment in full context
2. Planning the fix before making changes
3. Verifying correctness before submitting

## When to Use

Use this skill when:
- Addressing Gerrit review comments from upstream reviewers
- Fixing code changes requested during PR/CL review
- Responding to style or formatting feedback

## Workflow

### Step 1: Fetch Comments

Retrieve the review comments using Gerrit's command:

```bash
git cl comments
```

This displays all unresolved comments on the current CL.

### Step 2: Understand Context

Before planning a fix:

1. **Read the comment carefully** - Understand what the reviewer is asking for
2. **Locate the relevant code** - Open the affected files
3. **Examine surrounding context** - Look at nearby code for patterns, conventions, and dependencies
4. **Consider the broader impact** - Will this change affect other files or tests?

### Step 3: Create Fix Plan

Write a summary to `fix-plan.md` in the repository root. Use the template from `references/fix-plan-template.md`:

The plan should include:
- **Comment content** - What the reviewer said
- **Proposed fix** - The approach and specific changes
- **Rationale** - Why this fix addresses the comment correctly

### Step 4: Review the Plan

Before implementing:

1. Read through `fix-plan.md` completely
2. Verify the approach aligns with surrounding code conventions
3. Ensure the fix addresses the root cause, not just symptoms
4. Check if tests need updating

### Step 5: Implement the Fix

Make the code changes directly based on the approved plan.

### Step 6: Verify

Run the build to ensure correctness:

```bash
# For V8: use gm.py
tools/dev/gm.py quiet x64.optdebug

# Or run specific tests if needed
tools/run-tests.py --progress dots --outdir=out/x64.optdebug
```

### Step 7: Format

Apply code formatting before committing:

```bash
git cl format
```

### Step 8: Cleanup

Discard the temporary plan file:

```bash
rm fix-plan.md
```

## Best Practices

- **One comment at a time** - Focus on a single comment to avoid confusion
- **Context matters** - Always look at surrounding code before planning
- **Plan before code** - Writing the plan catches issues early
- **Build before format** - Verify correctness first, then apply style

## Common Patterns

### Style/Formatting Comments

- Run `git cl format` first to see if it resolves the issue
- Check surrounding code for consistent patterns
- Review the style guide if unsure

### Refactoring Suggestions

- Understand the reviewer's intent, not just the literal request
- Consider if similar changes should be made elsewhere
- Ensure the refactoring doesn't break existing tests

### Bug Fix Requests

- Identify the root cause, not just the symptom
- Add or update tests to prevent regression
- Document any non-obvious decisions in the plan

## Resources

### references/

- `fix-plan-template.md` - Template for structuring the fix plan document
