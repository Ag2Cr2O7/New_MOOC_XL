import requests
from lxml import etree
import csv
XL_Course_info={
1206390810: "心理学基础",
1001573001: "心理学与生活",
1002032006: "生活心理学",
1001515007: "沟通心理学",
1003410001: "犯罪心理学",
1002525010: "心理学入门",
1003721005: "情商与智慧人生",
1461181181: "情绪与健康",
1463180163: "社会心理学",
1205793808: "好心态 如何自己造——心理健康教育",
1463180166: "异常心理与危机干预",
1206454819: "心理学工作伦理与督导",
1461522173: "心理统计学",
1003045001: "心理学导论",
1003570008: "跨文化沟通心理学",
1205921805: "社会心理学",
1002587003: "探索心理学",
1461106168: "人格理论与个人成长",
1206493811: "发展与教育心理学",
1003562006: "积极心理学",
1206451819: "生涯发展与职业心理素质提升训练",
1463199166: "抑郁症的心理辅导",
1461785175: "实验心理学概论：管理学和语言学实验研究方法入门",
1206624828: "发展心理学",
1207048816: "实验心理学",
1206504809: "实验心理学：学会研究身边的现象",
1002939001: "心理发展与个体成长——发展心理学",
1461542169: "医学心理学",
1206447827: "生理心理学",
1460925166: "心理学与生活",
1207058807: "发展与教育心理学",
1003016011: "人格心理学",
234018: "管理心理学（上）",
1205705805: "创新创业中的消费心理洞察",
1205897802: "大学生心理学",
1461602168: "运动心理学",
235011: "心理健康与创新能力",
1206450817: "教育心理学",
1207057808: "心理统计与SPSS",
1461588171: "E-Prime实验设计技术",
1003386001: "心理咨询与心理健康",
1206688841: "心理的进化",
1206459817: "心理健康教育概论",
1002883003: "大学生心理健康",
1206458841: "走近儿童的心理世界",
1001893005: "心理咨询的理论与方法：会谈技巧",
1452116189: "学生心理辅导",
1207172803: "合理定位与职业选择",
1460911197: "职业生涯发展与就业指导",
1207477804: "心理咨询理论和技术",
1205898801: "压力与情绪管理",
1462050164: "心身疾病预防与心理调节",
1002766015: "乐商对话",
1206448817: "幸福心理学",
1002124005: "心理学：我知无不言，它妙不可言",
1461514169: "儿童发展心理学",
1206457816: "心理健康教育实践（含技术 )",
1003545121: "音乐心理学",
1458703164: "心理学基础",
1002186003: "婚恋-职场-人格",
1002552002: "爱情心理学",
1205905816: "大学生心理健康教育",
1002329032: "大学生心理健康教育",
1463304164: "社会心理学",
1206450822: "你、我，我们——人际交往心理学",
1206462812: "心理健康传播与普及",
1001930012: "大学生心理健康漫谈",
1206460812: "设计心理学：体验与创意",
1458484161: "大学生心理健康教育",
1002141008: "走进心理学",
1461795173: "心理学与自我成长",
1001564002: "管理心理学（下）",
1206677844: "大学生心理健康",
95002: "当代青年心理学（一）认识青年篇",
1001669001: "成功心理与人才发展",
1464024177: "研究设计与数据分析",
94003: "当代青年心理学（三）青年自我意识篇",
93002: "当代青年心理学（二）青年身心发展篇",
1450185252: "学习心理学",
1205915811: "学校心理学：让每一个学生顺利成长",
1450188236: "社会心理学",
1002250016: "创造性心理学",
1002923022: "发展心理学",
1206609801: "大学生心理健康教育",
1456046164: "“疫情心理防护”科普微课",
1206386810: "心理健康与心理咨询",
1002545001: "自我认知与情绪管理",
1003019012: "幸福心理学",
1206454837: "心理诊断学",
1003026007: "异常心理学（变态心理学）",
1205777805: "罪犯心理矫治"
}

def CommonC1(v,cid,name,page=1):
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
        "courseId": cid,
        "pageIndex": str(page),  # 页号
        "pageSize": "20",
        "orderBy": "3",
    }
    ret = requests.post(url=url, headers=headers, data=data)
    pgcount=ret.json()["result"]["query"]["totlePageCount"]
    if ret.json()["result"]["list"]:
        items = ret.json()["result"]["list"]  # 读取数据
        commentorid_, id_, commenttime_, content_, mark_, courseid_, agreecount_, coursename_ = [], [], [], [], [], [], [], []
        for item in items:
            if item['commentorId']!=1138255848:
              commentorid_.append(item['commentorId'])
              id_.append(item['id'])
              commenttime_.append(item['gmtModified'])
              content_.append(item['content'])
              mark_.append(item['mark'])
              courseid_.append(data["courseId"])
              agreecount_.append(item['agreeCount'])
              coursename_.append(name)
        # 拼接
        for i in range(len(mark_)):
            tmp = [commentorid_[i], id_[i], commenttime_[i], content_[i], mark_[i], courseid_[i], agreecount_[i],
                   coursename_[i]]
            v.append(tmp)
        print("爬取《{0}》页面{1}/{2}成功！".format(cid, page,pgcount))
    else:
        print("爬取《{0}》页面{1}/{2}失败！".format(cid, page,pgcount))
    return pgcount


def CommonC(v,cid,name):
    p = CommonC1(v,cid,name,1) #先爬第一页获取数据
    for i in range(2,p+1): #爬取剩下的页数
        CommonC1(v,cid,name,i)



