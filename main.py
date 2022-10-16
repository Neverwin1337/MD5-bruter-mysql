from asyncio import Task
import pymysql
from itertools import product
from time import sleep
from tqdm import tqdm
import hashlib
import pymysql






class conmysql():
    def __init__(self,host,user,password,database,table):
        self.table = table
        self.db = pymysql.connect(host=host,
                     user=user,
                     password=password,
                     database=database)
        self.cursor = self.db.cursor()
    
    def insert(self,text,hash):
        
        try:
   
            self.cursor.execute(f"INSERT INTO {self.table} VALUES ('{text}','{hash}')")
   
            self.db.commit()
        except:
   
            print(e)
            self.db.rollback()



class brute():
    
    def gentext(self,x=1):
        iter = ['0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']  
        for r in iter:
            for repeat in range(x,x+1):
                for ps in product(r,repeat=repeat):
                    yield ''.join(ps)
    def md5(self,text):
        return hashlib.md5(text.encode()).hexdigest()


    def start(self,slen,elen):
        self.task = []
        for i in range(slen,elen+1):
            self.task.append(i)
        for i in self.task:
            for text in tqdm(self.gentext(i)):
                md5h = self.md5(text)
                db.insert(text,md5h)



if __name__ == "__main__":
    try:
        bruter = brute()
        db = conmysql("20.196.84.78","root","a4b3c2d1","hash","MD5") #dbIP username pwd database table
        bruter.start(4,4)
    except:
        pass
    
    finally:
        db.db.close()

