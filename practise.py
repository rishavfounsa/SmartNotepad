#a=input("Enter your elements")
#b=""
#for x in a:
    #if x.isalnum():
       # b=(b+x)
       # b.split()
#print(list([b]))

i=0
full_name=[]
def get_full_name():
    global i
    while i<=4:
        a=input("Type your full name ")
        full_name.append(a)
        if len(full_name)<2:
            print("Please enter your full name")
            continue
        else:
            break
        i=i+1
        return print(max(full_name))

def get_password():
    while True:
        b=input("Enter your password")
        if b > '8 and A':
         print("password should contain atleast 8 character with atleast one digit and 1 capital letter")
         continue
        else:
            break
get_full_name()
get_password()

