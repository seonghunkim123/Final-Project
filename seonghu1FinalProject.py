import tkinter
import tkinter.messagebox

def startScreen():
    def openActual():
        startScreen.destroy()
        actualScreen()
    def openTutorial():
        startScreen.destroy()
        tutorialScreen()
    startScreen=tkinter.Tk()
    startScreen.title("Starting Menu")
    startScreen.geometry("400x500+440+150")
    startScreen.resizable(width=False,height=False)
    canvas=tkinter.Canvas(startScreen,background='pink')
    canvas.pack(fill=tkinter.BOTH,expand=tkinter.YES)
    button1=tkinter.Button(startScreen,text="Instruction",command=instructionScreen)
    button2=tkinter.Button(startScreen,text="Practice",command=openTutorial)
    button3=tkinter.Button(startScreen,text="Start",command=openActual)
    button1.place(height=65,width=150,x="33",y="280")
    button2.place(height=65,width=150,x="217",y="280")
    button3.place(height=65,width=150,x="125",y="375")
    def writeShape(x1,y1,x2,y2):
        # creating S
        canvas.create_line(x1,y1,x1,y1+50,fill="white",width=10)
        canvas.create_line(x1-5,y1+5,x1+55,y1+5,fill="white",width=10)
        canvas.create_line(x1-5,y1+45,x1+55,y1+45,fill="white",width=10)
        canvas.create_line(x1+50,y1+40,x1+50,y1+90,fill="white",width=10)
        canvas.create_line(x1-5,y1+85,x1+45,y1+85,fill="white",width=10)
        # creating H
        canvas.create_line(x1+70,y1,x1+70,y1+90,fill="white",width=10)
        canvas.create_line(x1+65,y1+45,x1+125,y1+45,fill="white",width=10)
        canvas.create_line(x1+120,y1,x1+120,y1+90,fill="white",width=10)
        # creating A
        canvas.create_line(x1+140,y1,x1+140,y1+90,fill="white",width=10)
        canvas.create_line(x1+135,y1+5,x1+195,y1+5,fill="white",width=10)
        canvas.create_line(x1+190,y1,x1+190,y1+90,fill="white",width=10)
        canvas.create_line(x1+135,y1+45,x1+195,y1+45,fill="white",width=10)
        # creating P
        canvas.create_line(x1+210,y1,x1+210,y1+90,fill="white",width=10)
        canvas.create_line(x1+205,y1+5,x1+265,y1+5,fill="white",width=10)
        canvas.create_line(x1+260,y1,x1+260,y1+50,fill="white",width=10)
        canvas.create_line(x1+205,y1+45,x1+265,y1+45,fill="white",width=10)
        # creating E
        canvas.create_line(x1+280,y1,x1+280,y1+90,fill="white",width=10)
        canvas.create_line(x1+275,y1+5,x1+335,y1+5,fill="white",width=10)
        canvas.create_line(x1+275,y1+45,x1+335,y1+45,fill="white",width=10)
        canvas.create_line(x1+275,y1+85,x1+335,y1+85,fill="white",width=10)
        # creating D
        canvas.create_line(x2,y2,x2,y2+90,fill="white",width=10)
        canvas.create_line(x2-5,y2+5,x2+55,y2+5,fill="white",width=10)
        canvas.create_line(x2-5,y2+85,x2+55,y2+85,fill="white",width=10)
        canvas.create_line(x2+50,y2,x2+50,y2+90,fill="white",width=10)
        # creating E
        canvas.create_line(x2+65,y2+20,x2+65,y2+90,fill="white",width=10)
        canvas.create_line(x2+60,y2+25,x2+105,y2+25,fill="white",width=10)
        canvas.create_line(x2+60,y2+55,x2+105,y2+55,fill="white",width=10)
        canvas.create_line(x2+60,y2+85,x2+105,y2+85,fill="white",width=10)
        # creating F
        canvas.create_line(x2+115,y2+20,x2+115,y2+90,fill="white",width=10)
        canvas.create_line(x2+110,y2+25,x2+155,y2+25,fill="white",width=10)
        canvas.create_line(x2+110,y2+55,x2+155,y2+55,fill="white",width=10)
        # creating E
        canvas.create_line(x2+165,y2+20,x2+165,y2+90,fill="white",width=10)
        canvas.create_line(x2+160,y2+25,x2+205,y2+25,fill="white",width=10)
        canvas.create_line(x2+160,y2+55,x2+205,y2+55,fill="white",width=10)
        canvas.create_line(x2+160,y2+85,x2+205,y2+85,fill="white",width=10)
        # creating N
        canvas.create_line(x2+215,y2+20,x2+215,y2+90,fill="white",width=10)
        canvas.create_line(x2+255,y2+20,x2+255,y2+90,fill="white",width=10)
        canvas.create_line(x2+215,y2+23,x2+255,y2+87,fill="white",width=10)
        # creating C
        canvas.create_line(x2+270,y2+20,x2+270,y2+90,fill="white",width=10)
        canvas.create_line(x2+265,y2+25,x2+310,y2+25,fill="white",width=10)
        canvas.create_line(x2+265,y2+85,x2+310,y2+85,fill="white",width=10)
        # creating E
        canvas.create_line(x2+320,y2+20,x2+320,y2+90,fill="white",width=10)
        canvas.create_line(x2+315,y2+25,x2+360,y2+25,fill="white",width=10)
        canvas.create_line(x2+315,y2+55,x2+360,y2+55,fill="white",width=10)
        canvas.create_line(x2+315,y2+85,x2+360,y2+85,fill="white",width=10)
    writeShape(40,40,20,150)
    startScreen.mainloop()

