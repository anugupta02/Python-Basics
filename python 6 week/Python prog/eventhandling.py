from pymysql import *
con = connect(db="batch1200",user="root",password="root",host="localhost");
cur=con.cursor()
id=int(input("Enter Id: "))
name = input("Enter Name: ")
price=int(input("Enter Price:"))
#mysql.connect
cur.execute('insert into product values(%d,%s,%d)' %(id,name,price))
con.commit()
print("record inserted")
def show():
    cur.execute("select * from product")
    data = cur.fetchall()
    print("=========================================")
    print("ID\tProduct Name\tProduct Price")
    print("=========================================")
    for x in data:
        print(f"{x[0]}\t{x[1]}\t\t{x[2]}")
    print("=========================================")
    data = cur.fetchall()
    print(data)

show()
con.close()

#update and delete -->> study urself