from tkinter import Tk, Label, Entry, StringVar, Listbox, Scrollbar, Button, messagebox, N, S, W, END
from backend import Database

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Book App")

        self.l1=Label(self.root, text='Title')
        self.l1.grid(row=0,column=0)

        self.l2=Label(self.root, text='Author')
        self.l2.grid(row=0,column=1)

        self.l3=Label(self.root, text='Year')
        self.l3.grid(row=0,column=2)

        self.l4=Label(self.root, text='ISBN')
        self.l4.grid(row=0,column=3)

        self.title_text=StringVar()
        self.e1=Entry(self.root,textvariable=self.title_text)
        self.e1.grid(row=1,column=0)

        self.author_text=StringVar()
        self.e2=Entry(self.root,textvariable=self.author_text)
        self.e2.grid(row=1,column=1)

        self.year_text=StringVar()
        self.e3=Entry(self.root,textvariable=self.year_text)
        self.e3.grid(row=1,column=2)

        self.isbn_text=StringVar()
        self.e4=Entry(self.root,textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3, padx=5, pady=5)

        self.list1 = Listbox(self.root, height=12, width=65)
        self.list1.grid(row=2, rowspan=6, padx=5, pady=5, column=0, columnspan=3)

        self.list1.bind('<<ListboxSelect>>', self.get_selection)

        self.sb1 = Scrollbar(self.root)
        self.sb1.grid(row=2, rowspan=6, column=3, sticky=N+S+W)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.b1 = Button(self.root, text="Clear", width=12, command=self.view_command)
        self.b1.grid(row=2, column=3)

        self.b2 = Button(self.root, text="Search", width=12, command=self.search_command)
        self.b2.grid(row=3, column=3)

        self.b3 = Button(self.root, text="Add", width=12, command=self.add_command)
        self.b3.grid(row=4, column=3)

        self.b4 = Button(self.root, text="Update", width=12, command=self.update_command)
        self.b4.grid(row=5, column=3)

        self.b5 = Button(self.root, text="Delete", width=12, command=self.delete_command)
        self.b5.grid(row=6, column=3)

        self.view_command()

    def view_command(self):
        self.clear_entries()
        self.list1.delete(0,END)
        for item in books.view_all():
            self.list1.insert(END, item)

    def search_command(self):
        results = books.search(title  = self.title_text.get(),
                               author = self.author_text.get(),
                               year   = self.year_text.get(),
                               isbn   = self.isbn_text.get(),
                               strict = False)
        if len(results) == 0:
            messagebox.showinfo("Search", "No matches found")
        else:
            self.list1.delete(0,END)
            for item in results:
                self.list1.insert(END, item)
            
    def add_command(self):
        self.list1.delete(0,END)
        books.add_entry(title  = self.title_text.get(),
                        author = self.author_text.get(),
                        year   = self.year_text.get(),
                        isbn   = self.isbn_text.get())
        self.view_command()

    def clear_entries(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)

    def get_selection(self, event):
        try:
            self.clear_entries()
            index = self.list1.curselection()[0] # id
            self.selection = self.list1.get(index)
            self.e1.insert(END, self.selection[1]) # title
            self.e2.insert(END, self.selection[2]) # author
            self.e3.insert(END, self.selection[3]) # year
            self.e4.insert(END, self.selection[4]) # isbn
        except:
            pass
            
    def update_command(self):
        try:
            books.update(self.selection[0],
                         self.title_text.get(),
                         self.author_text.get(),
                         self.year_text.get(),
                         self.isbn_text.get())
        except:
            pass
        self.view_command()
        
    def delete_command(self):
        try:
            books.delete(self.selection[0])
        except:
            pass
        self.view_command()

if __name__ == "__main__":
    books = Database('books.db')
    root = Tk()
    main_window = Window(root)
    root.mainloop()