# *[label-semester-issue-action](https://github.com/kostrykin/label-semester-issue-action)*

[![Example](https://github.com/kostrykin/label-semester-issue-action/actions/workflows/label.yml/badge.svg)](https://github.com/kostrykin/label-semester-issue-action/actions/workflows/label.yml)

Assigns semester labels to newly created issues based on the date when the issue was opened (e.g., "WS 24/25").

---

**Steps required to set this action up for a repository:**

1. The workflow should be triggered by newly opened issues:
   ```yml
   on:
     issues:
       types: [opened]
   ```
2. Make sure the workflow job has the following permissions:
   ```yml
   permissions:
     issues: write
   ```
3. Add the action to the workflow:
   ```yml
   - uses: kostrykin/label-semester-issue-action@v1.0
   ```
   If you want you can configure the color of the labels:
   ```yml
     with:
       color: FF0000
   ```

For a full example, see the workflow file *.github/workflows/label.yml*.

**List of further examples:**
- https://github.com/BMCV/mobi-fs3-python
- https://github.com/BMCV/mobi-fs5-python
