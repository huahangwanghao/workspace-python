#coding:utf-8
import  requests
import pymysql
import json
from bs4 import  BeautifulSoup
url="https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
'''
web_data=requests.get(url)
soup=BeautifulSoup(web_data.content,'html.parser')
# BeautifulSoup 不识别通过 google 开发者工具获取的CSS选择器nth-child(第几个子元素而且是特定元素),可以用nth-of-type(第几个特定元素)替换。
#titles=soup.select('#taplc_attraction_coverpage_attraction_0 > div:nth-of-type(1) > div > div > div.shelf_item_container > div:nth-of-type(1) > div.poi > div > div.item.name > a')
titles=soup.select("div .detail div.item.name")
#imgs=soup.select(".photo_image")
imgs=soup.select("img[width='200']")
cats=soup.select("div .detail > div:nth-of-type(3)")


for title,img,cat in zip(titles,imgs,cats):
    print("标题:%s,图片路径:%s,解释:%s" %(title.get("title"),img.get("src"),cat.text))
'''

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Cookie":"TAUnique=%1%enc%3AKpICeSYz1YlPa6kZ5ysxSNDvU2EOWK%2FjMKRhCsNYyfc%3D; TASSK=enc%3AAPZNcLmD%2BXCEkIDYE3ccyOs3KSJKA%2BpiM5sF18bJ3PMD7Yqbxi1HGhtGPH%2F0G0BxQ5HswBdZkfSsp62S7cmoJjSL2Z3K%2F9phpuy7LOtLFoy7ROmQyZSO0o%2FiTmQRZn7uig%3D%3D; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1508998602875; __gads=ID=a70e02be93a53179:T=1508393811:S=ALNI_MZeFfTUeMLcKI3ucsHzXczI1cmkwg; _jzqy=1.1508393670.1508393670.1.jzqsr=baidu|jzqct=tripadvisor.-; _jzqckmp=1; _smt_uid=59e842bd.192ff398; ki_t=1508393835217%3B1508393835217%3B1508393835217%3B1%3B1; ki_r=; _jzqx=1.1508397907.1508397907.1.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.-; TAAuth3=3%3A929a7d722a0bd5377f446d44602f6e8b%3AANiOlYqjKYveaubrD3dB5LxbIRUrEfNLobPlkn7RUzAN1Pf0MJzC6Lmam4JIIGBnvd1kjD2tGeH%2BtQjcOlZIbT217%2FiZnryaukEIOAmviUtemRb%2F6SCrQFX6byEhoReBwSFa3tUYoU%2BmDejuLQTrZbvnkqTjk3BdKHMTRxVXY01MFRMzIL625rr%2B7TPsVcm0iQ%3D%3D; ServerPool=R; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.110164_292l60763_292*RS.1; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; _ga=GA1.2.313178230.1508393654; _gid=GA1.2.623824553.1508393654; roybatty=TNI1625!AJCavjgo%2ByqUnf80vkzymGG1d2%2BjuXyRzVVFG1zF1ePjpmuLKnOG8SsQgfDmfdx0RUjB8cGLyf0CJuolQPiFCocM7O%2FMyOxIHBQHHDLj4i2%2F78Vz39BirYqcCpd4m%2F7Dmn0NTOVyNbAX06oHLbdOPfcuQG6sWhoJOXGUA599JQQo%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1508393661,1508393686,1508399103; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1508399103; TASession=%1%V2ID.62F5BE592709047B13EC99284EE92C9B*SQ.3*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*LS.DemandLoadAjax*GR.73*TCPAR.58*TBR.5*EXEX.58*ABTR.80*PHTB.76*FS.65*CPU.51*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.2A9C85CB98162CCF02834FA8E82A1484*FA.1*DF.0*FLO.60763*TRA.true*LD.60763; TAUD=LA-1508399252776-1*RDD-1-2017_10_19*LG-82-2.1.F.*LD-83-.....; _jzqa=1.2874234139399771600.1508393670.1508397907.1508399103.3; _jzqc=1; _qzja=1.324309981.1508393669949.1508397906841.1508399102930.1508397906841.1508399102930..0.0.5.3; _qzjb=1.1508397906840.2.0.0.0; _qzjc=1; _qzjto=5.3.0; _jzqb=1.1.10.1508399103.1"
}
web_data=requests.get(url,headers=header)
soup=BeautifulSoup(web_data.content,'html.parser')
print(soup)