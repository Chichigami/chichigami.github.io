# CI/CD

WIP

Automation of testing and deployment
`.github/workflow/ci.yml`

```
name: ci

on:
  pull_request:
    branches: [main]

jobs:
  tests:
    name: Tests
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: '1.23.0'

      - name: Echo Go version
        run: go version
```

Example of a ci.yml file
makes a environment based on input.
`code coverage = (lines_covered / total_lines) * 100`
How much code is covered via testing. If 100% code testing covered, doesn't mean there won't be bugged. If no code is covered, could be bugless.

Style
Aesthics of the code. Enforces whitespace, indentation, or line length
`go fmt ./...`

Linting
Analysis of the code. Detect functional issues. Provide warning or errors

```
brew install staticcheck
staticcheck ./...
```

staticcheck pretty meta for go lang

Security Check

```
go install github.com/securego/gosec/v2/cmd/gosec@latest
```

## CD.yml

```
name: cd

on:
  push:
    branches: [main]

jobs:
  tests:
    name: Deploy
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: "1.23.0"

      - name: Run build docker image
        run: ./scripts/buildprod.sh

```

Google Cloud Platform
Google Artifact Registry