def instructionScreen():
    window=tkinter.Tk()
    window.title("Instruction")
    window.geometry("400x500+400+100")
    window.resizable(width=False,height=False)
    title=tkinter.Label(window,text="Instructions")
    title.config(font=("Courier", 35))
    title.pack()
    file=open("file","r")
    line=file.readline()
    while line:
        instruction=tkinter.Label(window,text=str(line))
        instruction.pack()
        line=file.readline()
    window.mainloop()

def tutorialScreen():
    global circleDict
    circleDict={}
    global weaponDict
    weaponDict={}
    global life
    life=3
    global count
    count=0
    def tutorialMap(count):
        def findDistance(x1,y1,x2,y2):
            distance=((x1-x2)**2+(y1-y2)**2)**(1/2)
            return distance
        def createRectangle(x,y):
            global weaponDict
            weaponList=[]
            for weapon in weaponDict.keys():
                if weaponDict[weapon]["exist"]==True:
                    weaponList.append(weapon)
            if len(weaponList)<3:
                weaponDict[len(weaponDict)]={"x-coor":x,"y-coor":y,"range":300,"reload":0,"bullets":{},\
                                             "target":{"exist":False,"circle":""},"exist":True}
                displayWeapon()
            else:
                tkinter.messagebox.showinfo("Numbers of Permitted Weapons Reached","Only 3 Weapons Allowed, Place Wisely")
        def removeRectangle(x,y):
            global weaponDict
            for key,value in weaponDict.items(): 
                if value["x-coor"]==x and value["y-coor"]==y: 
                    weapon=key
                    weaponDict[weapon]["exist"]=False
            canvas.create_rectangle(x-15,y-15,x+15,y+15,fill="grey")
        def displayWeapon():
            for weapon in weaponDict.keys():
                x=weaponDict[weapon]["x-coor"]
                y=weaponDict[weapon]["y-coor"]
                canvas.create_rectangle(x-13,y-13,x+13,y+13,fill="pink")
                canvas.create_rectangle(x-3,y-3,x+3,y+3,fill="red")
        def createCircle():
            global circleDict
            circleDict[len(circleDict)]={"x-coor":0,"y-coor":270,"exist":True}
        def moveCircle():
            global life
            for circle in circleDict.keys():
                circleDict[circle]["x-coor"]=circleDict[circle]["x-coor"]+1
                x=circleDict[circle]["x-coor"]
                if x==940 and circleDict[circle]["exist"]==True:
                    life=life-1
                    circleDict[circle]["exist"]=False
        def displayCircle():
            global circleDict
            for circle in circleDict.keys():
                if circleDict[circle]["exist"]==True:
                    x=circleDict[circle]["x-coor"]
                    y=circleDict[circle]["y-coor"]
                    canvas.create_oval(x-15,y-15,x+15,y+15,fill="blue")
        def createBullet(weapon):
            if weaponDict[weapon]["target"]["exist"]==True:
                weaponDict[weapon]["bullets"][len(weaponDict[weapon]["bullets"])]={"x-coor":weaponDict[weapon]["x-coor"], \
                                                                                   "y-coor":weaponDict[weapon]["y-coor"], \
                                                                                   "exist":True,\
                                                                                   "target":{"exist":True,"circle":weaponDict[weapon]["target"]["circle"]}}
                weaponDict[weapon]["reload"]=200
        def chooseTarget():
            global weaponDict
            for weapon in weaponDict.keys():
                targetCandidates={}
                x1=weaponDict[weapon]["x-coor"]
                y1=weaponDict[weapon]["y-coor"]
                for circle in circleDict.keys():
                    x2=circleDict[circle]["x-coor"]
                    y2=circleDict[circle]["y-coor"]
                    distance=findDistance(x1,y1,x2,y2)
                    if distance<weaponDict[weapon]["range"] and circleDict[circle]["exist"]==True:
                        targetCandidates[circle]=distance
                if targetCandidates:
                    targetList=targetCandidates.keys()
                    minDistance=weaponDict[weapon]["range"]
                    for candidate in targetList:
                        if targetCandidates[candidate]<minDistance:
                            minDistance=targetCandidates[candidate]
                    for key,value in targetCandidates.items(): 
                        if value==minDistance: 
                            target=key
                    weaponDict[weapon]["target"]["exist"]=True
                    weaponDict[weapon]["target"]["circle"]=str(target)
        def moveBullet():
            global weaponDict
            global circleDict
            chooseTarget()
            for weapon in weaponDict.keys():
                if weaponDict[weapon]["reload"]==0:
                    createBullet(weapon)
                else:
                    weaponDict[weapon]["reload"]=weaponDict[weapon]["reload"]-1
                for bullet in weaponDict[weapon]["bullets"].keys():
                    if weaponDict[weapon]["bullets"][bullet]["exist"]==True:
                        if weaponDict[weapon]["bullets"][bullet]["target"]["exist"]==True:
                            target=weaponDict[weapon]["bullets"][bullet]["target"]["circle"]
                            x1=weaponDict[weapon]["bullets"][bullet]["x-coor"]
                            y1=weaponDict[weapon]["bullets"][bullet]["y-coor"]
                            x2=circleDict[int(target)]["x-coor"]
                            y2=circleDict[int(target)]["y-coor"]
                            distance=findDistance(x1,y1,x2,y2)
                            if distance<=5:
                                circleDict[int(target)]["exist"]=False
                                weaponDict[weapon]["target"]["exist"]=False
                                weaponDict[weapon]["target"]["circle"]=""
                                weaponDict[weapon]["bullets"][bullet]["exist"]=False
                            else:
                                x=x2-x1
                                y=y2-y1
                                weaponDict[weapon]["bullets"][bullet]["x-coor"]=weaponDict[weapon]["bullets"][bullet]["x-coor"]+((2*x)/distance)
                                weaponDict[weapon]["bullets"][bullet]["y-coor"]=weaponDict[weapon]["bullets"][bullet]["y-coor"]+((2*y)/distance)
                        else:
                            weaponDict[weapon]["bullets"][bullet]["exist"]==False
        def displayBullet():
            for weapon in weaponDict.keys():
                for bullet in weaponDict[weapon]["bullets"].keys():
                    if weaponDict[weapon]["bullets"][bullet]["exist"]==True:
                        x=weaponDict[weapon]["bullets"][bullet]["x-coor"]
                        y=weaponDict[weapon]["bullets"][bullet]["y-coor"]
                        canvas.create_rectangle(x-3,y-3,x+3,y+3,fill="red")
        def updateMap():
            global count
            global life
            global circleDict
            if life==0:
                opinion=tkinter.messagebox.askyesno("Game Over","You lost, do you want to try again?")
                if opinion>0:
                    canvas.destroy()
                    count=0
                    life=3
                    circleDict.clear()
                    weaponDict.clear()
                    tutorialMap(count)
                else:
                    window.destroy()
                    startScreen()
            else:
                canvas.destroy()
                count=count+1
                tutorialMap(count)
        canvas=tkinter.Canvas(window,background='lightgreen')
        canvas.pack(fill=tkinter.BOTH,expand=tkinter.YES)
        # creating Path and Finish Line
        canvas.create_line(0,270,960,270,fill="lightblue",width=40)
        canvas.create_line(920,270,960,270,fill="red",width=40)
        # creating L
        canvas.create_line(720,50,720,100,fill="white",width=10)
        canvas.create_line(715,95,750,95,fill="white",width=10)
        # creating I
        canvas.create_line(760,60,760,70,fill="white",width=10)
        canvas.create_line(760,75,760,100,fill="white",width=10)
        # creating F
        canvas.create_line(775,55,775,100,fill="white",width=10)
        canvas.create_line(770,60,795,60,fill="white",width=10)
        canvas.create_line(770,75,790,75,fill="white",width=10)
        # creating E
        canvas.create_line(800,70,800,100,fill="white",width=10)
        canvas.create_line(795,74,825,74,fill="white",width=8)
        canvas.create_line(795,85,825,85,fill="white",width=8)
        canvas.create_line(795,96,825,96,fill="white",width=8)
        canvas.create_line(820,70,820,85,fill="white",width=10)
        # creating Colon
        canvas.create_line(845,65,845,75,fill="white",width=10)
        canvas.create_line(845,85,845,95,fill="white",width=10)
        displayWeapon()
        if count%100==0:
            createCircle()
        moveCircle()
        moveBullet()
        displayCircle()
        displayBullet()
        if life==3:
            canvas.create_line(870,95,910,95,fill="white",width=10)
            canvas.create_line(870,70,910,70,fill="white",width=10)
            canvas.create_line(870,45,910,45,fill="white",width=10)
            canvas.create_line(905,40,905,100,fill="white",width=10)
        elif life==2:
            canvas.create_line(870,95,910,95,fill="white",width=10)
            canvas.create_line(870,70,910,70,fill="white",width=10)
            canvas.create_line(870,45,910,45,fill="white",width=10)
            canvas.create_line(905,40,905,75,fill="white",width=10)
            canvas.create_line(875,65,875,100,fill="white",width=10)
        elif life==1:
            canvas.create_line(870,95,905,95,fill="red",width=10)
            canvas.create_line(870,35,895,35,fill="red",width=10)
            canvas.create_line(890,30,890,100,fill="red",width=10)
        else:
            canvas.create_line(870,95,910,95,fill="red",width=10)
            canvas.create_line(870,35,910,35,fill="red",width=10)
            canvas.create_line(875,30,875,100,fill="red",width=10)
            canvas.create_line(905,30,905,100,fill="red",width=10)
        if count==0:
            def createSlots(xcoor,ycoor):
                canvas.create_rectangle(xcoor-15,ycoor-15,xcoor+15,ycoor+15,fill="grey")
                slot=tkinter.Menubutton(canvas,text="Choose the Location")
                slot.menu=tkinter.Menu(slot)
                slot["menu"]=slot.menu
                slot.menu.add_command(label="Place Weapon Here",command=lambda:(createRectangle(xcoor,ycoor)))
                slot.menu.add_command(label="Remove Weapon",command=lambda:(removeRectangle(xcoor,ycoor)))
                slot.place(x=xcoor+20,y=ycoor-10)
            createSlots(150,230)
            createSlots(450,230)
            createSlots(750,230)
            createSlots(50,310)
            createSlots(350,310)
            createSlots(650,310)
            startButton=tkinter.Button(canvas,text="Start",command=updateMap)
            startButton.place(height=65,width=155,x="770",y="450")
        else:
            window.after(10,updateMap)
    window=tkinter.Tk()
    window.title("Practice Defence")
    window.geometry("960x540+160+90")
    tutorialMap(count)
    window.mainloop()

