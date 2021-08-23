from tkinter import *

root =Tk()
root.geometry("400x400")
root.title("Student Registration") 
root.config(bg="purple")

def submit_signup():
    pass



def signup():

     mail = Label(text="Email: ",font=("bold"),bg="purple")
     mail.place(x=60,y=80)
     mail1=Entry(width=27)
     mail1.place(x=160,y=87)

     userw=Label(text="Username:",font=("bold"),bg="purple")
     userw.place(x=60,y=110)
     userw1= Entry(width=27)
     userw1.place(x=160,y=117)
     
     passw=Label(text="Password",font=("bold"),bg="purple")
     passw.place(x=60,y=140)
     passw1=Entry(width=27,show="*")
     passw1.place(x=160,y=147)

     cpassw=Label(text="Confirm: ",font=("bold"),bg="purple")
     cpassw.place(x=60,y=170)
     cpassw1=Entry(width=27,show="*")
     cpassw1.place(x=160,y=177)

     submit = Button(text="Submit",command=submit_signup,width=10)
     submit.place(x=160,y=300)
signup()
root.mainloop()     