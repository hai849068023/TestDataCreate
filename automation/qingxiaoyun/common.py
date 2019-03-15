# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/3/11 15:03'
# 定义一下公用组件方便代码复用
from config import pigcms


def updateImage(groupName, imagedir):
    getGroupslistele = pigcms.find_elements_by_css_selector('.li.typename.clearfix')
    is_group = True
    for groupele in getGroupslistele:
        if groupName in groupele.text:
            groupele.click()
            is_group = False
            break
    if is_group:
        # 添加分组
        pigcms.find_element_by_css_selector('.el-icon-circle-plus-outline').click()
        pigcms.find_element_by_css_selector('.setAddClassify input').send_keys(groupName)
        pigcms.find_element_by_css_selector('.el-icon-circle-check.i1').click()
        pigcms.find_elements_by_css_selector('.li.typename.clearfix')[-1].click()
    # 选中创建的分组
    getGroupslistele = pigcms.find_elements_by_css_selector('.li.typename.clearfix')
    for groupele in getGroupslistele:
        if groupName == groupele.text:
            groupele.find_element_by_tag_name('em').click()
            break
    # 上传图片操作
    pigcms.find_element_by_css_selector('.el-upload__input').send_keys(imagedir)
    # 选择上传的图片
    is_uped = True
    while is_uped:
        import time
        time.sleep(1)
        is_show = pigcms.find_elements_by_css_selector('.thinScrollbarMy li')[0].text
        if is_show == imagedir[-12:]:
            get_imglist = pigcms.find_elements_by_css_selector('.thinScrollbarMy li')
            for img in get_imglist:
                if imagedir[-12:] == img.text:
                    img.click()
                    is_uped = False
                    break
        else:
            print('图片未上传成功继续等待...')
    return 'success'


def timeSet(days=7):
    '''
    设置开始时间
    days参数是指活动周期天数默认7天
    调用时只要直接调用函数即可操作点击输入框并选择时间输入 
    '''

    # 点击开始时间框
    pigcms.find_elements_by_css_selector('.el-date-editor--datetime')[0].click()
    # 设置活动开始时间
    pigcms.find_element_by_css_selector('.el-button--text').click()

    # 设置结束时间
    # 点击结束时间框
    pigcms.find_elements_by_css_selector('.el-date-editor--datetime')[1].click()
    # 点击可选时间段第days天的时间点
    pigcms.find_elements_by_css_selector('.el-picker-panel__content')[1].\
        find_elements_by_css_selector('.available')[days].click()
    pigcms.find_elements_by_css_selector('.is-plain')[1].click()
    return 'success'


