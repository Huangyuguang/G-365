这是电脑作死-365(G-365)的官方安装程序： 
# 这是G-365的V0.0.3版本
首先，你需要安装依赖库
```shell
pip3 install opencv-python -i https://pypi.douban.com/simple/
pip3 install numpy -i https://pypi.douban.com/simple/
pip3 install pygame -i https://pypi.douban.com/simple
pip3 install beautifulsoup4 -i https://pypi.douban.com/simple
pip3 install requests -i https://pypi.douban.com/simple
```
其次，是教程：
````
1、运行
    1.主文件是main.py
2、视频监控功能
    1.
        使用它时需要按下'q'键才能退出
    2.
        默认运行的是你的主摄像头，若要修改请打开：
        Function_script/plug_in_unit/Video.py的第5行:
        '''python代码[
        # 打开默认的摄像头
        cap = cv2.VideoCapture(0)
        ]'''
        其中cv2.VudeoCapture(这里是你的摄像头编号，默认0开始)
````
只要你读完了README.md，我就相信你可以愉快的使用啦~~~~

此文档由电脑作死——一个普普通通的小学生编写
有可能有问题，若有问题，请bilibili私信我：
[bilibili链接](https://space.bilibili.com/687441273?spm_id_from=333.1007.0.0)
文件说明：
```
    ./
    ├── Function_script-------------------：附加的文件
    │   ├── pictures----------------------：程序用到的文件
    │   │   └── icon.png------------------：程序图标
    │   └── plug_in_unit------------------：功能脚本
    │       ├── Video.py------------------：视频监控脚本
    │       ├── __init__.py---------------：防止报错的填充文件
    │       └── pip_auto_install.py-------：pip自动安装程序
    │       └── music_player.py-----------：音乐播放器程序
    │       └── spider.py-----------------：爬虫程序
    │       └── __pycache__---------------：python的调用文件
    ├── .DS_store-------------------------：mac_os自己生成的
    ├── .idea-----------------------------：PyCharm CE生成的
    ├── README.md-------------------------：你现在看的
    └── main.py---------------------------：主文件
```