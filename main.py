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
        except Exception as e:
   
            print(e)
            self.db.rollback()



class brute():

    def gentext(self,x=1):
        iter = ['1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']  
        for r in iter:
            for repeat in range(x,x+1):
                for ps in product(r,repeat=repeat):
                    yield ''.join(ps)
    def md5(self,text):
        return hashlib.md5(text.encode()).hexdigest()


    def start(self,slen,elen):
        for i in range(slen-1,elen+1):
            for text in tqdm(self.gentext(i)):
                md5h = self.md5(text)
                db.insert(text,md5h)



if __name__ == "__main__":
    bruter = brute()
    db = conmysql("127.0.0.1","root","root","hash","MD5") #dbIP username pwd database table
    bruter.start(1,3)
    db.db.close()

