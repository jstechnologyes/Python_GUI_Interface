import tkinter as tk
r=tk.Tk()
r.title("main window")
button=tk.Button(r, text='Stop', width=50, command=r.destroy)
button.pack()
r.mainloop()