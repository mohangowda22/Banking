import sqlite3 as sql
import transaction
def displayChoice():
    print("\n\n\t***Welcome***\n")

    print("\t1:Deposit\n\t2:Withdrawal\n\t3:Balance Enq\n\t0:Exit\n")
    ch=int(input("Enter ur choice:"))
    if(ch==1):
        transaction.depositFun()
        input("\nPress Enter...\n\n")
        displayChoice()
    elif(ch==2):
        transaction.withdrawal()
        input("\n\nPress Enter...\n\n")
        displayChoice()
    elif(ch==3):
        transaction.balanceEnq()
        input("\nPress Enter....\n")
        displayChoice()
    elif(ch==0):
        exit()
    else:
        print("\nEnter valid choice\n")
        displayChoice()




def loginUser():
    conn=sql.connect("Banking.db")
    cur=conn.cursor()
    user_name=input("Uername:")
    password=input("Password:")
    if (user_name=="" and password==""):
        print("Please check username and password")
    else :
        query_1="select username,password from userData;"
        cur.execute(query_1)
        rows=cur.fetchall()
        #op in tuple
        #print(rows)
    for row in rows:
        if (row[0]==user_name and  row[1]==password):
            flag=True
            #print("User valid")
            break
        else:
            flag=False
            #print("Failed")

    if(flag==True):
            print("\n"*4)
            displayChoice()
    else:
            loginUser()

#loginUser()

if __name__ == '__main__':
    main()
