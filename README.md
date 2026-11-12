# Open Bazaar contrib index

`index.json` lists official Bazaar plugins, including built-in and independently distributed plugins for Bazaar Compute Node.
BCN fetches a snapshot when building the manager and ships it as a second built-in index. Default node and server configurations subscribe to both that local snapshot and this online index.

Merge index updates before building the BCN release. The packaged
`resource://bazaar_contrib_manager/open_bazaar_index.json` must include the same
display content for users who cannot reach the online index.

## Add a plugin

Open a pull request adding an entry to `contribs`:

```json
{
  "package": "your-distribution",
  "source": "https://pypi.org/simple/",
  "summary": "A short introduction to the plugin",
  "description": "## About\n\nA Markdown description of the plugin.",
  "icon_url": "https://example.org/icons/your-plugin.svg"
}
```

Use the distribution name and the package-index URL from which it can be installed. Publish the distribution before adding its entry. Keep entries sorted by package name. Version requirements belong to package dependencies and node configuration.

The document follows the manager's public `IndexDocument` contract.

`package` and `source` are required. `summary`, `description` and `icon_url` are
optional strings supported by manager 0.3.0rc30 and later. Omit any unavailable
field; the corresponding display region is omitted. The index author maintains
these values.

For duplicate package/source entries, the last configured index supplies the
display fields, including omissions. All contributing index locations remain
visible in the catalog. This lets an online index replace its packaged snapshot,
and a user append their own display information.

Official plugin icons are maintained in [`icons/`](icons/) and served from
`https://bazaar-assets.yuchanns.xyz/icons/` by the `bazaar-assets` R2 bucket.
Other index authors can use any public image URL. Keep the artwork's required
attribution with the original files.

## Check changes

```sh
uv sync --locked
uv run --no-sync python scripts/check.py
```

CI uses Python 3.15 and the manager contract from the revision pinned in `pyproject.toml`. Its environment setup reuses the BCN setup action at a fixed commit.
