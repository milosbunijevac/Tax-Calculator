from tkinter import *

def taxamount(price, tax):
    cost = price * (tax/100)
    totcost = price + cost
    return totcost

def butter():
    entryField.delete(0,'end') #Clears the entire entry field from index 0 to 'end
    price = pricefield.get()
    tax = taxfield.get()
    amount = taxamount(int(price),int(tax))
    entryer.set("The total cost after tip is: " + str(amount))


root = Tk()
root.configure(background="blue4")
root.title("Milos Tax Calculator")
root.resizable(1,0)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

entryer = StringVar()
entryField = Entry(root, textvariable=entryer,background="LightYellow2",foreground="blue4",justify=CENTER)
entryField.grid(row=0,column=0,columnspan=2,sticky=W+E)
entryField.columnconfigure(0,weight=1)

labelprice = Label(root, text="Price",background="blue4",foreground="PaleTurquoise1")
labelprice.grid(row=1,column=0, sticky=E)
taxpricelabel = Label(root, text="Tax amount (%)",background="blue4",foreground="PaleTurquoise1")
taxpricelabel.grid(row=2,column=0, sticky=E)

pricefield = Entry(root,background="SkyBlue2",foreground="blue4")
pricefield.grid(row=1,column=1,sticky=W)
taxfield = Entry(root,background="SkyBlue2",foreground="blue4")
taxfield.grid(row=2,column=1,sticky=W)

button = Button(root, text="Find total cost", command=butter)
button.grid(row=3, columnspan=2)


root.mainloop()

