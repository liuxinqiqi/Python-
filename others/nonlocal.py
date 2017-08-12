a = 1

def out():
    b = 2
    def inner():
        nonlocal b
        b += 1
        print (b)
        # global a
        # a += 1
        # print a
    inner()

out()
