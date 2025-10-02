#各ファンクションへ処理を渡す
import ui                       #ui.pyの使用に必要
import re                       #文章単位ごとに区切るのに必要
import os                       #txtファイルの開閉に必要
import tkinter as tk            #tkinterの宣言
from tkinter import messagebox  #メッセージボックスの表示に必要
import config
import checker_function
import write_function

#------------------------------------------------------------------------------------------------
#各関数へ仕事を割り振るメイン処理
def function_main(text_data):
    str_sumcount=0                              #文章すべの文字数の合計を格納する変数
    all_error_count=0                           #全体のエラーのカウントする変数
    function_file_reset(config.document_file_path)     #document.txtの中身を初期化する関数へ
    sentences=function_list(text_data)          #文章をリスト化する関数へ
    filelistdata_count=len(config.filelistdata)
    
    for document_str in sentences:              #1文ごとにfor文を回す。
        str_count=0                             #1文の長さをカウントする変数
        str_length_error=0
        
        #文章をチェックする処理
        str_count=len(document_str)             #文字列の長さをカウントする
        str_sumcount+=str_count                 #取得した1文の長さを加算する

        #document.txtへの書き込み処理
        write_function.write_document(document_str,config.document_file_path)   #1文をdocument.txtに書き込む
        write_function.write_line(config.document_file_path)                    #1文ごとに区切る線を書く関数へ
        write_function.write_str_count(str_count,config.document_file_path)   #1文の文字数をdocument.txtに書き込む

        str_length_error=write_function.write_str_long(str_count,config.document_file_path)
        all_error_count+=str_length_error

        for i in range(filelistdata_count):
            dummylist=list()
            dummylist.clear()
            dummy_count,dummylist=checker_function.check_readcsv(document_str,config.filelistdata[i][0])
            write_function.write_csv_error(dummylist,config.filelistdata[i][1])
            all_error_count+=dummy_count

        write_function.write_line(config.document_file_path)                     #1文ごとに区切る線を書く関数へ
    messagebox. showinfo("infomation",f"読み込みが完了しました。\nエラー数{all_error_count} ")

#⚫︎document, txtファイルの中身を初期化する関数
def function_file_reset(filepath_a):
    with open(filepath_a,"a",encoding="utf-8") as txt_file:
        txt_file.truncate(0)

#⚫︎文章をリスト化する関数
def function_list(textdata):
    sentences=re.split (r"(?<=[。】＞])",textdata)              #[。】＞]で文章を区切る
    sentences=[s.strip() for s in sentences if s. strip()]     #空白を削除する
    return sentences
