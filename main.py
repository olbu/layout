from Tkinter import *
#tjo man

def on_entry_click(event): #funktionen så det står texten ip
		global firstclick
		firstclick = True
		if firstclick:
			firstclick = False
			ip.delete(0, "end")

def on_focusout(event): #funktionen så texten ip försvinner
	firstclick = True
	if ip.get() == "":
		ip.insert(0, "Enter ip: ")

root = Tk() #Main screen
root.config(bg="grey")
root.title("PortScanner")

ip = Entry(root, font=10, justify="center") #Entry for ip
ip.insert(0, "Enter ip: ")
ip.bind('<FocusIn>', on_entry_click)
ip.bind('<FocusOut>', on_focusout)
ip.grid(pady=20,ipadx=10)

textBox = Text(root)
textBox.grid(padx=20, pady=7)
textBox.config(width=30,state=DISABLED)  #Textlåda

knapp=Button(root, text= "Start", fg="white", font=(None, 12))
knapp.grid(ipadx=50,ipady=5,pady=10) #detta är knappen
knapp.config(bg="black")




root.mainloop()
