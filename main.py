import boto3
import os, sys
from tkinter import *
import tkinter as tk
import codecs
from tkinter import ttk
from tkinter import filedialog
import time
from threading import Thread
import requests as rq
import json
from tkinter import messagebox
import webbrowser
login_bas=1
import time
from hurry.filesize import size
from tkinter.ttk import Combobox
from tkinter import colorchooser
from tkinter.filedialog import asksaveasfile
import tkinter.messagebox

def Save_f(path, text_for_save):
	filename1 = path
	file = open(filename1, 'w', encoding='utf8')
	file.write(text_for_save)
	file.close()

def window_text(path):
	if 1:
		if 1:
			if 1:
				newWin = tk.Tk()

				screen_w = 800#newWin.winfo_screenwidth()
				screen_h = 600#newWin.winfo_screenheight()

				w = screen_w-15
				h = screen_h-85

				resolution = str(w)+'x'+str(h)

				newWin.geometry(resolution)

				menu = Menu(newWin)
				new_item = Menu(menu)
				new_item.add_command(label='Сохранить', command=lambda: Save_f(path, message_text.get("1.0", tk.END)))
				new_item.add_command(label='Выйти', command=lambda: newWin.destroy())
				menu.add_cascade(label='Файл', menu=new_item)
				newWin.config(menu=menu)

				message_text = Text(newWin, bg='light cyan', fg='black')
				message_text.place(relx=.5, rely=.5, anchor="c", height=h-100, width=w-30)
				if 1:
					filename1 = path
					file1 = open(filename1, 'r', encoding='utf8')



					for l in file1:
						message_text.insert(tk.END, l)

					file1.close()
					fileopen = Label(text=str(filename1), bg='yellow')
					fileopen.grid(column=1, row=1)
					btn_cls = tk.Button(text="Х", command=lambda: btn_cls_func())
					btn_cls.grid(column=3, row=1)

					def btn_cls_func():
						win_ext = Tk()

						label_ext = tk.Label(win_ext, text='Вы действительно хотите выйти?')
						label_ext.pack()
						frame = Frame(win_ext)
						yes_ext = tk.Button(frame,text='Да', command=lambda:ext()).grid(padx=10, column=1, row=0 , pady=2 , sticky="nsew")
						no_ext = tk.Button(frame,text='Нет', command=lambda:win_ext.destroy()).grid( row=0, padx=10 , pady=2 , sticky="nsew")
						frame.pack()

						def ext():
							btn_cls.destroy()

							try:
								Save_f(path, message_text.get("1.0", tk.END))
							except AttributeError as error_data:
								pass

							fileopen.destroy()
							win_ext.destroy()
							message_text.delete('1.0', tk.END)







#
def save_settings():
	with open("settings.json", 'w') as set_prog_f:
		set_prog_f.write(json.dumps(settings))

#losd settings
settings = {"recent_use": []}
try:
	with open("settings.json", 'r') as set_prog_f:
		settings = json.loads(set_prog_f.read())
except:
	save_settings()

#
def add_tree_l(rec):
	settings['recent_use'].append(rec)
	save_settings()
	rtee.append(tree.insert('', 'end', text=os.path.basename(rec), values=(f_this_space(os.path.dirname(rec)))))

#
def  alert(msg_alert):
	messagebox.showinfo(message=msg_alert)

def f_this_space(text_w_probel):
	bez_probela = ''
	for jkjkjk in text_w_probel:
		if jkjkjk == ' ':
			bez_probela= bez_probela + '\ '
		else:
			bez_probela = bez_probela + jkjkjk
	return bez_probela

#
def obrtka(f_ober):
	try:
		f_ober()
	except BaseException as err:
		print(err)
		print(traceback.format_exc())

#
def stat_connekt():
	staaaatt['text'] = 'Подключение к серверу!'
	staaaatt['bg'] = 'yellow'
	time.sleep(5)
	while 1:
		try:
			try:
				r = rq.get('https://functions.yandexcloud.net/d4ek6eurb4ek7b51tl99')
				scodet = r.status_code
				if scodet == 200:
					staaaatt['text'] = 'Связь с сервером есть!'
					staaaatt['bg'] = 'green'
				else:
					staaaatt['text'] = 'Нет связи с сервером!'
					staaaatt['bg'] = 'red'
			except:
				staaaatt['text'] = 'Нет связи с сервером!'
				staaaatt['bg'] = 'red'
			time.sleep(5)
		except:
			break

#
def SAVE():
	pass

#
item_select = 0
def tree_selection(event):
	for selection in tree.selection():
		global item_select
		item_select = selection
		#print(tree.item(item_select)['text'])

