# Dev environment
You can check [Makefile]() to see the basic flow to dev at local

# Release Process

To publish a new version to PyPI:

1. Update the version in `pyproject.toml`
2. Commit the version change
3. Create and push a git tag starting with `v`:
   ```bash
   git tag v0.1.4
   git push origin v0.1.4
   ```
4. The GitHub Actions workflow will automatically build and publish to PyPI

Note: The workflow uses PyPI's trusted publishing (OIDC) for secure authentication. Make sure the PyPI project is configured to accept trusted publishing from this GitHub repository.

# 