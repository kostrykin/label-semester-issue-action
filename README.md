# *[label-semester-issue-action](https://github.com/kostrykin/label-semester-issue-action)*

[![Assign semester labels to new issues](https://github.com/kostrykin/label-semester-issue-action/actions/workflows/example.yml/badge.svg)](https://github.com/kostrykin/label-semester-issue-action/actions/workflows/example.yml)

Assigns semester labels to newly created issues based on the date when the issue was opened (e.g., "WS 24/25").

> [!CAUTION]
> Right now only winter term labels are supported (i.e. "WS", not "SS").

In this repository, the action will be used for any issue labeled with `example` when created ([list of examples](https://github.com/kostrykin/label-semester-issue-action/issues?q%253Dis%253Aissue%252Bis%253Aclosed%252Blabel%253Aexample)).

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
   - uses: kostrykin/label-semester-issue-action@v1.0.0
   ```
   If you want you can configure the color of the labels:
   ```yml
     with:
       color: FF0000
   ```

For a full example, see the workflow file *.github/workflows/example.yml* and the *example/* directory.

**List of further examples:**
- https://github.com/BMCV/mobi-fs3-python
- https://github.com/BMCV/mobi-fs5-python
