from tkinter import *
from tkinter import ttk

from sqlite3 import *
from tkinter import messagebox


class Contact:
    def __init__(self,root):
        self.root=root
        self.root.title("contacts Management System")
        self.root.geometry("1400x750+10+10")

        title=Label(self.root,text="Contacts Book",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="green" , fg="white")
        title.pack(side=TOP,fill=X)
        lbl_footer = Label(self.root, text="Developed by M.Jyotsna Manasa", font=("goudy old style", 15, "bold"),
                           bg="lightgreen", fg="black").place(x=0, y=710, relwidth=1, height=40)

        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.mobileNo_var=StringVar()
        self.teleNo_var=StringVar()
        self.dob_var=StringVar()
        self.address_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        




        #manage frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="mint cream")
        Manage_Frame.place(x=10,y=100,width=500,height=600)
        m_title=Label(Manage_Frame,text="Manage contacts",bg="mint cream",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=15)

        

        lbl_name=Label(Manage_Frame,text="Name *",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_name.grid(row=1,column=0,pady=5,padx=30,sticky="w")
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=3,relief=GROOVE)
        txt_name.grid(row=1,column=1,pady=5,padx=30,sticky="w")

        

        lbl_email=Label(Manage_Frame,text="Email *",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_email.grid(row=2,column=0,pady=5,padx=30,sticky="w")
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=2,column=1,pady=5,padx=30,sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender *",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=3,column=0,pady=5,padx=30,sticky="w")
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=3,column=1,padx=30,pady=5,sticky="w")


        lbl_mobileNo=Label(Manage_Frame,text="Mobile No *",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_mobileNo.grid(row=4,column=0,pady=5,padx=30,sticky="w")
        txt_mobileNo=Entry(Manage_Frame,textvariable=self.mobileNo_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_mobileNo.grid(row=4,column=1,pady=5,padx=30,sticky="w")

        lbl_mobileNo=Label(Manage_Frame,text="Tele No",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_mobileNo.grid(row=5,column=0,pady=5,padx=30,sticky="w")
        txt_mobileNo=Entry(Manage_Frame,textvariable=self.teleNo_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_mobileNo.grid(row=5,column=1,pady=5,padx=30,sticky="w")

        lbl_dob=Label(Manage_Frame,text="D.O.B *",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_dob.grid(row=6,column=0,pady=5,padx=30,sticky="w")
        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=5,padx=30,sticky="w")

        
       

        lbl_address=Label(Manage_Frame,text="Address *",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_address.grid(row=7,column=0,pady=5,padx=30,sticky="w")
        self.txt_address=t=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,pady=5,padx=30,sticky="w")

        lbl_msg=Label(Manage_Frame,text="* means Required fields",bg="mint cream",fg="black",font=("times new roman",15,"bold"))
        lbl_msg.grid(row=8,columnspan=2,pady=30)

        Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="mint cream")
        Btn_Frame.place(x=10,y=530,width=450)
        addbtn=Button(Btn_Frame,text="Add",font=("times new roman",12,"bold"),width=10,bg="green",fg="white",command=self.add_contacts).grid(row=0,column=0,padx=5,pady=5)
        updatebtn=Button(Btn_Frame,text="Update",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=self.update_data).grid(row=0,column=1,padx=5,pady=5)

        deletebtn=Button(Btn_Frame,text="Delete",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=self.delete_data).grid(row=0,column=2,padx=5,pady=5)
        clearbtn=Button(Btn_Frame,text="Clear",font=("times new roman",12,"bold"),bg="green",fg="white",width=10,command=self.clear).grid(row=0,column=3,padx=5,pady=5)




         #detail frame
        Details_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="mint cream")
        Details_Frame.place(x=525,y=100,width=850,height=600)
        
        lbl_search=Label(Details_Frame,text="Search",bg="mint cream",fg="black",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=30,sticky="w")
        combo_search=ttk.Combobox(Details_Frame,width=10,textvariable=self.search_by,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Name","MobileNo","Address")
        combo_search.grid(row=0,column=1,padx=30,pady=10,sticky="w")
        txt_search=Entry(Details_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=30,sticky="w")
        searchbtn=Button(Details_Frame,text="Search",bg="green",fg="white",font=("times new roman",12,"bold"),command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Details_Frame,text="Showall",bg="green",fg="white",font=("times new roman",12,"bold"),command=self.fetch_data,width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        #Table frame
        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="mint cream")
        Table_Frame.place(x=10,y=70,width=800,height=500)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.contacts_table=ttk.Treeview(Table_Frame,columns=("Name","Email","Gender","Mobile No","Tele No","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.contacts_table.xview)
        scroll_y.config(command=self.contacts_table.yview)
        
        self.contacts_table.heading("Name",text="Name")
        
        self.contacts_table.heading("Email",text="Email")
        self.contacts_table.heading("Gender",text="Gender")
        self.contacts_table.heading("Mobile No",text="Mobile No")
        self.contacts_table.heading("Tele No",text="Tele No")
        

        self.contacts_table.heading("DOB",text="dob")
        self.contacts_table.heading("Address",text="Address")
        self.contacts_table['show']="headings"
        
        self.contacts_table.column("Name",width=150)
        
        self.contacts_table.column("Email",width=150)
        self.contacts_table.column("Gender",width=100)
        self.contacts_table.column("Mobile No",width=150)
        self.contacts_table.column("Tele No",width=150)
        self.contacts_table.column("DOB",width=150)
        self.contacts_table.column("Address",width=150)
        self.contacts_table.pack(fill=BOTH,expand=1)
        self.contacts_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_contacts(self):
        if(self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.mobileNo_var.get()=="" or self.dob_var.get()=="" or self.txt_address.get('1.0',END)=="" ): 
            messagebox.showerror("Error","Required fields are not filled")
        else:
            conn=connect("contacts.db")
            cur=conn.cursor()
            cur.execute("insert into contacts values(?,?,?,?,?,?,?)",(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.mobileNo_var.get(),self.teleNo_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END)))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Successfully added")
    def fetch_data(self):
        conn=connect("contacts.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM contacts")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.contacts_table.delete(*self.contacts_table.get_children())
            for row in rows:
                self.contacts_table.insert('',END,values=row)
            conn.commit()
        conn.close()
    def clear(self):
        
        
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.mobileNo_var.set("")
        self.teleNo_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)
    def get_cursor(self,ev):
        cursor_row=self.contacts_table.focus()
        content=self.contacts_table.item(cursor_row)
        row=content['values']
        
        self.name_var.set(row[0])
        
        self.email_var.set(row[1])
        self.gender_var.set(row[2])
        self.mobileNo_var.set(row[3])
        self.teleNo_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
    def update_data(self):
        if(self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.mobileNo_var.get()=="" or self.dob_var.get()=="" or self.txt_address.get('1.0',END)=="" ): 
            messagebox.showerror("Error","Required fields are not filled")
        else:
            conn=connect("contacts.db")
            cur=conn.cursor()

            cur.execute("update contacts set Name=?,Gender=?,MobileNo=?,TeleNo=?,DateOfBirth=?,address=? WHERE Email=?",(self.name_var.get(),self.gender_var.get(),self.mobileNo_var.get(),self.teleNo_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.email_var.get()))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Successfully updated")
    def delete_data(self):
        if(self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.mobileNo_var.get()=="" or self.dob_var.get()=="" or self.txt_address.get('1.0',END)=="" ): 
            messagebox.showerror("Error","Required fields empty")
        else:
            conn=connect("contacts.db")
            cur=conn.cursor()
            sql_query=f"delete FROM contacts where MobileNo={self.mobileNo_var.get()}"
            
            cur.execute(sql_query)
            
            conn.commit()
            conn.close()
            self.clear()
            self.fetch_data()
            messagebox.showinfo("Success","Successfully Deleted")
    def search_data(self):
        conn=connect("contacts.db")
        cur=conn.cursor()
        sql_query=f"SELECT * FROM contacts where {self.search_by.get()} like '%{self.search_txt.get()}%'"
        
        cur.execute(sql_query)
        rows=cur.fetchall()
        if len(rows)!=0:
            self.contacts_table.delete(*self.contacts_table.get_children())
            for row in rows:
                self.contacts_table.insert('',END,values=row)
            conn.commit()
        else:
            messagebox.showerror("Error","No Data available")
            self.search_by.set("")
            self.search_txt.set("")
        conn.close()
    


root=Tk()
con=connect('contacts.db')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS contacts(Name text NOT NULL, Email text NOT NULL,Gender text NOT NULL,MobileNo integer(10) NOT NULL,teleNo integer(10) ,DateOfBirth text, Address text NOT NULL); ")
con.commit()
con.close()
ob = Contact(root)
root.mainloop()