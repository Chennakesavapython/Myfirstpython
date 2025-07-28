st_id = input("enter the student id")
st_name = input("enetr student name")
st_attendance = float(input("enter the attendance percentage"))

total_score = 0
subject_count = 0


while True:
    subject_count +=1
    score = int(input(f"enter the score of subject {subject_count}"))
    total_score +=score
    choice = input("do you want to add another subject please enter yes or no")

    if choice !="yes":
        break
average_score = total_score/subject_count

if average_score>=85:
    performance = "Excellent"
elif average_score>=75:
    performance = "good"
elif average_score >=50:
   performance = "average"
else:
    performance ="need Improvement"

if st_attendance>=75:
    attendence = "attendane is satisfied"
else:
    attendence = "Warning - low attendance"


print("///// STUDENT DETAILS")
print(f"student name : {st_name}")
print(f"student Id : {st_id}")
print(f"student attendance {st_attendance} %")
print(f"total score : {total_score}")
print(f"total number of subject is : {subject_count}")
print(f"average score is : {average_score}")
print(f"performance : {performance}")
print(f"attendance status : {attendence}")                       