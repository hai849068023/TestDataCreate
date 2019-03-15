# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/3/8 9:13'
from config import pigcms,loginQxy
from random import choice
import time


class AddPintuan:
    # 活动基础设置
    def setActivite(self, times):
        # 获取所有元素
        get_formele = pigcms.find_elements_by_css_selector('.turntip.flex')[:4]
        # 输入活动名称
        get_formele[0].find_element_by_tag_name('input').send_keys('老妖拼团第{}弹'.format(times))
        # 输入活动时间
        from automation.qingxiaoyun.common import timeSet
        timeset = timeSet(5)
        # 设置参团人数
        get_formele[2].find_element_by_tag_name('input').send_keys(choice(range(501)[1:501]))
        # 设置限购
        if choice(range(2)) == 0:
            # 去除限购设置
            pigcms.find_element_by_css_selector('.el-checkbox.is-checked').click()
        else:
            get_formele[3].find_element_by_tag_name('input').send_keys('2')

    # 设置商品内容
    def setGoods(self):
        pass




if __name__ == '__main__':
    # 登录操作
    loginQxy()
    pigcms.implicitly_wait(10)

    # 进入应用管理
    time.sleep(1)
    pigcms.find_element_by_link_text('应用模块').click()

    # 进入拼团页面
    time.sleep(2)
    applicationlist = pigcms.find_elements_by_css_selector('.el-submenu')
    i = 0
    for app in applicationlist:
        appname = app.text
        if '多人拼团' in appname:
            # 进入拼团内容
            app.click()
            break
        i += 1
    # 获取拼团所有菜单
    menu = applicationlist[i].find_elements_by_css_selector('.el-menu-item')
    # 进入拼团管理
    menu[0].click()

    # 添加拼团操作内容
    for i in range(15):
        # 点击添加按钮
        pigcms.find_elements_by_css_selector('.flex-pack-justify button')[0].click()

        # 初始化
        addpintuan = AddPintuan()
        addpintuan.setActivite(1)
