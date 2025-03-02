from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector

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

        B1=Button(login_reg_frame,text="Register",command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        B1.place(x=330,y=395,width=200)

        B1=Button(login_reg_frame,text="Login Now",borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        B1.place(x=620,y=395,width=200)

#---------------------------------------------Function Declaration-------------------------------------------
    def register_data(self):
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

if __name__ == "__main__": 
    root = Tk()
    obj = Register_window(root)
    root.mainloop()