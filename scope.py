# code from https://www.programiz.com/python-programming/namespace

 def outer_function():
     # a within this function's scope is now 20
     a = 20

     def inner_function():
         # a within this function's scope is now 30
         a = 30
         print('a =', a)  # this is printed first
         # so it prints a = 30

     # then we enter the inner function
     inner_function()
     # then the inner function is exited, a in this function is still 20
     print('a =', a)  # this is printed second
     # so it prints a = 20


 # a in the global scope is set to 10
 a = 10
 # then we get into the outer function
 outer_function()
 # after exiting the outer function, a in the global scope is still 10
 print('a =', a)  # this is printed third
 # so it prints a = 10


 def outer_function2():
     # since these functions now declare that they are using the global a
     # the changes they make to a now stick, even outside of the functions
     global a
     a = 20

     def inner_function2():
         global a
         # this is the assignment to a that happens the latest
         # so all the print statements will say a = 30 as the functions unwind
         a = 30
         print('a =', a)  # this happens first

     inner_function2()
     print('a =', a)  # this happens second


 a = 10
 outer_function2()
 print('a =', a) # this happens third
 input()  # empty prompt so it does not exit right away when run
