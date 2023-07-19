# CODE FOR BILL GENERATOR:

from tkinter import *
from PIL import ImageTk, Image
# menu dictionary
menu = {0: ['Aloo Paratha', 30], 1: ['Samosa', 15], 2: ['Burger', 100], 3: ['Pizza', 150], 4: ['Momos', 150], 5: ['Shawarma', 100],
     6: ['Thumbs Up', 50], 7: ['Sprite', 50], 8: ['Pepsi', 50], 9: ['Coke', 50], 10: ['Tea', 20], 11: ['Coffee', 25]}
# List to store quantity of items
qty = []

splash_root = Tk()
splash_root.geometry("700x600")
splash_root.title("Bill Generator".center(170))
splash_root.resizable(False,False)
splash_img = ImageTk.PhotoImage(Image.open('gradient.png'))
Label(splash_root, image=splash_img).pack()
Label(splash_root, text="FOOD N JOY", font="times 40", bg='#d74cd0').place(x=210,y=240)


# main window function
def main():
   splash_root.destroy()
   window = Tk()
   window.geometry("700x600")
   window.title("Menu".center(180))
   window.resizable(False,False)

   menu_img = ImageTk.PhotoImage(Image.open('Menubg.png'))
   Label(window, image=menu_img).pack()

   # function to calculate the price of all the orders
   def calculate():
       temp_window = Toplevel()
       temp_window.geometry("500x400")
       temp_window.resizable(False,False)
       temp_window.config(bg='#6b88fe')
       temp_window.title("Bill".center(130))
       selected = []
       qty_selected = []
       price_selected = []
       total_selected = []
       total = 0
       for i in range(len(qty)):
           if int(qty[i].get()) > 0:
               price = int(qty[i].get()) * menu[i][1]
               total += price
               selected.append(menu[i][0])
               price_selected.append(menu[i][1])
               qty_selected.append(qty[i])
               total_selected.append(price)
       labelH = Label(temp_window, text="FOOD N JOY", font="times 20 bold", bg='#6b88fe')
       labelH.place(x=160,y=5)
       label_total = Label(temp_window, text=total)
       label_total.place(x=350, y=345)
       item = Label(temp_window, text="Item")
       item.place(x=30, y=45)
       price = Label(temp_window, text="Price")
       price.place(x=150, y=45)
       quantity = Label(temp_window, text="Quantity")
       quantity.place(x=250, y=45)
       total = Label(temp_window, text="Total")
       total.place(x=350, y=45)
       total_bill = Label(temp_window, text="Total: ")
       total_bill.place(x=300, y=345)

       c = 25
       for i in range(len(selected)):
           printItem = Label(temp_window, text=selected[i], bg='#6b88fe')
           printItem.place(x=20, y=45 + c)
           printItem2 = Label(temp_window, text=qty_selected[i].get(), bg='#6b88fe')
           printItem2.place(x=250, y=45 + c)
           printItem3 = Label(temp_window, text=price_selected[i], bg='#6b88fe')
           printItem3.place(x=150, y=45 + c)
           printItem4 = Label(temp_window, text=total_selected[i],bg='#6b88fe')
           printItem4.place(x=350, y=45 + c)
           c += 20

       def payment():
           temp_window.destroy()
           pay_window = Toplevel()
           pay_window.geometry("400x300")
           pay_window.config(bg='#6b88fe')
           pay_window.title("Payment Options")
           pay_window.resizable(False, False)

           def message():
               Label(pay_window, text="                              ", bg='#6b88fe').place(x=142, y=112)
               Label(pay_window, text="Thank You! Please visit again.",bg='#6b88fe').place(x=130, y=250)

           def message1():
               Label(pay_window, text="Scan below code", bg='#6b88fe').place(x=142, y=112)
               Label(pay_window, text="Thank You! Please visit again.",bg='#6b88fe').place(x=130, y=250)

           def exitwin():
               pay_window.destroy()
               window.destroy()

           img = ImageTk.PhotoImage(Image.open('UPI.png'))
           Label(pay_window, image=img).place(x=140, y=140)
           Button(pay_window, text='CASH ON DELIVERY', font='times 14 bold', command= message).place(x=90,y= 20)
           Button(pay_window, text='PAY BY UPI ', font='times 14 bold', command= message1).place(x=130, y=70)
           Button(pay_window, text='Done', command=exitwin).place(x=345, y=265)
           pay_window.mainloop()

       b2 = Button(temp_window, text='Proceed to pay',command=payment)
       b2.place(x=400,y=370)
       temp_window.mainloop()
   label1 = Label(window,text="Menu", font="times 28 bold")
   label1.place(x=300, y=10)

   label2 = Label(window, text="Snacks", font="times 18")
   label2.place(x=50, y=50)

   label3 = Label(window, text="Item", font="times 15")
   label3.place(x=30, y=85)

   label4 = Label(window, text="₹", font="times 15")
   label4.place(x=130, y=85)

   label5 = Label(window, text="Refreshments", font="times 18")
   label5.place(x=450, y=50)

   label6 = Label(window, text="Item", font="times 15")
   label6.place(x=430, y=85)

   label7 = Label(window, text="₹", font="times 15")
   label7.place(x=530, y=85)

   label10 = Label(window, text="Aloo Paratha", font="times 13", bg='#6b88fe')
   label10.place(x=20, y=120)
   label10a = Label(window, text="30", font="times 13", bg='#6b88fe')
   label10a.place(x=130, y=120)
   sv1 = IntVar()
   sb1 = Spinbox(window, from_=0, to_=5, textvariable=sv1)
   sb1.place(x=170, y=120, width=30, height=25)
   qty.append(sv1)

   label11 = Label(window, text="Samosa", font="times 13", bg='#6b88fe')
   label11.place(x=20, y=150)
   label11a = Label(window, text="15", font="times 13", bg='#6b88fe')
   label11a.place(x=130, y=150)
   sv2 = IntVar()
   sb2 = Spinbox(window, from_=0, to_=5, textvariable=sv2)
   sb2.place(x=170, y=150, width=30, height=25)
   qty.append(sv2)

   label12 = Label(window, text="Veg Burger", font="times 13", bg='#6b88fe')
   label12.place(x=20, y=180)
   label12a = Label(window, text="100", font="times 13", bg='#6b88fe')
   label12a.place(x=130, y=180)
   sv3 = IntVar()
   sb3 = Spinbox(window, from_=0, to_=5, textvariable=sv3)
   sb3.place(x=170, y=180, width=30, height=25)
   qty.append(sv3)

   label13 = Label(window, text="Pizza", font="times 13", bg='#6b88fe')
   label13.place(x=20, y=210)
   label13a = Label(window, text="150", font="times 13", bg='#6b88fe')
   label13a.place(x=130, y=210)
   sv4 = IntVar()
   sb4 = Spinbox(window, from_=0, to_=5, textvariable=sv4)
   sb4.place(x=170, y=210, width=30, height=25)
   qty.append(sv4)

   label14 = Label(window, text="Momos", font="times 13", bg='#6b88fe')
   label14.place(x=20, y=240)
   label14a = Label(window, text="150", font="times 13", bg='#6b88fe')
   label14a.place(x=130, y=240)
   sv5 = IntVar()
   sb5 = Spinbox(window, from_=0, to_=5, textvariable=sv5)
   sb5.place(x=170, y=240, width=30, height=25)
   qty.append(sv5)

   label15 = Label(window, text="Shawarma", font="times 13", bg='#6b88fe')
   label15.place(x=20, y=270)
   label15a = Label(window, text="100", font="times 13", bg='#6b88fe')
   label15a.place(x=130, y=270)
   sv6 = IntVar()
   sb6 = Spinbox(window, from_=0, to_=5, textvariable=sv6)
   sb6.place(x=170, y=270, width=30, height=25)
   qty.append(sv6)

   label16 = Label(window, text="Thumbs Up", font="times 13", bg='#6b88fe')
   label16.place(x=420, y=120)
   label16a = Label(window, text="50", font="times 13", bg='#6b88fe')
   label16a.place(x=530, y=120)
   sv7 = IntVar()
   sb7 = Spinbox(window, from_=0, to_=5, textvariable=sv7)
   sb7.place(x=570, y=120, width=30, height=25)
   qty.append(sv7)

   label17 = Label(window, text="Sprite", font="times 13", bg='#6b88fe')
   label17.place(x=420, y=150)
   label17a = Label(window, text="50", font="times 13", bg='#6b88fe')
   label17a.place(x=530, y=150)
   sv8 = IntVar()
   sb8 = Spinbox(window, from_=0, to_=5, textvariable=sv8)
   sb8.place(x=570, y=150, width=30, height=25)
   qty.append(sv8)

   label18 = Label(window, text="Pepsi", font="times 13", bg='#6b88fe')
   label18.place(x=420, y=180)
   label18a = Label(window, text="50", font="times 13", bg='#6b88fe')
   label18a.place(x=530, y=180)
   sv9 = IntVar()
   sb9 = Spinbox(window, from_=0, to_=5, textvariable=sv9)
   sb9.place(x=570, y=180, width=30, height=25)
   qty.append(sv9)

   label19 = Label(window, text="Coke", font="times 13", bg='#6b88fe')
   label19.place(x=420, y=210)
   label19a = Label(window, text="50", font="times 13", bg='#6b88fe')
   label19a.place(x=530, y=210)
   sv10 = IntVar()
   sb10 = Spinbox(window, from_=0, to_=5, textvariable=sv10)
   sb10.place(x=570, y=210, width=30, height=25)
   qty.append(sv10)

   label20 = Label(window, text="Tea", font="times 13", bg='#6b88fe')
   label20.place(x=420, y=240)
   label20a = Label(window, text="20", font="times 13", bg='#6b88fe')
   label20a.place(x=530, y=240)
   sv11 = IntVar()
   sb11 = Spinbox(window, from_=0, to_=5, textvariable=sv11)
   sb11.place(x=570, y=240, width=30, height=25)
   qty.append(sv11)

   label21 = Label(window, text="Coffee", font="times 13", bg='#6b88fe')
   label21.place(x=420, y=270)
   label21a = Label(window, text="25", font="times 13", bg='#6b88fe')
   label21a.place(x=530, y=270)
   sv12 = IntVar()
   sb12 = Spinbox(window, from_=0, to_=5, textvariable=sv12)
   sb12.place(x=570, y=270, width=30, height=25)
   qty.append(sv12)

   Button(window, text="Get Bill", font="14",command=calculate).place(x=230, y=350, width=200, height=50)
   window.mainloop()


splash_root.after(1500,main)
mainloop()


