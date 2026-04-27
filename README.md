# pyplayground
pythonでちょっとした実験をするための遊び場

## Experimentally using uv instead of conda

Add Package
```sh
uv add [package]
```
```sh
uv add --dev [package]
```

Sync Environment
```sh
uv sync
```

## Using .py instead of.ipynb
Pycharmは重いし, VSCode/CodiumはデザインがいけてないのでZedを使いたい．
1. 以下の2コマンドでJupyter Kernelをインストールする
    1. `uv add ipykernel` (追加済みであれば`uv sync`)
    1. `uv run python -m ipykernel install --user --name pyplayground --display-name "pyplayground"`
1. .pyファイルの中でbreakpointを作りたいときに`# %%`行を挿入