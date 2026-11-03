# Repository validation

Branch pushes (excluding tags) and pull requests to `main` validate the repository instruction contract and dated changelog. The workflow also rejects five in-memory policy copies with one required rule removed from each, plus three copies hidden inside comments or code fences.

The inline check in [.github/workflows/policy.yml](.github/workflows/policy.yml) uses only the Python 3.12 standard library. To run it locally, execute its Python step from the repository root with `GITHUB_REPOSITORY=obiedeh/obiedeh`. No packages or services are required.
