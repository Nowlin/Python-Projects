from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import sqlite3

class MainWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(600,600)
        self.master.maxsize(600,600)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        self.load_gui()

    def load_gui(self):
        self.lbl_fname = tk.Label(self.master,text='First Name:')
        self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
        self.lbl_lname = tk.Label(self.master,text='Last Name:')
        self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
        self.lbl_phone = tk.Label(self.master,text='Phone Number:')
        self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
        self.lbl_email = tk.Label(self.master,text='Email Address:')
        self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
        self.lbl_course = tk.Label(self.master,text='Current Course:')
        self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

        self.txt_fname = tk.Entry(self.master,text='')
        self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_lname = tk.Entry(self.master,text='')
        self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_phone = tk.Entry(self.master,text='')
        self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_email = tk.Entry(self.master,text='')
        self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_course = tk.Entry(self.master,text='')
        self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.lstList1.bind('<<ListboxSelect>>',lambda event: self.onSelect(event))
        self.scrollbar1.config(command=self.lstList1.yview)
        self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
        self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

        self.btn_add = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: self.addToList())
        self.btn_add.grid(row=10,column=0,padx=(25,0),pady=(45,10),sticky=W)
        self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: self.onDelete())
        self.btn_delete.grid(row=10,column=1,padx=(25,0),pady=(45,10),sticky=W)

        self.create_db()
        self.onRefresh()

    def create_db(self):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_phonebook( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT, \
                col_lname TEXT, \
                col_fullname TEXT, \
                col_phone TEXT, \
                col_email TEXT \
                );")
            # You must commit() to save changes & close the database connection
            conn.commit()
        conn.close()
        self.first_run()

    def first_run(self):
        data = ('John','Doe','John Doe','111-111-1111','jdoe@email.com')
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            cur,count = self.count_records(cur)
            if count < 1:
                cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", (data))
                conn.commit()
        conn.close()

    def count_records(self, cur):
        count = ""
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        return cur,count
      
    #Select item in ListBox
    def onSelect(self,event):
        #calling the event is the self.lstList1 widget
        varList = event.widget
        select = varList.curselection()[0]
        value = varList.get(select)
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
            varBody = cursor.fetchall()
            # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
            for data in varBody:
                self.txt_fname.delete(0,END)
                self.txt_fname.insert(0,data[0])
                self.txt_lname.delete(0,END)
                self.txt_lname.insert(0,data[1])
                self.txt_phone.delete(0,END)
                self.txt_phone.insert(0,data[2])
                self.txt_email.delete(0,END)
                self.txt_email.insert(0,data[3])

    def addToList(self):
        var_fname = self.txt_fname.get()
        var_lname = self.txt_lname.get()
        # normalize the data to keep it consistent in the database
        var_fname = var_fname.strip() # This will remove any blank spaces before and after the user's entry
        var_lname = var_lname.strip() # This will ensure that the first character in each word is capitalized
        var_fname = var_fname.title()
        var_lname = var_lname.title()
        var_fullname = ("{} {}".format(var_fname,var_lname)) # combine our normailzed names into a fullname
        print("var_fullname: {}".format(var_fullname))
        var_phone = self.txt_phone.get().strip()
        var_email = self.txt_email.get().strip()
        if not "@" or not "." in var_email: # will use this soon, not in video!
            print("Incorrect email format!!!")
        if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and(len(var_email) > 0): # enforce the user to provide both names
            conn = sqlite3.connect('phonebook.db')
            with conn:
                cursor = conn.cursor()
                # Check the database for existance of the fullname, if so we will alert user and disregard request
                cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))#,(var_fullname))
                count = cursor.fetchone()[0]
                chkName = count
                if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                    print("chkName: {}".format(chkName))
                    cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                    self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                    self.onClear() # call the function to clear all of the textboxes
                else:
                    messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                    self.onClear() # call the function to clear all of the textboxes
            conn.commit()
            conn.close()
        else:
            messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")
            

    def onDelete(self):
        var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            # check count to ensure that this is not the last record in
            # the database...cannot delete last record or we will get an error
            cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
            count = cur.fetchone()[0]
            if count > 1:
                confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
                if confirm:
                    conn = sqlite3.connect('phonebook.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                    self.onDeleted() # call the function to clear all of the textboxes and the selected index of listbox
    ######             onRefresh(self) # update the listbox of the changes
                    conn.commit()
            else:
                confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
        conn.close()

    def onDeleted(self):
        # clear the text in these textboxes
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_email.delete(0,END)
    ##    onRefresh(self) # update the listbox of the changes
        try:
            index = self.lstList1.curselection()[0]
            self.lstList1.delete(index)
        except IndexError:
            pass

    def onClear(self):
        # clear the text in these textboxes
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_email.delete(0,END)
        

    def onRefresh(self):
        # Populate the listbox, coinciding with the database
        self.lstList1.delete(0,END)
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
            count = cursor.fetchone()[0]
            i = 0
            while i < count:
                    cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
                    varList = cursor.fetchall()[i]
                    for item in varList:
                        self.lstList1.insert(0,str(item))
                        i = i + 1
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    App = MainWindow(root)
    root.mainloop()
