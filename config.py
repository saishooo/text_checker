# config.py
# グローバル変数置き場

#ファイルパス
document_file_path=r"document.txt"
senmonyougo_file_path=r"csv_file/senmonyougo_check.csv"
setsuzokusi_file_path=r"csv_file/setsuzokusi_check.csv"

#listに入っている変数の中身を参照するよ！
#   [     ファイルパス名,           エラーメッセージ        ]
filelistdata=[
    [senmonyougo_file_path, "●E-3：専門用語が書かれています"],
    [setsuzokusi_file_path, "●E-2：接続詞が誤っています"]
]