# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/3/8 9:06'
import os
import time

from auth.JDspiders.Spider import goodsSipder
from automation.qingxiaoyun.common import updateImage
from automation.common import ranNumber
# 微商城系统数据创建脚本
from config import pigcms, loginQxy


class AddGoods:
    # 基础设置
    def baseSet(self, needtimes):
        # 输入具体内容
        get_element = pigcms.find_elements_by_css_selector('.bascInfo .turntip.flex')
        # 输入商品名称
        get_element[0].find_element_by_css_selector('.el-input__inner').send_keys(goodsData[needtimes+1][0])
        # 获取已存在的分组内容检测是否需要新建
        get_element[1].find_element_by_css_selector('.el-input--suffix').click()
        groupsele = pigcms.find_elements_by_css_selector('.el-select-dropdown__item')
        try:
            grouplist = []
            for group in groupsele:
                grouplist.append(group.text)
            index = grouplist.index(groupName[:2])
        except:
            # 如果触发异常说明不存在需要创建的分组手动创建
            pigcms.find_elements_by_css_selector('.cp.maincl.ml20')[1].click()
            pigcms.find_elements_by_css_selector('.inpBox.title.clearfix')[0] \
                .find_element_by_css_selector('.el-input__inner').send_keys(groupName[:2])
            pigcms.find_elements_by_css_selector('.popbtns button')[0].click()
            # 元素失效重新获取
            get_element = pigcms.find_elements_by_css_selector('.bascInfo .turntip.flex')
            get_element[1].find_element_by_css_selector('.el-select--small').click()
            groupsele = pigcms.find_elements_by_css_selector('.el-select-dropdown__item')
            grouplist = []
            for group in groupsele:
                grouplist.append(group.text)
            index = grouplist.index(groupName[:2])
            groupsele[index].click()
            pigcms.find_element_by_css_selector('.el-select.el-select--small').click()
        else:
            groupsele[index].click()
            pigcms.find_element_by_css_selector('.el-select.el-select--small').click()
        # 计量单位输入
        get_element[2].find_element_by_css_selector('.el-input__inner').send_keys('件')
        # 图片上传
        pigcms.find_elements_by_css_selector('.el-button.el-button--primary')[1].click()
        imagedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + \
                   '\\' + 'auth' + '\\' + 'static' + '\\' + 'goods' + '\\' + goodsData[needtimes+1][1]
        upresult = updateImage(groupName[:2], imagedir)


    # 库存规格
    def inventory(self, style):
        '''
        设置商品价格库存等信息
        '''
        # 获取所有表单列元素
        if style == 0:
            # 选择单规格
            pigcms.find_elements_by_css_selector('.skuGui .el-radio')[style].click()
            # 获取所有元素列表
            get_element = pigcms.find_elements_by_css_selector('.skuGui .specSet .turntip.flex')
            # 商品编码
            rannumber = ranNumber(6)
            get_element[0].find_element_by_css_selector('.el-input__inner').send_keys(rannumber)
            # 商品价格
            price = '0.01'
            get_element[1].find_element_by_css_selector('.el-input__inner').send_keys(price)
            # 商品划线价
            line_pirce = ranNumber(2)
            get_element[2].find_element_by_css_selector('.el-input__inner').send_keys(line_pirce)
            # 当前库存量
            get_element[3].find_element_by_css_selector('.el-input__inner').send_keys(50)
            # 商品重量
            get_element[4].find_element_by_css_selector('.el-input__inner').send_keys(5)
        else:
            # 选择多规格
            pigcms.find_elements_by_css_selector('.skuGui .el-radio')[style].click()
            # 添加规格
            pigcms.find_element_by_css_selector('.el-button.mb20.el-button--default.el-button--small').click()
            # 输入第一个规格名和值
            pigcms.find_elements_by_css_selector('.addSpec.mb30 .turntip.flex')[0].\
                find_element_by_css_selector('.el-input__inner').send_keys('规格一')
            pigcms.find_elements_by_css_selector('.addSpec.mb30 .turntip.flex')[1]. \
                find_element_by_css_selector('.el-input__inner').send_keys('初选_1')
            pigcms.find_elements_by_css_selector('.addSpec.mb30 button')[0].click()
            # 输入第二个规格名和值
            pigcms.find_element_by_css_selector('.el-button.mb20.el-button--default.el-button--small').click()
            pigcms.find_elements_by_css_selector('.addSpec.mb30 .turntip.flex')[0]. \
                find_element_by_css_selector('.el-input__inner').send_keys('规格二')
            pigcms.find_elements_by_css_selector('.addSpec.mb30 .turntip.flex')[1]. \
                find_element_by_css_selector('.el-input__inner').send_keys('再选_1')
            pigcms.find_elements_by_css_selector('.addSpec.mb30 button')[0].click()
            # 编辑详细规格
            pigcms.find_elements_by_css_selector('.spec')[0].\
                find_element_by_css_selector('.el-input__inner').send_keys('初选_2')
            pigcms.find_elements_by_css_selector('.spec')[0].find_element_by_tag_name('button').click()
            pigcms.find_elements_by_css_selector('.spec')[1]. \
                find_element_by_css_selector('.el-input__inner').send_keys('再选_2')
            pigcms.find_elements_by_css_selector('.spec')[1].find_element_by_tag_name('button').click()
            # 批量设置所有规格价格内容
            rannumber = ranNumber(6)
            pigcms.find_elements_by_css_selector('.flex.allSet.mb20 .el-input__inner')[0].send_keys(rannumber)
            price = '0.01'
            pigcms.find_elements_by_css_selector('.flex.allSet.mb20 .el-input__inner')[1].send_keys(price)
            pigcms.find_elements_by_css_selector('.flex.allSet.mb20 .el-input__inner')[2].send_keys(ranNumber(2))
            pigcms.find_elements_by_css_selector('.flex.allSet.mb20 .el-input__inner')[3].send_keys(50)
            pigcms.find_elements_by_css_selector('.flex.allSet.mb20 .el-input__inner')[4].send_keys(2)
            pigcms.find_element_by_css_selector('.flex.allSet.mb20 button').click()

    # 物流管理
    def setLogistics(self):
        '''
        设置物流信息
        '''
        # 设置运费
        pigcms.find_elements_by_css_selector('.logistics .turntip.flex')[0]. \
            find_element_by_tag_name('input').clear()
        pigcms.find_elements_by_css_selector('.logistics .turntip.flex')[0].\
            find_element_by_tag_name('input').send_keys('0.01')
        # 设置上架（默认上架）
        # 设置基础销量
        pigcms.find_elements_by_css_selector('.logistics .turntip.flex')[2]. \
            find_element_by_tag_name('input').clear()
        pigcms.find_elements_by_css_selector('.logistics .turntip.flex')[2]. \
            find_element_by_tag_name('input').send_keys('567')
        # 默认排序

    # 设置商品详情
    def setDetail(self, needtimes):
        '''
        设置商品详情
        '''
        # 点击下一步
        pigcms.find_element_by_css_selector('.nextbtn').click()
        pigcms.switch_to.frame(pigcms.find_element_by_css_selector('.edui-editor-iframeholder.edui-default iframe'))
        pigcms.find_element_by_tag_name('body').click()
        pigcms.find_element_by_tag_name('body').send_keys(goodsData[needtimes+1][2])
        pigcms.switch_to.parent_frame()
        # 保存
        pigcms.find_element_by_css_selector('.ml40').click()

