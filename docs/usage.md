# Usage

Run dice rolls using notation `XdY(+|-)Z`.

Examples:

- `pydice 1d6`
- `pydice 2d8+2`
- `pydice 3d4-1 --hist 1000`
- `pydice 4d10 --json`
- `pydice 5d12-3 --hist 500 --json`
- `pydice 100d6`  # large roll

Use `--json` to output result as JSON.

When `--hist` is specified, a PNG file named `hist.png` will be saved in the
current directory showing the distribution of generated totals.

## Advanced Notations

Вы можете использовать большие значения, например `20d100+50`, чтобы
смоделировать сложные броски в ролевых системах.
\nEnjoy rolling!
