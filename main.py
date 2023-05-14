from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student_details import Student
from train  import train
from face_recognition import face_recogniser
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root['background'] = '#F9CA23'
        
    
       
        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\title.png")
        img = img.resize((1530,80),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        label1 = Label(self.root,image=self.photoimg)
        label1.place(x=0,y=0,width=1530,height=80)


        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\first.png")
        img = img.resize((1530,790),Image.ANTIALIAS)
        self.photoimgnew = ImageTk.PhotoImage(img)

        label2 = Label(self.root,image=self.photoimgnew)
        label2.place(x=0,y=0,width=1530,height=790)

        

        #--------------------------------------------------

        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Student_details.png")
        img = img.resize((258,269),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img)

        label2 = Label(self.root,image=self.photoimg1)
        label2.place(x=148,y=261,width=258,height=269)

        b1=Button(self.root,image=self.photoimg1,cursor="hand2",command=self.student_details)
        b1.place(x=148,y=261,width=258,height=269)
       
#-----------------------------------------------------------------------------------

        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Recognition.png")
        img = img.resize((258,269),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img)

        label3 = Label(self.root,image=self.photoimg2)
        label3.place(x=636,y=261,width=258,height=269)

         
        b2=Button(self.root,image=self.photoimg2,cursor="hand2",command=self.face_recognition)
        b2.place(x=636,y=261,width=258,height=269) 

#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------

        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Close.png")
        img = img.resize((258,269),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img)

        label5 = Label(self.root,image=self.photoimg4)
        label5.place(x=1123,y=261,width=258,height=269)

        b4=Button(self.root,image=self.photoimg4,cursor="hand2",command=self.close)
        b4.place(x=1123,y=261,width=258,height=269)

#-----------------------------------------------------------------------------------

        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Images.png")
        img = img.resize((258,58),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img)
        
        
        label6 = Label(self.root,image=self.photoimg5)
        label6.place(x=144,y=672,width=258,height=58)

        b5=Button(self.root,image=self.photoimg5,cursor="hand2",command=self.open_img)
        b5.place(x=144,y=672,width=258,height=58)
#-----------------------------------------------------------------------------------

        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Train.png")
        img = img.resize((258,58),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img)

        label7 = Label(self.root,image=self.photoimg6)
        label7.place(x=1123,y=672,width=258,height=58)

        
        b6=Button(self.root,image=self.photoimg6,cursor="hand2",command=self.train_data)
        b6.place(x=1123,y=672,width=258,height=58)

    def open_img(self):
        os.startfile("data")

        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = train(self.new_window)     

    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recogniser(self.new_window)
   
    def close(self):
        self.root.destroy()

        
#---------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()        









