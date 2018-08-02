import sqlite3
import login

def deposit(acc_no,cash):
    conn= sqlite3.connect("Banking.db")
    cur=conn.cursor()
    cash=cash+int(input("Enter cash:"))
    sqlquery="update userData set cash={} where acc_no='{}';".format(cash,acc_no)
    conn.execute(sqlquery)
    conn.commit()
    print("Balance updated successfully")
    print("\nPlease login in again to check your Account balance:\n")
    balanceEnq()
#deposit()

def depositFun():
    acc_no=input("Enter the acc_no:")
    conn=sqlite3.connect("Banking.db")
    cur=conn.cursor()
    sqlQuery="select acc_no,cash from userData;"
    cur.execute(sqlQuery)
    data=cur.fetchall()
    try:
        for x in data:
            if(x[0]==acc_no):
                cash=x[1]
    except:
        print("")
    deposit(acc_no,cash)

def withdrawal():
    acc_no=input("Enter the acc_no:")
    user_name=input("Enter username:")
    password=input("Enter password:")
    withdrawalCash=int(input("Enter amount to withdraw:"))
    conn=sqlite3.connect("Banking.db")
    cur=conn.cursor()
    sqlQuery_1="select username,acc_no,cash,password from userData"
    try:
        cur.execute(sqlQuery_1)
    except Exception as e:
        print(e)
        print("Something went worng...\nTry again\n")
        input()
        login.displayChoice()
    data_1=cur.fetchall()
    flag=False
    data=[]
    cash=0
    try:
        for x in data_1:
            data.append(x)
        #print(data)
        for y in data:
            #print(y[0],y[1])
            if(y[0]==user_name and y[1]==acc_no and y[3]==password):
                cash=y[2]
                #print(cash,y[2])
                flag=True
                break
            else:
                flag=False
                #print("Try again Authentication Error")
                #login.displayChoice()
            print(cash)
    except Exception as e:
        print("Exit")
        print(e)
        exit()
    if(flag==True):
        if(withdrawalCash>cash):
            print("You dont have enough account balance...\nYour have Rs.{} in your account.".format(cash))
            login.displayChoice()
        else:
            cash=cash-withdrawalCash
            sqlQuery_2="update userData set cash={} where acc_no='{}';".format(cash,acc_no)
            conn.execute(sqlQuery_2)
            conn.commit()
            print("Rs.{} is debited from you Account".format(withdrawalCash))
    else:
        print("Try again Authentication Error")
        #login.displayChoice()
        print("Going back to welcome page2")

#withdrawal()
def balanceEnq():
    acc_no=input("Enter the acc_no:")
    #user_name=input("Enter username:")
    #password=input("Enter password:")
    #withdrawalCash=int(input("Enter amount to withdraw:"))
    conn=sqlite3.connect("Banking.db")
    cur=conn.cursor()
    sqlQuery_1="select acc_no,cash from userData"
    try:
        cur.execute(sqlQuery_1)
    except Exception as e:
        print(e)
        print("Something went worng...\nTry again\n")
        input()
        login.displayChoice()
    data_1=cur.fetchall()
    #flag=False
    data=[]
    try:
        for x in data_1:
            data.append(x)
        #print(data)
        for y in data:
            #print(y[0],y[1])
            if(y[0]==acc_no):
                #print("got it")
                cash=y[1]
                break
            else:
                cash=0
    except:
        print("Exit")
        exit()
    print("Your Account Balance is Rs.{}".format(cash))
    print("\n")
#balanceEnq()
