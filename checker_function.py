#問題がないかチェックする
import csv

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