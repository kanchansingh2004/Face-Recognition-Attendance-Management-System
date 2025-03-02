from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk 
from tkinter import messagebox
import mysql.connector
from details import  Student_Details
from face_detect import face_recognition
from attendance import Attendance
from train import Train

def main():
    win=Tk()
    app=login(win)
    win.mainloop()


    #---------------------------------Login Window--------------------------------

class login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        self.var_email = StringVar()
        self.var_password = StringVar()
        
        #Frame for face recognition system label
        frs_frame = Frame(self.root , bg = "#01454c" )
        frs_frame.place(x=0 , y=0 , width=1280 , height=100)
        
        #Label for face recognition system 
        frs_label = Label(frs_frame , text="FACE RECOGNITION ATTENDANCE SYSTEM" , fg = "White" , bg = "#015b66" , font=("Latin" , 30 , "bold"))
        frs_label.place(x=10 , y=10 , width=1260 , height=80  )
        
        
        # Frame for main body
        main_frame = Frame(self.root , bg = "#01454c")       
        main_frame.place(x=0 , y=100 , width=1280 , height=600)
        
        #Sub frame
        sub_frame = Frame(main_frame , bg = "#04163a")
        sub_frame.place(x=10 , y=10 , width=1260 , height=570)
        
        #Terms and Condition
        btm_frame = Frame(sub_frame , bg="#04163a" )
        btm_frame.place(x=0 , y=520 , width=1260 , height=50)
        
        term_label = Label(btm_frame , text="Terms & Condition" , fg="White" , bg="#04163a" , font=("Lucida Fax" , 10 , "bold"))
        term_label.pack(side=BOTTOM)
        
        
        #---------------------------------------Login Part---------------------------------------------
        
        #Frame for login 
        login_frame = Frame(sub_frame , bg = "#015b66")       
        login_frame.place(x=430 , y=60 , width=400 , height=450)
        
        #Login Logo
        log_img = Image.open(r"C:\projects\python\Face detection images\login_logo.png")
        log_img = log_img.resize((100, 100))
        self.photologimg = ImageTk.PhotoImage(log_img)
        
        log_lbl = Label(login_frame , image = self.photologimg , bg="#015b66")
        log_lbl.place(x=150 , y=10 , width=100 , height=100)
        
        
        #LookIn LOGO
        lookin_img = Image.open(r"C:\projects\python\Face detection images\LookIn.png")
        lookin_img = lookin_img.resize((150, 50))
        self.photolookin = ImageTk.PhotoImage(lookin_img)
        
        lookin_lbl = Label(login_frame , image = self.photolookin , bg="#015b66")
        lookin_lbl.place(x=130 , y=110 , width=150 , height=50)
        
        
        # get_str=Label(sub_frame,text="Get Started",font=("times new roman",22,"bold"),fg="white",bg="black") 
        # get_str.place(x=555,y=180)
        
        #label 
        username=lbl=Label(login_frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="#015b66") 
        username.place(x=50,y=150) 
        
        self.txtuser=ttk.Entry(login_frame,font=("times new roman",16,"bold")) 
        self.txtuser.place(x=50,y=250,width=270)
    
        password=lbl=Label(login_frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="#015b66")
        password.place(x=50,y=220)            
        
        
        self.txtpass=ttk.Entry(login_frame,font=("time new roman",16,"bold")) 
        self.txtpass.place(x=50,y=180,width=270) 
        #loginbutton 
        loginbtn=Button(login_frame,text="Login",font=("time new roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="#04163a",activeforeground="white",activebackground="#015b66",command=self.Login)
        loginbtn.place(x=110,y=310,width=145,height=30)  
        
        
        #registerbutton
        registerbtn=Button(login_frame,text=" Register New User",command=self.register_window,font=("time new roman",11,"bold"),borderwidth=0,fg="white",bg="#015b66",activeforeground="white",activebackground="#015b66")
        # registerbtn=Button(login_frame,text="New User register",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="",activeforeground="white",activebackground="blue")
        registerbtn.place(x=80,y=400,width=210,height=18)    
        #forgetpassbtn
        forgetbtn=Button(login_frame,text="Forget Password",font=("time new roman",11,"bold"),borderwidth=0,fg="white",bg="#015b66",activeforeground="white",activebackground="#015b66")
        # forgetbtn=Button(login_frame,text="Forget Password",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#04163a",activeforeground="white",activebackground="")
        forgetbtn.place(x=80,y=370,width=210,height=18)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_window(self.new_window)


    def Login(self): 
        # self.var_ename = StringVar()
        # self.var_passname = StringVar()

        if self.txtuser.get()=="" or self.txtpass.get()=="": 
            messagebox.showerror("Error","all field requried")
        elif self.txtuser.get().lower()=="rohit" and self.txtpass.get().lower()=="wish": 
            messagebox.showinfo("success","face recongition system") 
        else: 
            conn = mysql.connector.connect(host = "127.0.0.1" , username = "root" , password = "kanchan2601" , database = "register_data" )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from login_data where email=%s and password=%s",(
                                                                                        self.var_email.get(),
                                                                                        self.var_password.get()
                                                                                        ))
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Invalid","Invalid username or password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=Face_Recognition_System(new_window)
                else:
                    if not open_main:
                        return
                # self.new_window=Toplevel(self.new_window)
                # self.app=Face_Recognition_System(new_window)


            conn.commit()
            conn.close()
            
            
        #------------------------------Register Window---------------------------------


