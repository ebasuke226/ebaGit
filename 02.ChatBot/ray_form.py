from ray import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
import re

""" グローバル変数の定義
"""
entry = None         # 入力エリアのオブジェクトを保持
response_area = None # 応答エリアのオブジェクトを保持
action = None        # '科目'メニューの状態を保持
ray = Ray()          # Rayオブジェクトを保持
study = 0            # 質問か答えかを判別するためのフラグ
what = ''            # わからない質問を保持する変数

# 対話を行う関数
def talk():
    global study, what
    
    value = entry.get()
    subject = action.get()
    # 入力エリアが未入力の場合
    if not value:
       response_area.configure(text='なに?')
    elif subject==0 and study==0:
        # 入力文字列を引数にしてdialogue()の結果を取得
        response = ray.dialogue(value, subject, study, what)
        # 応答メッセージを表示
        response_area.configure(text=response)
        # フラグを立てる
        m = re.match('わかんないよ～', response)
        if m:
            study = 1
            what = value
        # 入力ボックスをクリア
        entry.delete(0, tk.END)
    # 教えてもらった答えを辞書に記録する
    elif subject==0 and study==1:
        # 入力文字列を引数にしてdialogue()の結果を取得
        response = ray.dialogue(value, subject, study, what)
        # 応答メッセージを表示
        response_area.configure(text=response)
        # フラグを戻す
        study = 0
        # whatをクリア
        what = ''
        # 入力ボックスをクリア
        entry.delete(0, tk.END)




    elif subject==1 and study==0:
        # 入力文字列を引数にしてdialogue()の結果を取得
        response = ray.dialogue(value, subject, study, what)
        # 応答メッセージを表示
        response_area.configure(text=response)
        # フラグを立てる
        m = re.match('わかんないよ～', response)
        print('m===',m)
        if m:
            study = 1
            what = value
        # 入力ボックスをクリア
        entry.delete(0, tk.END)
    # 教えてもらった答えを辞書に記録する
    elif subject==1 and study==1:
        # 入力文字列を引数にしてdialogue()の結果を取得
        response = ray.dialogue(value, subject, study, what)
        # 応答メッセージを表示
        response_area.configure(text=response)
        # フラグを戻す
        study = 0
        # whatをクリア
        what = ''
        # 入力ボックスをクリア
        entry.delete(0, tk.END)


#=================================================
# 画面を描画する関数
#=================================================
def run():
    # グローバル変数を使用するための記述
    global entry, response_area, action

    # メインウィンドウを作成
    root = tk.Tk()
    # ウィンドウのサイズを設定
    root.geometry('600x680')
    # ウィンドウのタイトルを設定
    root.title('Super Bot --Ray-- : ')
    # フォントの用意
    font=('Helevetica', 14)
    def callback():
        """ 終了時の処理
        """
        # メッセージボックスの[OK]ボタンクリック時の処理
        if tkinter.messagebox.askyesno(
            'Quit?', '辞書を更新してもいい?'):
            ray.save() # 記憶メソッド実行
            root.destroy()
	# [キャンセル]ボタンクリック
        else:
            root.destroy()

    root.protocol('WM_DELETE_WINDOW', callback)

    # メニューバーの作成
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    #「ファイル」メニュー
    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label='ファイル', menu=filemenu)
    filemenu.add_command(label='閉じる', command=callback)
    # 「科目」メニュー
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label='科目', menu=optionmenu)
    optionmenu.add_radiobutton(
        label='川崎フロンターレ',				# アイテム名
        variable = action,          # 選択時の値を格納するオブジェクト
        value = 0                   # アイテムの値を0にする
    )
#    optionmenu.add_radiobutton(
#        label='もうひと科目',				# アイテム名
#        variable = action,          # 選択時の値を格納するオブジェクト
#        value = 0                   # アイテムの値を0にする
#    )
    
    # キャンバスの作成
    canvas = tk.Canvas(
                root,               # 親要素をメインウィンドウに設定
                width = 600,        # 幅を設定
                height = 400,       # 高さを設定
                relief=tk.RIDGE,    # 枠線を表示
                bd=2                # 枠線の幅を設定
             )
    canvas.place(x=1, y=0)                  # メインウィンドウ上に配置
    
#    img = tk.PhotoImage(file = 'kawasaki.gif')  # 表示するイメージを用意
    img = ImageTk.PhotoImage(file="kawasaki.jpg")

    
    canvas.create_image(                    # キャンバス上にイメージを配置
        0,                                  # x座標
        0,                                  # y座標
        image = img,                        # 配置するイメージオブジェクトを指定
        anchor = tk.NW                      # 配置の起点となる位置を左上隅に指定
    )

    # 応答エリアを作成
    response_area = tk.Label(
                        root,               # 親要素をメインウィンドウに設定
                        width=60,           # 幅を設定
                        height=2,          # 高さを設定
                        bg='LightSkyBlue',        # 背景色を設定
                        font=font,          # フォントを設定
                        relief=tk.RIDGE,    # 枠線の種類を設定
                        bd=2                # 枠線の幅を設定
                    )
    response_area.place(x=6, y=500)         # メインウィンドウ上に配置


    # フレームの作成
    frame = tk.Frame(
                root,               # 親要素はメインウィンドウ
                relief=tk.RIDGE,    # ボーダーの種類
                borderwidth = 4     # ボーダー幅を設定
            )
    # 入力ボックスの作成
    entry = tk.Entry(
                frame,              # 親要素はフレーム
                width=40,           # 幅を設定
                font=font           # フォントを設定
            )
    entry.pack(side = tk.LEFT)      # フレームに左詰めで配置する
    entry.focus_set()               # 入力ボックスにフォーカスを当てる
    # ボタンの作成
    button = tk.Button(
                frame,              # 親要素はフレーム
                width=15,           # 幅を設定
                text='入力',        # ボタンに表示するテキスト
                command=talk        # クリック時にtalk()関数を呼ぶ
             )
    button.pack(side = tk.LEFT)     # フレームに左詰めで配置する
    frame.place(x=30, y=420)        # フレームを画面上に配置

	
    # メインループ
    root.mainloop()



#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    run()

