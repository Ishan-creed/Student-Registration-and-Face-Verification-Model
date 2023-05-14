from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from student_details import Student
import mysql.connector
import os
import cv2
import numpy as np

class face_recogniser:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # self.new_method()

        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Recogniserpng.png")
        img = img.resize((1530,80),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        label1 = Label(self.root,image=self.photoimg)
        label1.place(x=0,y=0,width=1530,height=80)


        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\first.png")
        img = img.resize((1530,790),Image.ANTIALIAS)
        self.photoimgnew = ImageTk.PhotoImage(img)

        label2 = Label(self.root,image=self.photoimgnew)
        label2.place(x=0,y=0,width=1530,height=790)

        
        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Recognition.png")
        img = img.resize((258,269),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img)

        label3 = Label(self.root,image=self.photoimg2)
        label3.place(x=550,y=261,width=258,height=269)

         
        b2=Button(self.root,image=self.photoimg2,cursor="hand2",command = self.face_recog)
        b2.place(x=550,y=261,width=258,height=269) 

    def new_method(self):
        self.root['background'] = '#F9CA23'


    def face_recog(self):

        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []
            try:

             
                for(x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict = clf.predict(gray_image[y:y+h,x:x+w])

                    confidence = int((100*(1-predict/300)))
                    
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recogniser")
                    my_cursor = conn.cursor()
                    
                    my_cursor.execute("Select Name from student where ID = "+str(id))
                    
                    n = my_cursor.fetchone()

                    n = "+".join(n)

                    my_cursor.execute("Select Roll from student where ID = "+str(id))
                    
                    r = my_cursor.fetchone()

                    r = "+".join(r)

                    my_cursor.execute("Select Department from student where ID = "+str(id))
                    
                    d = my_cursor.fetchone()

                    d = "+".join(d)

                         
                    if confidence > 77:
                        cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)


                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face Detected",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                    coord = [x,y,w,h]

            except Exception as e:
                messagebox.showerror("Error", f"Due to : {str(e)}", parent=self.root)    

            return coord

        def recognise(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)

            return img 

        try:


            face_cascade = cv2.CascadeClassifier("C:\\Users\\ishan\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("C:\\Users\\ishan\\OneDrive\\Desktop\\Physical detection model\\classifier.xml")

            cap1 = cv2.VideoCapture(0)

            while True:
                ret,img = cap1.read()
                img = recognise(img,clf,face_cascade)
                cv2.imshow("Recognition in progress",img)
                
                if cv2.waitKey(1) == 13:


                    break

            cap1.release()
            cv2.destroyAllWindows()
            
        except Exception as e:

            messagebox.showerror("Error", f"Due to : {str(e)}", parent=self.root)






if __name__ == "__main__":
    
    root=Tk()
    obj = face_recogniser(root)
    root.mainloop()            