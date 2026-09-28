# Global

# x = 20                                       #Global 
# print("Inside function:",x)

# def f():
#     print("Outside function:",x)
# f()


# Local
# def f():
#     x=20         # local
#     print("Inside function:",x)
# f()
# print("Outside function:",x)       # error(veliyil vilichaal work aavilla local aayondu)


# a way to access local:

# def f():
#   global x
#   x = 20                                #you can access local by using global keryword
#   print("Inside f function:",x)

# def g():
#     y = 30
#     print(x)
# print("Inside g function:",y)
# f()
# g()