#
tab_selection = 1
def Tab_selection_e(event):
	global tab_selection
	if tab_selection:
		tab_selection = 0
		Buttons['down_up_f']['text'] = 'Загрузить'

	else:
		tab_selection = 1
		Buttons['down_up_f']['text'] = 'Скачать'

#
def close_app():
	save_settings()
	root.destroy()
	sys.exit(1)

#
def ask_cont(ask):
	ask_how = messagebox.askyesno(
	   message=ask,
	   icon='question', title=ask, type='yesno')
	return ask_how

#
def win_info_f_dismiss (win_info_f):
	win_info_f.grab_release()
	win_info_f.destroy()

#
htyjtyjtyjytyjyj = ''
def dlg_dismiss (dlg, new_name_dlg):
	global htyjtyjtyjytyjyj
	htyjtyjtyjytyjyj = new_name_dlg.get()
	dlg.grab_release()
	dlg.destroy()
def dlg_cr_dir():
	global htyjtyjtyjytyjyj
	dlg = Toplevel(root)


	w = root.winfo_width()
	h = root.winfo_height()

	stgg = 0
	xcord = ''
	ycord = ''
	for kjkd in root.geometry():
		if kjkd == '+':
			stgg = stgg +1
		elif stgg==1:
			xcord = xcord + kjkd
		elif stgg==2:
			ycord = ycord + kjkd
		else:
			pass
	xcord=int(xcord)
	ycord=int(ycord)
	dlg.title('Cоздать директорию...')
	Label(dlg, text='Введите имя директории:').grid()
	new_name_dlg = Entry(dlg)
	new_name_dlg.grid()
	ttk.Button(dlg, text="Создать", command= lambda: dlg_dismiss(dlg, new_name_dlg)).grid()
	w = w//2
	h = h//2
	w1 = xcord + w
	w2 = ycord + h

	dlg.transient(root)   # dialog window is related to main
	dlg.wait_visibility() # can't grab until window appears, so we wait
	dlg.grab_set()        # ensure all input goes to our window

	w11 = dlg.winfo_width() //2
	w21 = dlg.winfo_height() //2
	dlg.geometry('+{}+{}'.format(w1 - w11, w2 - w21))

	dlg.protocol("WM_DELETE_WINDOW", lambda:  dlg_dismiss(dlg, new_name_dlg)) # intercept close button
	dlg.wait_window()     # block until window is destroyed
	return htyjtyjtyjytyjyj

def dlg_rename():
	global htyjtyjtyjytyjyj
	dlg = Toplevel(root)


	w = root.winfo_width()
	h = root.winfo_height()

	stgg = 0
	xcord = ''
	ycord = ''
	for kjkd in root.geometry():
		if kjkd == '+':
			stgg = stgg +1
		elif stgg==1:
			xcord = xcord + kjkd
		elif stgg==2:
			ycord = ycord + kjkd
		else:
			pass
	xcord=int(xcord)
	ycord=int(ycord)
	dlg.title('Переименовать')
	Label(dlg, text='Введите новое имя файла:').grid()
	new_name_dlg = Entry(dlg)
	new_name_dlg.grid()
	ttk.Button(dlg, text="Переименовать", command= lambda: dlg_dismiss(dlg, new_name_dlg)).grid()
	w = w//2
	h = h//2
	w1 = xcord + w
	w2 = ycord + h

	dlg.transient(root)   # dialog window is related to main
	dlg.wait_visibility() # can't grab until window appears, so we wait
	dlg.grab_set()        # ensure all input goes to our window

	w11 = dlg.winfo_width() //2
	w21 = dlg.winfo_height() //2
	dlg.geometry('+{}+{}'.format(w1 - w11, w2 - w21))

	dlg.protocol("WM_DELETE_WINDOW", lambda:  dlg_dismiss(dlg, new_name_dlg)) # intercept close button
	dlg.wait_window()     # block until window is destroyed
	return htyjtyjtyjytyjyj



#КНОПКИ

#
def add_f():
	if login_bas:
		print('add_f')
	filename = filedialog.askopenfilename()
	if os.path.isfile(filename):
		for antempxz in settings['recent_use']:
			if filename == antempxz:
				alert('Этот файл уже добавлен!')
				return 0
		add_tree_l(filename)
	else:
		alert('Кажется такой файл уже добавлен либо вы не выбрали файл!')

