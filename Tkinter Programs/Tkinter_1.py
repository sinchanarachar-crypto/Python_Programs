from tkinter import* # '*' indicates all libraries included

root = Tk()
#Creating  a Label Widget
myLabel = Label(root, text = "Hey Everyone!!") 
#Shoving it onto the screen

#myLabel.pack()

# Format 1 for packing   #Will always be at center as we haven't mentioned where to display and pack is used

label1 = Label(root, text = "I am Learning Tkinter").grid(row= 0, column= 0)
label2 = Label(root, text = "I'll build awesome projects").grid(row= 2, column= 0)

#label1 and label2 will be on the mentioned places as we have mentioned them where to store in grid
# pack and grid can't be used as same time


root.mainloop()
