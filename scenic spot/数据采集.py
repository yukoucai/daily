# _*_coding : utf-8 _*_
# @Time : 2022/6/7 10:13 
# @Author : hosee
# @File : xpath_去哪儿网景点数据爬取
# @Project : untitled
import requests
from bs4 import BeautifulSoup
import csv
import time

# 获取url
def get_url(page):
    url_request = "https://piao.qunar.com/ticket/list.htm?keyword=" + n + "&region=&from=mpl_search_suggest&page="
    url = url_request + str(page)
    return url

# 获取网页数据
def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'cookie': 'QN1=00006580306c427ef3484f9b; QN99=7116; QunarGlobal=10.68.40.45_-16874b3d_18126ddbc08_211e|1654216810124; QN601=ed23cadf05a74ac6b61715654b28466c; _i=DFiEZpFF30Ow_bp6tAYwT9jbB56w; QN48=4a07cf67-186c-4886-8f84-21cdcba96a2a; fid=7522e75d-95b9-4171-839b-1a1abdeaf1bc; ctt_june=1644991819166##iK3wWSjmWhPwawPwasPAEKHhXsgNED3nERvOERoDX2P8VDGGWSv8aPEGXPXOiK3siK3saKjAWR3nWStsWKP+VhPwaUvt; QN300=s=baidu; ctf_june=1644991819166##iK3waKjmWhPwawPwasaAVPXmEKXNXKPwa2iIE2DmVPPAWKfTaDjAaRoTVPD=iK3siK3saKjAWR3waRX+WKvsVhPwaUvt; cs_june=b32bc48cb10fee9b88375f4649c8e060815a1e03d3c940ae113a51fd348121e3677d6e1a1538da26718f49608e48429edc8ed7855fc8ca4267910f7f15aacc40b17c80df7eee7c02a9c1a6a5b97c117976729a5bf1b8cecf08b85e4edf895a0f5a737ae180251ef5be23400b098dd8ca; QN57=16542205141330.27030828881886926; quinn=2f45d9dba1d900657e812e97591e857532cda08598b6c1134c6918a56a8f21d06b670229cffbca41ffe011c6a5a04628; QN205=organic; QN277=organic; QN269=BDE94AA0CF8B11EDAC92FA163E03A4E8; _vi=BNHEMeWb8wmbT237GpAP0oxNMMwk34AZ-z1m15AtFB2Dnh7VKgJ4vQ7F-xUPX9j_ITCNbsBttYfUCmmvgd3RawkhLVKPqH5YvtId50ULA4HsPAZSx3i5tg4HxGS0vn--DH0PbxyBPqyudIBme82sPgChYdU1nMgj1-Z0z-4zlHq8; qunar-assist={"version":"20211215173359.925","show":false,"audio":false,"speed":"middle","zomm":1,"cursor":false,"pointer":false,"bigtext":false,"overead":false,"readscreen":false,"theme":"default"}; csrfToken=JbMQMu64A8jC82N2ul5nd4b7IFACjaQL; QN267=0483141159abf34a15; ariaDefaultTheme=undefined; QN58=1680275358816|1680275784960|12; QN271=c1265bad-31f8-4282-9bfb-436ce02da361'
    }
    response = requests.get(url=url,headers=headers)
    content = response.text
    return content

def down_load(content):
    # 使用bs4
    soup = BeautifulSoup(content, 'lxml')
    informations = soup.find_all('div',{'class':'result_list','id':'search-list'})[0].find_all('div',{'class':'sight_item'})

    for inf in informations:
        # 爬取景点名
        name = inf.find_all('a',{'data-click-type':'l_title','class':'name'})[0].text
        # 爬取景点省份
        if n == "黑龙江" or n == "内蒙古":
            area = inf.find_all('span',{'class':{'area'}})[0].text[1:4]
        else:
            area = inf.find_all('span', {'class': {'area'}})[0].text[1:3]
        # 爬取景点描述
        introduce = inf.find_all('div', {'class': {'intro', 'color999'}})[0].text
        # 爬取景点热度
        hot = inf.find_all('span',{'class':{'product_star_level'}})[0].text[3:]
        # 爬取景点等级
        try:
            level = inf.find_all('span',{'class':'level'})[0].text
        except:
            level = '普通景区'
        # 爬取景点门票价格
        try:
            price = inf.find_all('span', {'class': 'sight_item_price'})[0].find_all('em')[0].text
        except:
            price = 0
        # 爬取月销售量
        try:
            sales = int(inf.find_all('span', {'class': 'hot_num'})[0].text)
        except:
            sales = 0

        # 保存成csv文件
        text = [name,area,level,introduce,hot,price,sales]

        with open('sight.csv','a',encoding='utf_8_sig') as f:
            w = csv.writer(f)
            w.writerow(text)

    # 设置停顿时间
    time.sleep(1.5)


if __name__ == '__main__':
    # 列出所有省份
    pros = ["河北","山西","黑龙江","吉林","辽宁","江苏","浙江","安徽","福建",
            "江西","山东","河南","湖北","湖南","广东","海南","四川","贵州",
            "云南","陕西","甘肃","青海","台湾","内蒙古","广西","西藏","宁夏",
            "新疆","北京","天津","上海","重庆","香港","澳门"]
    # for循环遍历数组
    for pro in pros:
        n = str(pro)
        for page in range(1,151):
            url = get_url(page)
            content = get_content(url)
            down_load(content)
        print("**去哪儿网",pro,"前150页景点数据爬取成功**")
    print("------所有省份前150页景点数据爬取成功------")

