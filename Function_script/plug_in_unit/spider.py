global te
class Spider:
    def __init__(self):
        import requests
        import os
        from bs4 import BeautifulSoup
        import tkinter
        def ok():
            # 创建一个名为 image 的文件夹
            if not os.path.exists ( 'image' ) :
                os.makedirs ( 'image' )

            # 网页的 URL
            url = te.get()
            if not 'baike.baidu.com/pic/' in url:
                print(url)
                print('有反爬机制，爬不了')
            # 获取网页内容并解析成 BeautifulSoup 对象
            response = requests.get ( url )
            soup = BeautifulSoup ( response.content , 'html.parser' )

            # 找到网页中所有的图片标签
            img_tags = soup.find_all ( 'img' )

            # 遍历所有图片标签，下载图片并保存到 image 文件夹中
            for img in img_tags :
                img_url = img.get ( 'src' )
                img_name = img_url.split ( '/' ) [ -1 ] + '.png'
                response = requests.get ( img_url )
                content = response.content
                with open ( 'image/' + img_name , 'wb' ) as f :
                    f.write ( content )

            print ( '所有图片已经下载完成！' )
        root = tkinter.Tk()
        root.title('爬虫')
        root.geometry('400x400')
        root.minsize(width=400, height=400)
        root.maxsize(width=400, height=400)
        text = tkinter.Label(root,text = 'url:')
        text.pack()
        te = tkinter.Entry(root)
        te.pack()
        text = tkinter.Button(root,text = 'ok',command = ok)
        text.pack()
        root.mainloop()