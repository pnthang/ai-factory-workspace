
- In the example usage, add a check to ensure that the `get_commits` function returns a non-empty list.

## Updated Test Cases:

**tests/pull_request_test.py:**

- Update the test case to handle the case where the `get_commits` function returns an empty list.

**tests/main_test.py:**

- Update the test case to check the length of the `commits` list before calling the `create_pull_request` function.

## Expected Results:

After these changes, the tests should pass without any errors.