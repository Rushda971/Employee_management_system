# MENU DRIVEN  emp
#crud operation 

import mysql.connector
mydbs=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor=mydbs.cursor()

#create database
mycursor.execute("create database if not exists emp_db")
print("database created")

mycursor.execute("use emp_db")

mycursor.execute('''
     create table if not exists employees_details (
     id int auto_increment primary key,
     name varchar(30),
     dep varchar(20),
     role varchar(20),
     city varchar(20)
                 
)''')
print("table created successfully")

def menu():
    
    print('''MENU DRIVEN: 
               1.insert records
               2.update records
               3.delete records ''')
    
    user=int(input("Enter operation to perform (through number)"))
        
    if user == 1:
        insert_record()
        
    elif user == 2:
        update_record()
        
    elif user == 3:
        delete_record()
    
    
def insert_record():
    name=input("Enter name: ")
    dep=input("Enter department: ")
    role=input("Enter role: ")
    city=input("Enter city: ")
    
    #insert record(sql)
    sql="insert into employees_details(name,dep,role,city) values(%s,%s,%s,%s)"
    val=(name,dep,role,city)
    mycursor.execute(sql,val)
    
    mydbs.commit()
    
    print(mycursor.rowcount,"record inserted successfully")
    
def update_record():
   
    print('''
          1.update specific field
          2.update all''')
    #user with specific field
    user=input("enter your choose(in number): ")
    
    if user==1:
        field=input("Enter your (name/dep/role/city):").strip().lower()
        arr=["name","dep","role","city"]
        if field in arr:
            new_value=input("Enter new value: ")
            sql=f"update employees_details set {field}=%s where id=%s"
            val=(new_value,id)
            mycursor.execute(sql,val)
            mydbs.commit()
            print("Record updated successfully")
            
    elif user==2:
        name=input("Enter new name: ")
        dep=input("Enter new dep: ")
        role=input("Enter new role: ")
        city=input("Enter new city: ")
        sql="update employees_details set name=%s dep=%s role=%s city=%s where id=%s"
        val=(name,dep,role,city,id)
        mycursor.execute(sql,val)
        mydbs.commit()
        print("All fields are updated successfully")
    else:
        print("incorrect value are choosen")        
    #user with update all
    
def delete_record():
    user=input("Enter id to delete: ")
    sql="delete from employees_details where id =%s"
    mycursor.execute(sql)
    mydbs.commit()
    
menu()