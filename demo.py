#if conditio
n=10
#check the given value is positive


if n>0:
    print(f"given {n}  is positive")




    #check the number in between 10 to 20 range

    n=18

    if n>=10 and n<=20:
        print(f"give num {n} is in range")



        #given is positive or negative

    n=-10
#check the given value is positive by if-else


if n>0:
    print(f"given num {n}  is positive")

else:
    print(f"give num {n} is negative")    

#input()-> or input takinng

email = input("enter the e-mail")
print(f"entered email is {email}")


#check vote eligibility

age1=int(input("enter the age"))

if age1>=18:
    print("you can vote")
else:
    print("you cant vote") 

    #check the given value is positive by ternary

    age1= int(input("enter the age"))
    status = "you can vote" if age1>=18 else "you cant vote"
    print(status)


#elif 

avg_score = int(input("enter he avg score"))
if avg_score>=90:
    print("A grade")
elif avg_score>=75:
    print("B grade")   
elif avg_score>=60:
    print("c grade")   
elif avg_score>=50:
    print("D grade")
else:
    print("fail")               


#Match case

choice = int(input("enter the choice"))
match choice:
    case 1 :
        print("one")
    case 2 :
        print("two")
    case 3 :
        print("three")
    case _:
        print("Invalid")   


#nested condition
#club entry ----> if age is 21 or abobe and else a valid id should be presented.
 age= 23
has_id = True

if age>=21:
    if has_id:
        print("your are allowed to enter")
    else:
        print("you need id to enter")
else:
    print("you are too younger to enter")            




