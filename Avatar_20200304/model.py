import urllib
import urllib.request
import re   #正则表达式
from time import sleep  # 根据需要导入，控制下载速度

# 根据url解析包含图片的页面
def load_page(url):
    request = urllib.request.Request(url)   #发送网络请求
    response = urllib.request.urlopen(request)  # 根据url打开页面
    data = response.read() # 获取页面的响应数据
    return data

# 根据图片对应的html链接下载图片
def get_image(html):
    regx = r'http://[\S]*jpg'   # 定义正则表达式，匹配页面jpg图片元素
    pattern = re.compile(regx)  # 编译表达式，构造匹配模式
    # 进行正则匹配，返回包含jpg图片的所有链接
    get_image = re.findall(pattern,repr(html))

    num = 1
    #遍历取出以上所获取的图片
    for img in get_image:
        # 解析img变量取出的图片链接，赋给image变量
        image = load_page(img)
        # 将图片存入指定文件夹，并以从1开始递增的数字命名jpg图片
        with open('X:\\Py_LoadData\\%s.jpg' %num,'wb') as fb:
            fb.write(image) # fb相当于open(...);# wb：以二进制方式打开
            print("正在下载第%s张图片" %num)
            num = num+1
            sleep(2)
    print("下载完成！")

url = 'http://xxx/'
# 调用：解析url页面的方法
html = load_page(url)
# 调用：下载图片的方法
get_image(html)