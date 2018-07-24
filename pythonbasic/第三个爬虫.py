# coding:utf-8
#宅福利爬虫，输入第一页的url，自动爬取该主题所有图片
import bs4, requests, os
from bs4 import UnicodeDammit

urls = []

def getUrls():
    urlIndex = "http://yxpjwnet1.com/page/7.html"
    pageUrl = "http://yxpjwnet1.com/page/"
    topicUrl = "http://yxpjwnet1.com"
    a = 0
    b = 0
    page = 7
    while True:

        data = requests.get(urlIndex)
        data_soup = bs4.BeautifulSoup(data.content, 'lxml')


        web_urls = data_soup.select("article > header > h2 > a")
        print(web_urls)
        if web_urls == []:
            break
        for tag in web_urls:
            href = tag.get("href")
            urlHref = topicUrl + href
            urls.append(urlHref)
            b += 1
        a += 1
        print("第%d页已处理完成，共%d个主题"%(a, b))
        page += 1
        urlIndex = pageUrl + str(page) + ".html"
        # nextPage = data_soup.select("[class~=next-page] > a")
        # print(nextPage)
        # if nextPage == []:
        #     break
        # nextPage = nextPage[0].get("href")
        # print(nextPage)
        # urlIndex = pageUrl + nextPage
        # print(urlIndex)



#输入主题第一页的url，自动爬取该主题所有图片
def downloadTopic(urlRaw):
    #urlRaw = 'http://yxpjwnet1.com/luyilu/2018/0115/4516.html'
    urlMain = urlRaw[:-9]
    urlPart = urlRaw[-9:]
    url = urlMain + urlPart
    stop = True
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content, 'html5lib')


    #创建用于保存图片的文件夹

    objName = soup.select("h1")[0].get_text()

    os.makedirs(objName, exist_ok=True)
    i, j = 1, 1
    while stop:

        print("正在解析第%s个网页" % i )

        imgUrlList = soup.select("img[alt]")
        k = 1
        for imgUrlObj in imgUrlList:
            print("正在下载第%s个网页的第%s张图片,共计%s张图片"%(i, k, j))
            j += 1
            k += 1
            imgUrl = imgUrlObj.get("src")
            with open(os.path.join(objName, os.path.basename(imgUrl)), 'wb') as f:
                f.write(requests.get(imgUrl).content)
        i += 1
        nextUrl = soup.select(".next-page > a")
        if nextUrl == []:
            break
        urlPart = nextUrl[0].get("href")
        url = urlMain + urlPart
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')

    print("Done")

if __name__ == '__main__':
    getUrls()
    for url in urls:
        downloadTopic(url)






