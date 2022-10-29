import requests

def CourseJoin1(v,pn,page):
    pname=str(pn)
    s1="https://www.icourse163.org/home.htm?userId="
    s2=str(pname)
    tmpstr = [s1,s2]
    # str="4947184"
    # str="8370161"
    total ="".join(tmpstr).encode('utf-8')
    url = 'https://www.icourse163.org/web/j/learnerCourseRpcBean.getOtherLearnedCoursePagination.rpc?csrfKey=f03e9fe78d68403593ea981d996eec4e'
    # 在Headers中将相关的信息复制到此
    headers = {
        'origin': 'https://www.icourse163.org',
        'cookie': 'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; MOOC_PRIVACY_INFO_APPROVED=true; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; hb_MA-A976-948FFA05E931_source=www.baidu.com; WM_NI=IEs%2FyzlUgU8jUsnc4b6zovtcxGPuvJKhDlJRNm%2FBJeCBvLd27nKQfq5LpfB5KnwvVe1WRAceyCnL6lrOzhNB%2F5%2BpLTigYTYfkvqXus80vn%2BJXF4TQM92zfqYntw8s5elaGo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed2f842b2bd99a9e942baef8ea3c15a929e8f82c44eacf5b6b2f250f28abeb0f22af0fea7c3b92a8b9bbdd0fc72b08ba9b6bb6297ada284b76af6a6a197f769bc99a096f54289b88c8dc95a8eb3e1a3c96f819ebaade73af5b285b2e57bf794c087c13f89b2b997d56ff3899ea2e26fbb9da2adb568b291b689cd4aedebe591cf60abb997b5dc6ea9aabfb9f879fcf0ba8faa429c9afcb5d447fbeeb687f453aeacb9d9f23fa7b4afa8ee37e2a3; NTESSTUDYSI=f03e9fe78d68403593ea981d996eec4e; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654592762862"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdV6phSRy8nqqJTAGcr8tajAQ8GizSidSAX8kFR50vqjc4hlrKx4IW0RVj73ERyc8QIx9ae9/oxaCCLWPLVzkQTkLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mtsovcEKcHQg20GRdYm5KRlsxghbZLwWwN2SuMpiCD9ylAC6CSC8tPLgjcUupyjAmu30F+ynRDV9YS8gFHntL09c9/FVjR91yAynbLCToSOdlhkOiEplSEq+omuEZUqya9TZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654482856,1654484959,1654587445,1654592764; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654610296',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': total,
        'content-type': 'application/x-www-form-urlencoded'
    }
    # 这是请求所需的数据，在Payload->Form Data中将相关信息复制到此
    data = {
        "uid": str(pname),
        "pageIndex": str(page),
        "pageSize": "32"
    }
    ret = requests.post(url=url, headers=headers, data=data)
    if ret.json()["result"]["list"] is None: #如果没有关注人
      sz=0
    else:  #关注了人
      sz=len(ret.json()["result"]["list"])
    #print(sz)
    for index in range(0,sz):
      v.append(ret.json()["result"]["list"][index]["courseId"]) # 读取id数据

    #print("爬取用户名{0}，页码{1}/{2}结束！".format(pname,page,r et.json()["result"]["query"]["totlePageCount"]))
    return ret.json()["result"]["query"]["totlePageCount"]
#关注信息
def CourseJoin(v,pn): #数组，用户id
    tmp=[]
    p=CourseJoin1(tmp,pn,1) #
    for i in range(2,p+1):
        CourseJoin1(tmp,pn,i) #先看第一页
    v.append(tmp)
    print("爬取用户{0}参与的课程结束！".format(pn))

# v=[]
# FollowInfo(v,8370161) #少
# CourseJoin(v,"1035736710") #多
# print(v)