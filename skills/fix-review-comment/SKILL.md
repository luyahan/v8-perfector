---
name: fix-review-comment
description: Guide for addressing upstream Gerrit review comments. This skill should be used when the user wants to fix code review feedback, address reviewer comments, or respond to upstream PR/CL feedback. Triggers for requests like "fix review comment", "address reviewer feedback", "回应 reviewer 的 comment", or "修复上游 review".
---

# Fix Review Comment

This skill guides the process of addressing upstream Gerrit review comments with a structured, efficient approach.

## Purpose

Ensure review comments are addressed correctly by:
1. Fetching and understanding comments in context
2. Familiarizing with the overall change first
3. Making targeted fixes with confidence tracking

## When to Use

Use this skill when:
- Addressing Gerrit review comments from upstream reviewers
- Fixing code changes requested during PR/CL review
- Responding to style or formatting feedback

## Workflow

### Step 1: Fetch Comments

Retrieve unresolved comments in JSON format for easier parsing:

```bash
git cl comments --unresolved -j -
```

- If there are no comments, stop here and inform the user
- Focus only on the "comments" array in the output
- Tell the user how many comments were found

### Step 2: Familiarize with the Change

Before addressing individual comments, understand the overall change:

```bash
git diff --merge-base origin/main HEAD
```

This provides context for understanding:
- The scope and intent of the change
- Related code that might be affected
- Patterns and conventions already established in the change

### Step 3: Process Comments

Go through comment entries one by one. For each comment:

1. **Locate the relevant code** - Open the affected files
2. **Examine surrounding context** - Look at nearby code for patterns and dependencies
3. **Determine confidence level**:
   - If confident in how to address it: make the change
   - If not confident: skip and note the comment content for later review

### Step 4: Verify

Run the build to ensure correctness:

```bash
# For V8: use gm.py
tools/dev/gm.py quiet x64.optdebug

# For Chromium: use autoninja
autoninja -C out/Default
```

### Step 5: Format

Apply code formatting before finalizing:

```bash
git cl format
```

### Step 6: Summary

Report back to the user:

1. How many changes were made
2. Content of any comments that were not addressed (require user input)
3. Suggest next steps if applicable

## Best Practices

- **Context first** - Always run git diff to understand the overall change before fixing individual comments
- **Confidence-based** - Only make changes you're confident about; escalate uncertain ones
- **One comment at a time** - Process sequentially to avoid confusion
- **Build before format** - Verify correctness first, then apply style
- **Track unaddressed** - Keep a list of comments that need user guidance

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

### Uncertain Cases

If you're not confident about a comment:
- Skip making the change
- Note the comment content
- Present it to the user for guidance
- Consider asking clarifying questions

## Resources

### references/

- `fix-plan-template.md` - Template for documenting complex fixes (optional, use when needed)
