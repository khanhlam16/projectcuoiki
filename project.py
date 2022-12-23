from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import ttk
from keras.utils import load_img,img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import os
from tkinter.filedialog import *
from tkinter.messagebox import *
from functools import partial
import time
import numpy as np
file =''
Label1 = ''
model_CNN = ''
os.environ['TF CPP MIN LOG LEVEL'] = '2'
model_CNN = load_model('nhaccu.h5')
wd1 = Tk()
wd1.geometry('700x500+370+80')
wd1.title('Nhận diện nhạc cụ cổ truyền Việt Nam ')
wd1.iconbitmap('C:/Users/Khanh Lam/OneDrive/Desktop/Project AI cuoi ki//icon.ico')
wd1.resizable(False,False)
canvas_wd1 = Canvas(wd1, width=700, height=500)
bg_wd1 = Image.open('C:/Users/Khanh Lam/OneDrive/Desktop/Project AI cuoi ki//nen.jpg')
n_bg_wd1 = bg_wd1.resize((700,500),Image.Resampling.LANCZOS)
open_n_bg_wd1 = ImageTk.PhotoImage(n_bg_wd1)
canvas_wd1.create_image(0, 0, anchor=NW, image=open_n_bg_wd1)
canvas_wd1.pack()
def open_wd2():
	wd2 = Toplevel(wd1)
	wd2.title('Nhận diện nhạc cụ cổ truyền Việt Nam')
	wd2.iconbitmap('C:/Users/Khanh Lam/OneDrive/Desktop/Project AI cuoi ki//icon.ico')
	wd2.geometry('500x500+420+60')
	wd2.resizable(False, False)
	LB_wd2 = LabelFrame(wd2,bg = 'light blue', width=500, height=500)
	LB_wd2.pack()
	fr_wd2 = Frame(LB_wd2,bg = 'white', width = 490,height = 300)
	fr_wd2.place(x=3,y=3)
	Label2 = Label(LB_wd2,text = "Kết quả:",font = ('Arial',16),bg = 'light blue').place( x = 10, y = 350)
	Label2_value = Entry(LB_wd2,width = 20,font = ('Arial',16))
	Label2_value.place( x = 100, y = 350)
	wd1.withdraw()
	wd2.deiconify()
	def open_file():
		cancel()
		global file,Label1
		file = askopenfilename(defaultextension = '.jpg',filetypes = [('All Files','*.*'),('JPG Files','*.jpg'),('PNG Files','*.png')])
		if file == '':
			showinfo('Thông báo','Vui lòng chọn ảnh!')
		else:
			openfile = Image.open(file)
			n_openfile = openfile.resize((485,300), Image.Resampling.LANCZOS)
			showfile = ImageTk.PhotoImage(n_openfile)
			Label1 = Label(fr_wd2,image = showfile)
			Label1.pack()
			mainloop()
	def cancel():
		global Label1,Frame1,file
		if Label1 == '':
			return
		else:
			Label1.destroy()
		file = ''
		fr_wd2.configure()
		Label2_value.delete(0,END)
	def check():
		global file,model_CNN
		if file =='':
			showinfo('Thông báo','Vui lòng chọn ảnh!')
		else:
			img = load_img(file,target_size =(224,224))
			img = img_to_array(img)
			img = img.astype('float32')
			img = img/255
			img = np.expand_dims(img,axis=0)
			result = model_CNN.predict(img)
			classname = ['Sáo trúc', 'Song loan',"Đàn T'rưng",'Đàn bầu','Đàn cò','Đàn nguyệt',

			'Đàn sến','Đàn tranh','Đàn tì bà','Đàn đáy']
			for i in range (0,10):
				if round(result[0][i])== 1:
					prediction = classname[i]
			a = f"Đây là '{prediction}'"
			Label2_value.insert(0,a)
	button_check=Button(LB_wd2,text='Kiểm tra',font = ('Arial',16),bg='yellow',command = check)
	button_check.place(x=130,y=430)
	button_choose=Button(LB_wd2,text='Chọn ảnh',font = ('Arial',16),bg='blue',command = open_file)
	button_choose.place(x=20,y=430)
	button_cancel=Button(LB_wd2,text='Thoát',font = ('Arial',16),bg='red',command = cancel)
	button_cancel.place(x=230,y=430)
button_next=Button(wd1,text='BẮT ĐẦU',font = ('Arial',16),bg='yellow',command = open_wd2)
button_next.place(x=300,y=380)


mainloop()
