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

login_bas=1

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
	if 1:

		settings['recent_use'].append(rec)
		save_settings()
		nbgb = ''
		under = ''
		for litera in rec:
			if litera == '/':
				under = nbgb + '/'
				nbgb = ''
			else:
				nbgb = nbgb + litera

		if nbgb:
			kjkj  = nbgb
		else:
			kjkj = under
		rtee.append(tree.insert('', 'end', text=kjkj, values=(f_this_space(rec))))

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
def add_f():
	if login_bas:
		print('add_f')
	filename = filedialog.askopenfilename()
	for antempxz in settings['recent_use']:
		if filename == antempxz:
			alert('Этот файл уже добавлен!')
			return 0
	add_tree_l(filename)

#
def rem_f():
	if login_bas:
		print('rem_f')
	global item_select
	#print(tree.item(item_select)['values'][0].encode(encoding='UTF-8',errors='strict'))
	settings['recent_use'].remove(tree.item(item_select)['values'][0])
	tree.delete(item_select)
	save_settings()

#
def rename_f():
	if login_bas:
		print('rename_f')

#
def share_f():
	if login_bas:
		print('share_f')

#
def edit_f():
	if login_bas:
		print('edit_f')

#
def open_f():
	if login_bas:
		print('open_f')

#
def down_up_f():
	if login_bas:
		print('down_f')

#
def del_f():
	if login_bas:
		print('del_local_f')

#
def info_f():
	if login_bas:
		print('del_cloud_f')

#
def an_auth():
	if login_bas:
		print('an_auth')

#
def settings_p():
	if login_bas:
		print('settings')

#
def obrtka(f_ober):
	try:
		f_ober()
	except:
		pass

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

	print(tab_selection)

#
def close_app():
	save_settings()
	root.destroy()
	sys.exit(1)

root = tk.Tk()
root.geometry("500x500")
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
	nbgb = ''
	under = ''
	for litera in rec:
		if litera == '/':
			under = nbgb + '/'
			nbgb = ''
		else:
			nbgb = nbgb + litera
	if nbgb:
		kjkj  = nbgb
	else:
		kjkj = under
	rtee.append(tree.insert('', 'end', text=kjkj, values=(f_this_space(rec))))
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
Buttons['rename_f'] = Button(frame3, text='Переименовать', command=rename_f )

Buttons['down_up_f'] = Button(frame3, text='Скачать из облака', command=down_up_f )
Buttons['share_f'] = Button(frame3, text='Поделится', command=share_f )
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
tk.Button(frame4, text='НАСТРОЙКИ', command=settings ).pack(side=tk.RIGHT)

frame4.pack(fill=tk.X)

time.sleep(1)
Thread(target = lambda: obrtka(stat_connekt)).start()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
