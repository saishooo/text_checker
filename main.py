import ui                       #ui.pyの使用に必要
import re                       #文章単位ごとに区切るのに必要
import os                       #txtファイルの開閉に必要
import tkinter as tk            #tkinterの宣言
from tkinter import messagebox  #メッセージボックスの表示に必要
import csv                      #CSVファイルを扱えるようにするために必要

#グローバル変数
#ファイルパス
document_file_path=r"document.txt"
senmonyougo_file_path=r"senmonyougo_check.csv"
setsuzokusi_file_path=r"setsuzokusi_check.csv"

#指摘内容を保管するグローバル変数
senmonyougo_checklist_log=list()
setsuzokusi_checklist_log=list()

#listに入っている変数の中身を参照するよ！
filelistdata=[
    [senmonyougo_file_path, senmonyougo_checklist_log, "●E-3：専門用語が書かれています"],
    [setsuzokusi_file_path, setsuzokusi_checklist_log, "●E-2：接続詞が誤っています"]
]

#------------------------------------------------------------------------------------------------
#各関数へ仕事を割り振るメイン処理
def function_main(text_data):
    global str_count
    global filelistdata
    sumcount_a=0                                #文章すべの文字数の合計を格納する変数
    all_error_count=0                           #全体のエラーのカウントする変数
    function_file_reset(document_file_path)     #document.txtの中身を初期化する関数へ
    sentences=function_list(text_data)          #文章をリスト化する関数へ
    
    for document_str in sentences:              #1文ごとにfor文を回す。
        str_count=0                             #1文の長さをカウントする変数
        senmonyougo_count=0                     #専門用語がないかカウントする
        setsuzokusi_count=0                     #接続詞の誤りをカウントする変数
        str_length_error=0
        
        global senmonyougo_checklist_log
        global setsuzokusi_checklist_log

        senmonyougo_checklist_log.clear()
        setsuzokusi_checklist_log.clear()

        #文章をチェックする処理
        str_count=check_str_count(document_str)             #文字列の長さをカウントする
        sumcount_a+=str_count                               #取得した1文の長さを加算する

        #document.txtへの書き込み処理
        write_document(document_str,document_file_path)   #1文をdocument.txtに書き込む
        write_line(document_file_path)                    #1文ごとに区切る線を書く関数へ
        write_str_count(str_count,document_file_path)   #1文の文字数をdocument.txtに書き込む

        str_length_error=write_str_long(str_count,document_file_path)
        all_error_count+=str_length_error

        senmonyougo_count,senmonyougo_checklist_log=check_readcsv(document_str,filelistdata[0][0])     #専門用語がないか確認する
        setsuzokusi_count,setsuzokusi_checklist_log=check_readcsv(document_str,filelistdata[1][0])     #接続詞に誤りがないかカウントする
       
        write_csv_error(senmonyougo_checklist_log,filelistdata[0][2])
        write_csv_error(setsuzokusi_checklist_log,filelistdata[1][2])
        all_error_count+=(senmonyougo_count+setsuzokusi_count)

        write_line(document_file_path)                     #1文ごとに区切る線を書く関数へ
    messagebox. showinfo("infomation",f"読み込みが完了しました。\nエラー数{all_error_count} ")

#-------------------------------function-----------------------------------------------------------------
#⚫︎document, txtファイルの中身を初期化する関数
def function_file_reset(filepath_a):
    with open(filepath_a,"a",encoding="utf-8") as txt_file:
        txt_file.truncate(0)

#⚫︎文章をリスト化する関数
def function_list(textdata):
    sentences=re.split (r"(?<=[。】＞])",textdata)              #[。】＞]で文章を区切る
    sentences=[s.strip() for s in sentences if s. strip()]     #空白を削除する
    return sentences

#⚫︎1文の文字数をカウントする関数
def check_str_count(document_a):
    Str_count=0                 #一文の長さをカウントする変数
    Str_count=len(document_a)   #document_aの長さを取得する
    return Str_count

#⚫︎csvファイルでチェックしたものをカウントする関数
def check_readcsv(document_a,filepath):
    check_count=0

    checked_list_log=list()
    checked_list_log.clear()

    file_path=filepath
    
    with open(file_path,"r",encoding="utf-8") as csv_file:
        data_read=csv.reader(csv_file)
        rows=list(data_read)
        rows_count=len(rows[0])
        for count in range(rows_count):
            checklist=str(rows[0][count])
            if checklist in document_a:
                checked_list_log.append(checklist)
                check_count+=1

    return check_count, checked_list_log

#⚫︎1文をdocument.txtファイルに書き込む関数
def write_document(document_a,filepath_a):
    with open(filepath_a,"a",encoding="utf-8") as file:
        file.write(f"{document_a}\n")

#⚫︎1文の文字数をdocument.txtファイルに書き込む
def write_str_count(count,filepath_a):
    with open(filepath_a,"a",encoding="utf-8") as file:
        file.write(f"{count}文字\n")

#⚫︎csvに関する警告文をdocument.txtファイルに書き込む関数
def write_csv_error(csv_checkeddata,error_str):
    global document_file_path

    if not csv_checkeddata:
        return 

    with open(document_file_path,"a",encoding="utf-8") as file:
        file.write(f"{str(error_str)}\n")
        log_error_count=len(csv_checkeddata)
        for count in range(log_error_count):
            file.write(f"・{csv_checkeddata[count]}\n")

#一文の長さの警告を出す関数
def write_str_long(length,filepath):
    count=0
    if length>=120:
        with open (filepath,"a",encoding="utf-8") as file:
            file.write("●E-1：一文が120字以上です\n")
            count+=1
            return count
    else:
        return count

#⚫︎ラインをdocument.txtファイルに書き込む関数
def write_line(filepath_a): 
    with open(filepath_a,"a",encoding="utf-8") as file:
        file.write("-------------------------------------------------\n")