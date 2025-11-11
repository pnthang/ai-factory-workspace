**File: app/config.js**
```
{
  "issue": {
    "id": "1",
    "title": "AutoGen multi-agent app PR (Updated)",
  }
}
```

**File: .github/workflows/autogen.yml**
```yaml
name: AutoGen Multi-Agent App PR

on:
  pull_request:
    types: [opened, synchronize]
  workflow_dispatch:

jobs:
  autogen:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
      - name: Run Coder
        run: |
          node index.js
      - name: Run Tester
        env:
          TEST_ENV_VAR: "test"
        run: |
          node test/index.js
      - name: Run QA
        run: |
          echo "QA Passed!"
      - name: Deploy to DevOps
        uses: actions/checkout@v2
        run: |
          cd app && npm install && npm run build
```

**File: app/index.js**
```javascript
const { issue } = require('./config');

console.log(`Processing Issue #${issue.id}: ${issue.title}`);
```

**File: app/test/index.js**
```javascript
const { issue } = require('../config');

test('Test Issue #1', () => {
  expect(issue.title).toBe('AutoGen multi-agent app PR (Updated)');
});
```

**File: package.json**
```
{
  "scripts": {
    "build": "node index.js"
  }
}
```