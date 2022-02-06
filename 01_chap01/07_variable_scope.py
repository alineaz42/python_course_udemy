# local and global
va1 = "python"


def abc():
    global var2
    var2 = "world"
    print(var2)


abc()
print(va1+var2)