from tkinter import Tk, Label, Entry, StringVar, Listbox, Scrollbar, Button, messagebox, N, S, W, END
import backend as backend

def view_command():
    clear_entries()
    list1.delete(0,END)
    for item in backend.view_all():
        list1.insert(END, item)

def search_command():
    results = backend.search(title=title_text.get(),
                            author=author_text.get(),
                            year=year_text.get(),
                            isbn=isbn_text.get(),
                            strict=False)
    if len(results) == 0:
        messagebox.showinfo("Search", "No matches found")
    else:
        list1.delete(0,END)
        for item in results:
            list1.insert(END, item)
        
def add_command():
    list1.delete(0,END)
    backend.add_entry(title=title_text.get(),
                      author=author_text.get(),
                      year=year_text.get(),
                      isbn=isbn_text.get())
    view_command()

def clear_entries():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def get_selection(event):
    global selection
    try:
        clear_entries()
        index = list1.curselection()[0] # id
        selection = list1.get(index)
        e1.insert(END, selection[1]) # title
        e2.insert(END, selection[2]) # author
        e3.insert(END, selection[3]) # year
        e4.insert(END, selection[4]) # isbn
    except:
        pass
        
def update_command():
    try:
        backend.update(selection[0],
                    title_text.get(),
                    author_text.get(),
                    year_text.get(),
                    isbn_text.get())
    except:
        pass
    view_command()
    
def delete_command():
    try:
        backend.delete(selection[0])
    except:
        pass
    view_command()

#def close_command():
#    exit()

if __name__ == "__main__":
    window = Tk()
    window.title("Book App")

    l1=Label(window, text='Title')
    l1.grid(row=0,column=0)

    l2=Label(window, text='Author')
    l2.grid(row=0,column=1)

    l3=Label(window, text='Year')
    l3.grid(row=0,column=2)

    l4=Label(window, text='ISBN')
    l4.grid(row=0,column=3)

    title_text=StringVar()
    e1=Entry(window,textvariable=title_text)
    e1.grid(row=1,column=0)

    author_text=StringVar()
    e2=Entry(window,textvariable=author_text)
    e2.grid(row=1,column=1)

    year_text=StringVar()
    e3=Entry(window,textvariable=year_text)
    e3.grid(row=1,column=2)

    isbn_text=StringVar()
    e4=Entry(window,textvariable=isbn_text)
    e4.grid(row=1,column=3, padx=5, pady=5)

    list1 = Listbox(window, height=12, width=65)
    list1.grid(row=2, rowspan=6, padx=5, pady=5, column=0, columnspan=3)

    list1.bind('<<ListboxSelect>>', get_selection)

    sb1 = Scrollbar(window)
    sb1.grid(row=2, rowspan=6, column=3, sticky=N+S+W)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    b1 = Button(window, text="Clear", width=12, command=view_command)
    b1.grid(row=2, column=3)

    b2 = Button(window, text="Search", width=12, command=search_command)
    b2.grid(row=3, column=3)

    b3 = Button(window, text="Add", width=12, command=add_command)
    b3.grid(row=4, column=3)

    b4 = Button(window, text="Update", width=12, command=update_command)
    b4.grid(row=5, column=3)

    b5 = Button(window, text="Delete", width=12, command=delete_command)
    b5.grid(row=6, column=3)

 #   b6 = Button(window, text="Close", width=12, command=close_command)
 #   b6.grid(row=7, column=3)

    view_command()
    window.mainloop()