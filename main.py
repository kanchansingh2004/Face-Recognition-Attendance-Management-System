from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from details import  Student_Details
from face_detect import face_recognition
from attendance import Attendance
from train import Train

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x600+0+0")
        self.root.title("Face Recognition System")
        
        #Frame for face recognition system label
        frs_frame = Frame(self.root , bg = "#01454c" )
        frs_frame.place(x=0 , y=0 , width=1280 , height=100)
        
        #Label for face recognition system 
        frs_label = Label(frs_frame , text="FACE RECOGNITION ATTENDANCE SYSTEM" , fg = "White" , bg = "#015b66" , font=("Latin" , 30 , "bold"))
        frs_label.place(x=10 , y=10 , width=1260 , height=80  )
        
        
        #Frame for main body
        main_frame = Frame(self.root , bg = "#01454c")
        main_frame.place(x=0 , y=100 , width=1280 , height=600)
        
        #Sub frame
        sub_frame = Frame(main_frame , bg = "#04163a")
        sub_frame.place(x=10 , y=10 , width=1260 , height=570)
        
        
        # -----------------------------------Photo Buttons-------------------------------------------
        
        
        #Photo icons 1
        img1 = Image.open(r"C:\projects\python\Face detection images\clipart2845938.png")
        img1 = img1.resize((150,150))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        bttn1 = Button(sub_frame , image=self.photoimg1 , command=self.student_details)
        bttn1.place(x=250 , y=150 , width=150 , height=150)
        
        bttnlab1 = Button(sub_frame , text="Student Details" , command=self.student_details)
        bttnlab1.place(x=250 , y=300 , width=150 , height=30)
        
        #Photo icons 2
        img2 = Image.open(r"C:\projects\python\Face detection images\recog.png")
        img2 = img2.resize((150,150))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        bttn2 = Button(sub_frame , image=self.photoimg2, command=self.face_detection)
        bttn2.place(x=450 , y=150 , width=150 , height=150)
        
        bttnlab2 = Button(sub_frame , text="Face Recognition", command=self.face_detection)
        bttnlab2.place(x=450 , y=300 , width=150 , height=30)
        
        #Photo icons 3
        img3 = Image.open(r"C:\projects\python\Face detection images\train.png")
        img3 = img3.resize((150,150))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bttn3 = Button(sub_frame , image=self.photoimg3, command=self.traind)
        bttn3.place(x=650 , y=150 , width=150 , height=150)
        
        bttnlab3 = Button(sub_frame , text="Train Data", command=self.traind)
        bttnlab3.place(x=650 , y=300 , width=150 , height=30)
        
        #Photo icons 4
        img4 = Image.open(r"C:\projects\python\Face detection images\attendance.png")
        img4 = img4.resize((150,150))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        bttn4 = Button(sub_frame , image=self.photoimg4, command=self.attend)
        bttn4.place(x=850 , y=150 , width=150 , height=150)
        
        bttnlab4 = Button(sub_frame , text="Attendance", command=self.attend)
        bttnlab4.place(x=850 , y=300 , width=150 , height=30)
        
        
        
        #Terms and Condition
        btm_frame = Frame(sub_frame , bg="#04163a" )
        btm_frame.place(x=0 , y=520 , width=1260 , height=50)
        
        term_label = Label(btm_frame , text="Terms & Condition" , fg="White" , bg="#04163a" , font=("Lucida Fax" , 10 , "bold"))
        term_label.pack(side=BOTTOM)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_Details(self.new_window)

    def face_detection(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recognition(self.new_window)

    def attend(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def traind(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)




        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()