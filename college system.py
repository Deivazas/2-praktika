import mysql.connector as mysql

db = mysql.connect(host="localhost",user="root",password="",database="academic system")
command_handler = db.cursor(buffered=True)
class login:

    class session():

        def teacher_session():
            while 1:
                print("")
                print("Teacher Menu")
                print("1. Evaluate student")
                print("2. View student grades")
                print("3. Edit student grades")
                print("4. Logout")

                user_option = input(str("Option : "))
                if user_option == "1":
                    print("")
                    print("Mark student register")
                    command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
                    records = command_handler.fetchall()
                    date = input(str("Date : DD/MM/YYYY : "))
                    for record in records:
                        record = str(record).replace("'","")
                        record = str(record).replace(",","")
                        record = str(record).replace("(","")
                        record = str(record).replace(")","")
                        status = input(str("Status for " + str(record) + " " "1,2,3,4,5,6,7,8,9,10 : "))
                        query_vals = (str(record),date,status)
                        command_handler.execute("INSERT INTO evaluation (username, date, grade) VALUES(%s,%s,%s)",query_vals)
                        db.commit()
                        print(record + " Marked as " + status)
                elif user_option == "2":
                    print("")
                    print("Viewing all student registers")
                    command_handler.execute("SELECT username, date, grade FROM evaluation")
                    records = command_handler.fetchall()
                    print("Displaying all registers")
                    for record in records:
                        print(record)
                elif user_option == "3":
                    print("")
                    print("Enter student username to edit grades")
                    username = input(str("Username : "),)
                    command_handler.execute("UPDATE grade FROM evaluation WHERE username = %s",username)
                    records = command_handler.fetchall()
                    db.commit()
                    for record in records:
                        print(record)

                elif user_option == "4":
                    break
                else:
                    print("No valid option was selected")

        def admin_session():
            while 1:
                print("")
                print("Admin Menu")
                print("1.Create users database")
                print("2.Create evaluation database")
                print("3. Create student group")
                print("4. Create subject")
                print("5. Register new Student")
                print("6. Register new Teacher")
                print("7. Assign students to the group")
                print("8. Add teacher's/student's to subject")
                print("9. Delete Existing Student")
                print("10. Delete Existing Teacher")
                print("11. Delete Student Group")
                print("12. Delete Subject")
                print("13. Delete Students from group")
                print("14. Delete teacher's/student's from subject")
                print("15. Logout")

                user_option = input(str("Option : "))

                if user_option == "1":
                    print("")
                    print("Create users database")
                    command_handler.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), privilege VARCHAR(255))")
                    db.commit()
                    print("Users database created")

                elif user_option == "2":
                    print("")
                    print("Create evaluation database")
                    command_handler.execute("CREATE TABLE evaluation (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), date VARCHAR(255), grade VARCHAR(255))")
                    db.commit()
                    print("Evaluation database created")

                elif user_option == "3":
                    print("")
                    print("Create student group")
                    command_handler.execute("CREATE TABLE pi21a (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), privilege VARCHAR(255))")
                    db.commit()
                    print("Student group created")

                elif user_option == "4":
                    print("")
                    print("Create subject")
                    command_handler.execute("CREATE TABLE subject (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), privilege VARCHAR(255))")
                    db.commit()
                    print("Subject created")

                elif user_option == "5":
                    print("")
                    print("Register New Student")
                    username = input(str("Student username : "))
                    password = input(str("Student password : "))
                    query_vals = (username,password)
                    command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'student')",query_vals)
                    db.commit()
                    print(username + " has been registered as a student")

                elif user_option == "6":
                    print("")
                    print("Register New Teacher")
                    username = input(str("Teacher username : "))
                    password = input(str("Teacher password : "))
                    query_vals = (username,password)
                    command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'teacher')",query_vals)
                    db.commit()
                    print(username + " has been registered as a teacher")

                elif user_option == "7":
                    print("")
                    print("Assign student to the group")
                    username = input(str("Student username : "))
                    password = input(str("Student password : "))
                    privilege = input(str("Privilege : "))
                    if privilege == "student":
                        query_vals = (username,password,privilege)
                        command_handler.execute("INSERT INTO pi21a (username, password, privilege) VALUES (%s,%s,%s)",query_vals)
                        db.commit()
                        print("Student added to the group")
                    else:
                        print("Teacher can't be added to student group")
                        db.rollback()


                elif user_option == "8":
                    print("")
                    print("Add teacher's/student's to the subject")
                    username = input(str("Username : "))
                    password = input(str("Password : "))
                    privilege = input(str("Privilege : "))
                    query_vals = (username,password,privilege)
                    command_handler.execute("INSERT INTO subject (username, password, privilege) VALUES (%s,%s,%s)",query_vals)
                    db.commit()
                    print("Person added to the subject")

                elif user_option == "9":
                    print("")
                    print("Delete Existing Student Account")
                    username = input(str("Student username : "))
                    query_vals = (username,"student")
                    command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
                    db.commit()
                    if command_handler.rowcount < 1:
                        print("User not found")
                    else:
                        print(username + " has been deleted")

                elif user_option == "10":
                    print("")
                    print("Delete Existing Teacher Account")
                    username = input(str("Teacher username : "))
                    query_vals = (username,"teacher")
                    command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
                    db.commit()
                    if command_handler.rowcount < 1:
                        print("User not found")
                    else:
                        print(username + " has been deleted")

                elif user_option == "11":
                    print("")
                    print("Delete Student Group")
                    command_handler.execute("DROP TABLE pi21a")
                    db.commit()
                    print("Student group deleted")
                    
                elif user_option == "12":
                    print("")
                    print("Delete Subject")
                    command_handler.execute("DROP TABLE suject")
                    db.commit()
                    print("Subject deleted")

                elif user_option == "13":
                    print("")
                    print("Delete Student from group")
                    username = input(str("Student username : "))
                    query_vals = (username,"student")
                    command_handler.execute("DELETE FROM pi21a WHERE username = %s AND privilege = %s ",query_vals)
                    db.commit()
                    if command_handler.rowcount < 1:
                        print("User not found")
                    else:
                        print(username + " has been deleted")

                elif user_option == "14":
                    print("")
                    print("Delete teacher's/student's from subject")
                    username = input(str("Enter username : "))
                    privilege = input(str("Privilege : "))
                    query_vals = (username,privilege)
                    command_handler.execute("DELETE FROM subject WHERE username = %s AND privilege = %s ",query_vals)
                    db.commit()
                    if command_handler.rowcount < 1:
                        print("User not found")
                    else:
                        print(username + " has been deleted")
                    
                
                elif user_option == "15":
                    break
                else:
                    print("No valind option selected")
                

        def student_session(username):
            while 1:
                print("")
                print("Student's Menu")
                print("")
                print("1. View grades")
                print("2. Logout")

                user_option = input(str("Option : "))
                if user_option == "1":
                    username = (str(username),)
                    command_handler.execute("SELECT date, username, grade FROM evaluation WHERE username = %s",username)
                    records = command_handler.fetchall()
                    for record in records:
                        print(record)
                elif user_option == "2":
                    break
                else:
                    print("No valid option was selected")
    class auth():
        
        def auth_admin():
            print("")
            print("Admin login")
            print("")
            username = input(str("Username : "))
            password = input(str("Password : "))
            if username == "admin":
                if password == "password":
                    admin_session()
                else:
                    print("Incorrect password !")
            else:
                print("Login details not recognised")

        def auth_teacher():
            print("")
            print("Teacher's Login")
            print("")
            username = input(str("Username : "))
            password = input(str("Password : "))
            query_vals = (username, password)
            command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'",query_vals)
            if command_handler.rowcount <= 0:
                print("Login not recognized")
            else:
                teacher_session()

        def auth_student():
            print("")
            print("Student's Login")
            print("")
            username = input(str("Username : "))
            password = input(str("Password : "))
            query_vals = (username, password, "student")
            command_handler.execute("SELECT username FROM users WHERE username = %s AND password = %s AND privilege = %s",query_vals)
            if command_handler.rowcount <= 0:
                print("Invalid login details")
            else: 
                student_session(username)

        def main():
            while 1:
                print("Welcome to academic system")
                print("")
                print("1. Login as admin")
                print("2. Login as teacher")
                print("3. Login as student")

                user_option = input(str("Option : "))
                if user_option == "1":
                    auth_admin()
                elif user_option == "2":
                    auth_teacher()
                elif user_option == "3":
                    auth_student()
                else:
                    print("No valid option was selected")

        main()
