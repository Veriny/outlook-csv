import csv
from tkinter import *
def pogchamp():
    a = FirstName.get()
    b = LastName.get()
    d = Bio.get()
    c = GradYear.get()
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')
    with open('test.csv', mode = 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([a, b ,c, d, a, b, c, d])

root  = Tk()
label_1 = Label(root, text = "First Name")
label_2 = Label(root, text = "Last Name")
label_3 = Label(root, text = "Grad Year")
label_4 = Label(root, text = "Bio")

FirstName = StringVar()
LastName = StringVar()
GradYear = StringVar()
Bio = StringVar()

entry_1 = Entry(root, textvariable = FirstName)
entry_2 = Entry(root, textvariable = LastName)
entry_3 = Entry(root, textvariable = GradYear)
entry_4 = Entry(root, textvariable = Bio)

label_1.grid(row = 0)
label_2.grid(row = 1)
label_3.grid(row = 2)
label_4.grid(row = 3)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)
entry_3.grid(row = 2, column = 1)
entry_4.grid(row = 3, column = 1)



button1 = Button(root, text="Submit", command = pogchamp, fg = "blue")
button1.grid(columnspan = 2)
root.mainloop()
