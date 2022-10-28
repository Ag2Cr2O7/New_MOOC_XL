import  pickle
import csv
def save_to_csv(items, file):
  with open(file, "w", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in items:
      writer.writerow(item)

def save_to_csv_a(items, file): #追加保存，不会抹掉
  with open(file, "a+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in items:
      writer.writerow(item)

def save1(p,filename="default1.model"):
    f=open(filename,'wb')
    pickle.dump(p,f)
    f.close()

def load1(filename="default1.model"):
    f=open(filename,'rb')
    p=pickle.load(f)
    f.close()
    return p

def save2(p,q,filename="default2.model"):
    f=open(filename,'wb')
    pickle.dump((p,q),f)
    f.close()

def load2(filename="default2.model"):
    f=open(filename,'rb')
    p,q=pickle.load(f)
    f.close()
    return p,q

def save3(p,q,r,filename="default3.model"):
    f=open(filename,'wb')
    pickle.dump((p,q,r),f)
    f.close()

def load3(filename="default3.model"):
    f=open(filename,'rb')
    p,q,r=pickle.load(f)
    f.close()
    return p,q,r

def save4(p,q,r,s,filename="default4.model"):
    f=open(filename,'wb')
    pickle.dump((p,q,r,s),f)
    f.close()

def load4(filename="default4.model"):
    f=open(filename,'rb')
    p,q,r,s=pickle.load(f)
    f.close()
    return p,q,r,s