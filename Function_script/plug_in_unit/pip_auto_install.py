# 导入所需的tkinter模块和相关组件
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

# 创建一个tkinter窗口，设置标题和窗口大小
root = tk.Tk()
root.title('pip自动化安装工具')
root.geometry('400x400+700+300')

# 定义一个名为PipAutoInstall的类，用于控制整个GUI程序
class PipAutoInstall:
    def __init__(self, window):
        self.main_screen_button_text = None
        self.root = window
        self.main_screen_button_entry = None
        self.main_screen_button = None
        self.control_button_button = None
        self.install_library = None
        # 初始化程序界面，包括输入库名和安装按钮等部分
        self.control_library()
        self.control_button()

    # 该方法用于安装指定库
    def install( self ):
        # 获取用户输入的库名
        self.install_library = self.main_screen_button_entry.get()
        # 执行pip3 install命令来安装指定库
        os.system('pip3 install '+self.install_library+' -i https://pypi.douban.com/simple')
        # 尝试导入已安装的库，如果导入失败则说明安装失败
        try:
            exec('import '+self.install_library)
        except ModuleNotFoundError:
            messagebox.showinfo ( '消息' , '安装失败，\n解决办法\n\t1.检查网络连接\n\t2.python没有这个库\n\t3.这个库名不能在项目中直接调用（比如安装opencv-python实则导入cv2）' )
        # 如果安装成功，则弹出提示框
        messagebox.showinfo ( '消息' , '安装成功' )

    # 该方法用于控制用户输入库名的部分
    def control_library(self):
        self.main_screen_button_text = ttk.Label(self.root, text='库名：')
        self.main_screen_button_text.grid(row=0, column=0)
        self.main_screen_button_entry = ttk.Entry(self.root, width=35)
        self.main_screen_button_entry.grid(row=0, column=1)

    # 该方法用于控制安装按钮的部分
    def control_button(self):
        self.control_button_button = ttk.Button(self.root,text = '装你！',command = self.install)
        self.control_button_button.grid(row = 1 ,column = 1)

# 实例化PipAutoInstall类，并将tkinter窗口传递给它进行控制
PipAutoInstall(root)

# 进入主循环，以显示GUI界面
root.mainloop()
