import tkinterweb
import tkinter as tk
root = tk.Tk()
root.geometry("700x400")
root.maxsize(700,400)
root.eval('tk::PlaceWindow . center')
frame = tkinterweb.HtmlFrame(root)
frame.load_website('http://127.0.0.1:5000/')
frame.pack(fill="both", expand=True)
root.mainloop()