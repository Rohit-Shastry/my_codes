import time

num = input("Please enter the number of digits:- ")
print("[+]Printing pi in 3,2,1..")
time.sleep(3)

try:
    # import version included with old SymPy
    from sympy.mpmath import mp

except ImportError:
    # import newer version
    from mpmath import mp

mp.dps = num  # set number of digits(limit)
print(mp.pi)   # print pi to a thousand places
