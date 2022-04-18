# def function1():
#     print("subscribe now")

# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum

# a = funcret(1)
# print(a)

# def executer(func):
#     func("this")

def dec1(func1):
    def nowexec():
        print("Executing Now..")
        func1()
        print("func1 executed")
    return nowexec

# @dec1
def whoisharrry():
    print("harry is a good boy")

# whoisharrry = dec1(whoisharrry) #this can be written in similar manar using @ symbol followed by function name 
whoisharrry()