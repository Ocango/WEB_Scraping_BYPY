# 《python网络爬虫指南》学习笔记
没有什么特别想说的，就当我知识恐慌吧。

互联网其实就是一个用户界面不太友好的超级API

# 网络抓取的法律与道德约束
## 商标
商标则是针对利用方面，其由使用场景决定
## 版权

## 专利
专利偏向于信息的所构建的东西，而不是信息本身，所以这一方面不太会涉及
## 侵害动产
1. 缺少许可
2. 造成实际的伤害
3. 故意而为
这一点其实就是侵犯利益和影响服务有关。不得不说爬虫有可能演变成攻击

## 计算机欺诈和滥用法
远离受保护的计算机，不要接入没有授权的计算机，尤其要避开政府或财务计算机
## robots.txt和服务协议

# Section1 创建爬虫
- 通过网站域名获取HTML数据 
- 解析数据获取目标信息
- 存储目标信息
- 如有必要，移动到另一个网页重复这个过程
## 获得一个HTML页面
```
from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())
```
## BeautifulSoup
将html映射为对象结构
```
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(),'html.parser')
print(bs.h1)
```
### html解析器
html.parser    lxml       html5lib
### 预防爬虫宕机
其实就是异常处理
```
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
```
## 复杂的HTML解析
避免让他依赖于网站的结构不变
- 寻找打印此页的方法，或者寻求移动版
- 寻找隐藏在JS中的信息
- 网页的URL
- 其他的网页呢
### class标签筛选
http://www.pythonscraping.com/pages/warandpeace.html
```
namelist = bs.find_all('span',{'class':'green'})
for name in namelist:
    print(name.get_text())
```

find( name , attrs , recursive , text , **kwargs ) 

findall( name , attrs , recursive , text , **kwargs )
```
/*name:名为name的tag，可以用列表
keyword参数:tag的属性#这个方法其实不如用namelist = bs.find_all('',{'class':'green'})
按CSS搜索:4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag
text 参数:通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True .
limit 参数:可以使用 limit 参数限制返回结果的数量
recursive 参数:Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False
因为findall用太多，可以使用BeautifulSoup对象直接当做findall用
*/
```
name.get_text() #清理所处理文档的标签

### 导航树
#### 处理子标签和其他后代标签
http://www.pythonscraping.com/pages/page3.html
children()子标签
descendants()所有的后代标签

#### 处理兄弟标签
next_siblings() 调用后面的兄弟标签
previous_siblings() 调用前面的兄弟标签

#### 处理父标签
parent() 找爸爸

### 正则
- *
- +
- []
- ()
- {m,n}
- [^]
- |
- .
- ^
- \
- $
- ?!
### 获取属性
myTag.attrs 返回一个字典类型的tag全部属性

### Lambda
用find_all保留所有的为真的结果
bs.find_all(lambda tag:len(tag.attrs) == 2)

## 抓取整个网站
一个常见的方法：递归（深度遍历）
然后遍历并收集数据