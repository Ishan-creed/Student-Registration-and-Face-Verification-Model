 img = Image.open(r"C:\Users\ishan\OneDrive\Desktop\Physical detection model\images\first.png")
        img = img.resize((1530,790),Image.ANTIALIAS)
        self.photoimgnew = ImageTk.PhotoImage(img)

        label2 = Label(self.root,image=self.photoimgnew)
        label2.place(x=0,y=0,width=1530,height=790)