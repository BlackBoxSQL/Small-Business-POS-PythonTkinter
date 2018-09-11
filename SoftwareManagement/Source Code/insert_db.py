from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("E:/Database/store.db")
c = conn.cursor()


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Sayem Digital Studio", font=("Helvetica", 20, "bold"), fg='#4F4F4F')
        self.heading.place(x=0, y=0)
        self.subheading = Label(master, text="Panch Gaon Golap Bajar, Araihazar, Narayanganj",
                                font=("Helvetica", 9, "bold"), fg='#4F4F4F')
        self.subheading.place(x=0, y=35)
        self.subheading = Label(master, text="Proprietor : Sayem Library", font=("Helvetica", 10, "normal"),
                                fg='#4F4F4F')
        self.subheading.place(x=0, y=60)
        self.subheading = Label(master, text="Contact : 01787325232", font=("Helvetica", 10, "normal"), fg='#4F4F4F')
        self.subheading.place(x=0, y=80)

        # label and entries for the window
        self.name_p_l = Label(master, text="Product Name : ", font=("Helvetica", 12, "bold"), fg='#00A9A5')
        self.name_p_l.place(x=0, y=150)
        self.price_p_l = Label(master, text="Product Price : ", font=("Helvetica", 12, "bold"), fg='#00A9A5')
        self.price_p_l.place(x=0, y=180)
        self.stock_p_l = Label(master, text="Products on Stock : ", font=("Helvetica", 12, "bold"), fg='#00A9A5')
        self.stock_p_l.place(x=0, y=210)
        # entries for the labels
        self.name_p_e = Entry(master, width=20, font=('Hevaltica 12 normal'), fg='#FF5E5B')
        self.name_p_e.place(x=170, y=150)
        self.price_p_e = Entry(master, width=20, font=('Hevaltica 12 normal'), fg='#FF5E5B')
        self.price_p_e.place(x=170, y=180)
        self.stock_p_e = Entry(master, width=20, font=('Hevaltica 12 normal'), fg='#FF5E5B')
        self.stock_p_e.place(x=170, y=210)
        # buttons for inserting
        self.btn_add = Button(master, text="Insert", width=7, height=1, bg='green', fg='white',
                              font=('Hevaltica 12 bold'), command=self.items)
        self.btn_add.place(x=170, y=240)
        self.btn_update = Button(master, text="Update", width=7, height=1, bg='orange', fg='white',
                                 font=('Hevaltica 12 bold'), command=self.update)
        self.btn_update.place(x=260, y=240)
        self.btn_delete = Button(master, text="Delete", width=7, height=1, bg='red', fg='white',
                                 font=('Hevaltica 12 bold'), command=self.delete_record)
        self.btn_delete.place(x=170, y=280)
        self.btn_clear = Button(master, text="Clear", width=7, height=1, bg='Black', fg='white',
                                font=('Hevaltica 12 bold'), command=self.clear_all)
        self.btn_clear.place(x=260, y=280)
        # advertise
        self.company = Label(master, text="Made by Nazibur Rahman", font=("Consolas", 10, "bold"), fg='#4F4F4F')
        self.company.place(x=640, y=540)
        self.company = Label(master, text="B.Sc. in Computer Science & Engineering", font=("Consolas", 10, "bold"),
                             fg='#4F4F4F')
        self.company.place(x=520, y=560)
        self.company = Label(master, text="Manarat International University, Ashulia", font=("Consolas", 10, "bold"),
                             fg='#4F4F4F')
        self.company.place(x=508, y=580)

    def items(self, *args, **kwargs):
        # get from entries
        self.name = self.name_p_e.get()
        self.price = self.price_p_e.get()
        self.stock = self.stock_p_e.get()

        if self.name == '' or self.price == '' or self.stock == '':
            tkinter.messagebox.showinfo("Error", "Please fill all the Entries.")
        else:
            sql = "INSERT INTO inventory (p_name,p_price,p_stock) VALUES(?,?,?)"
            c.execute(sql, (self.name, self.price, self.stock))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Successfully added to database")

    def clear_all(self, *args, **kwargs):
        self.name_p_e.delete(0, END)
        self.price_p_e.delete(0, END)
        self.stock_p_e.delete(0, END)

    def update(self, *args, **kwargs):
        self.name = self.name_p_e.get()
        self.price = self.price_p_e.get()
        self.stock = self.stock_p_e.get()

        if self.name == '' or self.stock == '':
            tkinter.messagebox.showinfo("Error", "Insert all the field to be updated.")
        else:
            query = "UPDATE inventory SET p_price = ?,p_stock = ? WHERE p_name=?"
            c.execute(query, (self.price, self.stock, self.name_p_e.get()))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Successfully Updated to database")

    def delete_record(self, *args, **kwargs):
        productname = str(self.name_p_e.get())
        c.execute("DELETE FROM inventory WHERE p_name=?", (productname,))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Successfully Deleted from database")


root = Tk()
root.iconbitmap(default='logo.ico')
b = Database(root)
root.geometry("800x600+80+100")
root.title("Sayem Digital Studio Software (Point of Sale)")
root.mainloop()
