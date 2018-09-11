from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math

conn = sqlite3.connect("E:/Database/store.db")
c = conn.cursor()
date = datetime.datetime.now().date()

# temporary list like session
products_list = []
products_price = []
products_quantity = []


class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        # frames
        self.left = Frame(master, width=400, height=600, bg='#4F4F4F')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=400, height=600, bg='#FFFFEA')
        self.right.pack(side=RIGHT)
        # components
        self.heading = Label(self.left, text="Sayem Digital Studio", font=("Helvetica", 20, "bold"),
                             bg='#4F4F4F', fg='#FFFFEA')
        self.heading.place(x=0, y=0)
        self.subheading = Label(self.left, text="Panch Gaon Golap Bajar, Araihazar, Narayanganj",
                                font=("Helvetica", 9, "bold"),
                                bg='#4F4F4F', fg='#FFFFEA')
        self.subheading.place(x=0, y=35)
        self.subheading = Label(self.left, text="Proprietor : Sayem Library", font=("Helvetica", 10, "normal"),
                                bg='#4F4F4F', fg='#FFFFEA')
        self.subheading.place(x=0, y=60)
        self.subheading = Label(self.left, text="Contact : 01787325232", font=("Helvetica", 10, "normal"),
                                bg='#4F4F4F', fg='#FFFFEA')
        self.subheading.place(x=0, y=80)

        self.time_l = Label(self.right, text="Date : " + str(date), font=('consolas 12 bold'),
                            fg='#4F4F4F', bg='#FFFFEA')
        self.time_l.place(x=0, y=0)
        # invoice

        self.tproduct = Label(self.right, text="Products", font=('consolas 10 bold'),
                              fg='#4F4F4F', bg='#FFFFEA')
        self.tproduct.place(x=30, y=60)
        self.tquantity = Label(self.right, text="Quantity", font=('consolas 10 bold'),
                               fg='#4F4F4F', bg='#FFFFEA')
        self.tquantity.place(x=160, y=60)
        self.tamount = Label(self.right, text="Ammount", font=('consolas 10 bold'),
                             fg='#4F4F4F', bg='#FFFFEA')
        self.tamount.place(x=290, y=60)
        # enter stuff
        self.enterpname = Label(self.left, text="Enter Product Name : ", font=('Helvetica 10 bold'),
                                bg='#4F4F4F', fg='#FFFFEA')
        self.enterpname.place(x=0, y=130)
        self.enterpnamee = Entry(self.left, width=20, font=('helvetica 10 normal'),
                                 fg='#4F4F4F', bg='#FFFFEA')
        self.enterpnamee.place(x=180, y=130)
        # button
        self.search_btn = Button(self.left, text="Search", width=10, height=1,
                                 fg='#4F4F4F', bg='#FFFFEA',
                                 command=self.ajax)
        self.search_btn.place(x=180, y=160)
        # fill it by ajax
        self.productname = Label(self.left, text="", font=('consolas 12 bold'), bg='#4F4F4F', fg='#FFFFEA')
        self.productname.place(x=0, y=200)
        self.pprice = Label(self.left, text="", font=('consolas 12 bold'), bg='#4F4F4F', fg='#FFFFEA')
        self.pprice.place(x=0, y=220)
        self.pstock = Label(self.left, text="", font=('consolas 12 bold'), bg='#4F4F4F', fg='#FFFFEA')
        self.pstock.place(x=0, y=240)
        # total label
        self.total_l = Label(self.right, text="", font=('consolas 20 bold'), fg='#4F4F4F',
                             bg='#FFFFEA')
        self.total_l.place(x=0, y=550)

        # label for advertise
        self.company = Label(self.left, text="Made by Nazibur Rahman", font=("Consolas", 10, "bold"), bg='#4F4F4F',
                             fg='#FFFFEA', )
        self.company.place(x=0, y=520)
        self.company = Label(self.left, text="B.Sc. in Computer Science & Engineering", font=("Consolas", 10, "bold"),
                             bg='#4F4F4F', fg='#FFFFEA', )
        self.company.place(x=0, y=540)
        self.company = Label(self.left, text="Manarat International University, Ashulia", font=("Consolas", 10, "bold"),
                             bg='#4F4F4F', fg='#FFFFEA', )
        self.company.place(x=0, y=560)
        self.company = Label(self.left, text="Contact: 01759219292;01620130616", font=("Consolas", 10, "bold"),
                             bg='#4F4F4F', fg='#FFFFEA', )
        self.company.place(x=0, y=580)

        self.master.bind("<Return>", self.ajax)
        self.master.bind("<Up>", self.addtocart)
        self.master.bind("<space>", self.genbil)

    def ajax(self, *args, **kwargs):
        productname = str(self.enterpnamee.get())
        result = c.execute("SELECT p_name, p_price,p_stock FROM inventory WHERE p_name=?", (productname,))
        for self.r in result:
            self.get_p_name = self.r[0]
            self.get_p_price = self.r[1]
            self.get_p_stock = self.r[2]

        self.productname.configure(text="Product's Name : " + str(self.get_p_name))
        self.pprice.configure(text="Price : " + str(self.get_p_price) + " Tk")
        self.pstock.configure(text="In stock : " + str(self.get_p_stock))

        # quantity
        self.quantityl = Label(self.left, text="Enter Quantity", font=('helvetita 10 bold'), bg='#4F4F4F', fg='#FFFFEA')
        self.quantityl.place(x=0, y=290)
        self.quantitye = Entry(self.left, width=10, font=('helvetica 10 normal'),
                               fg='#4F4F4F', bg='#FFFFEA')
        self.quantitye.place(x=100, y=290)
        # add to cart
        self.cart_btn = Button(self.left, text="Add to Cart",
                               width=10, height=1, fg='#4F4F4F', bg='#FFFFEA',
                               command=self.addtocart)
        self.cart_btn.place(x=200, y=290)
        # generate bill & Change
        self.change_l = Label(self.left, text="Given Ammount", font=('helvetita 10 bold'), bg='#4F4F4F', fg='#FFFFEA')
        self.change_l.place(x=0, y=350)
        self.change_e = Entry(self.left, width=10, font=('consolas 10 normal'), fg='#4F4F4F', bg='#FFFFEA')
        self.change_e.place(x=120, y=350)
        # calculate change
        self.calculatechange_btn = Button(self.left, text="Calculate Change", font=('helvetica 10 bold'),
                                          width=20, height=1, fg='#4F4F4F', bg='#FFFFEA',
                                          command=self.changecal)
        self.calculatechange_btn.place(x=120, y=380)
        # generate bill button
        self.genbill_btn = Button(self.left, text="Generate Bill", font=('helvetica 10 bold'),
                                  width=30, height=3, fg='#4F4F4F', bg='#FFFFEA',
                                  command=self.genbil)
        self.genbill_btn.place(x=30, y=420)

    def addtocart(self, *args, **kwargs):
        self.quantityv = int(self.quantitye.get())
        if self.quantityv > int(self.get_p_stock):
            tkinter.messagebox.showinfo("Error", "Not enough products in stock")
        else:
            self.final_price = float(self.quantityv) * float(self.get_p_price)
            products_list.append(self.get_p_name)
            products_price.append(self.final_price)
            products_quantity.append(self.quantityv)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('consolas 10 bold'),
                                      fg='#4F4F4F', bg='#FFFFEA')
                self.tempname.place(x=30, y=self.y_index)
                self.tempqt = Label(self.right, text=str(products_quantity[self.counter]), font=('consolas 10 bold'),
                                    fg='#4F4F4F',
                                    bg='#FFFFEA')
                self.tempqt.place(x=160, y=self.y_index)
                self.tempprice = Label(self.right, text=str(products_price[self.counter]), font=('consolas 10 bold'),
                                       fg='#4F4F4F',
                                       bg='#FFFFEA')
                self.tempprice.place(x=290, y=self.y_index)

                self.y_index += 25
                self.counter += 1

                # total_l configure
                self.total_l.configure(text="Total Bill : " + str(sum(products_price)) + " Tk")

                # forget values
                self.quantityl.place_forget()
                self.quantitye.place_forget()

                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.pstock.configure(text="")
                self.cart_btn.destroy()

                self.enterpnamee.focus()
                self.enterpnamee.delete(0, END)

    # get the amount given by the customer

    def changecal(self, *args, **kwargs):
        self.givenammount = float(self.change_e.get())
        self.ourtotal = float(sum(products_price))
        self.togive = self.givenammount - self.ourtotal

        self.amounttogive = Label(self.left, text="Change " + str(self.togive) + " Tk", font=('helvetita 10 bold'),
                                  bg='#4F4F4F', fg='#FFFFEA')
        self.amounttogive.place(x=200, y=350)

        self.change_l.place_forget()
        self.change_e.place_forget()
        self.calculatechange_btn.destroy()

    def genbil(self, *args, **kwargs):
        # decrease the stock
        self.amounttogive.place_forget()
        pname = self.enterpnamee.get()
        self.x = 0

        initial = "SELECT * FROM inventory WHERE p_name=?"
        result = c.execute(initial, (products_list[self.x],))

        for i in products_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(products_quantity[self.x])

            sql = "UPDATE inventory SET p_stock=? WHERE p_name=?"
            c.execute(sql, (self.new_stock, products_list[self.x]))
            conn.commit()
            print("Done...")
            self.x += 1


root = Tk()
b = Application(root)
root.iconbitmap(default='logo.ico')
root.title("Sayem Digital Studio Software (Point of Sale)")
root.geometry("800x600+80+100")
root.mainloop()
