# Figma Image Fetcher

This Python script automates the extraction of image URLs from specified nodes within a Figma file, aiding designers and developers by providing programmable access to image assets.

## Features

- Fetches nodes using Figma API
- Extracts IDs and names starting with "FR_"
- Retrieves image URLs in PNG format
- Saves image URLs and metadata to JSON

## How to Use

1. **Environment Setup:** Ensure Python 3.x is installed.
2. **Dependencies:** Install `requests`:
3. **Script Configuration:** Replace placeholder values for `API_TOKEN`, `FILE_ID`, and `NODE_ID` with actual values.
4. **Execution:** Run the script:

## Security Note

Avoid hardcoding sensitive information like API tokens. Use environment variables or a configuration file instead.

# Figma画像取得ツール

このPythonスクリプトは、指定されたFigmaファイル内のノードから画像URLを自動的に抽出し、デザイナーや開発者がプログラムを通じて画像アセットにアクセスできるように支援します。

## 特徴

- Figma APIを使用してノードを取得
- "FR_"で始まるIDと名前を抽出
- PNG形式で画像URLを取得
- 画像URLとメタデータをJSONに保存

## 使い方

1. **環境設定:** Python 3.xがインストールされていることを確認してください。
2. **依存関係のインストール:** `requests`をインストールします
3. **スクリプトの設定:** `API_TOKEN`、`FILE_ID`、そして`NODE_ID`のプレースホルダーを実際の値に置き換えてください。
4. **実行:** スクリプトを実行します：
   
## セキュリティに関する注意

APIトークンのような機密情報をハードコードしないでください。環境変数または設定ファイルを代わりに使用してください。


