#coding:utf-8
import  requests
import pymysql
import time
from bs4 import  BeautifulSoup

'''
得到租房详情页面
'''
def getDetailInfo(url):
    print(url)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.content, 'html.parser')
    #需要soup选择器

    # introducePart > div:nth-of-type(4) > div.info_r > div.info_text_mid > p
    jiaotongs=soup.select("#introducePart > div:nth-of-type(3) > div > div")
    print(jiaotongs)

def getInfo(url):
    time.sleep(2)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.content, 'html.parser')
    house_names = soup.select(".result_title.hiddenTxt")
    house_prices=soup.select(".result_price i")
    hrefs=soup.select(".resule_img_a")
   # print(hrefs)
    for href in hrefs:
        h=href["href"]
        imgs=href.find("img")
        print("租房详情页面%s,图片路径%s" %(h,imgs["lazy_src"]))
        getDetailInfo(h)
    # for house_price in house_prices:
    #     print(house_price.text)
    # for house_name in house_names:
    #     print("招租主题:%s" % house_name.text)

    return None

xiaozhu_url=["http://bj.xiaozhu.com/zhengzu-duanzufang-p{}-2/".format(str(i)) for i in range(1,2)]
for url in xiaozhu_url:
    getInfo(url)




