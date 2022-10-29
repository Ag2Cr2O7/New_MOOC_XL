from include.comfuncourse import *
import codecs
from include.savefile import save_to_csv

filename= "new/new课程与评价.csv"
f=open(filename,'w')
f.close()
data,name=[],[]
with codecs.open("new/new所有的心理课.csv", encoding='utf-8') as f: #打开文件
  items=csv.reader(f) #读取文件，这里不能直接输出
  for row in items:
    data.append(row[0]) #保存文件中第1列的用户id
    name.append(row[1])
data.pop(0) #第一个元素是列名称，所以要删掉
name.pop(0)
v=[["评论者id","id","评论时间","评论内容","评分","课程id","点赞数","课程名"]]
for index in range(len(data)): #课程的map数据
     print(str(index + 1) + "/" + str(len(data)), end='') #当前。总数
     CommonC(v, data[index],name[index]) #数组，课程id,页码
save_to_csv(v,filename)
print("写入文件：{}结束！".format(filename))

#统计
# x=[]
# with codecs.open(filename, encoding='utf-8') as f: #打开文件
#   items=csv.reader(f) #读取文件，这里不能直接输出
#   for row in items:
#     x.append(row[1]) #保存文件中第1列的用户id
# x.pop(0) #第一个元素是列名称，所以要删掉
# y=list(set(x))
# #print(y)
# s1=len(x)
# s2=len(y)
# print("心理学评价总数为{},参与人数为{}".format(s1,s2))

