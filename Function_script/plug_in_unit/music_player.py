#导入必要的库
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import pygame
#初始化pygame.mixer
pygame.mixer.init()
#创建一个tk窗口对象
root = tk.Tk()
#设置窗口大小和位置
root.geometry('400x400+700+300')
#设置窗口标题
root.title('音乐播放器')


class Musicplayer:
    # 初始化函数
    def __init__(self,window):
        self.button_unpause = None
        self.button_pause = None
        self.button_stop = None
        self.button_play = None
        self.file_path = None
        self.button_choose = None
        self.root = window
        self.button()
        self.root.mainloop()
    def choose_file( self ):
        self.file_path = filedialog.askopenfilename (
            initialdir = './' ,
            title = '选择音乐文件' ,
            filetypes = [ ('MP3 文件' , '*.mp3') ,
                          ('WAV 文件' , '*.wav') ,
                          ('OGG 文件' , '*.ogg') ,
                          ('MIDI 文件' , '*.mid') ,
                          ('MOD 文件' , '*.mod') ,
                          ('WMA 文件' , '*.wma') ]
        )
        pygame.mixer.music.load(self.file_path)
    @staticmethod
    def play( ):
        pygame.mixer.music.play()
    @staticmethod
    def stop( ):
        pygame.mixer.music.stop()
    @staticmethod
    def pause( ):
        pygame.mixer.music.pause()
    @staticmethod
    def unpause( ):
        pygame.mixer.music.unpause()
    def button( self ):
        self.button_choose = ttk.Button(self.root,text = '选择文件',command = self.choose_file)
        self.button_choose.pack()
        self.button_play = ttk.Button ( self.root , text = '开始播放' , command = self.play )
        self.button_play.pack ( )
        self.button_stop = ttk.Button ( self.root , text = '停止播放' , command = self.stop )
        self.button_stop.pack ( )
        self.button_pause = ttk.Button ( self.root , text = '暂停' , command = self.pause )
        self.button_pause.pack ( )
        self.button_unpause = ttk.Button ( self.root , text = '继续' , command = self.unpause )
        self.button_unpause.pack ( )
#创建Musicplayer类的实例并将tk窗口对象作为参数传入
Musicplayer(root)
