import pandas as pd
import os
import pickle
import requests
import re
import requests
from lxml import etree
def get_data(url):
    h = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    # headers = {
    #     'cookie': 'EDUWEBDEVICE=2238272f616d4e99ad13968d8d17f809; __yadk_uid=t0iXnOH0k9JwcF8PTqxAhWmcwBDP4dtF; hb_MA-A976-948FFA05E931_source=www.google.com; WM_TID=ILwtvT7dT6RBFRQFUFd%2FxCfvKSYqEX5l; NTES_YD_PASSPORT=.s7xlH654bAgEJPo5Gfxb88hqQiqK5gHzvTFL6hTdethXQ9oyGH_5xUlolOCxE7NVVp8_BfZ2ktClDexY90T8_s2y7l1LenYOdxGQgYC0YKBgWTqdYSIfqES0SxNn2okp3n.vwQ.ySQX7VayQuYz4MW_vzPgPwyOH68bz4tqXyowTdX4MN_6Q18wKAuf59E6DHY5twbVeamUZ4a5J73N6a6bt; P_INFO=13717378202|1616508252|1|imooc|00&99|hongkong&1615101737&epay#gud&441900#10#0#0|&0|null|13717378202; __utma=63145271.1945292559.1616508903.1616508903.1616508903.1; __utmz=63145271.1616508903.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); NTESSTUDYSI=5a94833dae334cbd9c15b67ff50ee25f; STUDY_INFO="yd.9c87ec9048f04d6bb@163.com|8|1141190892|1617063201131"; STUDY_SESS="HSWw+UKn4Fn/O1hClGLQDIgcvj9DLtzp2edCyM/BR4m1IcnA9H2BXSSGOe/wVXK3SjPKhIFzp/bViei9eLNWz2ojWiKvzIqgaCZdCbaQNnyxPz2EhX65A6NRYMLs3r50nf0b6Zou8l1d0Es+es1Uik2hRGd4LmYBRWoHTK34u4MLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="BrgWbQ8sf5eHRWkAZTjIHfiw+0/gMJH4njBby+08N4vY7AZsnFf2cUVqsF945RigeyMhSStj4PT/4nU0qHRwHRjdf8CF46rXRI2Hin7O4CpgzceCvEQ5mo30i372i2Z4AxMvPml6mpNk3inuq+uFl0Turwg5WrfPIFGaczvXc+4OXKAv4OA41eproyM6T3UORoOye1j8TeMGVnGgNBZ7cmkPLlDKoC7+/tDf/+PjaW/ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1141190892#|#1527731391171; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1616160084,1616508185,1617063203; WM_NI=fOdEwe9ZJX7RjhodcQzLpF1Lyb06n7AunM7WDcdUFKWkxg8GdbQILkpd8MBfPttrsbD4f%2BGSbrzPUC84%2BfZ%2Fn56kXZ5uPzJckekfDAKicMVswW2to4%2Fq3dpGNQVMxckqb3Q%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed1d9728de8aea2ea39b1868ba2c54f929f9fbaf5688a8a8aacf77df1b3aca6e82af0fea7c3b92aa691aca6f66ffb8686b9b65aaab8a185e25bba94c0a7b448bbbe00d7ed3d83aba2aeb65d88bdacb6c54195b5b888bb4da8be9faacf61b4bcf8aec16e94acbc93f26a88ecaaccc659a2aeb6b1d849fcece587d925aeebfa8cdb52f7aba09bc969a9bba587c74b89b7adaed579b589fe95ee40edaffd85f34d8e8f9aaefb69a9afaed4d437e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1617066587',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    # }
    #
    # sd = {
    #     'origin': 'https://www.icourse163.org',
    #     'cookie': 'EDUWEBDEVICE=2238272f616d4e99ad13968d8d17f809; __yadk_uid=t0iXnOH0k9JwcF8PTqxAhWmcwBDP4dtF; hb_MA-A976-948FFA05E931_source=www.google.com; NTES_YD_PASSPORT=.s7xlH654bAgEJPo5Gfxb88hqQiqK5gHzvTFL6hTdethXQ9oyGH_5xUlolOCxE7NVVp8_BfZ2ktClDexY90T8_s2y7l1LenYOdxGQgYC0YKBgWTqdYSIfqES0SxNn2okp3n.vwQ.ySQX7VayQuYz4MW_vzPgPwyOH68bz4tqXyowTdX4MN_6Q18wKAuf59E6DHY5twbVeamUZ4a5J73N6a6bt; P_INFO=13717378202|1616508252|1|imooc|00&99|hongkong&1615101737&epay#gud&441900#10#0#0|&0|null|13717378202; __utma=63145271.1945292559.1616508903.1616508903.1616508903.1; __utmz=63145271.1616508903.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); NTESSTUDYSI=4832f42c38cd47c982ac779abf327d21; STUDY_INFO="yd.9c87ec9048f04d6bb@163.com|8|1141190892|1617193630442"; STUDY_SESS="HSWw+UKn4Fn/O1hClGLQDIgcvj9DLtzp2edCyM/BR4m1IcnA9H2BXSSGOe/wVXK3SjPKhIFzp/bViei9eLNWz4r75dqQC5euKvC6vYnkhVEiQpx2QJ03IM8Y1I82kN0y6LO8AyazsdGR5hO7CgVNuTkaWURJxfgOPSX+abPid6ULhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="BrgWbQ8sf5eHRWkAZTjIHfiw+0/gMJH4njBby+08N4vY7AZsnFf2cUVqsF945RigeyMhSStj4PT/4nU0qHRwHRjdf8CF46rXRI2Hin7O4CpbNVqauTGgffj8vKdN89WJQkVyH7lJvPuwgiudz2UqyOoJBj6bCGlgQ/f0pcfC5rTZaCt052U2BlAlDQcFZqHzRGmDBh8X9qdMm3xyxOTZ1uFcNL5qjyWwL3zNPvI0nV3ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1141190892#|#1527731391171; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1616160084,1616508185,1617063203,1617193634; WM_NI=DJiSnswLEbxl6xBEK0PSm2EcrTJQzRl33g2Mp283KRSCxCslaTzI5U8DHti7s+//xZHxHebnEtCbtd2VMQHCIQJN4NRD2Dst6Eay+QacKPN9hIHAqtbjQGgDCPLnyol0YTc=; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb3ae4887ed87aded70948e8ab7c45a868f8eaaaa648a8d8aafc14d97b6a18ac92af0fea7c3b92a8896a7b4ed79b5948b83fb68f6a88ea6ca3c948da3d3c869b28c86b2f95ab0edfd88b147b4eef8d4ca5a919db8a4f268a38cb6aab85ffc9c8895ec3db1f5e1d0fb528ca88886e16687ac8d83f770f28a83b2cb498b8f86afb746929cfea5f280f69baf9aaa5ba3bd85b1cd33ac9788a2f480a2b69fa8e6508190848ffc65b0f097b5e237e2a3; WM_TID=ILwtvT7dT6RBFRQFUFd/xCfvKSYqEX5l; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1617193966',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    #     'referer': 'https://www.icourse163.org/course/PKU-21016',
    #     'content-type': 'application/x-www-form-urlencoded'
    # }
    r = requests.get(url, headers=h).text
    schoolId = re.findall(r'schoolId = "(\d+)"', r)[0]
    return schoolId


