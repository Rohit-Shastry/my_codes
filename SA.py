import time

#func to calc the TSA
def calc(length, breadth, height):
    Surface_Area = (2 * length * breadth) + (2 * length * height) + (2 * height * breadth)
    return Surface_Area

#creates a banner
def banner():
    print("---------------------------------------------")
    print("       Cuboid Surface Area Calculator        ")
    print("---------------------------------------------")
    print("Enter the details :- ")
    print("                                             ")
    time.sleep(2)


# ------------------------------------------------------------------------------
banner()#Func for the banner
#getting the input
length = int(input("Please enter the Length of the Cuboid:- "))
breadth = int(input("Please enter the Breadth of the Cuboid:- "))
height = int(input("Please enter the Height of the Cuboid:- "))
ans = calc(length, breadth, height)
print("[+]Calculation Complete...")
time.sleep(1)
print("[+] Total Surface Area = ", ans)
