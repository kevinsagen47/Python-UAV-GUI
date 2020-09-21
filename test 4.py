from tkinter import *

root =Tk()
root.title("some application")
root.geometry("1024x600")


# upper left grid 

#upperleft = tk.Canvas(root, width=512, height=400, background="#ffffff")
upperleft = Frame(root, bg='cyan', width = 512, height=300, pady=3).grid(row=0, columnspan=4)
Label(upperleft, text = 'Model Dimensions').grid(row = 0, columnspan = 3)
Label(upperleft, text = 'Width:').grid(row = 1, column = 0)
Label(upperleft, text = 'Length:').grid(row = 1, column = 2)
entry_W = Entry(upperleft).grid(row = 1, column = 1)
entry_L = Entry(upperleft).grid(row = 1, column = 3)

#upperleft.grid(row=1, column=2)

#upper right

upperright = Frame(root, bg='red', width = 512, height=300, pady=3).grid(row=0, columnspan=4,column=4)
Label(upperright, text = 'Model Dimensions').grid(row = 0, columnspan = 3)
Label(upperright, text = 'Width:').grid(row = 1, column = 0)
Label(upperright, text = 'Length:').grid(row = 1, column = 2)
entry_W = Entry(upperright).grid(row = 1, column = 1)
entry_L = Entry(upperright).grid(row = 1, column = 3)


# lower left




#lowe right



root.mainloop()