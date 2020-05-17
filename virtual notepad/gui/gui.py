from digit import *
import tkinter as tk
import cv2
root = tk.Tk()
root.title('handwriting recogntion')

button1=tk.Button(root,text='Clear',fg='blue',command=clear)
button1.place(x=70,y=70,width=100,height=40)
button2=tk.Button(root,text='Start',fg='green',command=number)
button2.place(x=200,y=70,width=70,height=40)

button = tk.Button(root,text="QUIT",fg="red",command=quit)
button.place(x=130,y=170,width=100,height=40)

root.geometry("400x300")
root.mainloop()