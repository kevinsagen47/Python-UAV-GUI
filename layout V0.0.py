import tkinter as tk

class Example():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UAV Control GUI")

        # menu left
        self.menu_left = tk.Frame(self.root, width=512, bg="#ababab")
        self.menu_left_upper = tk.Frame(self.menu_left, width=512, height=300, bg="red")
        self.menu_left_lower = tk.Frame(self.menu_left, width=512, bg="blue")

        self.test = tk.Label(self.menu_left_upper, text="test")
        self.test.pack()

        self.menu_left_upper.pack(side="top", fill="both", expand=True)
        self.menu_left_lower.pack(side="top", fill="both", expand=True)

        # right area
        self.menu_right = tk.Frame(self.root, width=512, bg="#ababab")
        self.menu_left_upper = tk.Frame(self.menu_left, width=150, height=300, bg="red")
        self.menu_left_lower = tk.Frame(self.menu_left, width=150, bg="blue")

        self.test = tk.Label(self.menu_left_upper, text="test")
        self.test.pack()

        self.menu_left_upper.pack(side="top", fill="both", expand=True)
        self.menu_left_lower.pack(side="top", fill="both", expand=True)






        # status bar
        self.status_frame = tk.Frame(self.root)
        self.status = tk.Label(self.status_frame, text="this is the status bar")
        self.status.pack(fill="both", expand=True)

        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.some_title_frame.grid(row=0, column=1, sticky="ew")
        self.canvas_area.grid(row=1, column=1, sticky="nsew") 
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.root.mainloop()

Example()
