from include.memberinfo import *
from include.savefile import *
filename="new/new用户.csv"
x=[]
with codecs.open('new/new课程与评价.csv', encoding='utf-8') as f: #打开文件
  items=csv.reader(f) #读取文件，这里不能直接输出
  for row in items:
    x.append(row[0]) #保存文件中第一列的用户id
x.pop(0) #第一个元素是列名称，所以要删掉
x=list(set(x))
v1=[["评论者id","简介","学校id","类型","最高学历","关注数","粉丝数","贴子数","回复数","评论数","学习时长"]]
save_to_csv(v1,filename) #先将标题放入
v1=[]
f=[] #保存访问失败的用户id
for i in range(len(x)): # [begin,end)
  print(str(i+1)+"/"+str(len(x)),end=' ')
  PersonInfo(v1,x[i],f) #学生信息存入v1
save_to_csv_a(v1,filename) #先保存访问成功的
print("写入文件：{}结束！".format(filename))

#处理失败的访问，反复循环
f=list(set(f))
if len(f)>0:
  print('需要处理第一次访问失败的用户列表...({})'.format(len(f)))
  for p in f:
    print(p)

file="model/UserInfo.model"
save2(v1,f,filename=file) #保存数组
print('数组保存成功！')

x,y=load2(filename=file) #加载v1和f的数组信息
print('读取成功用户和失败用户的数组信息...')
# print('v1=')
# print(x)
print('f=')
print(y)

#处理第一次访问失败的用户
#PersonInfo(newv1,uid,newf) #再次访问失败的
#["评论者id","简介","学校id","类型","最高学历","关注数","粉丝数","贴子数","回复数","评论数","学习时长"]
x.append(["1399886128","","","","","0","0","0","0","0","85"]) #实在爬不进去手工添加数据
x.append(["3448559","","","","","0","0","0","136","1","2377"])
x.append(["1144180836","","","","","0","0", "0","8","0","236"])
x.append(["1444092586","","","","","0","0", "0","0","0","17"])
x.append(["1482704765","","","","","0","0","0","1","0","22"])
x.append(["1137369856","","","","2","0","0","18","10","6209","4","483597"])
x.append(["1387217510","","","","","0","0",  "0","0","0","326"])
x.append(["1445136014","","","","","0","0",  "0","0","0","24"])
x.append(["1027226014","深度学习  收获交叉学科的复利","","1","3","17","54","64","1591","31","1042458"])
x.append(["1443867925","","","","","0","0",  "1","2","0","165"])
x.append(["1443946326","","","","","0","0",  "0","15","0","352"])
x.append(["9845409","","","2","0","127","96","48","10423","2","855747"])
#加上第一行的标题栏
x.insert(0,["评论者id","简介","学校id","类型","最高学历","关注数","粉丝数","贴子数","回复数","评论数","学习时长"])
save_to_csv_a([["3448559","","","0","","","0","0","136","1","2377"]],filename)
save_to_csv(x,filename)
del x[0] #只保存数据
save(x,y)
print("写入文件：{}结束！".format(filename))

# x,y=load() #加载xy的数组信息
# print('读取成功用户和失败用户的数组信息...')
# print('f=')
# print(y)


