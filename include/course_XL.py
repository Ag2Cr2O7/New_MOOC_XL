import requests
from lxml import etree
import csv
import codecs

def findpj(str,cid): #课程网页获得评价条数
    total=str
    url = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getEvaluateAvgAndCount.rpc?csrfKey=910d79dddc854d868ab5914fda253226'
    # 在Headers中将相关的信息复制到此
    headers = {
        'origin': 'https://www.icourse163.org',
        # 'path': '/web/j/channelBean.getCustomCourseModuleVo.rpc?csrfKey=61c303d38e5d4630ab3de249fd373283',
        'cookie': 'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; MOOC_PRIVACY_INFO_APPROVED=true; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; hb_MA-A976-948FFA05E931_source=www.baidu.com; WM_NI=JSzFqexnxqVsUIIVSe6YwKUgKoq7B8rq9jTuHrwmaFOhaoBQSvDpHDOezge1IXNMzVD10tI3TjyIqjDwzCIRbHO%2BsIhw7zCjCnlxwyU6NmZ2wnHUew0MFoE3hr43B32fODU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea5ce59e9eda297e13da2bc8fa7c45f838a9bb0c45ef8be868ed625f4b2a995d82af0fea7c3b92a8a8db6a7f46fbcb2b892d579979787b7d26ff687b9acd86d89b1bfd8c134b2aff78bd77f8caeb98ee44e8db8af90c15b91aa8c91cb508dbbb688e83b8b8882aef95e88ef0095cc3998b6b7aaf46288a9b6a4cc5aa29881ccf243aca9f99bc26281b2a499f67397ea828ed93ab5b288b6e87df4938a90c839acaefcd4c139f2ba81a5d837e2a3; NTESSTUDYSI=910d79dddc854d868ab5914fda253226; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1656157421839"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdUD5gFGGlGf/PQMWJBxGdZxbtF+Wvtf66GyjBRAetIlPFcX65mBS6PLGoOrTWWwxHF0gewG75zxYhGO8VuUW7c0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mttg9Wuw4zdlHI0UQ1tX5fE5RXrUeVQ6mJxHV0cXNWycGmm8joTCfe1WLWj2uIVRaEuh3bAFw7GVI3GzmrUvSwiuDVZCOD6EbrPbfCQheML7QDrAq4hrMkyjQMYMR/nsoUTZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1655976173,1656070267,1656157096,1656157423; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1656159337',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': total,
        'content-type': 'application/x-www-form-urlencoded'
    }
    # 这是请求所需的数据，在Payload->Form Data中将相关信息复制到此
    data = {
        "courseId": cid
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]["evaluateCount"]  #
    return items


def CourseInfo1(v,page):
    total ="https://www.icourse163.org/channel/3007.htm?cate=1001043135&subCate=-1"
    url = 'https://www.icourse163.org/web/j/mocSearchBean.searchCourseCardByChannelAndCategoryId.rpc?csrfKey=61c303d38e5d4630ab3de249fd373283'
    mydata="{'categoryId':'1001043135','categoryChannelId':'3007','orderBy':0,'stats':30,'pageIndex':"+str(page)+",'pageSize':'20'}"
    # 在Headers中将相关的信息复制到此
    headers = {
        'origin': 'https://www.icourse163.org',
        #'path': '/web/j/channelBean.getCustomCourseModuleVo.rpc?csrfKey=61c303d38e5d4630ab3de249fd373283',
        'cookie': 'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; MOOC_PRIVACY_INFO_APPROVED=true; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; hb_MA-A976-948FFA05E931_source=www.baidu.com; NTESSTUDYSI=61c303d38e5d4630ab3de249fd373283; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654827856986"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdcC+HrNHt+PmvmZQLBGgPDgHTwx3QmgmMfKURGki6/Yi/w99QxR9avSJGSGk37QiHziFZG/qWTQ4AHdzW8KgN28Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mtuW1zjgInQKA8TPm3rJ3P1WU0rsbepDY24N1VOlrgdThkEwn1vRD6DldYS3i6Z5SZUVAYlu3WqMc9HHOfZ7WKwU6lo8vaRiB6+xie9CTiE0IZ8+yD5hvhGR1ezNm0tTj1TZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654592764,1654658145,1654661491,1654827860; WM_NI=jDLCCSISoCRUWxzb1%2Bx990Em8hAHj54D4fO%2FObbCvSkI3jlcDLSxoew976SJ1exgKAhMHJtY36fr2jT29jdZr9MaLe%2F55fvBxXQ17pE2tRrKbw4Bu2EQ%2FixYuM7P1BAeYnE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb4e263acb79abae544aea88fb2d84a928b8a82c85ff18881b0e446a2eb8993d32af0fea7c3b92aaa9c84a4c2598b8da1a4d15f95a8b683b421bce7f7d1c867fcb88fa9e93ff89cfc87ce258dbeaea4f559a997fd8bef6988949d99ee6fb5e7f9d7d242f3bbb888ca4bac9388abf753f1eaaa93b16298eef78be752b2e78382cf6fedebfb87f54abc889fd2b67c87eebcb3f141a2a9fca3f83a878fe18afb53b793f9b1b44a83bb978fc837e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654830220',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': total,
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    # 这是请求所需的数据，在Payload->Form Data中将相关信息复制到此
    data = {
       "mocCourseQueryVo": mydata
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items=ret.json()["result"]["list"]  #print(items) #课程列表

    courseid,coursename,schoolid,schoolname,teacherid,teachername,canjia,pingjiarenshu=[],[],[],[],[],[],[],[]
    for item in items:
        courseid.append(item["mocCourseBaseCardVo"]["id"])
        coursename.append(item["mocCourseBaseCardVo"]["name"])
        schoolid.append(item["mocCourseBaseCardVo"]["schoolId"])
        schoolname.append(item["mocCourseBaseCardVo"]["schoolName"])
        teacherid.append(item["mocCourseBaseCardVo"]["teacherId"])
        teachername.append(item["mocCourseBaseCardVo"]["teacherName"])
        canjia.append(item["mocCourseBaseCardVo"]["enrollCount"])

        web = item["mocCourseBaseCardVo"]["schoolSN"]  # 学校简称
        web = "https://www.icourse163.org/course/"+web+"-"+str(item["mocCourseBaseCardVo"]["id"]) #该课程的网站
        pingjiarenshu.append(findpj(web,item["mocCourseBaseCardVo"]["id"])) #评价有多少条

    for i in range(len(courseid)):
        tmp=[courseid[i],coursename[i],schoolid[i],schoolname[i],teacherid[i],teachername[i],canjia[i],pingjiarenshu[i]]
        v.append(tmp)
    print("爬取全部心理学课程页码{0}/{1}结束！".format(page,ret.json()["result"]["query"]["totlePageCount"]))
    return ret.json()["result"]["query"]["totlePageCount"]
#关注信息
def CourseInfo(v): #数组，用户id
    p=CourseInfo1(v,1) #
    for i in range(2,p+1):
        CourseInfo1(v,i) #先看第一页

#
# v=[]
# CourseInfo(v) #少
# print(v)
