import os
from tkinter import *
from PIL import ImageTk, Image
from tkVideoPlayer import TkinterVideo

def close_window_fx(window):
	window.destroy()
def activate_fx(btn):
	btn["state"] = "active"
def toggle_fx(o, window):
	if o["state"]=="active" or o["state"]=="normal":
		o["state"] = "disabled"
	else:
		o["state"] = "active"
		window.destroy()

def open_new_txtWindow_fx(window, title, txt, dimensions):
	newWindow = Toplevel(window)
	newWindow.title(title)
	newWindow.configure(bg = "white")
	newWindow.geometry(dimensions)
	message = Label(newWindow, text = txt)
	message.config(bg = "white", fg = "black")
	message.pack()
	if title=="Instructions":
		# startSession_btn["state"] = "active"
		toggle_fx(o = instruction_btn, window = newWindow)
		consent_btn = Button(newWindow, text = "OK")
		consent_btn.config(highlightbackground = "white")
		consent_btn.config(command = lambda: [toggle_fx(o = instruction_btn, window = newWindow),
			activate_fx(btn = startSession_btn)])
		consent_btn.pack()
		newWindow.protocol("WM_DELETE_WINDOW", lambda: toggle_fx(o = instruction_btn, window = newWindow))

	# ## little practice for future parts of the code; to be deleted ##
	# def iteri_fx(i):
	# 	i += 1
	# 	if i<4:
	# 		iteri_fx(i)
	# 	else:
	# 		print(i)
	# iteri_fx(i = 0)

def open_sessionWindow_fx(window, dimensions):
	sessionWindow = Toplevel(window)
	sessionWindow.title("Experiment 1")
	sessionWindow.geometry(dimensions)
	sessionWindow.configure(bg = "white")

	toggle_fx(o = startSession_btn, window = sessionWindow)

	vid_player = TkinterVideo(scaled=True, master=sessionWindow)
	vid_player.pack() # pack(expand=True, fill="both")
	vid_player.load("img/avi.mp4")
	vid_player.play()

	txt_below_vid = """ Forward / Backward for Present / Absent """
	Label_below_vid = Label(sessionWindow, text = txt_below_vid)
	Label_below_vid.config(bg = "white", fg = "black")
	Label_below_vid.pack()

	sb = Scrollbar(sessionWindow)
	sb.pack(side = RIGHT, fill = Y)

	sessionWindow.protocol("WM_DELETE_WINDOW", lambda: toggle_fx(o = startSession_btn, window = sessionWindow))

root = Tk()
root.title("FFG-STIWA, Experiment 1")
root.configure(bg = "white")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("500x500+250+250")

intro_message = Label(root, text = """Please start by pressing the instructions button 
	and reading the information carefully.""")
intro_message.config(bg = "white", fg = "black") # fg: parameter controling the color of the letters
intro_message.place(x = 10, y = 10)
# intro_pic = Image.open("img/test.png")
# intro_pic.resize((200,400))
# intro_pic = ImageTk.PhotoImage(intro_pic)
# pic_label = Label(root, image = intro_pic)

intro_pic = Image.open("img/test.png")
intro_pic = intro_pic.resize((200,260))
intro_pic = ImageTk.PhotoImage(intro_pic)
pic_label = Label(root, image = intro_pic)
pic_label.place(x=10,y=50)

exit_btn = Button(root, text = "Exit")
exit_btn.config(highlightbackground = "white")
exit_btn.config(command = lambda: close_window_fx(window = root))
exit_btn.place(x = 10, y = 340)

instruction_btn = Button(root, text = "Instructions")
instruction_btn.config(highlightbackground="white")
instruction_btn.config(command = lambda: open_new_txtWindow_fx(window = root, 
	title = "Instructions", txt = "In the following... ", dimensions = "500x500+800+250"))
instruction_btn.place(x = 100, y = 340)

startSession_btn = Button(root, text = "Start Session")
startSession_btn.config(command = lambda: open_sessionWindow_fx(window = root, dimensions = "500x500+800+250"))
startSession_btn["state"] = "disabled"
startSession_btn.config(highlightbackground = "white")
startSession_btn.place(x = 250, y = 340)

root.mainloop()