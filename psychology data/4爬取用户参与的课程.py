from include.member_join_course import *
from include.savefile import *
import codecs

filename="new/new用户参与的课程.csv"
x=[]
with codecs.open('new/new关注与粉丝.csv',encoding='utf-8') as f: #打开文件
  items=csv.reader(f) #读取文件，这里不能直接输出
  for row in items:
    x.append(row[0]) #用户id
x.pop(0)
v=[["用户id","参与的课程数","参与的课程"]]
v1=[]
for i,p in enumerate(x):
  print(str(i+1)+"/"+str(len(x)),end=' ')
  CourseJoin(v1,p) #关注数组
for i,p in enumerate(v1): #写入
    tmp=[x[i],len(v1[i]),v1[i]]
    v.append(tmp)
save_to_csv(v,filename)
savename="model/CourseJoin.model"
del v[0]
save1(v,filename=savename) #保存数据
print('数组已保存！')
# v=pd.DataFrame({"用户ID": x,"参与的课程": v1}) #第一列为数字序号
# v.to_csv(filename)
print("写入文件：{}结束！".format(filename))