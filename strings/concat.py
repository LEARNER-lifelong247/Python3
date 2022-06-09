
def attach(arg1, arg2):
    return arg1 + arg2
arg1, arg2 = input("Enter two strings with comma sperator: ").strip().split(",")
print(attach(arg1,arg2))
arg1, arg2 = input("Enter two intergers with comma sperator: ").strip().split(',')
print(attach(int(arg1),int(arg2)))