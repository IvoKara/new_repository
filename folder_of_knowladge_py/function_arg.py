def multiple_arg(some_arg, *marg):
    print(some_arg)
    print(type(marg))
    print(marg)
    print(*marg)
    #print(type(*marg))

multiple_arg(1,3,464,745)
multiple_arg(1,2)
multiple_arg(1,True, False)
multiple_arg("lol", "That", "is", "new!")

def def_arg(first_arg, def_arg = True):
    print(first_arg, def_arg)

def_arg(234)
def_arg("Not", "Default")

def keyword_arg(a, b, *marg, **kwarg):
    print(a, b, marg, kwarg)

keyword_arg(3,4,23,543,6)
keyword_arg(3,4,23,543,6, x="some str", y="other str")
