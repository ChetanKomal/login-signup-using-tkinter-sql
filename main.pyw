from tkinter import *
import os
from tkinter import messagebox
import mysql.connector as sql

db = sql.connect(host="localhost",user="root",password="root",database="tkinter_users")
cursor = db.cursor()

root =Tk()
root.geometry("400x400")
root.resizable(False,False)
root.title("Student Registration")
root.config(bg="purple") 



def start():

 def login():   
     def submit_login():
         x=user1.get()
         y=passw1.get()
        #  f=open("cred.txt","r+")
        #  z=f.read()
        #  if x in z and y in z:
        #      messagebox.showinfo("login success","Successfully loggedin")
        #  else:
        #      messagebox.showinfo("login failed","creds are wrong")

         if x == "" and y == "": messagebox.showinfo("Empty fields","Please enter something") 
         if x == "" : messagebox.showinfo("Error","enter username")
         if y == "" : messagebox.showinfo("Error","enter password")
         cursor.execute(f"select * from users_1 where username like '{x}' and password like '{y}'")
         c=cursor.fetchall()
         for i in c:
          for j in i: 
            if x in j and y in j:
               messagebox.showinfo("Successfully logged in","Credentials are correct")
               break
            else:
              messagebox.showinfo("Error","Invalid Credentials")
              break

     Login.place_forget()
     SignUp.place_forget()   
     user = Label(text="Username: ",font=("bold",15),bg="purple")
     user.place(x=60,y=140)
     user1=Entry(width=27)
     user1.place(x=160,y=147)
     passw=Label(text="Password: ",font=("bold",15),bg="purple")
     passw.place(x=60,y=190)
     passw1= Entry(width=27,show="*")
     passw1.place(x=160,y=197)
     submit = Button(text="Submit",command=submit_login,width=10)
     submit.place(x=110,y=300)
     def back1():
        user.place_forget()
        user1.place_forget()
        passw.place_forget()
        passw1.place_forget()
        submit.place_forget()
        back.place_forget()
        start()
     back=Button(text="Back",width=10,command=back1)
     back.place(x=200,y=300)

 def signup():
     
     def submit_signup():
      xx=mail1.get()
      yy=userw1.get()
      zz=passww2.get()
      qq=cpassw1.get()
      # if os.path.exists("cred.txt"):
       
      #  if zz == qq and xx=="" or yy=="" or zz=="":
      #    filee=open("cred.txt","a")
      #    filee.write(xx)
      #    filee.write(":")
      #    filee.write(yy)
      #    filee.write(":")
      #    filee.write(zz)
      #    filee.write("\n")
      #    filee.close()
      #  else:
      #    messagebox.showinfo("Wrong Password or empty fields",
      #    "password wrong or fields are empty.")    
      # else:
      #  f=open("cred.txt","x")
      #  f=open("cred.txt","a")
      #  if zz == qq:
      #    f.write(xx)
      #    f.write(":")
      #    f.write(yy)
      #    f.write(":")
      #    f.write(zz)
      #    f.write("\n")
      #    f.close()
      #  else:
      #    messagebox.showinfo("Wrong Password or empty fields",
      #    "password wrong or fields are empty.")         

     Login.place_forget()
     SignUp.place_forget()
     mail = Label(text="Email: ",font=("bold",15),bg="purple")
     mail.place(x=60,y=80)
     mail1=Entry(width=27)
     mail1.place(x=160,y=87)

     userw=Label(text="Username:",font=("bold",15),bg="purple")
     userw.place(x=60,y=110)
     userw1= Entry(width=27)
     userw1.place(x=160,y=117)
     
     passww=Label(text="Password",font=("bold",15),bg="purple")
     passww.place(x=60,y=140)
     passww2=Entry(width=27,show="*")
     passww2.place(x=160,y=147)

     cpassw=Label(text="Confirm: ",font=("bold",15),bg="purple")
     cpassw.place(x=60,y=170)
     cpassw1=Entry(width=27,show="*")
     cpassw1.place(x=160,y=177)

     submit2 = Button(text="Submit",command=submit_signup,width=10)
     submit2.place(x=110,y=300)
     def back():
          mail.place_forget()
          mail1.place_forget()
          userw.place_forget()
          userw1.place_forget()
          passww.place_forget()
          passww2.place_forget()
          cpassw.place_forget()
          cpassw1.place_forget()
          submit2.place_forget()
          back2.place_forget()
          start()
     back2=Button(text="Back",width=10,command=back)
     back2.place(x=200,y=300)

 
 
 Login = Button(text="Login",font=("bold",15),command=login)
 Login.place(x=120,y=165)
 SignUp=Button(text="Signup",font=("bold",15),command=signup)
 SignUp.place(x=200,y=165)
   


start()
root.mainloop()