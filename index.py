import signup
import login

def main_prog():
    print("\t***Welcome***\n\n")
    print("\n\t1:Signup\n\n\t2:Login\n\n")
    ch=int(input("Enter your ch:"))
    if(ch==1):
        signup.dataEntry()
        input()
        main_prog()
    elif(ch==2):
        login.loginUser()
    else:
        exit()
main_prog()