class Register_window:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x760+0+0")
        self.root.title("face recognition system")

        #--------------------------Variables---------------------------
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_cname = StringVar()
        self.var_ename = StringVar()
        self.var_sname = StringVar()
        self.var_ansname = StringVar()
        self.var_passname = StringVar()
        self.var_conname = StringVar()
        # self.var_check = StringVar()
        
        #Frame for face recognition system label
        frs_frame = Frame(self.root , bg = "#01454c" )
        frs_frame.place(x=0 , y=0 , width=1280 , height=100)
        
        #Label for face recognition system 
        frs_label = Label(frs_frame , text="FACE RECOGNITION ATTENDANCE SYSTEM" , fg = "White" , bg = "#015b66" , font=("Latin" , 30 , "bold"))
        frs_label.place(x=10 , y=10 , width=1260 , height=80  )
        
        
        # Frame for main body
        main_frame = Frame(self.root , bg = "#01454c")       
        main_frame.place(x=0 , y=100 , width=1280 , height=600)
        
        #Sub frame
        sub_frame = Frame(main_frame , bg = "#04163a")
        sub_frame.place(x=10 , y=10 , width=1260 , height=530)
        
        #Terms and Condition
        btm_frame = Frame(sub_frame , bg="#04163a" )
        btm_frame.place(x=0 , y=520 , width=1260 , height=50)
        
        term_label = Label(btm_frame , text="Terms & Condition" , fg="White" , bg="#04163a" , font=("Lucida Fax" , 10 , "bold"))
        term_label.pack(side=BOTTOM)
        
        
        #---------------------------------------Login Part---------------------------------------------
        
        #Frame for login 
        login_reg_frame = Frame(sub_frame , bg = "#015b66")       
        login_reg_frame.place(x=40, y=32 , width=1180 , height=460)
        
        reg_lbl=Label(login_reg_frame,text="Register Page",font=("times new roman",20,"bold"),fg="white",bg="#015b66")
        reg_lbl.place(x=475,y=10)

        #---------------------------------------Label And Entry-----------------------------------------

        #First Name 
        FName_frame=Label(login_reg_frame,text="First Name",font=("Lucida Fax",13,"bold"),fg="white",bg="#015b66")
        FName_frame.place(x=330,y=60)

        FName_entry=ttk.Entry(login_reg_frame,textvariable=self.var_fname,font=("times new roman",13))
        FName_entry.place(x=330,y=85,width=180)

        #last Name
        lName_frame=Label(login_reg_frame,text="Last Name",font=("Lucida Fax",13,"bold"),fg="white",bg="#015b66")
        lName_frame.place(x=620,y=60)

        self.txt_lname=ttk.Entry(login_reg_frame,textvariable=self.var_lname,font=("times new roman",13))
        self.txt_lname.place(x=620,y=85,width=180)

        #contact Name
        cName_frame=Label(login_reg_frame,text="Contact No.",font=("Lucida Fax",13,"bold"),fg="white",bg="#015b66")
        cName_frame.place(x=330,y=120)

        self.txt_cname=ttk.Entry(login_reg_frame,textvariable=self.var_cname,font=("times new roman",13))
        self.txt_cname.place(x=330,y=145,width=180) 
        
        #email Name
        eName_frame=Label(login_reg_frame,text="Email",font=("Lucida Fax",13,"bold"),fg="white",bg="#015b66")
        eName_frame.place(x=620,y=120)

        self.txt_ename=ttk.Entry(login_reg_frame,textvariable=self.var_ename,font=("times new roman",13))
        self.txt_ename.place(x=620,y=145,width=180)
        
        #security question
        ScName_frame=Label(login_reg_frame,text="Security Question",font=("Lucida Fax",13,"bold"),fg="white",bg="#015b66")
        ScName_frame.place(x=330,y=180)

        self.combo_secu_que=ttk.Combobox(login_reg_frame,textvariable=self.var_sname,font=("times new roman",13),state="readonly")
        self.combo_secu_que["values"]=("Select","Your Birth Place","Your best Friend","Your Favorite Movie")
        self.combo_secu_que.place(x=330,y=205,width=180)
        self.combo_secu_que.current(0)
        
        #Security question answer
        AnsName_frame=Label(login_reg_frame,text="Security Answer",font=("Lucida Fax",13,"bold"),fg="white",bg="#015b66")
        AnsName_frame.place(x=620,y=180)

        self.txt_Ansname=ttk.Entry(login_reg_frame,textvariable=self.var_ansname,font=("times new roman",13))
        self.txt_Ansname.place(x=620,y=205,width=180)

        #Password
        PassName_frame=Label(login_reg_frame,text="Password",font=("Lucida Fax",13,"bold"),fg="white",bg="#015b66")
        PassName_frame.place(x=330,y=240)

        self.txt_passname=ttk.Entry(login_reg_frame,textvariable=self.var_passname,font=("times new roman",13))
        self.txt_passname.place(x=330,y=265,width=180)


        #Confirm Password
        ConName_frame=Label(login_reg_frame,text="Confirm Password",font=("Lucida Fax",13,"bold"),fg="white",bg="#015b66")
        ConName_frame.place(x=620,y=240)

        self.txt_Conname=ttk.Entry(login_reg_frame,textvariable=self.var_conname,font=("times new roman",13))
        self.txt_Conname.place(x=620,y=265,width=180)
        

        #------------------------------ Check Button--------------

        self.var_check=IntVar()
        checkbtn=Checkbutton(login_reg_frame,variable=self.var_check,text="I agree the Terms and Conditions",font=("times new roman",13,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=420,y=330)


        #-------------------------------- Buttons ---------------------------------

        B1=Button(login_reg_frame,text="Register",command=self.reg_data,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        B1.place(x=330,y=395,width=200)

        B1=Button(login_reg_frame,text="Login Now",borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        B1.place(x=620,y=395,width=200)

#---------------------------------------------Function Declaration-------------------------------------------
    def reg_data(self):
        if self.var_fname.get()=="" or self.var_ename.get()=="" or self.var_sname.get()=="Select" :
            messagebox.showerror("Error" , "All Fields are Required")
            
        elif self.var_passname.get()!=self.var_conname.get() :
            messagebox.showerror("Error" , "Password and Confirm password must be same")
            
        elif self.var_check.get()==0 :
            messagebox.showerror("Error" , "Please Agree Terms And Condition")

        else:
            conn = mysql.connector.connect(host = "127.0.0.1" , username = "root" , password = "kanchan2601" , database = "register_data" )
            my_cursor = conn.cursor()
            query=("select * from login_data where email=%s")
            value=(self.var_ename.get(),)
            my_cursor.execute(query,value)
            Row=my_cursor.fetchone()

            if Row!=None:
                messagebox.showerror("Error","User already exist , please try another email")
            else:
                my_cursor.execute("insert into login_data values(%s,%s,%s,%s,%s,%s,%s)" ,  (
                                                                                                                                                                                        self.var_fname.get(),
                                                                                                                                                                                        self.var_lname.get(),
                                                                                                                                                                                        self.var_cname.get(),
                                                                                                                                                                                        self.var_ename.get(),
                                                                                                                                                                                        self.var_sname.get(),
                                                                                                                                                                                        self.var_ansname.get(),
                                                                                                                                                                                        self.var_passname.get()
                                                                                                                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

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
    main()



