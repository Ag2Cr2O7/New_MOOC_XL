from include.concern2ed import *
from include.savefile import *

filename="new/new关注与粉丝.csv"
savename="model/follow&ed.model"
x,y,z=[],[],[]
with codecs.open('new/new用户.csv',encoding='utf-8') as f: #打开文件
  items=csv.reader(f) #读取文件，这里不能直接输出
  for row in items:
    x.append(row[0]) #用户id
    y.append(row[5]) #关注数
    z.append(row[6]) #粉丝数
x.pop(0)
y.pop(0)
z.pop(0)
ori=len(x) #原数组大小
#去重
ump1,ump2={},{}
for i in range(len(x)):
    ump1[x[i]]=y[i]
    ump2[x[i]]=z[i]
x=list(ump1.keys())
y=list(ump1.values())
z=list(ump2.values())
print("原数组大小为{},去重后数组大小分别为:{},{},{}".format(ori,len(x),len(y),len(z)))

print("开始爬取...")
v=[["用户Id","关注数","粉丝数","关注的人","粉丝"]]
v1,v2=[],[]
for i,p in enumerate(x):
  print(str(i+1)+"/"+str(len(x)),end=' ')
  FollowInfo(v1,p) #关注数组
  FollowedInfo(v2,p) #粉丝数组
for i,p in enumerate(v1): #写入
    tmp=[x[i],y[i],z[i],v1[i],v2[i]]
    v.append(tmp)
save_to_csv(v,filename)
del v[0]
save1(v,filename=savename) #保存数据
print('数组已保存！')
print("写入文件：{}结束！".format(filename))
