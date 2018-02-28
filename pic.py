import requests
from urllib import parse
import re
from tkinter import *



root = Tk()
root.title("图片下载器")
root.geometry("300x100")
root.resizable(width=False, height=False)

pictype = StringVar()
pictype_entry = Entry(root, textvariable=pictype)
pictype.set("输入图片类型如:美女")
pictype_entry.place(x=150,y=0)



picnum = StringVar()
picnum_entry = Entry(root, textvariable=picnum)
picnum.set("请输入小与等于30的数字")
picnum_entry.place(x=150,y=20)


picpath = StringVar()
picpath_entry = Entry(root, textvariable=picpath)
picpath.set('D:\\')
picpath_entry.place(x=150,y=40)



def picdownload():
    pictype_string = pictype.get()
    urlcode = parse.quote(pictype_string)
    num = picnum.get()
    path = picpath.get()
    print(path)
    urlbaidupic = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+urlcode+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word='+urlcode+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn='+num
    picinfo = requests.get(urlbaidupic)
    picture_url = re.findall('"middleURL":"(.*?)"',picinfo.text)

    for urlpic in picture_url[:int(num)]:
        pic = requests.get(urlpic) 
        with open(path+r'\{}' .format(urlpic[-25:]) ,'wb') as f:
            f.write(pic.content)



Button(root, text="GO", command=picdownload).pack(side=BOTTOM)

#Button(root, text="GO", command=picdownload(urlcode,picnum_string,picpath_string)).pack(side=BOTTOM)

label1 = Label(root,text="请输入需要下载的图片类型")
label2 = Label(root,text="请输入需要下载的数量")
label3 = Label(root,text="请输入保存图片的绝对路径")
label1.place(x=0,y=0)
label2.place(x=0,y=20)
label3.place(x=0,y=40)
#label2.pack(side = LEFT)


root.mainloop()
