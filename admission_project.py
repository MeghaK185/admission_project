import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="admission_table")
mycursor=mydb.cursor()
print("      --------------STUDENT ADMISSION---------------------    ")
option=0
opt=0
try:
    while option<=3:
        print("+-------------------+")
        print("|   ENTER           |")
        print("| 1.ADMISSION       |")
        print("| 2.COURSES         |")
        print("| 3.EXIT            |")
        print("+-------------------+")
        while True:
            try:
                option=int(input("Enter your option:"))
                if option>0 and option<=3:
                    break
                else:
                    print("choose 1,2 or 3")
            except:
                print("Invalid Option!!!!")

        if option==1:
            print("+......................+")
            print("|1.NEW ADMISSION       |")
            print("|2.EDIT ADMISSION      |")
            print("|3.DELETE              |")
            print("|4.VIEW                |")
            print("|5.BACK                |")
            print("+......................+")  
            while True:       
                try:
                    opt=int(input("enter option:"))
                    if opt>0 and opt<=5:
                        break
                    else:
                        print("choose a valid option!!!!")
                except:
                    print("invalid option!!!!+++")
            if opt==1:
                # NEW ADMISSION
                print("--ENTER--")
                name = input("Name:")
                while not name:
                    print("Name cannot be empty. Please enter a valid name.")
                    name = input("Name:")
                while True:
                    try:
                        ph = int(input("Phone number:"))
                        break
                    except ValueError:
                        print("Invalid phone number. Please enter a valid value.")
                addr = input("Address:")
                while not addr:
                    print("Address cannot be empty. Please enter a valid address.")
                    addr = input("Address:")
                gmail = input("Gmail:")
                while not gmail:
                    print("Gmail cannot be empty. Please enter a valid Gmail address.")
                    gmail = input("Gmail:")
                district = input("District:")
                while not district:
                    print("District cannot be empty. Please enter a valid district name.")
                    district = input("District:")
                g_name = input("Guardian name:")
                while not g_name:
                    print("Guardian name cannot be empty. Please enter a valid name.")
                    g_name = input("Guardian name:")
                print("SELECT A COURSE TO BE ENROLLED")
                mycursor.execute("SELECT * FROM courses")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['ID','NAME', 'FEES','Duration'], tablefmt='psql'))
                while True:
                    try:
                        enrolled=int(input("enter course id:"))   
                        for x in myresult:
                            if enrolled == x[0]:
                                sql="INSERT INTO admission(name,ph_no,address,gmail,district,guardian,enrolled) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                                val=(name,ph,addr,gmail,district,g_name,x[1])
                                mycursor.execute(sql,val)
                                mydb.commit()
                                print("Added sucessfully!!")
                                break
                        else:
                            print("id not found!!!.Try again!!")     
                    except ValueError:
                        print("invalid!!!!")
                    break
                # -------------EDIT-----------
            if int(opt) == 2:
                # EDIT ADMISSION
                op=1
                while op<=8:
                    print("_Edit__")
                    print("+.........................+")
                    print("|0.VIEW(ID,NAME           |")
                    print("|1.NAME                   |")
                    print("|2.PHONE NUMBER           |")
                    print("|3.ADDRESS                |")
                    print("|4.GMAIL                  |")
                    print("|5.DISTRICT               |")
                    print("|6.GUARDIAN               |")
                    print("|7.ENROLLED COURSE        |")
                    print("|8.Back                   |")
                    print("+.........................+")
                    while True:
                        try:
                            op=int(input("Enter your option:"))
                            if op>=0 and op<=8:
                                break
                            else:
                                print("choose between 0-8")
                        except:
                            print("invalid")                  
                    if(op==0):
                        # show name and id
                        print("ID  NAME")
                        mycursor.execute("SELECT id,name FROM admission")
                        myresult = mycursor.fetchall()
                        print(tabulate(myresult, headers=['ID','NAME'], tablefmt='psql'))
                        break
                    
                    elif op==1: 
                        #EDIT NAME  
                        print("edit name")
                        mycursor.execute("SELECT id FROM admission")
                        adm = mycursor.fetchall()
                        while True:
                            try:
                                id1 = int(input("Enter the ID of the student to be edited: "))
                                for x in adm:
                                    if id1 == x[0]:
                                        new_name = input("Enter the new name: ")
                                        while not new_name:
                                            print("you must enter a value")
                                            new_name = input("Enter the new name: ")                                          
                                        sql = "UPDATE admission SET name = %s WHERE id = %s"
                                        val = (new_name, id1)
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print("Done!")
                                        break
                                else:
                                    print("ID not found")
                            except ValueError:
                                print("Invalid ID! Please enter a valid numeric ID.") 
                            try:
                                if id1 == x[0]:
                                    break
                            except:
                                pass
                    elif op==2: 
                        # EDIT PHONE NUMBER
                        print("edit name")
                        mycursor.execute("SELECT id FROM admission")
                        adm = mycursor.fetchall()
                        while True:
                            try:
                                id1 = int(input("Enter the ID of the student to be edited: "))
                                for x in adm:
                                    if id1 == x[0]:
                                        new_ph = input("Enter the new number: ")
                                        while not new_ph:
                                            print("you must enter a value")
                                            new_ph = input("Enter the new number: ")                                          
                                        sql = "UPDATE admission SET name = %s WHERE id = %s"
                                        val = (new_ph, id1)
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print("Done!")
                                        break
                                else:
                                    print("ID not found")
                            except ValueError:
                                print("Invalid ID! Please enter a valid numeric ID.")  
                            try:   
                                if id1 == x[0]:
                                    break
                            except:
                                pass
                                    
                    elif op==3:
                        # EDIT ADDRESS
                        print("edit address")
                        mycursor.execute("SELECT id FROM admission")
                        adm = mycursor.fetchall()
                        while True:
                            try:                             
                                id1=int(input("enter the id of student to be edited:"))
                                for x in adm:
                                    if id1==x[0]:
                                        new_addr=input("enter the new address:")
                                        while not new_addr:
                                            print("you must enter a value")
                                            new_addr=input("enter the new address:")
                                        sql = "UPDATE admission SET  address=%s WHERE id= %s"
                                        val= (new_addr,id1)
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print("done!!")
                                        break
                                else:
                                    print("id not found")
                            except ValueError:
                                print("invalid id!!!")
                            try:
                                if id1 == x[0]:
                                    break
                            except:
                                pass
                    elif op==4:
                        # EDIT GMAIL
                        print("edit gmail")
                        mycursor.execute("SELECT id FROM admission")
                        adm = mycursor.fetchall()
                        while True:
                            try:                             
                                id1=int(input("enter the id of student to be edited:"))
                                for x in adm:
                                    if id1==x[0]:
                                        new_id=input("enter the new gmail id:")
                                        while not new_id:
                                            print("you must enter a value")
                                            new_id=input("enter the new gmail id:")
                                        sql = "UPDATE admission SET  gmail=%s WHERE id= %s"
                                        val= (new_id,id1)
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print("done!!")
                                        break
                                else:
                                    print("id not found")
                            except ValueError:
                                print("invalid id!!!")
                            try:
                                if id1 == x[0]:
                                    break
                            except:
                                pass

                    elif op==5:
                        # EDIT DISTRICT
                        print("edit district")
                        mycursor.execute("SELECT id FROM admission")
                        adm = mycursor.fetchall()
                        while True:
                            try:                             
                                id1=int(input("enter the id of student to be edited:"))
                                for x in adm:
                                    if id1==x[0]:
                                        new_disct=input("enter the new district:")                                   
                                        while not new_disct:
                                            print("you must enter a value")
                                            new_id=input("enter District:")
                                        sql = "UPDATE admission SET district= %s WHERE id= %s"
                                        val= (new_disct,id1)
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print("done!!!")
                                        break
                                else:
                                    print("id not found")
                            except ValueError:
                                print("invalid id!!!")
                            try:
                                if id1 == x[0]:
                                    break
                            except:
                                 pass
                    elif op==6:
                        # EDIT GUARDIAN NAME
                        print("edit guardian name")
                        mycursor.execute("SELECT id FROM admission")
                        adm = mycursor.fetchall()
                        while True:
                            try:                             
                                id1=int(input("enter the id of student to be edited:"))
                                for x in adm:
                                    if id1==x[0]:
                                        new_gn=input("enter the new guardian name:")
                                        while not new_gn:
                                            print("you must enter a value")
                                            new_gn=input("enter the new guardian name:")
                                        sql = "UPDATE admission SET guardian= %s WHERE id= %s"
                                        val= (new_gn,id1)
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print("done!!!")
                                        break
                                else:
                                    print("id not found")
                            except ValueError:
                                print("invalid id!!!")
                            try:
                                if id1 == x[0]:
                                    break
                            except:
                                 pass

                    elif op==7:
                        # EDIT ENROLLED COURSE
                        print("Edit enrolled course")
                        mycursor.execute("SELECT id FROM admission")
                        adm = mycursor.fetchall()
                        while True:
                            try:
                                id1 = int(input("Enter the ID of the student to be edited:"))
                                for x in adm:
                                    if id1 == x[0]:
                                        print("SELECT A COURSE TO BE ENROLLED")
                                        mycursor.execute("SELECT * FROM courses")
                                        myresult = mycursor.fetchall()
                                        print(tabulate(myresult, headers=['ID', 'NAME', 'FEES', 'Duration'], tablefmt='psql'))
                                        while True:
                                            try:
                                                new_course = int(input("Enter the new course ID:"))
                                                for x in myresult:
                                                    if new_course == x[0]:
                                                        sql = "UPDATE admission SET enrolled=%s WHERE id=%s"
                                                        val = (x[1], id1)
                                                        mycursor.execute(sql, val)
                                                        mydb.commit()
                                                        print("Added successfully!!")
                                                        break
                                                else:
                                                    print("Course ID not found! Try again.")
                                            except ValueError:
                                                print("Invalid input! Please enter a valid course ID.")
                                            break
                                        break
                                else:
                                    print("Student ID not found! Please try again.")
                            except ValueError:
                                print("Invalid input! Please enter a valid student ID.")
                            try:
                                if id1 == x[0]:
                                    break
                            except:
                                    pass  
                            break                     
                    else:
                        if op==8:
                            break    
                    break            
            elif opt==3:
                # DELETE STUDENT ID
                print("DELETE STUDENT")
                mycursor.execute("SELECT * FROM admission")
                myresult = mycursor.fetchall()
                while True:
                    try:
                        id_to_delete = int(input("Enter the ID you want to delete: "))
                        for x in myresult:
                            if id_to_delete==x[0]:
                                sql = f"DELETE FROM admission WHERE id = {id_to_delete}"
                                mycursor.execute(sql)
                                mydb.commit()
                                print("Student deleted!")
                                break                 
                        else:
                            print("id not found")
                    except ValueError:
                        print("invalid value!!!")
                    try:
                        if id_to_delete == x[0]:
                            break
                    except:
                        pass
        
            elif opt==4:
                # VIEW STUDENT TABLE
                print("view")
                mycursor.execute("SELECT * FROM admission")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['ID','NAME', 'PHONE','EMAIL','DISTRICT','GUARDIAN','ENROLLED COURSE'], tablefmt='psql'))                   
            else:
                if opt==5:
                    pass   
        # -----------------------COURSE TABLE----------------------------
        if option==2:
            print("+....................+")
            print("|1.ADD COURSE        |")
            print("|2.EDIT COURSE       |")
            print("|3.AVAILABLE COURSES |")
            print("|4.DELETE COURSE     |")
            print("|5.BACK              |")
            print("+....................+")
            op=1
            while True:
                try:
                    op=int(input("enter your choice:"))
                    if op>0 and op<=5:
                        break
                    else:
                        print("choose a value between 1-5")
                except:
                    print("invalid choose a valid option!!")                     
            while op<=5:               
                if op==1:
                    print("ADD COURSE")
                    while True:
                        try:
                            c_name = input("Name of course: ")
                            if not c_name:
                                print("You must enter a value for the course name!")
                            else:
                                break
                        except:
                            print("An error occurred. Please try again.")

                    while True:
                        try:
                            c_fee = float(input("Enter the fees: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid numeric value for fees.")

                    while True:
                        C_duration = input("Enter the duration of course: ")
                        if not C_duration:
                            print("You must enter a value for the course duration!")
                        else:
                            break                              
                    sql="INSERT INTO courses(NAME,FEES,DURATION) VALUES(%s,%s,%s)"                   
                    val=(c_name,c_fee,C_duration)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("course added succesfully")
                    break
                        #  -----EDIT COURSE----------
                if op==2:
                    print("EDIT COURSE")
                    print("+......................+")
                    print("|1.EDIT COURSE NAME    |")
                    print("|2.EDIT COURSE DURATION|")
                    print("|3.EDIT COURSE FEES    |")
                    print("+......................+")
                    opt=0

                    while True:
                        try:
                            opt=int(input("choose an option:"))
                            if opt>0 and op<=3:
                                break
                            else:
                                print("Enter values between 1-3")
                        except:
                            print("choose a valid option!!!")
                    while opt<=3:
                        if opt==1:
                            # EDIT COURSE NAME
                            print("EDIT COURSE NAME")
                            mycursor.execute("SELECT ID FROM courses")
                            adm = mycursor.fetchall()
                            while True:
                                try:                             
                                    id1=int(input("enter the course id to be edited:"))
                                    for x in adm:
                                        if id1==x[0]:
                                            new_name=input("enter the new name:")                                   
                                            while not new_name:
                                                print("you must enter a value")
                                                new_name=input("enter the new gmail id:")
                                            sql = "UPDATE courses SET name= %s WHERE id= %s"
                                            val= (new_name,id1)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                            print("done!!!")
                                            break
                                    else:
                                            print("id not found")
                                    try:
                                        if id1 == x[0]:
                                            break
                                    except:
                                        pass
                                except ValueError:
                                    print("invalid id!!!")
                            break
                        elif opt==2:
                            # EDIT COURSE DURATION
                            print("EDIT COURSE DURATION")
                            mycursor.execute("SELECT ID FROM courses")
                            adm= mycursor.fetchall()
                            while True:
                                try:
                                    id2=int(input("enter the course id:"))
                                    for x in adm:
                                        if id2==x[0]:
                                            new=input("enter the new name of course :")
                                            while not new:
                                                print("you must enter a value")
                                                new=input("enter the duration of course :")                              
                                            sql = "UPDATE courses SET DURATION= %s WHERE ID= %s"
                                            val=(new,id2)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                            print("Done!!!")
                                            break
                                    else:
                                        print("id not found!!")
                                except:
                                    print("add a valid value!!!")
                                try:
                                    if id2 == x[0]:
                                        break
                                except:
                                    pass
                                break                         
                        elif opt==3:
                            # EDIT COURSE FEES
                            print("EDIT COURSE FEES")
                            mycursor.execute("SELECT ID FROM courses")
                            crs = mycursor.fetchall()
                            while True:
                                try:
                                    course_id = int(input("Enter the course ID:"))
                                    for x in crs:
                                        if course_id == x[0]:
                                            new_fee = input("Enter the new fee:")
                                            while not new_fee:
                                                print("You must enter a value")
                                                new_fee = input("Enter the new fee:")
                                            sql = "UPDATE courses SET FEES = %s WHERE ID = %s"
                                            val = (new_fee,course_id)
                                            mycursor.execute(sql, val)
                                            mydb.commit()
                                            print("Done!!!")
                                            break
                                    else:
                                        print("Course ID not found")
                                except ValueError:
                                    print("Invalid value! Please enter a valid course ID.")
                                try:
                                    if course_id == x[0]:
                                        break
                                except:
                                    pass
                                break
                        break
                elif op==3:
                    # SHOW AVAILABLE COURSES
                    print("_____AVAILABLE COURSES_____")
                    mycursor.execute("SELECT * FROM courses")
                    myresult = mycursor.fetchall()
                    print(tabulate(myresult, headers=['ID','NAME', 'FEES','Duration'], tablefmt='psql'))
                    break
                elif op==4:
                    # DELETE COURSE
                    print("DELETE COURSE")
                    mycursor.execute("SELECT ID FROM courses")
                    adm = mycursor.fetchall()
                    while True:
                        try:
                            id=int(input("enter the id you want to delete:"))
                            for x in adm:
                                if id==x[0]:
                                    sql=f"DELETE FROM courses WHERE ID={id}"
                                    mycursor.execute(sql)
                                    mydb.commit()
                                    print("deleted course!!!!")
                                    break
                            else:
                                print("id not found!!!")
                            if id==x[0]:
                                break
                        except ValueError:
                            print(" invalid!!!")
                                             
                elif op==5:
                    print("Back")
                    break
                break
        if option==3:
            print("exit")
            break
except:
    pass



                

