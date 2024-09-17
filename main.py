from tkinter import *

window = Tk()
window.title("Converter")
window.minsize(width=400, height=40)

#Conversion method

def convert_milestokm():
    mile = float(first_unit.get())
    Km = round(mile * 1.609)

    results.config(text=Km)
def conver_kmtomiles():
    km = float(first_unit.get())
    Mile = round(km / 1.609)

    results.config(text=Mile)
def convert_cmtoinches():
    Cm = float(first_unit.get())
    Inch = round(Cm / 2.54)

    results.config(text=Inch)
def convert_inchestocm():
    Inch = float(first_unit.get())
    Cm = round(Inch * 2.54)

    results.config(text=Cm)



#Miles input
first_unit = Entry(width=10)

first_unit.place(x=130, y=45)
#Miles label
first_unit_label = Label(text="Miles")
first_unit_label.place(x=180, y=45)
#button
button = Button(text="calculate", command=convert_milestokm)
button.place(x=130, y=100)
#equal to label
is_equal = Label(text=f"Is equal to")
is_equal.place(x=70, y=70)

#results
results = Label(text="0")
results.place(x=150, y=70)

#2nd unit
second_unit_label = Label(text="Km")
second_unit_label.place(x=180, y=70)

#Reset
def reset():
    results.config(text="0")

def listbox_used(event):
    # Gets current selection from listbox
    if listbox.get(listbox.curselection()) == "Km to Miles":
        reset()
        second_unit_label.config(text="Miles")
        first_unit_label.config(text="Km")
        button.config(command=conver_kmtomiles)
    elif listbox.get(listbox.curselection()) == "Miles to Km":
        reset()
        second_unit_label.config(text="Km")
        first_unit_label.config(text="Miles")
        button.config(command=convert_milestokm)
    elif listbox.get(listbox.curselection()) == "Cm to Inches":
        reset()
        second_unit_label.config(text="Inches")
        first_unit_label.config(text="Cm")
        button.config(command=convert_cmtoinches)
    elif listbox.get(listbox.curselection()) == "Inches to Cm":
        reset()
        second_unit_label.config(text="Cm")
        first_unit_label.config(text="Inches")
        button.config(command=convert_inchestocm)


listbox = Listbox(height=4)
fruits = ["Miles to Km", "Km to Miles", "Cm to Inches", "Inches to Cm"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.place(x=200, y=100)







window.mainloop()
