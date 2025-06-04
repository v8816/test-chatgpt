# PyDice

![Build](https://github.com/example/pydice/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-green.svg)

Command line dice roller.

See [GIF screencast](https://example.com/pydice.gif).

## Installation

```bash
poetry install
```

Alternatively install from PyPI:

```bash
pip install pydice
```

## Usage

```bash
pydice 2d6+1
pydice 1d20 --hist 1000 --json
pydice 4d10 --json
pydice 3d6 --hist 200
```

Detailed usage in [docs/usage.md](docs/usage.md).
More history in [docs/extra.md](docs/extra.md).
Changelog: [docs/changelog.md](docs/changelog.md).
API reference in [docs/api_reference.md](docs/api_reference.md).
FAQ: [docs/faq.md](docs/faq.md).
Acknowledgements in [docs/acknowledgements.md](docs/acknowledgements.md).

## Contributing

Pull requests are welcome. Run `poetry run coverage run -m pytest` before
submitting.
\nHappy rolling!
