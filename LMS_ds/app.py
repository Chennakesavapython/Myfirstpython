#lms project using data structures

#system information

SYSTEM_INFO = ("LMS Student Portal","v1.0","2025","LMS University")
ADMIN_INFO = ("chennakesavarao89@gmail.com","7989004552","201")

#DISPLAY SYSTEM INFO
print("="*50)
print(f"WELCOME TO {SYSTEM_INFO[0]}")  #WELCOME TO LMS SSTUDENT PORTAL  BY USING TUPLES WE DO THIS
print(f"DEVELOPED BY {SYSTEM_INFO[3]}") #DEVELOPED BY LMS UNIVERSITY
print("="*50) 

#STORE ALL THE STUDENTS
#to store details we use dictionaries

Students = {}

#start with menu selection or option selection
#we use lopping system

while True:
    print("Choose an option from (1-5): ")
    print("1.Add student")
    print("2.Update student")
    print("3.delete student")
    print("4.List all students")
    print("5.exist system")


    choice = input("Enter Your Choice: ")

    if choice =="1":
        print("Performming Operation 1")
        std_id  = input("enter the student Id : ")
        #if exists
        if std_id in Students:
             print("student Id already exists in the system")
        else: 
            std_name = input("enter student name").title()
            #store multiple scoores
            scores = []
            while True:
            
             score_input = input("enter the score or done: ") 
             #validate input it num or done
             if score_input == "done":
                 break
             if score_input.isdigit():
                score = int(score_input)

                if 0 <= score <= 100:
                 scores.append(score)
                else:
                 print("Score should be between 1-100")
             else:
                print("Score should be numbers only")    

            # store multiple unique skills
            skills = set()
            while True:
                skill_input = input("enter the skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input.strip().title())

            #save student details received so d=far
            Students[std_id] = {
                "name": std_name,
                "scores":scores,
                "skills": skills
            }      
            print("student added successfully!")

            #for verification
            print(Students)          
                  
                     



    elif choice =="2":
        print("Performming Operation 2")  
        std_id = input("enter the student ID :  ")
        if std_id in Students:
            new_name = input("Enter NEW NAME to Update").title()
            Students[std_id] ["name"] = new_name
            print("Student Updation is successfully")
        else:
            print("student ID doesn't exists")  
            print(Students)  



    elif choice == "3":
         print("Performming Operation 3")
         std_id = input("enter the student Id : ")
         removed = Students.pop(std_id,None)
         if removed:
             print("student removed successfully!")
         else:
             print("student doesn't exists")
             print(Students)    

    elif choice == "4":
         print("Performming Operation 4")
         #studentid --> std_id
         #skills
         #scores
         #students
         if not Students:
             print("No students Available")
         else:
             print("="*50)
             print("STUDENT DETAILS") 
             print("="*50)


             for sid, data in Students.items():#items() is used when the keys and values are available in the data
                 name = data["name"]
                 scores = data["scores"]


                 if scores:
                     avg = sum(scores)/len(scores)
                 else:
                     avg = 0
                 if scores:
                     top_score = max(scores)        
                 else:
                     top_score = 0
                 skills = data["skills"] 
                 print(f"ID: {sid}") 
                 print(f"Name: {name}")
                 print(f"scores: {scores}")
                 print(f"Avarage Score : {avg}")   
                 print(f"Top Score : {top_score}")
                 print(f"skills count : {len(skills)}")

    elif choice == "5":
         print("Performming Operation 5")
         print("="*50)
         print("Contact Admin for further queries")
         print(f"admin contact {ADMIN_INFO[0]}")
         print(f"admin contact {ADMIN_INFO[1]}")
         print("="*50)
         
        

         break
    else: 
         print("Invalid Choice")     
         print("please select from above options")  


