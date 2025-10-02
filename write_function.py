#document.txtファイルへ書き込みを行う
import config

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
    if not csv_checkeddata:
        return 

    with open(config.document_file_path,"a",encoding="utf-8") as file:
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