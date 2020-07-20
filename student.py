from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def get_data(name,age,address):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="nikhil",host="localhost",port="5432")
    cur = conn.cursor()
    query=('''INSERT INTO student(NAME,AGE,ADDRESS)VALUES (%s,%s,%s);''')
    cur.execute(query,(name,age,address))
    print("Data inserted...")
    conn.commit()
    conn.close()

def searchID(ID):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="nikhil",host="localhost",port="5432")
    cur = conn.cursor()
    query='''select *from student where id=%s'''
    cur.execute(query,(ID))
    row=cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()

def display_search(row):
    listbox = Listbox(frame,width=20,height=1)
    listbox.grid(row=8,column=1)
    listbox.insert(END,row)

canvas = Canvas(root,height=300,width=500)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label = Label(frame,text="ADD DATA")
label.grid(row=0,column=1)

label = Label(frame,text="Name",fg = "green")
label.grid(row=1,column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label = Label(frame,text="Age",fg = "green")
label.grid(row=2,column=0)
entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

label = Label(frame,text="Address",fg = "green")
label.grid(row=3,column=0)
entry_address = Entry(frame)
entry_address.grid(row=3,column=1)

button = Button(frame,text = "Add",command = lambda:get_data(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=5, column=1)

label = Label(frame,text="SEARCH DATA")
label.grid(row=6,column=1)

label = Label(frame,text="Enter ID: ",fg = "green")
label.grid(row=7,column=0)

entry_id = Entry(frame)
entry_id.grid(row=7,column=1)

button=Button(frame,text="search",command=lambda:searchID(entry_id.get()))
button.grid(row=7,column=2)

root.mainloop()