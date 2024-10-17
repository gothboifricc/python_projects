from tkinter import *

window=Tk()
bgimage=PhotoImage(file="buttonimg.png")
#Label(window, image = bgimage).place(x=0,y=0)

l1=Button(window,image=bgimage,border=0)
l1.pack()

window.mainloop()

 #canvas = tk.Canvas(self, bg="red", height=600, width=600)

#        canvas.pack(expand=True, fill=tk.BOTH)

#        img = Image.open(r"img/myimg.png")
#        canvas.image = ImageTk.PhotoImage(img)
#        canvas.create_image(0,0, image=canvas.image, anchor='nw')
