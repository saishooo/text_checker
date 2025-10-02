# config.py
# グローバル変数置き場

#ファイルパス
document_file_path=r"document.txt"
senmonyougo_file_path=r"csv_file/senmonyougo_check.csv"
setsuzokusi_file_path=r"csv_file/setsuzokusi_check.csv"
ranukikotoba_file_path=r"csv_file/ranukikotoba_check.csv"
gojikatakana_file_path=r"csv_file/gojikatakana_check.csv"

#listに入っている変数の中身を参照するよ！
#   [     ファイルパス名,           エラーメッセージ        ]
filelistdata=[
    [senmonyougo_file_path,  "●wraning-2：専門用語が書かれています"],
    [setsuzokusi_file_path,  "●error-2  ：接続詞が誤っています"],
    [ranukikotoba_file_path, "●error-3  ：ら抜き言葉があります"],
    [gojikatakana_file_path, "●error-4  ：誤ったカタカナがあります"]
]