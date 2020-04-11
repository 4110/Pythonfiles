from tkinter import *
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import tkinter
import tkinter.messagebox

def proces():
  name1=Entry.get(E1)
  name="'"+name1+"'"+","
  email=Entry.get(E2)
  email="'"+email+"'"+','
  password=Entry.get(E3)
  password="'"+password+"'"+','
  phone=Entry.get(E4)
  phone="'"+phone+"'"
  #adding ' at start of inputs got due to fromat specifier
  try:
      connection = mysql.connector.connect(host='localhost',
                                          database='test',
                                          user='root',
                                          password='')
      mySql_insert_query = """INSERT INTO user (name, email, password,phone) 
                            VALUES 
                            ( """+name+email+password+phone+""")"""

      cursor = connection.cursor()
      if len(name)>3 and len(email)>3 and len(password)>3 and len(phone)>2:
        cursor.execute(mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        E1.delete(0,END)
        E2.delete(0,END)
        E3.delete(0,END)
        E4.delete(0,END)
        tkinter.messagebox.showinfo( "Sucess", "Welcome "+name1+ " Sucessfully registered")
        cursor.close()
      else:
        tkinter.messagebox.showinfo( "Error", "Please enter all fields")
  except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

  finally:
      if (connection.is_connected()):
          connection.close()
          print("MySQL connection is closed")
def dele():
  E1.delete(0,END)
  E2.delete(0,END)
  E3.delete(0,END)
  E4.delete(0,END)
top = tkinter.Tk()
top.title("Register")
L2 = Label(top, text="Name",).grid(row=1,column=2)
E1 = Entry(top, bd =5)
E1.grid(row=2,column=2)
L3 = Label(top, text="Email",).grid(row=3,column=2)
E2 = Entry(top, bd =5)
E2.grid(row=4,column=2)
L4 = Label(top, text="Password",).grid(row=5,column=2)
E3 = Entry(top, bd =5)
E3.grid(row=6,column=2)
L5 = Label(top, text="Phone",).grid(row=7,column=2)
E4 = Entry(top, bd =5)
E4.grid(row=8,column=2)
B=Button(top, text ="Submit",command = proces).grid(row=10,column=2)
C=Button(top, text ="Clear",command = dele).grid(row=9,column=2)
top.mainloop()
