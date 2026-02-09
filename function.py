# # particular business logic is called function , Functions are used to reuse the business logic
# def db_call():
#     print("MongoDB connection soon..")
# db_call()
# No parameters and return type 

# def db_call(username,password):
#     print("Login success") if username== "admin" and password== "admin@123" else print("login fail")
# db_call("admin","admin@123")
# with parameters

# def db_call():
#     return "DB Connection soon..."
# res = db_call()
# print(res)
# with parameters & return types

# res=""
# def db_call(username, passoword):
#     if username =="admin" and passoword == "admin@123":
#         res= "login success"
#     else:
#         res ="Login failed"
#     return res
# x = db_call("admin","admin@123")
# print(x)


# def greet(msg="Good evening!!"):
#     print("Hello", msg)
# greet()
# greet("Good Morning")

# def add(*numbers):
#     print(sum(numbers))
# add (10,20,30)

# def square(num):
#     return num*num
# res =square(10)
# print(res)

# res = lambda num: num*num
# print(res(10))

# def outer():
#     def inner():
#         print("Hello, Inner function")
#     inner()
# outer()

# add =lambda a,b:a+b
# print(add(100,200))
