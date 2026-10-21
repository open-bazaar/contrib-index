# Open Bazaar contrib index

`index.json` lists independently distributed Open Bazaar plugins for Bazaar Compute Node.
BCN takes a snapshot at release preparation, records its Git commit and SHA-256, and ships it as a second built-in index. Installed nodes read that packaged snapshot locally.

## Add a plugin

Open a pull request adding an entry to `contribs`:

```json
{
  "package": "your-distribution",
  "source": "https://pypi.org/simple/",
  "version": ">=0.3,<0.4"
}
```

Use the distribution name, the package-index URL from which it can be installed, and an optional PEP 440 version specifier. Publish the distribution before adding its entry. Keep entries sorted by package name.

The document follows the manager's public `IndexDocument` contract. The initial index is empty while the independent Open Bazaar plugins prepare their first distributions.

## Check changes

```sh
uv sync --locked
uv run --no-sync python scripts/check.py
```

CI uses Python 3.15 and the published manager contract. Its environment setup reuses the BCN setup action at a fixed commit.