#
def rem_f():
	if login_bas:
		print('rem_f')
	global item_select
	if item_select:
		#print(tree.item(item_select)['values'][0].encode(encoding='UTF-8',errors='strict'))
		settings['recent_use'].remove(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text'])
		tree.delete(item_select)
		save_settings()

#
def rename_f():
	if login_bas:
		print('rename_f')

	global item_select
	if tab_selection:
		alert('Мы пока не работаем с облаком(')
	else:
		if item_select:
			if os.path.isfile(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']):

				temp_name = dlg_rename()
				old_path = tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']
				old_dir = tree.item(item_select)['values'][0] + '/'
				os.rename(old_path, old_dir + temp_name)
				iterdorsss = 0
				for vremen in settings['recent_use']:
					if vremen==old_path:
						settings['recent_use'][iterdorsss] = old_dir + temp_name
					iterdorsss = iterdorsss + 1

				save_settings()
				tree.delete(item_select)
				rtee.append(tree.insert('', 'end', text=os.path.basename(old_dir + temp_name), values=(f_this_space(os.path.dirname(old_dir + temp_name)))))
			else:
				alert('Файл был удалён или перемещён')

#
def share_f():
	if login_bas:
		print('share_f')
	alert('Мы пока не работаем с облаком(')

#
def edit_f():
	if login_bas:
		print('edit_f')
	if os.path.isfile(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']):
		window_text(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text'])
	else:
		alert('Файл был удалён или перемещён')

#
def open_f():
	if login_bas:
		print('open_f')
	if tab_selection:
		alert('Мы пока не работаем с облаком(')
	else:
		if item_select:
			if os.path.isfile(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']):
				webbrowser.open(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text'])
			else:
				alert('Файл был удалён или перемещён')

#
def down_up_f():
	if login_bas:
		print('down_f')
	alert('Мы пока не работаем с облаком(')

#
def del_f():
	if login_bas:
		print('del_local_f')
	if tab_selection:
		alert('Мы пока не работаем с облаком(')
	else:
		if item_select:
			ffffff = tree.item(item_select)['text']
			if ask_cont(f'Вы действительно хотите удалить {ffffff}?'):
				if os.path.isfile(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']):
					os.remove(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text'])
					rem_f()
				else:
					alert('Файл был удалён или перемещён')

#
def info_f():
	if login_bas:
		print('del_cloud_f')
	if os.path.isfile(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']):
		win_info_f = Toplevel(root)

		w = root.winfo_width()
		h = root.winfo_height()
		path = tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']
		stgg = 0
		xcord = ''
		ycord = ''
		for kjkd in root.geometry():
			if kjkd == '+':
				stgg = stgg +1
			elif stgg==1:
				xcord = xcord + kjkd
			elif stgg==2:
				ycord = ycord + kjkd
			else:
				pass
		xcord=int(xcord)
		ycord=int(ycord)
		win_info_f.title('О файле: '+tree.item(item_select)['text'])


		Label(win_info_f, text='Время последнего доступа к файлу:').grid( sticky='nsew')
		Label(win_info_f, text=time.ctime(os.path.getatime(path)) ).grid()

		Label(win_info_f, text='Время последнего изменения файла:').grid()
		Label(win_info_f, text=time.ctime(os.path.getmtime(path))  ).grid()

		Label(win_info_f, text='Время создания файла:').grid()
		Label(win_info_f, text= time.ctime(os.path.getctime(path)) ).grid()

		Label(win_info_f, text='Размер файла:').grid()
		Label(win_info_f, text= size(os.path.getsize(path) )).grid()


		w = w//2
		h = h//2
		w1 = xcord + w
		w2 = ycord + h

		win_info_f.transient(root)   # dialog window is related to main
		win_info_f.wait_visibility() # can't grab until window appears, so we wait
		win_info_f.grab_set()        # ensure all input goes to our window

		w11 = win_info_f.winfo_width() //2
		w21 = win_info_f.winfo_height() //2
		win_info_f.geometry('+{}+{}'.format(w1 - w11, w2 - w21))

		win_info_f.protocol("WM_DELETE_WINDOW", lambda:  win_info_f_dismiss(win_info_f)) # intercept close button
		win_info_f.wait_window()     # block until window is destroyed
	else:
		alert('Файл был удалён или перемещён')

#
def replace_f():
	if login_bas:
		print('replace_f')
	if os.path.isfile(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']):
		alert('Выберите в какую папку переместить файл')
		dir = filedialog.askdirectory(mustexist=1, title='Куда переместить файл')
		os.replace(tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text'], dir+ '/' + tree.item(item_select)['text'])

		old_path = tree.item(item_select)['values'][0] + '/' + tree.item(item_select)['text']
		old_dir = tree.item(item_select)['values'][0] + '/'
		iterdorsss = 0
		for vremen in settings['recent_use']:
			if vremen==old_path:
				settings['recent_use'][iterdorsss] = dir +'/' + tree.item(item_select)['text']
			iterdorsss = iterdorsss + 1

		save_settings()
		f_name =tree.item(item_select)['text']
		tree.delete(item_select)
		rec = dir +'/' + f_name
		rtee.append(tree.insert('', 'end', text=os.path.basename(rec), values=(f_this_space(os.path.dirname(rec)))))
	else:
		alert('Файл был удалён или перемещён')


#
def create_f():
	if login_bas:
		print('create_f')
	newfile = filedialog.asksaveasfilename()
	my_file = open(newfile, "w")
	my_file.close()
	if os.path.isfile(newfile):
		for antempxz in settings['recent_use']:
			if newfile == antempxz:
				alert('Этот файл уже добавлен!')
				return 0
		add_tree_l(newfile)
	else:
		alert('Кажется такой файл уже добавлен либо вы не выбрали файл!')
	#alert('Недоступно, обращайтесь к @GunsForHand_s')

#
def create_dir():
	if login_bas:
		print('create_dir')
	alert('Выберите расположение новой директории')
	dir_path = filedialog.askdirectory(mustexist=False, title='Выберите расположение новой директории')
	dirname = dlg_cr_dir()
	os.mkdir(dir_path+'/' +dirname)
	alert('Директория созданна - '+dir_path+'/'+dirname)


#
def an_auth():
	if login_bas:
		print('an_auth')
	alert('Недоступно, обращайтесь к @GunsForHand_s')

#
def settings_p():
	if login_bas:
		print('settings')
	alert('Недоступно, обращайтесь к @GunsForHand_s')


root = tk.Tk()
root.geometry("500x475")
root.title('CloudFILE')


#f1
frame1 = tk.Frame(master=root,borderwidth=5)

Label(master=frame1, text="CloudFILE").pack(side=tk.LEFT)
tk.Button(frame1, text='ВОЙТИ', command=an_auth ).pack(fill=tk.Y, side=tk.RIGHT)

frame1.pack(fill=tk.X)


#f2
frame2 = tk.Frame(master=root,borderwidth=5)

n = ttk.Notebook(frame2)

frame21 = tk.Frame(master=n,borderwidth=5)
tree = ttk.Treeview(frame21)
tree['columns'] = ('Путь')

rtee=[]

for rec in settings['recent_use']:
	if os.path.isfile(rec):
		rtee.append(tree.insert('', 'end', text=os.path.basename(rec), values=(f_this_space(os.path.dirname(rec)))))
tree.bind("<<TreeviewSelect>>", tree_selection)

tree.pack()
frame21.place(relx=.5, rely=.5, anchor="c", height=300, width=400)

frame22 = tk.Frame(master=n,borderwidth=5)
treec = ttk.Treeview(frame22)
treec['columns'] = ('path')

treec.pack()
frame22.pack()

n.add(frame21, text='Локально')
n.add(frame22, text='Облако')
n.bind(" <<NotebookTabChanged>>", Tab_selection_e)
n.pack()

frame2.pack()


#f3
frame3 = tk.Frame(master=root,borderwidth=5)
Buttons = {}
Buttons['add_f'] = Button(frame3, text='Добавить файл', command=add_f )
Buttons['info_f'] = Button(frame3, text='О файле', command=info_f )
Buttons['rem_f'] = Button(frame3, text='Убрать файл', command=rem_f )

Buttons['open_f'] = Button(frame3, text='Открыть', command=open_f )
Buttons['edit_f'] = Button(frame3, text='Редактировать', command=edit_f )
Buttons['down_up_f'] = Button(frame3, text='Скачать из облака', command=down_up_f )

Buttons['replace_f'] = Button(frame3, text='Переместить', command=replace_f )
Buttons['share_f'] = Button(frame3, text='Поделится', command=share_f )
Buttons['rename_f'] = Button(frame3, text='Переименовать', command=rename_f )

Buttons['create_f'] = Button(frame3, text='Создать файл', command=create_f )
Buttons['create_dir'] = Button(frame3, text='Создать папку', command=create_dir )
Buttons['del_f'] = Button(frame3, text='Удалить', command=del_f )

roww = 0
coll = 0
for but in Buttons:
	Buttons[but].grid(row=roww, column=coll, padx=10 , pady=2 , sticky="nsew")
	coll= coll +1
	if coll==3:
		coll = 0
		roww = roww +1

frame3.pack()


#4
frame4 = tk.Frame(master=root,borderwidth=5)

staaaatt = Label(master=frame4, text="Подключение к серверу!", bg='yellow')
staaaatt.pack(side=tk.LEFT)
tk.Button(frame4, text='НАСТРОЙКИ', command=settings_p ).pack(side=tk.RIGHT)

frame4.pack(fill=tk.X)


time.sleep(1)
Thread(target = lambda: obrtka(stat_connekt)).start()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