def actualScreen():
    global circleDict
    circleDict={}
    global weaponDict
    weaponDict={}
    global life
    life=3
    global count
    count=0
    def actualMap(count):
        def findDistance(x1,y1,x2,y2):
            distance=((x1-x2)**2+(y1-y2)**2)**(1/2)
            return distance
        def createRectangle(x,y):
            global weaponDict
            weaponList=[]
            for weapon in weaponDict.keys():
                if weaponDict[weapon]["exist"]==True:
                    weaponList.append(weapon)
            if len(weaponList)<3:
                weaponDict[len(weaponDict)]={"x-coor":x,"y-coor":y,"range":300,"reload":0,"bullets":{},\
                                             "target":{"exist":False,"circle":""},"exist":True}
                displayWeapon()
            else:
                tkinter.messagebox.showinfo("Numbers of Permitted Weapons Reached","Only 3 Weapons Allowed, Place Wisely")
        def removeRectangle(x,y):
            global weaponDict
            for key,value in weaponDict.items(): 
                if value["x-coor"]==x and value["y-coor"]==y: 
                    weapon=key
                    weaponDict[weapon]["exist"]=False
            canvas.create_rectangle(x-15,y-15,x+15,y+15,fill="grey")
        def displayWeapon():
            for weapon in weaponDict.keys():
                if weaponDict[weapon]["exist"]==True:
                    x=weaponDict[weapon]["x-coor"]
                    y=weaponDict[weapon]["y-coor"]
                    canvas.create_rectangle(x-13,y-13,x+13,y+13,fill="pink")
                    canvas.create_rectangle(x-3,y-3,x+3,y+3,fill="red")
        def createCircle():
            global circleDict
            circleDict[len(circleDict)]={"x-coor":0,"y-coor":270,"exist":True}
        def moveCircle():
            global life
            for circle in circleDict.keys():
                if circleDict[circle]["y-coor"]==270 and circleDict[circle]["x-coor"]<240:
                    circleDict[circle]["x-coor"]=circleDict[circle]["x-coor"]+1
                elif circleDict[circle]["x-coor"]==240 and circleDict[circle]["y-coor"]>135:
                    circleDict[circle]["y-coor"]=circleDict[circle]["y-coor"]-1
                elif circleDict[circle]["y-coor"]==135 and circleDict[circle]["x-coor"]<480:
                    circleDict[circle]["x-coor"]=circleDict[circle]["x-coor"]+1
                elif circleDict[circle]["x-coor"]==480 and circleDict[circle]["y-coor"]<405:
                    circleDict[circle]["y-coor"]=circleDict[circle]["y-coor"]+1
                elif circleDict[circle]["y-coor"]==405 and circleDict[circle]["x-coor"]<720:
                    circleDict[circle]["x-coor"]=circleDict[circle]["x-coor"]+1
                elif circleDict[circle]["x-coor"]==720 and circleDict[circle]["y-coor"]>270:
                    circleDict[circle]["y-coor"]=circleDict[circle]["y-coor"]-1
                else:
                    circleDict[circle]["x-coor"]=circleDict[circle]["x-coor"]+1
                x=circleDict[circle]["x-coor"]
                if x==940 and circleDict[circle]["exist"]==True:
                    life=life-1
                    circleDict[circle]["exist"]=False
        def displayCircle():
            global circleDict
            for circle in circleDict.keys():
                if circleDict[circle]["exist"]==True:
                    x=circleDict[circle]["x-coor"]
                    y=circleDict[circle]["y-coor"]
                    canvas.create_oval(x-15,y-15,x+15,y+15,fill="blue")
        def createBullet(weapon):
            if weaponDict[weapon]["target"]["exist"]==True and weaponDict[weapon]["exist"]==True:
                weaponDict[weapon]["bullets"][len(weaponDict[weapon]["bullets"])]={"x-coor":weaponDict[weapon]["x-coor"], \
                                                                                   "y-coor":weaponDict[weapon]["y-coor"], \
                                                                                   "exist":True,\
                                                                                   "target":{"exist":True,"circle":weaponDict[weapon]["target"]["circle"]}}
                weaponDict[weapon]["reload"]=200
        def chooseTarget():
            global weaponDict
            for weapon in weaponDict.keys():
                targetCandidates={}
                x1=weaponDict[weapon]["x-coor"]
                y1=weaponDict[weapon]["y-coor"]
                for circle in circleDict.keys():
                    x2=circleDict[circle]["x-coor"]
                    y2=circleDict[circle]["y-coor"]
                    distance=findDistance(x1,y1,x2,y2)
                    if distance<weaponDict[weapon]["range"] and circleDict[circle]["exist"]==True:
                        targetCandidates[circle]=distance
                if targetCandidates:
                    targetList=targetCandidates.keys()
                    minDistance=weaponDict[weapon]["range"]
                    for candidate in targetList:
                        if targetCandidates[candidate]<minDistance:
                             minDistance=targetCandidates[candidate]
                    for key,value in targetCandidates.items(): 
                        if value==minDistance: 
                            target=key
                    weaponDict[weapon]["target"]["exist"]=True
                    weaponDict[weapon]["target"]["circle"]=str(target)
        def moveBullet():
            global weaponDict
            global circleDict
            chooseTarget()
            for weapon in weaponDict.keys():
                if weaponDict[weapon]["reload"]==0:
                    createBullet(weapon)
                else:
                    weaponDict[weapon]["reload"]=weaponDict[weapon]["reload"]-1
                for bullet in weaponDict[weapon]["bullets"].keys():
                    if weaponDict[weapon]["bullets"][bullet]["exist"]==True:
                        if weaponDict[weapon]["bullets"][bullet]["target"]["exist"]==True:
                            target=weaponDict[weapon]["bullets"][bullet]["target"]["circle"]
                            x1=weaponDict[weapon]["bullets"][bullet]["x-coor"]
                            y1=weaponDict[weapon]["bullets"][bullet]["y-coor"]
                            x2=circleDict[int(target)]["x-coor"]
                            y2=circleDict[int(target)]["y-coor"]
                            distance=findDistance(x1,y1,x2,y2)
                            if distance<=5:
                                circleDict[int(target)]["exist"]=False
                                weaponDict[weapon]["target"]["exist"]=False
                                weaponDict[weapon]["target"]["circle"]=""
                                weaponDict[weapon]["bullets"][bullet]["exist"]=False
                            else:
                                x=x2-x1
                                y=y2-y1
                                weaponDict[weapon]["bullets"][bullet]["x-coor"]=weaponDict[weapon]["bullets"][bullet]["x-coor"]+((2*x)/distance)
                                weaponDict[weapon]["bullets"][bullet]["y-coor"]=weaponDict[weapon]["bullets"][bullet]["y-coor"]+((2*y)/distance)
                        else:
                            weaponDict[weapon]["bullets"][bullet]["exist"]==False
        def displayBullet():
            for weapon in weaponDict.keys():
                for bullet in weaponDict[weapon]["bullets"].keys():
                    if weaponDict[weapon]["bullets"][bullet]["exist"]==True:
                        x=weaponDict[weapon]["bullets"][bullet]["x-coor"]
                        y=weaponDict[weapon]["bullets"][bullet]["y-coor"]
                        canvas.create_rectangle(x-3,y-3,x+3,y+3,fill="red")
        def updateMap():
            global count
            global life
            global circleDict
            if life==0:
                opinion=tkinter.messagebox.askyesno("Game Over","Your score is {}, do you want to try again?".format(count))
                if opinion>0:
                    canvas.destroy()
                    count=0
                    life=3
                    circleDict.clear()
                    weaponDict.clear()
                    actualMap(count)
                else:
                    window.destroy()
                    startScreen()
            else:
                canvas.destroy()
                count=count+1
                actualMap(count)
        canvas=tkinter.Canvas(window,background='lightgreen')
        canvas.pack(fill=tkinter.BOTH,expand=tkinter.YES)
        # creating Path and Finish Line
        canvas.create_line(0,270,260,270,fill="lightblue",width=40)
        canvas.create_line(240,290,240,115,fill="lightblue",width=40)
        canvas.create_line(220,135,500,135,fill="lightblue",width=40)
        canvas.create_line(480,115,480,425,fill="lightblue",width=40)
        canvas.create_line(460,405,740,405,fill="lightblue",width=40)
        canvas.create_line(720,425,720,250,fill="lightblue",width=40)
        canvas.create_line(700,270,920,270,fill="lightblue",width=40)
        canvas.create_line(920,270,960,270,fill="red",width=40)
        # creating L
        canvas.create_line(720,50,720,100,fill="white",width=10)
        canvas.create_line(715,95,750,95,fill="white",width=10)
        # creating I
        canvas.create_line(760,60,760,70,fill="white",width=10)
        canvas.create_line(760,75,760,100,fill="white",width=10)
        # creating F
        canvas.create_line(775,55,775,100,fill="white",width=10)
        canvas.create_line(770,60,795,60,fill="white",width=10)
        canvas.create_line(770,75,790,75,fill="white",width=10)
        # creating E
        canvas.create_line(800,70,800,100,fill="white",width=10)
        canvas.create_line(795,74,825,74,fill="white",width=8)
        canvas.create_line(795,85,825,85,fill="white",width=8)
        canvas.create_line(795,96,825,96,fill="white",width=8)
        canvas.create_line(820,70,820,85,fill="white",width=10)
        # creating Colon
        canvas.create_line(845,65,845,75,fill="white",width=10)
        canvas.create_line(845,85,845,95,fill="white",width=10)
        displayWeapon()
        if len(circleDict)<30:
            if count%100==0:
                createCircle()
        elif len(circleDict)<60:
            if count%70==0:
                createCircle()
        else:
            if count%50==0:
                createCircle()
        moveCircle()
        moveBullet()
        displayCircle()
        displayBullet()
        if life==3:
            canvas.create_line(870,95,910,95,fill="white",width=10)
            canvas.create_line(870,70,910,70,fill="white",width=10)
            canvas.create_line(870,45,910,45,fill="white",width=10)
            canvas.create_line(905,40,905,100,fill="white",width=10)
        elif life==2:
            canvas.create_line(870,95,910,95,fill="white",width=10)
            canvas.create_line(870,70,910,70,fill="white",width=10)
            canvas.create_line(870,45,910,45,fill="white",width=10)
            canvas.create_line(905,40,905,75,fill="white",width=10)
            canvas.create_line(875,65,875,100,fill="white",width=10)
        elif life==1:
            canvas.create_line(870,95,905,95,fill="red",width=10)
            canvas.create_line(870,35,895,35,fill="red",width=10)
            canvas.create_line(890,30,890,100,fill="red",width=10)
        else:
            canvas.create_line(870,95,910,95,fill="red",width=10)
            canvas.create_line(870,35,910,35,fill="red",width=10)
            canvas.create_line(875,30,875,100,fill="red",width=10)
            canvas.create_line(905,30,905,100,fill="red",width=10)
        if count==0:
            def createSlots(xcoor,ycoor):
                canvas.create_rectangle(xcoor-15,ycoor-15,xcoor+15,ycoor+15,fill="grey")
                slot=tkinter.Menubutton(canvas)
                slot.menu=tkinter.Menu(slot)
                slot["menu"]=slot.menu
                slot.menu.add_command(label="Place Weapon Here",command=lambda:(createRectangle(xcoor,ycoor)))
                slot.menu.add_command(label="Remove Weapon",command=lambda:(removeRectangle(xcoor,ycoor)))
                slot.place(x=xcoor+20,y=ycoor-10)
            createSlots(50,230)
            createSlots(50,310)
            createSlots(145,230)
            createSlots(145,310)
            createSlots(200,135)
            createSlots(200,180)
            createSlots(240,310)
            createSlots(280,270)
            createSlots(280,223)
            createSlots(280,175)
            createSlots(360,175)
            createSlots(440,175)
            createSlots(280,95)
            createSlots(360,95)
            createSlots(440,95)
            createSlots(440,265)
            createSlots(440,355)
            createSlots(440,445)
            createSlots(520,185)
            createSlots(520,275)
            createSlots(520,365)
            createSlots(520,445)
            createSlots(600,365)
            createSlots(600,445)
            createSlots(680,275)
            createSlots(680,365)
            createSlots(680,445)
            createSlots(760,230)
            createSlots(760,310)
            createSlots(760,405)
            createSlots(860,310)
            createSlots(860,230)
            startButton=tkinter.Button(canvas,text="Start",command=updateMap)
            startButton.place(height=65,width=155,x="770",y="450")
        else:
            window.after(10,updateMap)
    window=tkinter.Tk()
    window.title("Shape Defence")
    window.geometry("960x540+160+90")
    actualMap(count)
    window.mainloop()

startScreen()
