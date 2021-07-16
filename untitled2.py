from tkinter import*
from tkinter import filedialog
from PIL import ImageTk,Image
import os

root=Tk()
root.title("HTML")
root.geometry("650x650")

image=Image.open('folder.png')
image = image.resize((30, 30), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)

image1=Image.open('save.png')
image = image.resize((30, 30), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)

image2=Image.open('play.png')
image = image.resize((30, 30), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)

open_image=ImageTk.PhotoImage(Image.open("folder.png"))
save_image=ImageTk.PhotoImage(Image.open("save.png"))
close_image=ImageTk.PhotoImage(Image.open("images.png"))

file_name_label=Label(root,text="File Name")
file_name_label.place(relx=0.4,rely=0.1,anchor=CENTER)
input_file=Entry(root)
input_file.place(relx=0.6,rely=0.1,anchor=CENTER)

input_textArea=Text(root,height=35,width=150)
input_textArea.place(relx=0.1,rely=0.2)

html_name=""
def open_file():
    global html_name
    input_textArea.delete(1.0,END)
    input_file.delete(0,END)
    text_file=filedialog.askopenfilename(title="open text file",filetypes=(("text files","*.txt"),))
    print(text_file)
    html_name=os.path.basename(text_file)
    formatted_name=html_name.split('.')[0]
    input_file.insert(END,formatted_name)
    root.title(formatted_name)
    text_file=open(html_name,'r')
    paragraph=text_file.read()
    input_textArea.insert(END,paragraph)
    text_file.close()
    
def save():
    input_name=input_file.get()
    file=open(input_name+".txt","w")
    data=input_textArea.get(1.0,END)
    print(data)
    file.write(data)
    input_file.delete(0,END)
    input_textArea.delete(1.0,END)
    messagebox.showinfo("Update","Success")
    
def close():
    root.destroy()
    
btn_open=Button(root,image=open_image,text="image",command=open_file)
btn_open.place(relx=0.1,rely=0.1,anchor=CENTER)
btn_save=Button(root,image=save_image,text="image1",command=save)
btn_save.place(relx=0.2,rely=0.1,anchor=CENTER)
btn_close=Button(root,image=close_image,text="image2",command=close)
btn_close.place(relx=0.3,rely=0.1,anchor=CENTER)

root.mainloop()