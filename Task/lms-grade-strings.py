#print lms grade tracker


print("="*30)
print("Grade Tracker")
print("="*30)

#validate id

st_id_valid = False

while not st_id_valid:
    st_id= input("enter your id")

    #check if valid id based on - sign
    if st_id.startswith("-")and st_id[1:].isdigit():
        print("please enter positive numbers only")

    #check if valid id
    if st_id.isdigit():
        st_id = int(st_id)
        if st_id>0:
            st_id_valid = True
        else:
            print("please enter non-zero value")
    else:
        print("enter only numbers")

        