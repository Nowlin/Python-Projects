import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column=2, padx=(10,10) , pady=(10,10))

        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        self.btn.grid(row=3, column=3, padx=(10,10) , pady=(10,10))

        self.lbl_ctext = tk.Label(self.master,text='Enter custom text of click the Default HTML page button')
        self.lbl_ctext.grid(row=1, column=1, columnspan=2, padx=(10,10) , pady=(10,10))

        self.htmlText = tk.Entry(self.master,text='', width=100)
        self.htmlText.grid(row=2, column=1, columnspan=3, padx=(10,10) , pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customText(self):
        htmlText = self.htmlText.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
