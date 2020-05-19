def hello(var):
    print(var)
    if var == 10:
        return
    var  = var+1
    hello(var)

hello(1)