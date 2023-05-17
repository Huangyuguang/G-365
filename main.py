import tkinter

root = tkinter.Tk()
root.title('G-365 V0.0.1')
root.iconphoto(False,tkinter.PhotoImage(file = 'Function_script/pictures/icon.png'))
root.geometry('400x400+500+200')
def music_player():
    root.destroy()
    from Function_script.plug_in_unit import music_player
    music_player.Musicplayer()
def spider():
    root.destroy()
    from Function_script.plug_in_unit import spider
    spider.Spider()
def video():
    root.destroy()
    from Function_script.plug_in_unit import Video
    Video.Video()
def pip_auto_install():
    root.destroy()
    from Function_script.plug_in_unit import pip_auto_install
    pip_auto_install.PipAutoInstall()
tkinter.Label(root,text = '欢迎使用G-365，祝你使用愉快！').pack()
tkinter.Button(root,text = '视频监控',command = video).pack()
tkinter.Button(root,text = '自动化pip安装工具',command = pip_auto_install).pack()
tkinter.Button(root,text = 'mp3播放器▶️',command = music_player).pack()
tkinter.Button(root,text = '爬虫',command = spider).pack()
root.mainloop()