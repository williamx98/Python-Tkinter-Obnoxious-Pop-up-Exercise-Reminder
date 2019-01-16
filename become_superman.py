import Tkinter
import time 

openTime = [0]

window = Tkinter.Tk()

# sets up the main window elements
window.attributes('-fullscreen', True)
window.attributes("-topmost", True)
window.title('BECOME SUPERMAN')
window.configure(background='red')

#this makes the exercise label
Tkinter.Label(window, text="EXERCISE!!!", font=("Comic Sans MS", 350), background="red", fg="blue").pack(expand="YES")

def countDown():
	sleep = 10
	while sleep > 0:
		print str(sleep) + " seconds left"
		sleep = sleep - 1
		time.sleep(1)

#this will reopen the window if the done button is pressed too soon
#this also sets up the window to reopen in 1 hour
def closeWindow(event):
	window.withdraw()

	if time.time() - openTime[0] < 20:
		print str(time.time() - openTime[0])
		print "you didn't do anything!!!"
		time.sleep(2)
	else:
		countDown()
	
	openTime[0] = time.time()
	window.deiconify()

#this makes the done "button". Mac OS doesn't have full Tkinter button support so a label is turned into a button.
doneButton = Tkinter.Label(window, text="DONE!!!", font=("Comic Sans MS", 75), background="blue", fg="yellow")
doneButton.pack(expand="YES")
doneButton.bind("<Button>", closeWindow)

#initate the program
countDown()
openTime[0] = time.time()
window.mainloop()