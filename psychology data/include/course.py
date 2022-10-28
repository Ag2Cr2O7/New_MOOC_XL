#爬取慕课中json文件
import requests
from lxml import etree
import csv

def save_to_csv(items, file):
  with open(file, "a+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in items:
      writer.writerow(item)

#ctrl+R刷新，找到元素所在的文件mocCourseV2RpcBean.get...并复制其地址到此处
def no1_XLXYSH(v,page=1):
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=f53df406309946cc9be63bde7ca98dc5'
    # 在Headers中将相关的信息复制到此
    headers = {
        'origin': 'https://www.icourse163.org',
        'cookie': 'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=VQVri%2BVK3x2xcBnTwuMKntQ%2BHyzOX6lPB%2B9oHbdfTIqBA7LvnlubtjbrG2e0eCfI8mXu3%2FFZJz4tGBLuVM00EoOsaana6OivuQfwbtwBn1bgtO5PJiCxT2wvSo%2FjvfIyWDQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed1c74aa2bc9eb7f84ae9ef8aa2c85b928b9bacd45bb5b39f8be5638288828ec52af0fea7c3b92a968f9a93ec219695fd99b174a19ea2b5f67f8f95a295d4218ca7b6b0db3eb0908eccbc658cbeac87d743b39e8fd8cf7eaeb4bb83f762a2ae89d3e83ca79daaaabb679cabfdd0c5528aa6fc95c64a90ab9aaeb33c87b18194e46baebffab0ec7eb78faa98e180b59ea2d2e16db891fbb1c96381a89cd3f67e91b1e18bf56e8ba799a5d437e2a3; WM_TID=4HxxUqSSjZJFBVFBBVaRAlmVnPjQWdjU; NTESSTUDYSI=f53df406309946cc9be63bde7ca98dc5; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654247282464"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdTHx34sebKQ8S3avkSAD+3XMFXATDTtKp6sls1B/oqYNsvKu7cdJJSLtiUDMWxqyuUMDEpj5vhnSQy6MVPXQzf0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mtveQ8nG8daX2DwKmplO0TuEZxxJZwr2duILDeXin9jhAfuCi0y0Zhn71bqd06yQV9029JuakE7oYjO5A8nj0vb2/LL50xjm99NSwXtsS0SK9m2WbEEfxZfZFYks8yZuKqXZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654226375,1654239566,1654244826,1654247283; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654255876',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/NJU-1001573001',
        'content-type': 'application/x-www-form-urlencoded'
    }
    # 这是请求所需的数据，在Payload->Form Data中将相关信息复制到此
    data = {
        "courseId": "1001573001",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    #数据处理
    commentorid_ ,id_, commenttime_ ,content_,mark_,courseid_,agreecount_,coursename_=[],[],[],[],[],[],[],[]
   #心理学与生活
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append('心理学与生活')
    #拼接
    for i in range(len(mark_)):
        tmp = []
        tmp.append(commentorid_[i])
        tmp.append(id_[i])
        tmp.append(commenttime_[i])
        tmp.append(content_[i])
        tmp.append(mark_[i])
        tmp.append(courseid_[i])
        tmp.append(agreecount_[i])
        tmp.append(coursename_[i])
        v.append(tmp)
    print("爬取《心理学与生活》页面{}结束！".format(page))

###############################2##################################################################
# def no2_HIT(v,page=1):
#     url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=7bbf52fe144d4490ad4bc110a48423c3'
#     headers = {
#         # 不变
#         'origin': 'https://www.icourse163.org',
#         'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=7bbf52fe144d4490ad4bc110a48423c3; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654311752229"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdUefAJzDVDyXil0NALfZ8udoX+O4XePatUVOusx+c83fRjvTZ8UYWiFG2WSN2/SZLfYXqTUPDFYiMehnieAiAQsLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttHOoHS7F7IaNmAlsoVkNOyB2bRoBaUPl6nAAnAOF5Ry/+6PMxrIn6+u8fj43BmF4dqaflFNff5r5EZFIf4ide2FGsdyqcLgcsYMp9UmXCMkMvMbTN6tDkcNBCsvAqADt3ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654244826,1654247283,1654308063,1654311759; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654311975',
#         #不变
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
#         'referer': 'https://www.icourse163.org/course/HIT-1002032006',
#         # 不变
#         'content-type': 'application/x-www-form-urlencoded'
#     }
#     data = {
#         "courseId": "1002032006",
#         "pageIndex": str(page),  # 页号
#         "pageSize": "20",
#         "orderBy": "3",
#     }
#     ret = requests.post(url=url, headers=headers, data=data)
#     items = ret.json()["result"]["list"]  # 读取数据
#     commentorid_ = []
#     id_=[]
#     commenttime_ = []
#     content_=[]
#     mark_ = []
#     courseid_=[] #1001573001
#     agreecount_ = []
#     coursename_=[] #心理学与生活
#     for item in items:
#         commentorid_.append(item['commentorId'])
#         id_.append(item['id'])
#         commenttime_.append(item['gmtModified'])
#         content_.append(item['content'])
#         mark_.append(item['mark'])
#         courseid_.append(data["courseId"])
#         agreecount_.append(item['agreeCount'])
#         coursename_.append('生活心理学')
#     #拼接
#     for i in range(len(mark_)):
#         tmp = []
#         tmp.append(commentorid_[i])
#         tmp.append(id_[i])
#         tmp.append(commenttime_[i])
#         tmp.append(content_[i])
#         tmp.append(mark_[i])
#         tmp.append(courseid_[i])
#         tmp.append(agreecount_[i])
#         tmp.append(coursename_[i])
#         v.append(tmp)
#     print("爬取《生活心理学》页面{}结束！".format(page))

###################################2###############################################
def no2_GTXLX(v,page=1):
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'

    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654333464',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/HIT-1001515007',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1001515007", #只改这个
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_ ,id_, commenttime_ ,content_,mark_,courseid_,agreecount_,coursename_=[],[],[],[],[],[],[],[]
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append('沟通心理学')
    #拼接
    for i in range(len(mark_)):
        tmp = []
        tmp.append(commentorid_[i])
        tmp.append(id_[i])
        tmp.append(commenttime_[i])
        tmp.append(content_[i])
        tmp.append(mark_[i])
        tmp.append(courseid_[i])
        tmp.append(agreecount_[i])
        tmp.append(coursename_[i])
        v.append(tmp)
    print("爬取《沟通心理学》页面{}结束！".format(page))

###################################3###############################################
def no3_FZXLX(v,page=1):
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654333686',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/cupl-1003410001',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1003410001",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_ ,id_, commenttime_ ,content_,mark_,courseid_,agreecount_,coursename_=[],[],[],[],[],[],[],[]
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append('犯罪心理学')
    #拼接
    for i in range(len(mark_)):
        tmp = []
        tmp.append(commentorid_[i])
        tmp.append(id_[i])
        tmp.append(commenttime_[i])
        tmp.append(content_[i])
        tmp.append(mark_[i])
        tmp.append(courseid_[i])
        tmp.append(agreecount_[i])
        tmp.append(coursename_[i])
        v.append(tmp)
    print("爬取《犯罪心理学》页面{}结束！".format(page))

##########################4444444444#################################
def no4_XLXDL(v,page=1):
    nm = "心理学导论"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654334393',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/UESTC-1003045001',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1003045001",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_ ,id_, commenttime_ ,content_,mark_,courseid_,agreecount_,coursename_=[],[],[],[],[],[],[],[]
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    #拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

##########################4444444444#################################
def no5_TSXLX(v,page=1):
    nm="探索心理学"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654334393',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/UESTC-1003045001',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1003045001",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_ ,id_, commenttime_ ,content_,mark_,courseid_,agreecount_,coursename_=[],[],[],[],[],[],[],[]
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    #拼接
    for i in range(len(mark_)):
        tmp=[commentorid_[i],id_[i],commenttime_[i],content_[i],mark_[i],courseid_[i],agreecount_[i],coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))


##########################66666#################################
def no6_RGXLX(v,page=1):
    nm="人格心理学"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654334975',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/CNU-1003016011',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1003016011",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_ ,id_, commenttime_ ,content_,mark_,courseid_,agreecount_,coursename_=[],[],[],[],[],[],[],[]
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    #拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

#########################77777#################################
def no7_GLXLX_1(v,page=1):
    nm="管理心理学（上）"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654343468',

        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/UESTC-234018',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "234018",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

#########################77777#################################
def no7_GLXLX_2(v,page=1):
    nm="管理心理学（下）"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654343721',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/UESTC-1001564002',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1001564002",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

############################8888888888$$$$$$$$$$$$$$$$$$$$$$$$
def no8_XLJKYCXNL(v,page=1):
    nm="心理健康与创新能力"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654343926',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/UESTC-235011',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "235011",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

########################9999#########################
def no9_XLXWZWBY_CCNU(v,page=1):
    nm="心理学：我知无不言，它妙不可言"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654344284',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/CCNU-1002124005',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1002124005",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

########################10101010#########################
def no10_YYXLX(v,page=1):
    nm="音乐心理学"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654344482',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/SHNU-1003545121',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1003545121",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

#######################111111#########################
def no11_HLZCRG(v,page=1):
    nm="婚恋-职场-人格"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654344859',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/WHUT-1002186003',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1002186003",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

#######################121212#########################
def no12_AQXLX(v,page=1):
    nm="爱情心理学"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654345039',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/WHUT-1002552002',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1002552002",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

#######################131313#########################
def no13_ZJXLX(v,page=1):
    nm="走进心理学"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654345331',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/SWJTU-1002141008',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "1002141008",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

#######################141414#########################
def no14_DDQNXLX_1(v,page=1):
    nm="当代青年心理学（一）认识青年篇"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654345514',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/SWJTU-95002',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "95002",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

#######################141414#########################
def no14_DDQNXLX_2(v,page=1):
    nm="当代青年心理学（二）青年身心发展篇"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654345610',
        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/SWJTU-93002',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "93002",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))

#######################141414#########################
def no14_DDQNXLX_3(v,page=1):
    nm="当代青年心理学（三）青年自我意识篇"
    #在同一个文件中就不变
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc?csrfKey=04ba973687f04180b3154f9cd3449dff'
    headers = {
        # 不变
        'origin': 'https://www.icourse163.org',
        #'cookie':'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654345721',

        'cookie': 'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=04ba973687f04180b3154f9cd3449dff; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654327363964"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdffMHvn6phJjtrZfJ3T/fJ3T+0xplVv1A3Vyd08Bgt8MCCLwnQGe6p1UXJWaXcgUnjYUhijngEnnSlBSTwziDO0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttE/8BVsKX/ACCD1SwAytCDVzXl+oNl+q+uSBSaQm4fs5I7/7IHYPPWlA58nsD+l9R6S5HpxGANr5jCxm3RZqxddIBNG2WkjcONoi3hdYyUkj6ABzpiYJ/GLSd5keFYHK7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654247283,1654308063,1654311759,1654327367; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654345610',

        #不变
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': 'https://www.icourse163.org/course/SWJTU-94003',
        # 不变
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "courseId": "94003",
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["list"]  # 读取数据
    commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
    for item in items:
        commentorid_.append(item['commentorId'])
        id_.append(item['id'])
        commenttime_.append(item['gmtModified'])
        content_.append(item['content'])
        mark_.append(item['mark'])
        courseid_.append(data["courseId"])
        agreecount_.append(item['agreeCount'])
        coursename_.append(nm)
    # 拼接
    for i in range(len(mark_)):
        tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
               coursename_[i]]
        v.append(tmp)
    print("爬取《{0}》页面{1}结束！".format(nm,page))