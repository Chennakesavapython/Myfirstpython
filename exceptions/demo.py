#exception
print("program iis running")
n=10
l=23
print(n/l)


print("program is completed")

#error with with single error
print("program is running")
k=10
h=0
#print(k/h)#ZeroDivisionError: division by zero
print("program is executed")




#handling of an error

print("="*50)

print("program is running")
k=10
h=0
try:
    print(k/h)
except:
    print("OPPS! you got ERROR i.e denominator not to be Zero")    
print("program is executed")

print("="*50)

#without an error

print("program is running")
k=10
h=2
try:
    print(k/h)
except:
    print("OPPS! you got ERROR i.e denominator not to be Zero")    
print("program is executed")



#eror with multiple error
import sys
print("program is running")
data  = [1,2,3,4,"python",0,2]
for i in data:
    #print(1/i) #TypeError: unsupported operand type(s) for /: 'int' and 'str'
    #ZeroDivisionError('division by zero')
    try:
        print(1/i)
    except TypeError:
       # print(sys.exc_info())
        print("Dont pass string we cant divide  string and number")  
    except ZeroDivisionError:
        print("OPPS ! you can't divide by zero number")       

print('program is completed')  



print("="*50)


import sys
print("program is running")
data  = [1,2,3,4,3,2]
for i in data:
    #print(1/i) #TypeError: unsupported operand type(s) for /: 'int' and 'str'
    #ZeroDivisionError('division by zero')
    try:
        print(1/i)
    except TypeError:
       # print(sys.exc_info())
        print("Dont pass string we cant divide  string and number")  
    except ZeroDivisionError:
        print("OPPS ! you can't divide by zero number")       

print('program is completed') 




print("="*50)

print("program is running")
k=10
h=0
try:
    print(k/h)
except:
    print("OPPS! you got ERROR i.e denominator not to be Zero")   

else:
    print("calculation is successfull")#it is executed when there is no error in the try block.     
finally:
    print("program is executed")

print("="*50)




#exceptions class
print(help(Exception))


