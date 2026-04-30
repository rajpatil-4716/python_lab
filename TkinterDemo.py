from tkinter import *

def insert_data():
    print("Insert Clicked")

def search_data():
    print("SEARCH Clicked")    

def update_data():
    print("UPDATE Clicked")

def delete_data():
    print("DELETE Clicked")

root=Tk()
root.geometry("400x380")
root.title("My Tkinter Example")
root.resizable(width=False, height=False)

l_id=Label(root,text="ID",font=("Arial",10))
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME",font=("Arial",10))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME",font=("Arial",10))
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL",font=("Arial",10))
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE",font=("Arial",10))
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=200,y=50)

e_fname=Entry(root)
e_fname.place(x=200,y=100)

e_lname=Entry(root)
e_lname.place(x=200,y=150)

e_email=Entry(root)
e_email.place(x=200,y=200)

e_mobile=Entry(root)
e_mobile.place(x=200,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial",10),command=insert_data)
insert.place(x=50,y=300)

insert=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial",10),command=search_data)
insert.place(x=120,y=300)

insert=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",10),command=update_data)
insert.place(x=201,y=300)

insert=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",10),command=delete_data)
insert.place(x=280,y=300)
