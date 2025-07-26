St_name=input("Enter the student name:")
St_grade = int(input("Enter the student grade betwen 1-12"))
tution_fee = int(input("enter the tution base fee"))
topper_st = input("wheather the student is topper(yes or no) ")


if not(1<=St_grade <=12):
    print("student grade is invalid ")
    print("please enter grade  between 1-12")
else:
    discount =0
    if 9<=St_grade <=12:
        if topper_st.lower()=='yes':
            discount=20
        else:
            discount=10
    elif 6<=St_grade <=8 :
        discount=5
    elif St_grade<6:
        discount=0


   #for additional dicount
match St_grade:
    case 10:
        discount+=3
    case 12:
        discount+=5



total_fee = tution_fee-(discount/100)*tution_fee
total_discount = discount
discount_saved = tution_fee-total_fee


print(f"student name : {St_name}")
print(f"student grade : {St_grade}")

print(f"student topper : {topper_st}")
print(f"accademic tution fee  : {St_name}")
print(f"dicount percentage : {total_discount}")
print(f"discount amount saved : {discount_saved}")
print(f"Amount after discount {total_fee}")

