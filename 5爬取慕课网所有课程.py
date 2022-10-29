from include.Allcourse import *
from include.savefile import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36'}  # 请求头部
res = requests.get("https://www.icourse163.org/university/view/all.htm#/", headers=headers)
page = etree.HTML(res.text)
#['/university/PKU', '/university/NJU']
s = page.xpath('//*[@id="g-body"]/div/div[2]/div[2]//a/@href')
#print(s)
#print(len(s)) 学校总数
urls=[]
url = "https://www.icourse163.org"
#获取每个学校的网址
for i in s:
    urls.append(url+i)
for p in s:
    text="https://www.icourse163.org/"+p+"#/c"
coursenum=len(s) #当前的学校总数467

schoolid=[]
index=0
for i in urls[:coursenum]:
    print(index,i)
    index+=1 #下标
    schoolid.append(get_data(i)) #获取学校id
#print(schoolid) #学校id
save1(schoolid,"model/AllSchoolid")
print("schoolid数组保存成功！")
v=[]
for i in range(coursenum):
  print(str(i)+"/"+str(coursenum)+":",end='')
  Coursedata(v,s[i],schoolid[i]) #保存的数组，['/university/PKU']数组,课程id数组
a,b,c,d,e,f,g=[],[],[],[],[],[],[]
for i in range(len(v)):
  a.append(v[i][0])
  b.append(v[i][1])
  c.append(v[i][2])
  d.append(v[i][3])
  e.append(v[i][4])
  f.append(v[i][5])
  g.append(v[i][6])
savefile="model/Allcourses.model"
file="new/new所有慕课课程.csv"
save1(v,filename=savefile)
print("保存数组成功！")
ans=pd.DataFrame({"课程id":a,"课程名":b,"学校名":c,"学校简称":d,"开始时间":e,"教师id":f,"教师姓名":g})
ans.to_csv(file,index=True,index_label="序号")
print('写入文件{}完成!'.format(file))



#重新写文件解除注释
# v=load1("model/Allcourses.model")
# a,b,c,d,e,f,g=[],[],[],[],[],[],[]
# for i in range(len(v)):
#   a.append(v[i][0])
#   b.append(v[i][1])
#   c.append(v[i][2])
#   d.append(v[i][3])
#   e.append(v[i][4])
#   f.append(v[i][5])
#   g.append(v[i][6])
# file="new/new所有慕课课程.csv"
# ans=pd.DataFrame({"课程id":a,"课程名":b,"学校名":c,"学校简称":d,"开始时间":e,"教师id":f,"教师姓名":g})
# ans.to_csv(file,index=True,index_label="序号")
# print('写入文件{}完成!'.format(file))