import tkinter
import tkinter.messagebox
import tkinter.font

def loginScreen():
    
    def movePage():
        loginScreen.destroy()
        startScreen()

    loginScreen=tkinter.Tk()
    loginScreen.title("Login")
    loginScreen.geometry("200x150+540+285")
    loginScreen.resizable(width=False,height=False)
    
    username=tkinter.Label(loginScreen,text="Username")
    password=tkinter.Label(loginScreen,text="Password")
    typeUsername=tkinter.Entry(loginScreen)
    typePassword=tkinter.Entry(loginScreen,show="*")
    okButton=tkinter.Button(loginScreen,text="OK",command=movePage)
    newButton=tkinter.Checkbutton(loginScreen,text="I am new to this Game")

    username.pack()
    typeUsername.pack()
    password.pack()
    typePassword.pack()
    okButton.pack()
    newButton.pack()

    loginScreen.mainloop()
    return

def startScreen():

    def messageBox():
        tkinter.messagebox.showinfo("Unaccessible","This feature hasn't been developed")
    def movePage():
        startScreen.destroy()
        gameMap()

    startScreen=tkinter.Tk()
    startScreen.title("Starting Menu")
    button1=tkinter.Button(startScreen,text="Start Match",command=movePage)
    button2=tkinter.Button(startScreen,text="Create Account",command=messageBox)
    button3=tkinter.Button(startScreen,text="Player's Ranking",command=messageBox)
    button4=tkinter.Button(startScreen,text="All Levels",command=messageBox)
    startScreen.geometry("400x500+440+150")
    startScreen.resizable(width=False,height=False)
    startScreen.configure(bg="pink")
    button1.place(height=65,width=160,x="120",y="48")
    button2.place(height=65,width=160,x="120",y="161")
    button3.place(height=65,width=160,x="120",y="274")
    button4.place(height=65,width=160,x="120",y="387")

    startScreen.mainloop()
    return

def gameMap():

    global count
    count=0

    global circleDict
    circleDict={}
    
    global life
    life=3
        
    def firstMap(count):
        def circle(x,y):
            global life
            if x==50:
                life=life-1
            map1.create_oval(x-15,y-15,x+15,y+15,fill="blue")
            return
        def moveCircle():
            circleList=circleDict.keys()
            for key in circleList:
                circle(count-circleDict.get(key),270)
        def createCircle():
            initialNum=count
            global circleDict
            circleDict[str(count)]=int(initialNum)
        def updateMap():
            global count
            global life
            global circleDict
            if life==0:
                opinion=tkinter.messagebox.askyesno("Game Over","You lost, do you want to try again?")
                if opinion>0:
                    map1.destroy()
                    count=0
                    life=3
                    circleDict.clear()
                    firstMap(count)
                else:
                    gameMap.destroy()
                    startScreen()
            else:
                map1.destroy()
                count=count+1
                firstMap(count)
        map1=tkinter.Canvas(gameMap,background='lightgreen')
        map1.pack(fill=tkinter.BOTH,expand=tkinter.YES)
        map1.create_line(0,270,960,270,fill="lightblue",width=40)
        map1.create_line(920,270,960,270,fill="red",width=40)
        font=tkinter.font.Font(size=20)
        font2=tkinter.font.Font(size=25)
        if life<=1:
            lifeLabel=tkinter.Label(map1,text="Life Remaining : {}".format(life),bg="lightgreen",fg="red",font=font2)
            lifeLabel.place(height=80,width=200,x="700",y="20")
        else:
            lifeLabel=tkinter.Label(map1,text="Life Remaining : {}".format(life),bg="lightgreen",fg="black",font=font)
            lifeLabel.place(height=80,width=200,x="700",y="20")
        if count%100==0:
            createCircle()
        moveCircle()
        gameMap.after(10,updateMap)

    gameMap=tkinter.Tk()
    gameMap.title("Tower Defence")
    gameMap.geometry("960x540+160+90")
    gameMap.after(0,firstMap(count))
    gameMap.mainloop()

loginScreen()
