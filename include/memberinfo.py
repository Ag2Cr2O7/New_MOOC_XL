#爬取慕课中json文件
import requests
from lxml import etree
import csv
import codecs
import pickle

def save(p,q,filename="default.model"):
    f=open(filename,'wb')
    pickle.dump((p,q),f)
    f.close()

def load(filename="default.model"):
    f=open(filename,'rb')
    p,q=pickle.load(f)
    f.close()
    return p,q

def PersonInfo(v,pn,f):
    total ="https://www.icourse163.org/home.htm?userId="+str(pn)+"#/home/course"
    url = 'https://www.icourse163.org/web/j/memberBean.getMocMemberPersonalDtoById.rpc?csrfKey=ff08c822a72243ceac0ccb4aa620ef89'
    # 在Headers中将相关的信息复制到此
    headers = {
        'origin': 'https://www.icourse163.org',
        'cookie': 'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; hb_MA-A976-948FFA05E931_source=www.icourse163.org; MOOC_PRIVACY_INFO_APPROVED=true; WM_NI=dKVBKfmXPgA%2Fwh87c0z4qxxB%2FF3v6eOyL%2BINVP0rtQrueNdymh9l8x3QJ%2FiZ%2BcnyC%2F%2BTzI1XAJ%2F63u%2FjhC3bnV2Fw4eE29lJ7NZBqwQtHuO3PUQUjYeysVytBENTul6TWjk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d1638ee9a088ec63899e8ba6c84a929a8ab0d54af3b2ff87e648908fafccd32af0fea7c3b92aa8959aa3ca6eaf88a088c425b5b8f8d8e23cbaecbf99fb4aed9afd97b56f8da784cccc4696900093f75bb2ababafe773afb8f78dbb74f18f86d0ec52e9bda29ac225e98cb6aab4548396e1d7b27fedb6a8a4b26aae8afea7f640a79bfedaef42f59296a3f47d93ac8896ce39948b9fb6e953a7a7bdb7fc80829b82b5f868f68c998bea37e2a3; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; NTESSTUDYSI=ff08c822a72243ceac0ccb4aa620ef89; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654346816478"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdQ/QUVZZfKf0Pxgcke8RYqe5aJjFmR3hGV5MZTONaaBupFbulDkW915EfD5jDmJaREuJCgkD6KwFke38U840RrMLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mtvV5h8hMdi2U1UCryBJRrYDqQQ17QSLEw7cos1siEnDHbCbECmTLOYqscT/BiS1FBwnA6MYF8Uvnq3xwKlHXIr7RsuwbR90XpjL+hV0QUPrbOWWUMY5UEU5JTybgsXB+KTZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654308063,1654311759,1654327367,1654346818; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654354909',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': total,
        'content-type': 'application/x-www-form-urlencoded'
    }
    # 这是请求所需的数据，在Payload->Form Data中将相关信息复制到此
    data = {
        "memberId": str(pn)
    }
    ret = requests.post(url=url, headers=headers, data=data)
    items = ret.json()["result"]  # 读取数据
    # print(items)
    if items:
        memberid_, descrip_, schoolid_, membertype_, hidegree_, followc_, followedc_ = [], [], [], [], [], [], []
        # for item in items:
        memberid_.append(items['memberId'])
        descrip_.append(items['description'])
        schoolid_.append(items['schoolId'])
        membertype_.append(items['memberType'])
        hidegree_.append(items['highestDegree'])
        followc_.append(items['followCount'])
        followedc_.append(items['followedCount'])
        # 第二部分数据
        url1 = 'https://www.icourse163.org/web/j/MocActivityScholarshipRpcBean.getActivityStatisticsByUser.rpc?csrfKey=17be623c07aa42f1ae0235561003a3d2'
        headers1 = {
            'origin': 'https://www.icourse163.org',
            'cookie': 'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; NTES_YD_PASSPORT=rS9mVP2KGeKhxJXV1FF8Ky6k7urOYCwCL4aCAZxH5948LRgoLmWedX.iIWaeykNASO03BbFJ.QOo0EmAD7bgUDEg3UYFBCZ.V8qZo.iuGN7j6Clpb9kgS4pxRX4IoyoKw28vdzNjGeJu_X9r5fj_PJIHlgw3hxQ9Bnz.Qx7gPQDiYkaV.paqbs7rw9HHV5JhtvT9Tt39hHo7.WKt0iHAiMVwS; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; MOOC_PRIVACY_INFO_APPROVED=true; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; hb_MA-A976-948FFA05E931_source=www.baidu.com; NTESSTUDYSI=17be623c07aa42f1ae0235561003a3d2; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1654417663841"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdQPJcxH2aFa95qP+qzcCe0A6eFyojyt55/A0VTd6i9dUN3a3J9gbyCniMhzQnNtUxyohvujTJ7JIUUBPJZb5hmILhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mtvzxdLM2yF03U/q1AEILV272U1G4WqzHZ17xfTA+7mbMZ3Jk5rECrrliwR4fO8KR7e8Zh+H62nNmCfeMHn7JT6uiEkB2g1Aq2fim9/SsjYujBh/dJZ8vw/X68tn3ZFPX2rZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1654346818,1654355945,1654356837,1654417665; WM_NI=FmfpBCCX2cmZQb1GgiZrVM9hdwoFDnoXMhTWfFeBSvKVCMjlHPT%2Brs3V%2FYqtQuoAIKshJHol%2FDmuxuhspRPgMlJNof2b4JOBWzrN3HsnUVFkmQmUUcx9gYA77QhwvVmKb2k%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb8ed7fbcbdb6b9d774878a8ea2d15a878b8fb0c14ab0ecad93ee618faca9b0aa2af0fea7c3b92a86b3aa91c1498188fe84f05293beffa8e6639aae9aaebc64a8a9a1a7c766ad888389d75da69aaba3d27e898a8daee9688c909cccf179f18ae1baf48093aba1a2cc41b1b886a9ee68ed9ca396fb7facadc0b3d36d8fb486afee6ef2befcabce4a95a6beafb244b1b29bb7c561af8fa3b6d869bce7a9bac43df58fa898f55eaf95aed3ea37e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1654417671',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
            'referer': str(total),
            'content-type': 'application/x-www-form-urlencoded'
        }
        # 这是请求所需的数据，在Payload->Form Data中将相关信息复制到此
        data1 = {
            "userId": str(pn).encode('UTF-8')
        }
        ret1 = requests.post(url=url1, headers=headers1, data=data1)
        if ret1.json()["result"]:
            items1 = ret1.json()["result"]["statistics"]  # 读取数据
            # print(items1)
            postc_, replyc_, commentc_, learnltc_ = [], [], [], []
            for item in items1:
                postc_.append(items1['postCount'])
                replyc_.append(items1['replyCount'])
                commentc_.append(items1['commentCount'])
                learnltc_.append(items1['learnLongTimeCount'])

            for i in range(1):
                tmp = [memberid_[i], descrip_[i], schoolid_[i], membertype_[i], hidegree_[i], followc_[i],
                       followedc_[i],
                       postc_[i], replyc_[i], commentc_[i], learnltc_[i]]
                v.append(tmp)
            print("爬取用户：{}成功！".format(pn)) #两个响应都成功
        else: #第一个响应成功，第二个响应失败
            print("爬取用户：{}失败!!!!!!!!!!!".format(pn))
            f.append(pn)
    else: #第一个响应就不成功直接到这里
        print("爬取用户：{}失败!!!!!!!!!!!!".format(pn))
        f.append(pn)


# str="4947184"
# str="8370161"

# v=[]
# PersonInfo(v,9845409)
# print(v)
