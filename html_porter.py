#python3
import urllib.request
kaitou='''
             HTML_PORTER
                  V2.0
 
注意：
保存路径请使用绝对路径
格式如下：

Linux:
//xx//xx//xx.html
'''
print(kaitou)
url = input("Website_URL->")
save = input("保存路径->")
#打开一个网页链接
htmlhandler = urllib.request.urlopen(url)

#在本机上创造一个新文件
file = open((save), "wb")

#将网页储存在本机文件里，每次读取512个字节,并告示使用者
print("正在保存中，请稍候....")
while 1:
   deta = htmlhandler.read(512)
   if not deta:
      break
   file.write(deta)

#关闭本机文件
file.close()

#关闭网页文件
htmlhandler.close()

#提示使用者文件保存完毕，并退出程序
print("保存完成！")
exit()
