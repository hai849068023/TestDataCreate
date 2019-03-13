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