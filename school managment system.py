students = ['test']
teacher = []
running = True

while running:
    print("School managment system\n")
    print("1. View Student")
    print("2. View Teacher")
    print("3. Add Student")
    print("4. Add Teacher")
    print("5. Update Student")
    print("6. Update Teacher")
    print("7. Delete Student")
    print("8. Delete Teacher")
    print("9. Exit")

    choice = int(input("choose an option: "))

    if choice == 1:
        if len(students) != 0:
            print("\nStudents")
            for i in range(0, len(students)):
                print((i+1),". ", students[i])
            print("")
        else:
            print("no records found\n")

    elif choice == 2:
        if len(teacher) != 0:
            print("\nTeacher")
            for j in range(0, len(teacher)):
                print((j+1), ". ", teacher[j])
            print("")
        else:
            print("no records found\n")

    elif choice == 3:
        print("")
        student_name = input("enter student's name: ")
        students.append(student_name)
        found = False
        for s in range(0, len(students)):
            if student_name == students[s]:
                print("record added successfully\n")
                found = True
        if found == False:
            print("error pls try again\n")

    elif choice == 4:
        print("")
        teacher_name = input("enter teacher's name: ")
        teacher.append(teacher_name)
        t_found = False
        for t in range(0, len(teacher)):
            if teacher_name == teacher[t]:
                print("record added successfully\n")
                t_found = True
        if t_found == False:
            print("error pls try again\n")

    elif choice == 5:
        if len(students) != 0:
            print("\nstudents: ")
            for q in range(0, len(students)):
                print((q+1),". ", students[q])

            choice_student = int(input("choose a student: "))

            students[choice_student-1] = input("update student's name: ")
            print("record updates successfully\n")
        else:
            print("no records found\n")

    elif choice ==6:
        if len(teacher) != 0:
            print("\nteacher: ")
            for m in range(0, len(teacher)):
                print((m+1),". ", teacher[m])
            print("")
            choice_teacher = int(input("choose a teacher: "))

            teacher[choice_teacher-1] = input("update teacher name: ")
            print("record updated successfully\n")
        else:
            print("no records found\n")

    elif choice == 7:
        if len(students) != 0:
            print("\nstudents")
            for e in range(0, len(students)):
                print((e+1),". ", students[e])
            print("")
            student_delete = int(input("choose a student to delete: "))
            students.pop(student_delete-1)
            print("record deleted successfully\n")
        else:
            print("no record found\n")

    elif choice == 8:
        if len(teacher)!=0:
            print("\nteacher")
            for o in range(0,len(teacher)):
                print((o+1),". ", teacher[o])
            print("")
            teacher_delete = int(input("choose a teacher to delete: "))
            teacher.pop(teacher_delete-1)
            print("record deleted successfully\n")
        else:
            print("no record found\n")

    elif choice == 9:
        print("\nsee you soon... :) \n")
        running = False
    
    else:
        print("\ninvalid option.. try again..\n ")