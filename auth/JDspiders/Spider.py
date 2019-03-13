# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/3/8 9:50'
import requests, os
from bs4 import BeautifulSoup


# 商品爬去
def goodsSipder(keyword, activite, number=10):
    # 获取的数据字典
    data = {}  #商品名称、图片名称、详情描述
    # 定义请求头
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'close',
        # 'Cookie':'xtest=9213.cf6b6759; ipLoc-djd=1-72-2799-0; __jda=122270672.1548034938529233599140.1548034939.1548034939.1548034939.1; __jdv=122270672|direct|-|none|-|1548034938531; __jdc=122270672; __jdu=1548034938529233599140; shshshfpa=ac503162-a56e-40bc-ef56-ef5402d7bfea-1548034941; shshshfpb=j4uGE09uYj6gf0h1dYVJb1w%3D%3D; rkv=V0300; 3AB9D23F7A4B3C9B=4A3ZMTLQHNW5T54CHZLT5BVI4N5Y6CV5VYTTYF7DJP77HIRPEXM77JB7P6Q73QBJQDGSWHXHIGRR4HFFANEWV6VW3A; qrsc=3; _gcl_au=1.1.1403731449.1548035538; shshshfp=94e15a9ba84ffd460305bace788b2659; mt_xid=V2_52007VwMWV1RZUF8XSxBYBm8AEFBZUFpaGkgpX1Y3ChUGWA1ODRtKTEAAZ1FHTlQNWgoDTBtUBTVREQYJX1UKL0oYXA17AhJOXlhDWxdCHVsOZAMiUG1YYlkZTRFZAm4DFmJdXVRd; shshshsID=744213646502d28f0b0890c1baed1abf_9_1548035784132; __jdb=122270672.9.1548034938529233599140|1.1548034939',
        # 'Host':'search.jd.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3',
    }
    # 请求链接
    pintuancontent = requests.get('https://search.jd.com/Search?keyword={}&enc=utf-8&pvid=f7580c4d17e54c4981f482d7e61dfe55'.format(keyword), headers = headers)
    pintuancontent.encoding = 'utf-8'
    # 获取商品详细信息并记录到数据字典供接口返回
    pintuantext = pintuancontent.text
    soup = BeautifulSoup(pintuantext, 'html.parser')
    # 获取页面上品url
    goodslist = soup.select('.p-img a')
    i = 1
    for goods in goodslist:
        if i > number:
            break
        url = goods.attrs['href']
        if 'http' not in url:
            url = 'https://'+url[2:]
        goodsdetail = requests.get(url, headers=headers)
        goodsdetail.encoding = 'gbk'
        goodstext = goodsdetail.text
        soup = BeautifulSoup(goodstext, 'html.parser')
        pintuandata = []
        # 获取商品名称
        goodsnameele = soup.select('.sku-name')
        goodsname = goodsnameele[0].text.strip()
        pintuandata.append(goodsname)
        # 获取商品图片
        from automation.common import ranStr
        imagename = ranStr(8)
        pintuandata.append('{}.jpg'.format(imagename))
        goodsimageele = soup.select('#spec-img')
        goodsimage = goodsimageele[0].attrs['data-origin']
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        imgcontent = requests.get('http://'+goodsimage[2:])
        dir = path+'\\'+'static'+ '\\' + activite
        isExists = os.path.exists(dir)
        if not isExists:
            os.makedirs(dir)
        imgpath = path+'\\'+'static'+ '\\' + '{}'.format(activite) + '\\' +'{}.jpg'.format(imagename)
        f = open(imgpath, 'wb')
        f.write(imgcontent.content)
        f.close()
        # 获取商品详情
        goodsdetailele = soup.select('.parameter2.p-parameter-list')
        goodsdetail = goodsdetailele[0].text
        pintuandata.append(goodsdetail)

        data[i] = pintuandata
        i += 1
    return data


if __name__ == '__main__':
    goodsSipder('男装', 'goods')