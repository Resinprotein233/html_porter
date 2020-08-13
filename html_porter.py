#python3
import urllib.request
url = input("Website_URL->")
save = input("")

#打开一个网页链接
htmlhandler = urllib.request.urlopen(url)

#在本机上创造一个新文件
file = open("//root//html_porter//save.html", "wb")

#将网页储存在本机文件里，每次读取512个字节
while 1:
   deta = htmlhandler.read(512)
   if not deta:
      break
   file.write(deta)

#关闭本机文件
file.close()

#关闭网页文件
htmlhandler.close()
