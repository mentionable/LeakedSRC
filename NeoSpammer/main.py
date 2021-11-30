from tkinter import *
from PIL import ImageTk, Image
import threading, requests, random, base64
from licensing.models import *
from licensing.methods import Key, Helpers

window = Tk()

proxies: list = open("data/proxies.txt", 'r').read().splitlines()

def click() -> None:
	if activate.status == True:
		victim = userid.get()
		name = groupnames.get()
		groups: list = open("data/groupids.txt", 'r').read().splitlines()
		for group in groups:
			threading.Thread(target=gcfunc, args=(victim, group, name,)).start()
	else:
		pass

def gcfunc(userid: str, groupid: str, groupchoice: str) -> None:

	tokens = token.get()

	headers = {
	"authorization" : tokens
	}
	_payload = {
	"name" : groupchoice
	}

	while True:

		r = requests.put(f"https://discord.com/api/v9/channels/{groupid}/recipients/{userid}", headers=headers, proxies={"http" : "http://" + random.choice(proxies)})

		if r.status_code == "204" or r.status_code == 204:

			f = requests.patch(f'https://discord.com/api/v9/channels/{groupid}', headers=headers, json=_payload, proxies={"http" : "http://" + random.choice(proxies)})

			while True:

				f = requests.patch(f'https://discord.com/api/v9/channels/{groupid}', headers=headers, json=_payload, proxies={"http" : "http://" + random.choice(proxies)})

				if f.status_code == "200" or 200:

					break

				else:
					_ = '_'

			break

		else:
			_ = "_"

def remove() -> None:
	if activate.status == True:
		victim = userid.get()
		groups: list = open("data/groupids.txt", 'r').read().splitlines()
		for group in groups:
			threading.Thread(target=gcrfunc, args=(victim, group,)).start()
	else:
		pass
def gcrfunc(userid: str, group: str) -> None:
    headers = {
    "authorization" : token.get()
    }
    while True:

    	r = requests.delete(f"https://discord.com/api/v9/channels/{group}/recipients/{userid}", headers=headers, proxies={"http" : "http://" + random.choice(proxies)})

    	if r.status_code == "204" or r.status_code == 204:

    		break

    	else:

    		_ = "_"

def icofunc() -> None:
	if activate.status == True:
		icon = base64.b64encode(open(str(icondir.get()).replace('"', ''), 'rb').read()).decode('utf-8')
		icon = f'data:image/png;base64,%s' % icon
		groups: list = open("data/groupids.txt", 'r').read().splitlines()
		for group in groups:
			threading.Thread(target=iconfunc, args=(group, icon,)).start()
	else:
		pass
def iconfunc(groupid, icon) -> None:
	while True:
		_payload = {
		"icon" : icon
		}
		r = requests.patch("https://discord.com/api/v9/channels/{}".format(groupid), headers={"authorization" : token.get()}, json=_payload, proxies={"http" : "http://" + random.choice(proxies)})

		if r.status_code == 200 or r.status_code == "200":
			break
		else:
			_ = '_'

def rcofunc() -> None:
	if activate.status == True:
		name = groupnames.get()
		groups: list = open("data/groupids.txt", 'r').read().splitlines()
		for group in groups:
			threading.Thread(target=rconfunc, args=(group, name,)).start()
	else:
		pass

def rconfunc(groupid, name) -> None:
	while True:
		_payload = {
		"name" : name
		}

		r = requests.patch("https://discord.com/api/v9/channels/{}".format(groupid), headers={"authorization" : token.get()}, json=_payload, proxies={"http" : "http://" + random.choice(proxies)})

		if r.status_code == 200 or r.status_code == "200":
			break
		else:
			_ = '_'

def activate() -> None:
	gkey = icondrir.get()
	activate.status = True

window.title("NeoSpam")
window.geometry("540x400")
window.configure(background="black")
Label (window, text="Neo GC Spammer | Version 1.0 | kunt#1337", bg="black", fg="blue", font="ubuntu 12").grid(row=0, column=0, sticky=W)
Label (window, text="Target User-ID Below:", bg="black", fg="blue", font="ubuntu 12").grid(row=2, column=0, sticky=W)
userid = Entry(window, width=60, bg="blue")
userid.grid(row=4, column=0, sticky=W)
Label (window, text="Group Chat Names Below:", bg="black", fg="blue", font="ubuntu 12").grid(row=6, column=0, sticky=W)
groupnames = Entry(window, width=60, bg="blue")
groupnames.grid(row=8, column=0, sticky=W)
Label (window, text="Token Below:", bg="black", fg="blue", font="ubuntu 12").grid(row=10, column=0, sticky=W)
token = Entry(window, width=60, bg="blue")
token.grid(row=12, column=0, sticky=W)
Label (window, text="Icon Directory Below:", bg="black", fg='blue', font="ubuntu 12").grid(row=14, column=0, sticky=W)
icondir = Entry(window, width=60, bg='blue')
icondir.grid(row=16, column=0, sticky=W)
Label (window, text="Activation Key Below:", bg="black", fg='blue', font="ubuntu 12").grid(row=18, column=0, sticky=W)
icondrir = Entry(window, width=60, bg='blue')
icondrir.grid(row=20, column=0, sticky=W)
Label (window, text="Options: ", bg="black", fg="blue", font="ubuntu 12").grid(row=22, column=0, sticky=W)
x = Button(window, text="Spam", width=20, bg="blue", command=click)
x.grid(row=24, column=0, sticky=W)
n = Button(window, text="Remove", width=20, bg="blue", command=remove)
n.grid(row=26, column=0, sticky=W)
l = Button(window, text='Change Icon', width=20, bg='blue', command=icofunc)
l.grid(row=28, column=0, sticky=W)
ki = Button(window, text='Rename', width=20, bg='blue', command=rcofunc)
ki.grid(row=30, column=0, sticky=W)
kil = Button(window, text='Activate', width=20, bg='blue', command=activate)
kil.grid(row=32, column=0, sticky=W)
window.resizable(False, False)
window.mainloop()