def Coursedata1(v,cstr,cid,page=1):
    url = 'https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?csrfKey=638e95f214264cc8b5994a4496ebbee3'.encode('UTF-8').decode("latin1")
    # 在Headers中将相关的信息复制到此
    headers = {
        'origin': 'https://www.icourse163.org',
        'cookie': 'EDUWEBDEVICE=ab76c39957d245f082d4243c271aff02; __yadk_uid=N9ZVMMfjUg6BnOQ9clafTva4IIm515ll; P_INFO=18987350670|1654177889|1|imooc|00&99|null&null&null#fuj&350200#10#0|&0|null|18987350670; MOOC_PRIVACY_INFO_APPROVED=true; WM_TID=ey%2FaBvgRMUJBQERABAbQVwIIrZi4KnYw; hb_MA-A976-948FFA05E931_source=www.baidu.com; NTESSTUDYSI=638e95f214264cc8b5994a4496ebbee3; STUDY_INFO="yd.2276988ae5be4dbbb@163.com|8|1456852832|1656640695685"; STUDY_SESS="Ec0iw8CkPdSDb4f80NFEO9XLuHsKSykCodGmqP8I40vOUpxonN18Y/9F90l+bb0nv6ZbSj5d94KDZbQch7YMdTlBrg+kFaY99pfZGvFj8E31w3sUbaX2OA5YTSpZGMc4s6YyGAz85SaQwcYHaowWBGcZrIuGdfEe1xEUXrWz3NcLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="6lUj1WQur5ws3+/xkcr2JyJRMhQ/cdbJ8al482a4hrT1Vx5IbPp82oiP24UplD89CiiWmdbvVB6DufZboPl388tOSVUdCVTs499MePd9mts+TXSjWH1UwMZ4tNhgr/Mje5h6LIV1A/LsLWwRL6abL8mj4W3EfnDFDL7xiZRlXMWOs4aVkfCtGeeSMZFc7FgUKOGaEzZU5ZZDs/oy8LK3RGKW/LUVmwFIog9XuyL7pT7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1456852832#|#1612723608349; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1656487181,1656507094,1656511082,1656640707; WM_NI=1aOJ6r1amExGdXipxXuLIl1oTFTp1k5lb0oxvaaSi48tsA1uUgj6XQZtqbLbhWr%2FX035BcDNl%2FOosk2KsXi3%2FTUS7o3JFpd8UxVg52zOO%2BDofWBbUk80PHRV2RTXE5ugeDc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee88f83cb7aaaf90f245a68a8fa6d54f879a9fadd44ff8adbbadb766b286fe85c22af0fea7c3b92af3bf81abb57af3bfa3a6fb4da888a791fb54b794878db465989a9c91b461f7b4aed1ee74b6bfafb4ec40fcacbda2b47f97b9a6d7db5b9aacbf83cf6aac89bed0db3cf1eb8e84c746b0f18190f261f295bdb9ec39ed8c9bb4b665f1968a91e73497a89a88b83aba9181ccc765a6898e83d861fcf0a0a9d15ef28e9cb9c83fb7b9aba5e237e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1656651398',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'referer': ('https://www.icourse163.org'+cstr).encode('UTF-8').decode("latin1"),
        'content-type': 'application/x-www-form-urlencoded'
    }
    # 这是请求所需的数据，在Payload->Form Data中将相关信息复制到此
    data = {
        "schoolId": cid,
        "p": str(page),  # 页号
        "psize": "20",
        "courseStatus": "30",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    pgcount=ret.json()["result"]["query"]["totlePageCount"]
    if ret.json()["result"]["list"]:
        items = ret.json()["result"]["list"]  # 读取数据
    #     commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
        for item in items:
            #课程id,课程名，学校名，学校简称，开始时间，教师id，教师姓名
            tmp=[item["id"],item["name"],item["schoolName"],item["schoolSN"],item["startTime"],
                item["teacherId"],item["teacherName"]]
            v.append(tmp)
        print("爬取《{}》页面{}/{}成功！".format(cstr,page,pgcount))
    else:
        print("爬取《{}》页面{}/{}失败！".format(cstr,page,pgcount))
    return pgcount

#
def Coursedata(v,cstr,cid):
    p = Coursedata1(v,cstr,cid,1) #先爬第一页获取数据
    for i in range(2,p+1): #爬取剩下的页数
        Coursedata1(v,cstr,cid,i)



