#UIの表示を行う
import tkinter as tk            #インターフェイス
from main import function_main

#テキストボックス内の文章を吸い上げる関数
def copy_document():
    text=textbox.get("1.0","end")
    function_main(text)

#インターフェイス
root=tk. Tk()
root.title("文章校閲システム")
root. geometry("600x480")       #ウィンドウサイズ

#ラベル
label_document=tk.Label(root,text="文章を入力してください")
label_document.grid(padx=5,sticky=tk.W)

#入力ボックス
textbox=tk.Text (root,height=30,width=83)
textbox.grid(padx=5, sticky=tk. W)

#ボタン
button=tk.Button (root,text="開始",command=copy_document)
button.grid(pady=5,padx=5,sticky=tk.W)

root.mainloop()

