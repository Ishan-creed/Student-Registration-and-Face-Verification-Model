from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from student_details import Student
import os
import cv2
import numpy as np

class train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root['background'] = '#F9CA23'


        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Data_train.png")
        img = img.resize((1530,80),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        label1 = Label(self.root,image=self.photoimg)
        label1.place(x=0,y=0,width=1530,height=80)


        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\first.png")
        img = img.resize((1530,790),Image.ANTIALIAS)
        self.photoimgnew = ImageTk.PhotoImage(img)

        label2 = Label(self.root,image=self.photoimgnew)
        label2.place(x=0,y=0,width=1530,height=790)

        
        img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\Button_Train.png")
        img = img.resize((258,269),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img)

        label3 = Label(self.root,image=self.photoimg2)
        label3.place(x=550,y=261,width=258,height=269)

         
        b2=Button(self.root,image=self.photoimg2,cursor="hand2",command=self.train)
        b2.place(x=550,y=261,width=258,height=269) 


    def train(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #Grayscale Conversion
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow(f"Training + {id}",imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        try:

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training Completed")

        except Exception as e:
            messagebox.showerror("Error",f"Due to : {str(e)}", parent=self.root)

                    

             
if __name__ == "__main__":
    
    root=Tk()
    obj = train(root)
    root.mainloop()    