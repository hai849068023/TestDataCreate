# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/3/8 9:13'
from config import pigcms,loginQxy
import time
from auth.JDspiders.Spider import JdSpider


# 登录操作
loginQxy()
pigcms.implicitly_wait(10)

# 进入应用管理
pigcms.find_element_by_link_text('应用管理').click()

# 进入拼团页面
time.sleep(2)
applicationlist = pigcms.find_elements_by_css_selector('.el-submenu')
for app in applicationlist:
    appname = app.text
    if '微拼团' in appname:
        # 进入拼团内容
        app.click()
        # 获取拼团所有菜单
        menu = app.find_elements_by_css_selector('.el-menu-item')
        # 进入拼团管理
        menu[0].click()

        # 添加拼团操作内容
        addbutton = pigcms.find_elements_by_css_selector('.topOpaa.mt20.flex.flex-pack-justify button')
        addbutton[0].click()

        # 内容创建流程规划
        pass
