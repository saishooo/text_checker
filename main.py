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

#------------------------------------------------------------------------------------------------
#各関数へ仕事を割り振るメイン処理
def function_main(text_data):
    sumcount_a=0                                #文章すべの文字数の合計を格納する変数
    all_error_count=0                           #全体のエラーのカウントする変数
    function_file_reset(document_file_path)     #document.txtの中身を初期化する関数へ
    sentences=function_list(text_data)          #文章をリスト化する関数へ
    
    for document_str in sentences:              #1文ごとにfor文を回す。
        str_count=0                             #1文の長さをカウントする変数
        setsuzoku_count=0                       #接続詞の誤りをカウントする変数
        senmonyougo_count=0                     #専門用語がないかカウントする

        #文章をチェックする処理
        str_count=check_str_count(document_str)             #文字列の長さをカウントする
        sumcount_a+=str_count                               #取得した1文の長さを加算する
        #setsuzoku_count=check_setsuzokusi(document_str)     #接続詞に誤りがないかカウントする

        setsuzoku_count=check_readcsv(document_str,1)
        senmonyougo_count=check_readcsv(document_str,2)
        #senmonyougo_count=check_senmonyougo(document_str)   #専門用語がないか確認する
        
        #document.txtへの書き込み処理
        write_document(document_str,document_file_path)   #1文をdocument.txtに書き込む
        write_line(document_file_path)                    #1文ごとに区切る線を書く関数へ
        write_str_count(str_count,document_file_path)     #1文の文字数をdocument.txtに書き込む

        #警告文の種類を判別する処理
        if str_count>=120:
            caveat=1        #警告文の種類を判別する変数 1=1文の長さに関するエラー
            write_caveat(caveat,document_file_path)
            all_error_count+=1
        if setsuzoku_count!=0:
            caveat=2       #告文の種類を判別する変数 2=誤った接続詞に関するエラー
            write_caveat(caveat,document_file_path)
            all_error_count+=setsuzoku_count
        if senmonyougo_count!=0:
            caveat=3        #告文の種類を判別する変数 3=専門用語を指摘する
            write_caveat(caveat,document_file_path)
            all_error_count+=senmonyougo_count
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

def check_readcsv(document_a,pattern):
    check_count=0
    global setsuzokusi_checklist_log
    global senmonyougo_checklist_log

    setsuzokusi_checklist_log.clear()
    senmonyougo_checklist_log.clear()

    checked_list_log=list()
    checked_list_log.clear()

    if pattern==1:
        file_path=setsuzokusi_file_path
    elif pattern==2:
        file_path=senmonyougo_file_path
    
    with open(file_path,"r",encoding="utf-8") as csv_file:
        data_read=csv.reader(csv_file)
        rows=list(data_read)
        rows_count=len(rows[0])
        for count in range(rows_count):
            checklist=str(rows[0][count])
            if checklist in document_a:
                checked_list_log.append(checklist)
                check_count+=1

    if pattern==1:
        setsuzokusi_checklist_log=checked_list_log
    elif pattern==2:
        senmonyougo_checklist_log=checked_list_log
    
    return check_count
"""
#⚫︎専門用語をカウントする関数
def check_senmonyougo(document_a):
    check_count=0               #専門用語の数をカウントする変数
    senmonyougo_checklist_log.clear()

    with open(senmonyougo_file_path,"r",encoding="utf-8") as csv_file:
        senmonyougo_data_read=csv.reader(csv_file)
        senmonyougo_rows=list(senmonyougo_data_read)
        senmonyougo_rows_count=len(senmonyougo_rows[0])

        for count in range (senmonyougo_rows_count):        #csvファイルに書かれている要素数だけ実行する
            senmonyougo_checklist=str(senmonyougo_rows[0][count])
            if senmonyougo_checklist in document_a:
                senmonyougo_checklist_log.append(senmonyougo_checklist)
                check_count+=1
    return check_count

#⚫︎1文の接続詞の誤りをカウントする関数
def check_setsuzokusi(document_a):
    check_count=0               #誤った接続詞をカウントする変数
    setsuzokusi_checklist_log.clear()

    with open(setsuzokusi_file_path,"r",encoding="utf-8") as csv_file:
        setsuzoku_data_read=csv.reader(csv_file)
        setsuzoku_rows=list(setsuzoku_data_read)        #csvファイルのデータをsetsuzoku_datareadに格納する
        setsuzoku_rows_count=len(setsuzoku_rows[0])     #setsuzoku_check.csvに書かれているリストの数を取得する
        for count in range (setsuzoku_rows_count):      #csvファイルに書かれている要素数だけ実行する
            setsuzoku_checklist=str(setsuzoku_rows[0][count])
            if setsuzoku_checklist in document_a:
                setsuzokusi_checklist_log.append(setsuzoku_checklist)
                check_count+=1
    return check_count
"""
#⚫︎1文をdocument.txtファイルに書き込む関数
def write_document(document_a,filepath_a):
    with open(filepath_a,"a",encoding="utf-8") as file:
        file.write(f"{document_a}\n")

#⚫︎1文の文字数をdocument.txtファイルに書き込む
def write_str_count(count,filepath_a):
    with open(filepath_a,"a",encoding="utf-8") as file:
        file.write(f"{count}文字\n")

#⚫︎警告文をdocument.txtファイルに書き込む関数
def write_caveat(caveat_juge,filepath_a) :
    with open (filepath_a,"a",encoding="utf-8") as file:
        if caveat_juge==1:
            file.write("●E-1：一文が120字以上です\n")
        elif caveat_juge==2:
            file.write("●E-2：接続詞が誤っています\n")
            error_setsuzokusi_cnt=len(setsuzokusi_checklist_log)
            for count in range (error_setsuzokusi_cnt):
                file.write(f"・{setsuzokusi_checklist_log[count]}\n")
        elif caveat_juge==3:
            file.write("●E-3：専門用語が書かれています\n")
            error_senmonyougo_cnt=len(senmonyougo_checklist_log)
            for count in range (error_senmonyougo_cnt):
                file.write(f"・{senmonyougo_checklist_log[count]}\n")

#⚫︎ラインをdocument.txtファイルに書き込む関数
def write_line(filepath_a): 
    with open(filepath_a,"a",encoding="utf-8") as file:
        file.write("-------------------------------------------------\n")