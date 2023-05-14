from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from cv2 import VideoCapture
from cv2 import waitKey
from cv2 import CascadeClassifier



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root['background'] = '#F9CA23'
# -----------------------------------------------------------------

        self.var_department = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_contact = StringVar()
        self.var_CGPA = StringVar()
        self.var_email = StringVar()
        self.var_LinkedIn = StringVar()
        self.var_address = StringVar()
        self.var_gender = StringVar()
        self.var_ID = StringVar()

        img = Image.open(
            r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Details.png")
        img = img.resize((1530, 80), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        label1 = Label(self.root, image=self.photoimg)
        label1.place(x=0, y=0, width=1530, height=80)

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=15, y=115, width=1500, height=620)

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=40, y=10, width=700, height=580)
 # ---------------------------------------------------------

        
        Student_ID = Label(main_frame,text="StudentID",
                     font=("times new roman", 12, "bold"))
        Student_ID.place(x=50,y=40)
        

        ID_entry = ttk.Entry(main_frame, textvariable=self.var_ID, width=20, font=(
            "times new roman", 12, "bold"))
        ID_entry.place(x=140,y=40)
        
        



        Current_Course = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Course Information", font=(
            "times new roman", 12, "bold"))
        Current_Course.place(x=2.5, y=60, width=690, height=160)

        # Department

        dep_label = Label(Current_Course, text="Department",
                          font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(Current_Course, textvariable=self.var_department, font=(
            "times new roman", 12, "bold"), width=17, state='readonly')
        dep_combo["values"] = ("Select Department", "Computer Science",
                               "Information Technology", "ECE", "ECM", "BT", "BI", "Phd")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Year

        year_label = Label(Current_Course, text="Year",
                           font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=0, pady=10)

        year_combo = ttk.Combobox(Current_Course, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly", width=17)
        year_combo["values"] = (
            "Select Year", "2019-2023", "2020-2024", "2021-2025", "2022-2026")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)

        # Semester

        sem_label = Label(Current_Course, text="Semester",
                          font=("times new roman", 12, "bold"))
        sem_label.grid(row=2, column=0, padx=0, pady=10)

        sem_combo = ttk.Combobox(Current_Course, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="readonly", width=17)
        sem_combo["values"] = ("Select Semester", "1",
                               "2", "3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.grid(row=2, column=1, padx=2, pady=10)
        # ---------------------------------------------------

        Student_info = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Student Information", font=(
            "times new roman", 12, "bold"))
        Student_info.place(x=2.5, y=230, width=690, height=315)

        # Student Roll
        Roll = Label(Student_info, text="Roll Number",
                     font=("times new roman", 12, "bold"))
        Roll.grid(row=0, column=0, padx=6, pady=10)

        roll_entry = ttk.Entry(Student_info, textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=1, padx=10, pady=2)

        # Name

        Name = Label(Student_info, text="Name",
                     font=("times new roman", 12, "bold"))
        Name.grid(row=0, column=2, padx=6, pady=10)

        name_entry = ttk.Entry(Student_info, textvariable=self.var_name, width=20, font=(
            "times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=2)

        # Contact:

        Contact = Label(Student_info, text="Contact No.",
                        font=("times new roman", 12, "bold"))
        Contact.grid(row=1, column=0, padx=6, pady=10)

        contact_entry = ttk.Entry(Student_info, textvariable=self.var_contact, width=20, font=(
            "times new roman", 12, "bold"))
        contact_entry.grid(row=1, column=1, padx=10, pady=2)

        # CGPA:

        CGPA = Label(Student_info, text="Current CGPA",
                     font=("times new roman", 12, "bold"))
        CGPA.grid(row=1, column=2, padx=6, pady=10)

        CGPA_entry = ttk.Entry(Student_info, textvariable=self.var_CGPA, width=20, font=(
            "times new roman", 12, "bold"))
        CGPA_entry.grid(row=1, column=3, padx=10, pady=2)

        # Gender:
        gender = Label(Student_info, text="Gender",
                       font=("times new roman", 12, "bold"))
        gender.grid(row=2, column=0, padx=6, pady=10)

        # gender_entry=ttk.Entry(Student_info,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=2)
        gender_combo = ttk.Combobox(Student_info, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly", width=17)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10)

        # Address:

        address = Label(Student_info, text="Address",
                        font=("times new roman", 12, "bold"))
        address.grid(row=2, column=2, padx=6, pady=10)

        address_entry = ttk.Entry(Student_info, textvariable=self.var_address, width=20, font=(
            "times new roman", 12, "bold"))
        address_entry.grid(row=2, column=3, padx=10, pady=2)

        # SEmail:

        email = Label(Student_info, text="Email",
                      font=("times new roman", 12, "bold"))
        email.grid(row=3, column=0, padx=6, pady=10)

        email_entry = ttk.Entry(Student_info, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=2)

        # Linkdin Handle:

        linkdin = Label(Student_info, text="LinkedIn",
                        font=("times new roman", 12, "bold"))
        linkdin.grid(row=3, column=2, padx=6, pady=10)

        linkdin_entry = ttk.Entry(Student_info, textvariable=self.var_LinkedIn, width=20, font=(
            "times new roman", 12, "bold"))
        linkdin_entry.grid(row=3, column=3, padx=10, pady=2)

        self.var_radio_button1 = StringVar()
        radiobutton1 = ttk.Radiobutton(
            Student_info, variable=self.var_radio_button1, text="Take an Image Sample", value="Yes")
        radiobutton1.grid(row=4, column=0, padx=6, pady=3)

        radiobutton2 = ttk.Radiobutton(
            Student_info, variable=self.var_radio_button1, text="No Image Sample", value="No")
        radiobutton2.grid(row=4, column=1, padx=6, pady=3)

        btn_frame = Frame(Student_info, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=10, y=212, width=665, height=40)

        save_btn = Button(btn_frame, text="Save", width=17, font=(
            "times new roman", 12, "bold"), command=self.add_data, bg="#312E2E", fg="#F9CA23")
        save_btn.grid(row=0, column=0, padx=3)

        update_btn = Button(btn_frame, text="Update", width=17, font=(
            "times new roman", 12, "bold"),command=self.update_data , bg="#312E2E", fg="#F9CA23")
        update_btn.grid(row=0, column=1, padx=3)

        delete_btn = Button(btn_frame, text="Delete", width=17, font=(
            "times new roman", 12, "bold"),command=self.delete_data,bg="#312E2E", fg="#F9CA23")
        delete_btn.grid(row=0, column=2, padx=3)

        reset_btn = Button(btn_frame, text="Reset", width=17, font=(
            "times new roman", 12, "bold"),command=self.reset_details, bg="#312E2E", fg="#F9CA23")
        reset_btn.grid(row=0, column=3, padx=3)

        img_btn_frame = Frame(Student_info, bd=2, relief=RIDGE, bg='white')
        img_btn_frame.place(x=10, y=255, width=665, height=30)

        take_photo_btn = Button(img_btn_frame, text="Take Image", width=30, font=(
            "times new roman", 12, "bold"),command=self.generate_dataset ,bg="#312E2E", fg="#F9CA23")
        take_photo_btn.grid(row=0, column=0, padx=10)

        update_photo_btn = Button(img_btn_frame, text="Update Image", width=30, font=(
            "times new roman", 12, "bold"), bg="#312E2E", fg="#F9CA23")
        update_photo_btn.grid(row=0, column=1, padx=35)

# ----------------------------------------------------------------
#
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Database", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=700, height=580)

    # ---------------------------------------------------------------------
    # Search System

        Search_info = LabelFrame(Right_frame, bd=2, relief=RIDGE,
                                 text="Search Details", font=("times new roman", 12, "bold"))
        Search_info.place(x=2.5, y=60, width=690, height=70)

        Search_by = Label(Search_info, text="Search By",
                          font=("times new roman", 12, "bold"))
        Search_by.grid(row=0, column=0, padx=6, pady=10)

        search_combo = ttk.Combobox(Search_info, font=(
            "times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll No.", "Name", "Contact No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10)

        search_entry = ttk.Entry(
            Search_info, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=2)

        search_btn = Button(Search_info, text="Search", width=13, font=(
            "times new roman", 12, "bold"), bg="#312E2E", fg="#F9CA23")
        search_btn.grid(row=0, column=3, padx=3)

        show_all_btn = Button(Search_info, text="Show all", width=13, font=(
            "times new roman", 12, "bold"), bg="#312E2E", fg="#F9CA23")
        show_all_btn.grid(row=0, column=4, padx=3)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=2.5, y=140, width=690, height=420)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Department", "Year", "Semester", "Name", "Roll", "Contact", "LinkedIn",
                                          "Address", "Gender", "CGPA", "Email", "Image Sample","ID"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X,)
        scroll_y.pack(side=RIGHT, fill=Y,)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll", text="Roll")
        self.student_table.heading("Contact", text="Contact")
        self.student_table.heading("LinkedIn", text="LinkedIn")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("CGPA", text="CGPA")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Image Sample", text="Image Sample")
        self.student_table.heading("ID",text="ID")

        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
# _---------------------------------------------------------------------------------

    def add_data(self):

        if self.var_department.get() == "Select Department" or self.var_name.get() == "" or self.var_roll.get() == "":
            messagebox.showerror(
                "Invalid Details", "All details are to be filled!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="12345", database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_department.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_contact.get(),
                    self.var_LinkedIn.get(),
                    self.var_address.get(),
                    self.var_gender.get(),
                    self.var_CGPA.get(),
                    self.var_email.get(),
                    self.var_radio_button1.get(),
                    self.var_ID.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Details saved successfully!", parent=self.root)

            except Exception as e:
                messagebox.showerror(
                    "Error", f"Due to :{str(e)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="12345", database="face_recogniser")
        my_cursor = conn.cursor()

        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"] 

        self.var_department.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_name.set(data[3]),
        self.var_roll.set(data[4]),
        self.var_contact.set(data[5]),
        self.var_LinkedIn.set(data[6]),
        self.var_address.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_CGPA.set(data[9]),
        self.var_email.set(data[10]),
        self.var_radio_button1.set(data[11]),
        self.var_ID.set(data[12])

        # update function:

    def update_data(self):


        if self.var_department.get() == "Select Department" or self.var_name.get() == "" or self.var_roll.get() == "":
            messagebox.showerror(
                "Invalid Details", "All details are to be filled!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update the details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="12345", database="face_recogniser")
                    my_cursor = conn.cursor()
                    # sql=("Update student set Department=%s,Year=%s,Semester=%s,Name=%s,Contact=%s,LinkedIn=%s,Address=%s,Gender=%s,CGPA=%s,Email=%s,Image Sample=%s where Roll=%s")
              
                    my_cursor.execute("UPDATE student SET Department=%s WHERE ID = %s",(
                        self.var_department.get(),
                   
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET Name=%s WHERE ID = %s",(
                      
                        self.var_name.get(), 
                  
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET Year=%s WHERE ID = %s",(
                       
                        self.var_year.get(),
                   
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET Semester=%s WHERE ID = %s",(

                        self.var_semester.get(),
                
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET Contact=%s WHERE ID = %s",(
                
                        self.var_contact.get(),
                    
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET LinkedIn=%s WHERE ID = %s",(
                
                        self.var_LinkedIn.get(),
                   
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET Address=%s WHERE ID = %s",(
             
                        self.var_address.get(),
                      
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET Gender =%s WHERE ID = %s",(
                        # self.var_department.get(),
                        # self.var_year.get(),
                        # self.var_semester.get(),
                        # self.var_name.get(), 
                        # self.var_roll.get(),
                        # self.var_contact.get(),
                        # self.var_LinkedIn.get(),
                        # self.var_address.get(),
                        self.var_gender.get(),
                        # self.var_CGPA.get(),
                        # self.var_email.get(),
                        # self.var_radio_button1.get(),
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET CGPA=%s WHERE ID = %s",(
            
                        self.var_CGPA.get(),
                        
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET Emaill =%s WHERE ID = %s",(
            
                        self.var_email.get(),
                     
                        self.var_ID.get()
                       

                    ))
                    my_cursor.execute("UPDATE student SET Image_sample =%s WHERE ID = %s",(
 
                        self.var_radio_button1.get(),
                        self.var_ID.get()
                       

                    ))
                else:
                    if not Update:
                        return

                messagebox.showinfo(
                    "Success", "Details Updated!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Due to: {str(e)}", parent=self.root)

    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","ID is required!")
        else:
            try:
                delete = messagebox.askyesno("Deletion Request","Do you want to delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="12345", database="face_recogniser")
                    my_cursor = conn.cursor()
                    sql="delete from student where Roll=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student's details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self.root)


    
    def reset_details(self):
        self.var_department.set("Select Department")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_contact.set("")
        self.var_LinkedIn.set("")
        self.var_address.set("")
        self.var_gender.set("Select Gender")
        self.var_CGPA.set("")
        self.var_email.set("")
        self.var_radio_button1.set("")


        #---------------------------------Face Recognition

    def generate_dataset(self):


        if self.var_department.get() == "Select Department" or self.var_name.get() == "" or self.var_roll.get() == "":
            messagebox.showerror(
                "Invalid Details", "All details are to be filled!", parent=self.root)
        else:

            try:


                conn = mysql.connector.connect(
                    host="localhost", username="root", password="12345", database="face_recogniser")
                my_cursor = conn.cursor()

                my_cursor.execute("Select * from student ")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Department=%s WHERE ID = %s",(

                self.var_department.get(),
                   
                self.var_ID.get()
                       

                ))
                my_cursor.execute("UPDATE student SET Name=%s WHERE ID = %s",(
                  
                    self.var_name.get(), 
              
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET Year=%s WHERE ID = %s",(
                   
                    self.var_year.get(),
               
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET Semester=%s WHERE ID = %s",(

                    self.var_semester.get(),
            
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET Contact=%s WHERE ID = %s",(
            
                    self.var_contact.get(),
                
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET LinkedIn=%s WHERE ID = %s",(
            
                    self.var_LinkedIn.get(),
               
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET Address=%s WHERE ID = %s",(
         
                    self.var_address.get(),
                  
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET Gender =%s WHERE ID = %s",(
                  
                    self.var_gender.get(),
                    
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET CGPA=%s WHERE ID = %s",(
        
                    self.var_CGPA.get(),
                    
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET Emaill =%s WHERE ID = %s",(
        
                    self.var_email.get(),
                 
                    self.var_ID.get()
                   

                ))
                my_cursor.execute("UPDATE student SET Image_sample =%s WHERE ID = %s",(

                    self.var_radio_button1.get(),
                    self.var_ID.get()
                   

                ))

                conn.commit()
                self.fetch_data()
    
                conn.close()


                #Load data for the face using open cv

                face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):

                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_detector.detectMultiScale(gray,1.3,5)



                    for (x,y,w,h) in faces:


                        face_cropped = img[y:y+h,x:x+w]

                        return face_cropped

                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:

                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:

                            img_id+=1

                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                        file_path = "Data/user."+ str(id) + "." + str(img_id) + ".jpg"  

                        cv2.imwrite(file_path)
                        cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)

                        cv2.imshow("Detected Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:

                            break


                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data set completed successfully!!")
                            
            except Exception as e:


                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self.root)


















        

       
                

                




                    # -----------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
