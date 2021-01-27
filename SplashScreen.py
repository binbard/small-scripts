import tkinter
from tkinter import *
from tkinter.ttk import *
import time
import os
def showProgress():
	global val
	while val<100:
		val+=5
		mypb['value']=val
		mypb.update()
		if val<=100:
			perc.set("Loading..."+str(val)+" % complete")
		time.sleep(.1)
	mypb['value']=0
	val=0
	mywin.destroy()
	os.system('python mainframe.py')   
mywin = Tk()
val=0
perc=StringVar()
mywin.overrideredirect(1) # To hide title bar of tkinter window
mywin.geometry("400x130+400+300")
mywin.config(bg='black')
mypb = Progressbar(mywin,orient=HORIZONTAL,length=300,mode='determinate',value=val)
mypb.pack(side=TOP,pady=20)
#Button(mywin,text="close",command=mywin.quit).pack(side=BOTTOM)
lb1 = tkinter.Label(mywin,textvariable=perc,text='.')
lb1.config(font=('arial',15,'bold'),bg='black',fg='white')
lb1.pack(side=TOP)
#Button(mywin,text="start",command=showProgress).pack(side=BOTTOM)
showProgress()
mywin.mainloop()
