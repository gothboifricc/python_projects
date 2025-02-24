from tkinter import *
import backend

window=Tk()

bgimage=PhotoImage(file='Data/user2.png')
Label(window, image = bgimage).place(x=0,y=0)

icon_image = PhotoImage(file = 'Data/icon1.png')
window.iconphoto(False, icon_image)

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),pages_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),pages_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),pages_text.get()))

def delete_command():
    backend.delete(get_selected[0]) #the [0] gets the serial no. that is in 0 index of the whole row#

def get_selected_row(entry):
    global get_selected
    try:
        index=list1.curselection()[0]
        get_selected=list1.get(index)
        e1.delete(0,END)
        e1.insert(END, get_selected[1])
        e2.delete(0,END)
        e2.insert(END, get_selected[2])
        e3.delete(0,END)
        e3.insert(END, get_selected[3])
        e4.delete(0,END)
        e4.insert(END, get_selected[4])
    except IndexError:
        pass


def update_command():
    backend.update(get_selected[0],title_text.get(),author_text.get(),year_text.get(),pages_text.get())
    #print(title_text.get(),author_text.get(),year_text.get(),pages_text.get())

window.wm_title("My Library")

l1=Label(window,text="Title", width=12)
l1.grid(row=0,column=0)

l2=Label(window,text="Author", width=12)
l2.grid(row=0,column=2)

l3=Label(window,text="Year", width=12)
l3.grid(row=1,column=0)

l4=Label(window,text="Pages",width=12)
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text,width=20)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text,width=20)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text,width=20)
e3.grid(row=1,column=1)

pages_text=StringVar()
e4=Entry(window,textvariable=pages_text,width=20)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=8,columnspan=2)

list1.bind("<<ListboxSelect>>",get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=8)

sb2=Scrollbar(window,orient='horizontal')
sb2.grid(row=8,column=0,columnspan=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
sb2.configure(command=list1.xview)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