if __name__ == '__main__':
    # 登录操作
    loginQxy()
    # 进入应用管理
    time.sleep(1)
    pigcms.find_element_by_link_text('应用模块').click()

    # 进入微商城
    time.sleep(2)
    applicationlist = pigcms.find_elements_by_css_selector('.el-submenu')
    i = 0
    for app in applicationlist:
        appname = app.text
        if '电商系统' in appname:
            # 进入商城内容
            app.click()
            break
        i += 1
    # 获取商城所有菜单
    menu = applicationlist[i].find_elements_by_css_selector('.el-menu-item')
    # 进入商城管理
    menu[0].click()
    # 添加商品
    groupName = input('输入一个商品分类及数量（如：男装 12）：')
    # 调用爬虫函数
    goodsData = goodsSipder(groupName[:2], 'goods', int(groupName[-2:]))

    '''
    添加数据操作
    首先人工确定需要添加数据的条数
    然后使用爬去的数据填充内容进行添加测试
    '''
    for i in range(int(groupName[-2:])):
        # 点击添加按钮
        pigcms.find_element_by_css_selector('.topOpaa.mb20.flex.flex-pack-justify button').click()
        # 初始化
        addgoods = AddGoods()
        # 填写表单
        addgoods.baseSet(i)
        from random import choice
        style = choice(range(2))
        addgoods.inventory(style)
        addgoods.setLogistics()
        addgoods.setDetail(i)
    pigcms.quit()