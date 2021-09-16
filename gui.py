from tkinter import *
import tkinter.messagebox

app = Tk()
app.title("Card Games")

labelText = StringVar()
labelText.set("Click Button")
label1 = Label(app, textvariable=labelText, height=4)
label1.pack()

checkBoxVal = IntVar()
checkBox1 = Checkbutton(app, variable=checkBoxVal, text="Happy?")
checkBox1.pack()


app.mainloop()