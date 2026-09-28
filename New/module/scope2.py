def outer():
    x = 20          #Nonlocal/enclosing: it can be accessed both inner and outer function
    print("Outer:",x)
    
    def inner():
        print("Inner:",x)
        return
    
    inner()

outer()