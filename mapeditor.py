from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as show
root = Tk()
biomText = ["X", "░", "/", "▒", "░", "░"]
biomColor = ["white", "greenyellow", "blue", "yellow", "green", "white"]
biomFG = ["red", "green", "white", "orange", "orange", "light blue"]
texture = 1
def change(event):
    gi=event.grid_info()
    x=gi['row']-3
    y=gi['column']
    buttons[x][y].configure(bg=biomColor[texture], fg=biomFG[texture], text=biomText[texture], activebackground=biomColor[texture], activeforeground=biomFG[texture])
class t:
    def grass():
        global texture
        texture = 1
    def water():
        global texture
        texture = 2
    def sand():
        global texture
        texture = 3
    def woods():
        global texture
        texture = 4
    def snow():
        global texture
        texture = 5
def clean(sit=0):
    global buttons
    global texture
    if sit == 1 or show.askyesno("Очищення", "Ви дійсно хочете очистити свою карту?"):
        buttons = []
        for row in range(0, 5):
            buttons.append([])
            for col in range(0, 24):
                buttons[row].append(Button(text=biomText[texture], relief="solid", bd=1, bg=biomColor[texture], fg=biomFG[texture], activebackground=biomColor[texture], activeforeground=biomFG[texture], font=["PxPlus IBM VGA 8x16"]))
                buttons[row][col].configure(command=lambda button=buttons[row][col]: change(button))
                buttons[row][col].grid(row=row + 3, column=col)
def openfile():
    global buttons
    filename = fd.askopenfilename(defaultextension="*.txt", filetypes = [("Текстовий документ", "*.txt"), ("Усі файли","*.*")])
    if filename != "":
        file = open(filename, "r")
        maps = file.read().split("n")
        try:
            map = maps[int(slot.get()) - 1].split("/")
            buttons = []
            for row in range(0, 5):
                buttons.append([])
                for col in range(0, 24):
                    sym = int(map[row][col])
                    buttons[row].append(Button(text=biomText[sym], relief="solid", bd=1, bg=biomColor[sym], fg=biomFG[sym], activebackground=biomColor[sym], activeforeground=biomFG[sym], font=["PxPlus IBM VGA 8x16"]))
                    buttons[row][col].configure(command=lambda button=buttons[row][col]: change(button))
                    buttons[row][col].grid(row=row + 3, column=col)
        except IndexError:
            show.showerror("Помилка слота", "В файлі " + filename + " немає слота №" + str(slot.get()) + "!")
def savefile():
    global buttons
    filename = fd.asksaveasfilename(defaultextension="*.txt", filetypes = [("Текстовий документ", "*.txt"), ("Усі файли","*.*")])
    try:
        file = open(filename, "r")
        oldFile = file.read()
        maps = oldFile.split("n")
        while True:
            if len(maps) == slot:
                break
            maps.append((("1" * 24) + "/") * 5)
    except FileNotFoundError:
        file = open(filename, "w")
        file.close()
        file = open(filename, "w")
        maps = open(filename).read().split("n")
        while True:
            if len(maps) == slot:
                break
            maps.append((("1" * 24) + "/") * 5)
        for row in range(0, 5):
            for col in range(0, 24):
                b = buttons[row][col]
                if b.cget("text") == "░":
                    if b.cget("fg") == "green":
                        file.write("1")
                    elif b.cget("fg") == "brown":
                        file.write("4")
                    elif b.cget("fg") == "light blue":
                        file.write("5")
                elif b.cget("text") == "▒":
                    file.write("3")
                elif b.cget("text") == "/":
                    file.write("2")
            file.write("/")
        file.write("n".join(maps))
    file.close()
grass = Button(text="░", relief="solid", bd = 1, bg="greenyellow", fg="green", font=["PxPlus IBM VGA 8x16"], command=t.grass)
grass.grid(row=1, column=3)
water = Button(text="/", relief="solid", bd = 1, bg="blue", fg="white", font=["PxPlus IBM VGA 8x16"], command=t.water)
water.grid(row=1, column=7)
sand = Button(text="▒", relief="solid", bd = 1, bg="yellow", fg="orange", font=["PxPlus IBM VGA 8x16"], command=t.sand)
sand.grid(row=1, column=11)
woods = Button(text="░", relief="solid", bd = 1, bg="green", fg="brown", font=["PxPlus IBM VGA 8x16"], command=t.woods)
woods.grid(row=1, column=15)
snow = Button(text="░", relief="solid", bd = 1, bg="white", fg="light blue", font=["PxPlus IBM VGA 8x16"], command=t.snow)
snow.grid(row=1, column=19)
clean(1)
openbutton = Button(text="Відкрити", command=openfile)
openbutton.grid(row=8,column=1,columnspan=3)
savebutton = Button(text="Зберігти", command=savefile)
savebutton.grid(row=8,column=4,columnspan=3)
cleanbutton = Button(text="Очистити", command=clean)
cleanbutton.grid(row=9, column=13, columnspan=4)
Label().grid(row=0, column=0)
Label().grid(row=2, column=0)
Label(text="Слот:").grid(row=9, column=2, columnspan=2)
slot = Spinbox(width=23, from_=1, to=10)
slot.grid(row=9, column=4, columnspan=9)
root.title("Minecraft RPG Map editor")
root.resizable(False,False)
root.mainloop()