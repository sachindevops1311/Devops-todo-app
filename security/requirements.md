# Security Requirements

## REQ-01: Secret management
No credentials, API keys, or tokens shall be committed to the repository.
A .gitignore file must be present covering .env, *.key, *.pem files.

## REQ-02: Branch protection
Direct pushes to main shall be disabled.
All changes must go through a pull request with at least one reviewer.

## REQ-03: CI/CD security gates
All pull requests must pass automated security checks before merging.
Checks shall include: secret scanning, dependency audit, and static analysis.

## REQ-04: Dependency management
All dependencies must be declared in a manifest file (package.json or equivalent).
A lockfile must be present and committed to pin dependency versions.

## REQ-05: Container security
If a Dockerfile is introduced, it must use a non-root user and a current base image.
Images must be scanned with Trivy before deployment.

