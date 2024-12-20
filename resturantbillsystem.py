from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys




def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Resturant Management System")

        self.title_lable = Label(self.win,text = "Resturant Management System",font=('Arial',35,'bold'),bg="lightyellow",bd=8,relief=GROOVE)
        self.title_lable.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=220,y=150,width=800,height=450)

        self.login_lbl = Label(self.main_frame,text="LOGIN",bd=6,relief=GROOVE,anchor=CENTER,bg="lightyellow",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Your Details",bd=5,relief=GROOVE,bg="lightgrey",font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)


        self.entus_lbl = Label(self.entry_frame,text="Enter Username :",bg="lightgrey",font=('sans-serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)
        #==========================  VARIABLES  ==============================#
        username = StringVar()
        password = StringVar()
       
        #==========================  VARIABLES  ==============================#
        self.entus_ent = Entry(self.entry_frame,font=('sana-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)        
        
        self.entpass_lbl = Label(self.entry_frame,text="Enter Password :",bg="lightgrey",font=('sans-serif',15))
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.entpass_ent = Entry(self.entry_frame,font=('sana-serif',15),bd=6,textvariable=password,show='*')
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)

        #============================== FUNCTIONS ==============================#

        def check_login():
            '''  This function check login '''
            if username.get() == "" and password.get() == "":
                self.billing_btn.config(state="normal")
            else:
                pass #---->  Message Box

        def reset():
            username.set("")
            password.set("")

        def billing_sect():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)    
        #============================== FUNCTIONS ==============================#

        #=======================  BUTTONS  ==============================#
        self.button_frame = LabelFrame(self.entry_frame,text="OPTIONS",font=('Arial',15),bg="lightyellow",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=740,height=85)

        self.login_btn = Button(self.button_frame,text="LOGIN",font=('Arial',15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn = Button(self.button_frame,text="BILLING",font=('Arial',15),bd=5,width=15,command=billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame,text="RESET",font=('Arial',15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)

        #=======================  BUTTONS  ==============================#

class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1300x750+0+0")
        self.win.title("Resturant Management BILLING System")

        self.title_lable = Label(self.win,text = "Resturant Management BILLING System",font=('Arial',35,'bold'),bg="lightyellow",bd=8,relief=GROOVE)
        self.title_lable.pack(side=TOP,fill=X)

        #======================= VARIABLES ==============================#
        bill_no = random.randint(100,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        calc_var = StringVar()

        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cone = StringVar()

        date_pr.set(datetime.now())

        total_list = []
        self.grd_total = 0
        #======================= VARIABLES ==============================#

        #=======================  ENTRY AREA  ==============================#

        self.entry_frame = LabelFrame(self.win,text="ENTER DETAILS",bg="lightgrey",font=('Arial',15),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=550)

        self.bill_no_lbl = Label(self.entry_frame,text="BILL NUMBER ",font=('Arial',15),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent = Entry(self.entry_frame,bd=5,font=('Arial',15),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state='disabled')

        self.cust_nm_lbl = Label(self.entry_frame,text="CUSTOMER NAME ",font=('Arial',15),bg="lightgrey")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Arial',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_cot_lbl = Label(self.entry_frame,text="CUSTOMER CONTACT ",font=('Arial',15),bg="lightgrey")
        self.cust_cot_lbl.grid(row=2,column=0,padx=2,pady=2)

        self.cust_cot_ent = Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=('Arial',15))
        self.cust_cot_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lbl = Label(self.entry_frame,text="DATE ",font=('Arial',15),bg="lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)

        self.item_pur_lbl = Label(self.entry_frame,text="ITEM PURCHASED ",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.item_pur_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Arial',15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qty_lbl = Label(self.entry_frame,text="ITEM QUANTITY ",font=('Arial',15),bg="lightgrey")
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.item_qty_ent = Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Arial',15))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lbl = Label(self.entry_frame,text="COST OF ONE ITEM ",font=('Arial',15),bg="lightgrey")
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)

        self.cost_one_ent = Entry(self.entry_frame,bd=5,textvariable=cone,font=('Arial',15))
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)

        #=======================  BUTTONS   FUNCTIONS  ==============================#
        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tRADHE RESTAURANT")
            self.bill_txt.insert(END,"\n\t\t07 Street,CHHOTI BALLIA,LAKHMINIA,BEGUSARAI,BIHAR,851211")
            self.bill_txt.insert(END,"\n\t\t\t\tContact No : +91 84097553++")
            self.bill_txt.insert(END,"\n==================================================================================")
            self.bill_txt.insert(END,f"\nBill Number : {bill_no_tk.get()}")

        def add_func():
            if item_pur.get() == "" or item_qty.get() == "":
                messagebox.showerror("Error !!","Please enter all the fields correct...",parent=self.win)
            else:
                qty = int(item_qty.get())
                cones = int(cone.get())
                total = qty * cones
                total_list.append(total)
                self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t            {item_qty.get()}\t\t\t       Rs.{cone.get()}\t\t               Rs.{total}")

        def genbill():
            if cust_nm.get() == "" or (cust_cot.get() == "" or len(cust_cot.get()) != 10):
                messagebox.showerror("Error !!","Please enter all the fields correct...",parent=self.win)
            else:
                self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
                self.bill_txt.insert(END,f"\nCustomer Contact : {cust_cot.get()}")
                self.bill_txt.insert(END,f"\nDate : {date_pr.get()}")
                self.bill_txt.insert(END,"\n==================================================================================")
                self.bill_txt.insert(END,"\nProduct Name\t\t         Quantity           \t\tPer Cost\t\t                  Total")
                self.bill_txt.insert(END,"\n==================================================================================")

                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")
            

        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")

        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            default_bill()

        def save_func():
            user_choice = messagebox.askyesno("Confirm",f"Do you want to save the bill {bill_no_tk.get}",parent=self.win)
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                try:                    
                    con = open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error !!",f"Error due to {e}",parent=self.win)
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success !",f"Bill {bill_no_tk.get()} has been saved successfully !",parent=self.win)
            else:
                return

        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,"\n----------------------------------------------------------------------------------")
            self.bill_txt.insert(END,f"\t\t\t\t\t\t\t\tGrand Total : Rs.{self.grd_total}")
            self.bill_txt.insert(END,"\n----------------------------------------------------------------------------------")
            self.save_btn.config(state="normal")
            
        
        #=======================  BUTTONS  FUNCTIONS  ==============================#

        #=======================  BUTTONS  ==============================#

        self.button_frame = LabelFrame(self.entry_frame,bd=5,text="OPTIONS",bg="lightgrey",font=('Arial',15))
        self.button_frame.place(x=20,y=280,width=360,height=210)

        self.add_btn = Button(self.button_frame,bd=4,text="ADD",font=('Arial',12),width=10,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.generate_btn = Button(self.button_frame,bd=4,text="GENERATE",font=('Arial',12),width=10,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.clear_btn = Button(self.button_frame,bd=4,text="CLEAR",font=('Arial',12),width=10,height=3,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)        

        self.reset_btn = Button(self.button_frame,bd=4,text="RESET",font=('Arial',12),width=10,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=0,padx=4,pady=2)

        self.save_btn = Button(self.button_frame,bd=4,text="SAVE",font=('Arial',12),width=10,height=3,command=save_func)
        self.save_btn.grid(row=1,column=1,padx=4,pady=2)

        self.total_btn = Button(self.button_frame,bd=4,text="TOTAL",font=('Arial',12),width=10,height=3,command=total_func)
        self.total_btn.grid(row=1,column=2,padx=4,pady=2)

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")
        #=======================  BUTTONS  ==============================#

        #===========================  CALCULATOR FRAME  ==============================#
        self.calc_frame = Frame(self.win,bd=8,bg="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=570,y=100,width=700,height=300)

        self.num_ent = Entry(self.calc_frame,bd=15,bg="lightgrey",textvariable=calc_var,font=('Arial',15,'bold'),width=59,justify=RIGHT)
        self.num_ent.grid(row=0,column=0,columnspan=7)

        def press_btn(event):
            text = event.widget.cget("text")
            if text  == "=":
                if text.isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "C":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()


        self.btn7 = Button(self.calc_frame,bg="lightgrey",text="7",bd=8,width=13,height=1,font=('Arial',15))
        self.btn7.grid(row=1,column=0,padx=4,pady=2)
        self.btn7.bind("<Button-1>",press_btn)

        self.btn8 = Button(self.calc_frame,bg="lightgrey",text="8",bd=8,width=13,height=1,font=('Arial',15))
        self.btn8.grid(row=1,column=1,padx=3,pady=2)
        self.btn8.bind("<Button-1>",press_btn)

        self.btn9 = Button(self.calc_frame,bg="lightgrey",text="9",bd=8,width=13,height=1,font=('Arial',15))
        self.btn9.grid(row=1,column=2,padx=3,pady=2)
        self.btn9.bind("<Button-1>",press_btn)

        self.btnadd = Button(self.calc_frame,bg="lightgrey",text="+",bd=8,width=12,height=1,font=('Arial',15))
        self.btnadd.grid(row=1,column=3,padx=3,pady=2)
        self.btnadd.bind("<Button-1>",press_btn)

        self.btn4 = Button(self.calc_frame,bg="lightgrey",text="4",bd=8,width=13,height=1,font=('Arial',15))
        self.btn4.grid(row=2,column=0,padx=2,pady=2)
        self.btn4.bind("<Button-1>",press_btn)

        self.btn5 = Button(self.calc_frame,bg="lightgrey",text="5",bd=8,width=13,height=1,font=('Arial',15))
        self.btn5.grid(row=2,column=1,padx=3,pady=2)
        self.btn5.bind("<Button-1>",press_btn)

        self.btn6 = Button(self.calc_frame,bg="lightgrey",text="6",bd=8,width=13,height=1,font=('Arial',15))
        self.btn6.grid(row=2,column=2,padx=3,pady=2)
        self.btn6.bind("<Button-1>",press_btn)

        self.btnsubs = Button(self.calc_frame,bg="lightgrey",text="-",bd=8,width=12,height=1,font=('Arial',15))
        self.btnsubs.grid(row=2,column=3,padx=3,pady=2)
        self.btnsubs.bind("<Button-1>",press_btn)

        self.btn1 = Button(self.calc_frame,bg="lightgrey",text="1",bd=8,width=13,height=1,font=('Arial',15))
        self.btn1.grid(row=3,column=0,padx=2,pady=2)
        self.btn1.bind("<Button-1>",press_btn)

        self.btn2 = Button(self.calc_frame,bg="lightgrey",text="2",bd=8,width=13,height=1,font=('Arial',15))
        self.btn2.grid(row=3,column=1,padx=3,pady=2)
        self.btn2.bind("<Button-1>",press_btn)

        self.btn3 = Button(self.calc_frame,bg="lightgrey",text="3",bd=8,width=13,height=1,font=('Arial',15))
        self.btn3.grid(row=3,column=2,padx=3,pady=2)
        self.btn3.bind("<Button-1>",press_btn)

        self.btnmulti = Button(self.calc_frame,bg="lightgrey",text="*",bd=8,width=12,height=1,font=('Arial',15))
        self.btnmulti.grid(row=3,column=3,padx=3,pady=2)
        self.btnmulti.bind("<Button-1>",press_btn)

        self.btn0 = Button(self.calc_frame,bg="lightgrey",text="0",bd=8,width=13,height=1,font=('Arial',15))
        self.btn0.grid(row=4,column=0,padx=2,pady=2)
        self.btn0.bind("<Button-1>",press_btn)

        self.btnpoint = Button(self.calc_frame,bg="lightgrey",text=".",bd=8,width=13,height=1,font=('Arial',15))
        self.btnpoint.grid(row=4,column=1,padx=3,pady=2)
        self.btnpoint.bind("<Button-1>",press_btn)

        self.btnclear = Button(self.calc_frame,bg="lightgrey",text="=",bd=8,width=13,height=1,font=('Arial',15))
        self.btnclear.grid(row=4,column=2,padx=3,pady=2)
        self.btnclear.bind("<Button-1>",press_btn)

        self.btndiv = Button(self.calc_frame,bg="lightgrey",text="/",bd=8,width=12,height=1,font=('Arial',15))
        self.btndiv.grid(row=4,column=3,padx=3,pady=2)
        self.btndiv.bind("<Button-1>",press_btn)
        #===========================  CALCULATOR FRAME  ==============================#

        #===========================  BILL FRAME  ==============================#
        self.bill_frame = LabelFrame(self.win,text="BILL AREA",font=('Arial',18),bg="lightyellow",bd=8,relief=GROOVE)
        self.bill_frame.place(x=570,y=400,width=700,height=248)

        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)


        default_bill()
        #===========================  BILL FRAME  ==============================#
                
        
if __name__ == "__main__":
    main()            