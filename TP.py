from cmu_112_graphics import *
import math, copy, random

#app started contains all variables for start of game and many booleans which
#are used throughout the game for different situations
def appStarted(app):
    app.homeScreen = True
    app.startScreen = False
    app.gameStarted = False
    app.buttonlen = 70
    app.gameMode = 0
    app.wantsToQuit = False
    app.quarter = 1
    app.score = 0
    app.oppScore = 0
    app.pauseGame = False
    app.timerDelay = 400
    app.mx = 400
    app.my = 430
    app.oppTD = [230,0,570,0,593,50,207,50]
    app.ownTD = [823,550,-23,550,-46,600,846,600]
    app.lines = []
    for i in range(9):
        app.lines.append([0+23*i,500-50*i,800-23*i,500-50*i])
    app.LOS = 400
    app.offplayerLoc = [[app.mx,app.my],[370,410],[385,410],[400,410],[415,410],[430,410],[415,430],[250,410],[300,410],[450,410],[500,410]]
    app.defplayerLoc = [[350,350],[400,350],[450,350],[370,390],[390,390],[410,390],[430,390],[app.offplayerLoc[7][0],390],[app.offplayerLoc[8][0],390],[app.offplayerLoc[9][0],390],[app.offplayerLoc[10][0],390]]
    app.onOff = True
    app.ballSnapped = False
    app.ready = False
    app.call = False
    app.play = 0
    #I got these images from google images and 
    #they are from the Madden videogame
    app.play1 = app.scaleImage(app.loadImage("play1.png"),7/10)
    app.play2 = app.scaleImage(app.loadImage("play2.png"),1/4)
    app.play2 = app.play2.transpose(Image.FLIP_LEFT_RIGHT)
    app.play3 = app.scaleImage(app.loadImage("play3.png"),1/4)
    app.football = app.scaleImage(app.loadImage("football.png"),1/40)
    app.fx = app.mx
    app.fy = app.my
    app.timerDelay = 0
    app.hasBall = [True,False,False,False,False,False]
    app.hasBallT = [False,False,False,False,False,False]
    app.route = True
    app.ballThrown = False
    app.qbrun = False
    app.down = 1
    app.rx = 0
    app.ry = 0
    app.ydis = app.ry-app.fy
    app.xdis = app.rx-app.fx
    app.ballCatch = False
    app.bx = 450
    app.br = True
    app.chance = 0
    app.ballCaught = False
    app.gotaTD = False
    app.botTime = 0
    app.botR = 0
    app.counter = 0
    app.gameOver = False

#next down - function which sets the next down and if needed, switched the ball
#over to opposite team if there are a turnover on downs or Touchdown
def nextDown(app):
    #there are 4 different scenarios and the variables may look mostly similar
    #between all 4, there are a few different variables in each case which makes
    #it hard to write all of these resets in one seperate function
    #first case is when a ball is not caught
    if not app.ballCaught and app.ballThrown:
        app.down += 1
        if app.down>4:
            app.ballCaught = True
            nextDown(app)
        app.qbrun = False
        app.ballThrown = False
        app.ballSnapped = False
        app.ballCaught = False
        app.ready = False
        app.ballCatch = False
        app.pauseGame = False
        app.my = app.LOS+30
        app.mx = 400
        app.play = 0
        app.counter = 0
        app.hasBall = [True,False,False,False,False,False]
        app.hasBallT = [False,False,False,False,False,False]
        app.offplayerLoc = [[app.mx,app.my],[370,app.LOS+10],[385,app.LOS+10],[400,app.LOS+10],[415,app.LOS+10],[430,app.LOS+10],[415,app.LOS+30],[250,app.LOS+10],[300,app.LOS+10],[450,app.LOS+10],[500,app.LOS+10]]
        app.defplayerLoc = [[350,app.LOS-50],[400,app.LOS-50],[450,app.LOS-50],[370,app.LOS-10],[390,app.LOS-10],[410,app.LOS-10],[430,app.LOS-10],[app.offplayerLoc[7][0],app.LOS-10],[app.offplayerLoc[8][0],app.LOS-10],[app.offplayerLoc[9][0],app.LOS-10],[app.offplayerLoc[10][0],app.LOS-10]]
        if app.onOff:
            app.call = True
        else: 
            app.call = False
            app.ready = True
    #second case is when either side scores a touchdown
    elif app.gotaTD:
        app.down = 1
        app.gotaTD = False
        app.LOS = 400
        app.qbrun = False
        app.ballThrown = False
        app.ballSnapped = False
        app.ballCaught = False
        app.ready = False
        app.ballCatch = False
        app.pauseGame = False
        app.my = app.LOS+30
        app.mx = 400
        app.play = 0
        app.counter = 0
        app.onOff = not app.onOff
        app.hasBall = [True,False,False,False,False,False]
        app.hasBallT = [False,False,False,False,False,False]
        app.offplayerLoc = [[app.mx,app.my],[370,app.LOS+10],[385,app.LOS+10],[400,app.LOS+10],[415,app.LOS+10],[430,app.LOS+10],[415,app.LOS+30],[250,app.LOS+10],[300,app.LOS+10],[450,app.LOS+10],[500,app.LOS+10]]
        app.defplayerLoc = [[350,app.LOS-50],[400,app.LOS-50],[450,app.LOS-50],[370,app.LOS-10],[390,app.LOS-10],[410,app.LOS-10],[430,app.LOS-10],[app.offplayerLoc[7][0],app.LOS-10],[app.offplayerLoc[8][0],app.LOS-10],[app.offplayerLoc[9][0],app.LOS-10],[app.offplayerLoc[10][0],app.LOS-10]]
        if app.onOff:
            app.quarter += 1
            app.call = True
        else: 
            app.call = False
            app.ready = True
    #the fourth case is when 4th down is over
    elif app.down > 3:
        app.down = 1
        app.LOS = 400
        app.qbrun = False
        app.ballThrown = False
        app.ballSnapped = False
        app.ballCaught = False
        app.ready = False
        app.ballCatch = False
        app.pauseGame = False
        app.my = app.LOS+30
        app.mx = 400
        app.play = 0
        app.counter = 0
        app.onOff = not app.onOff
        app.hasBall = [True,False,False,False,False,False]
        app.hasBallT = [False,False,False,False,False,False]
        app.offplayerLoc = [[app.mx,app.my],[370,app.LOS+10],[385,app.LOS+10],[400,app.LOS+10],[415,app.LOS+10],[430,app.LOS+10],[415,app.LOS+30],[250,app.LOS+10],[300,app.LOS+10],[450,app.LOS+10],[500,app.LOS+10]]
        app.defplayerLoc = [[350,app.LOS-50],[400,app.LOS-50],[450,app.LOS-50],[370,app.LOS-10],[390,app.LOS-10],[410,app.LOS-10],[430,app.LOS-10],[app.offplayerLoc[7][0],app.LOS-10],[app.offplayerLoc[8][0],app.LOS-10],[app.offplayerLoc[9][0],app.LOS-10],[app.offplayerLoc[10][0],app.LOS-10]]
        if app.onOff:
            app.quarter += 1
            app.call = True
        else: 
            app.call = False
            app.ready = True
    #last case is simply moving on to the next down
    else:
        if app.fy<=50:
            touchDown(app)
        app.down += 1
        app.LOS = app.fy
        app.qbrun = False
        app.ballThrown = False
        app.ballSnapped = False
        app.ballCaught = False
        app.ready = False
        app.ballCatch = False
        app.pauseGame = False
        app.my = app.LOS+30
        app.mx = 400
        app.play = 0
        app.counter = 0
        app.hasBall = [True,False,False,False,False,False]
        app.hasBallT = [False,False,False,False,False,False]
        app.offplayerLoc = [[app.mx,app.my],[370,app.LOS+10],[385,app.LOS+10],[400,app.LOS+10],[415,app.LOS+10],[430,app.LOS+10],[415,app.LOS+30],[250,app.LOS+10],[300,app.LOS+10],[450,app.LOS+10],[500,app.LOS+10]]
        app.defplayerLoc = [[350,app.LOS-50],[400,app.LOS-50],[450,app.LOS-50],[370,app.LOS-10],[390,app.LOS-10],[410,app.LOS-10],[430,app.LOS-10],[app.offplayerLoc[7][0],app.LOS-10],[app.offplayerLoc[8][0],app.LOS-10],[app.offplayerLoc[9][0],app.LOS-10],[app.offplayerLoc[10][0],app.LOS-10]]
        if app.onOff:
            app.call = True
        else: 
            app.call = False
            app.ready = True
    #checks if the game is over, and if it is, ends the game
    if app.quarter==5:
        app.gameOver = True

#when touchdown is scored, it adds to the score and changes teams   
def touchDown(app):
    if app.onOff:
        app.score += 7
    else:
        app.oppScore += 7
    app.LOS = 400
    app.gotaTD = True
    nextDown(app)

#when ball is thrown
def ballinAir(app):
    app.ballThrown = True
    if app.onOff:
        if tackled(app,app.fx,app.fy,app.rx,app.ry):
            app.ballCatch = True
        else:
            app.fx += app.xdis/100
            app.fy += app.ydis/100
    else:
        if tackled(app,app.fx,app.fy,app.rx,app.ry):
            app.ballCatch = True
        else:
            app.fx += app.xdis/100
            app.fy += app.ydis/100

#players moving - changes the specific position of each player on the field 
#based on the specific play chosen by the user or bot. 
def playersMoving(app):
    #seperate cases for how and when the players move, whether they have the
    #ball or not
    #first case is when the user route running
    if app.onOff and app.route and not app.qbrun:
        dline(app)
        if app.play==1:
            play1(app)
        elif app.play==2:
            play2(app)
        elif app.play==3:
            play3(app)
    #second is when a user does a qb run or the ball is caught
    if app.qbrun or app.ballCaught:
        for i in range(11):
            if app.fy > app.defplayerLoc[i][1]:
                app.defplayerLoc[i][1] += 1
            if app.fy < app.defplayerLoc[i][1]:
                app.defplayerLoc[i][1] -= 1
            if app.fx > app.defplayerLoc[i][0]:
                app.defplayerLoc[i][0] += 1
            if app.fx < app.defplayerLoc[i][0]:
                app.defplayerLoc[i][0] -= 1
            if tackled(app,app.defplayerLoc[i][0],app.defplayerLoc[i][1],app.fx,app.fy):
                nextDown(app)
                break
    #third is when the ball is thrown
    if app.ballThrown:
        app.pauseGame = True
    #fourth is when the bot is route running
    if not app.onOff and app.route:
        app.offplayerLoc[0][1] += 0.1
        app.fx = app.offplayerLoc[0][0]
        app.fy = app.offplayerLoc[0][1]
        dline(app)
        if app.play==1:
            play1(app)
        elif app.play==2:
            play2(app)
        elif app.play==3:
            play3(app)
    #fifth case is when the bot catches a ball
    if not app.onOff and app.ballCaught:
        app.offplayerLoc[app.botR+5][1] -= 1
        app.rx = app.offplayerLoc[app.botR+5][0]
        app.ry = app.offplayerLoc[app.botR+5][1]
        app.fx = app.rx
        app.fy = app.ry
        if app.ballCaught and app.fy<=50:
            touchDown(app)

#function for safety movement(3 defensive players in the back):
def saf(app):
    for i in range(3):
        if app.defplayerLoc[i][1]>300:
            app.defplayerLoc[i][1] -= 1
        elif app.defplayerLoc[i][1]>=100 and app.defplayerLoc[i][1]<=300: 
            app.defplayerLoc[i][1] -= 0.5
        elif app.defplayerLoc[i][1]>=30 and app.defplayerLoc[i][1]<=100:
            app.defplayerLoc[i][1] -= 0.1

#function for defensive line movement
def dline(app):
    app.offplayerLoc[1][1] += 0.05
    app.offplayerLoc[5][1] += 0.05
    app.offplayerLoc[2][1] += 0.025
    app.offplayerLoc[4][1] += 0.024
    app.offplayerLoc[3][1] += 0.0125
    app.defplayerLoc[3][1] += 0.125
    app.defplayerLoc[4][1] += 0.1
    app.defplayerLoc[5][1] += 0.1
    app.defplayerLoc[6][1] += 0.125
    if app.offplayerLoc[3][1]< app.defplayerLoc[4][1]:
        for i in range(3,7):
            if app.offplayerLoc[0][1] > app.defplayerLoc[i][1]:
                app.defplayerLoc[i][1] += 1
            if app.offplayerLoc[0][1] < app.defplayerLoc[i][1]:
                app.defplayerLoc[i][1] -= 1
            if app.offplayerLoc[0][0] > app.defplayerLoc[i][0]:
                app.defplayerLoc[i][0] += 1
            if app.offplayerLoc[0][0] < app.defplayerLoc[i][0]:
                app.defplayerLoc[i][0] -= 1
            if tackled(app,app.defplayerLoc[i][0],app.defplayerLoc[i][1],app.fx,app.fy):
                nextDown(app)
                break

#function for play1 route running
def play1(app):
    if not app.ballCaught:
        if app.offplayerLoc[8][1]>=0:
            app.offplayerLoc[8][1] -= 1
        else:
            app.offplayerLoc[8][1] += 2
        if app.offplayerLoc[7][1]>=app.LOS-70:
            app.offplayerLoc[7][1] -= 1
        else:
            app.offplayerLoc[7][0] += 0.5
        if app.offplayerLoc[6][1]>=app.LOS-70:
            app.offplayerLoc[6][1] -= 1
        else:
            app.offplayerLoc[6][1] += 0.2
            app.offplayerLoc[6][0] -= 0.2
        if app.offplayerLoc[9][1]>=app.LOS-100:
            app.offplayerLoc[9][1] -= 1
        elif app.offplayerLoc[9][1]<=0:
            app.offplayerLoc[9][1] += 2
        elif not isInBounds(app.offplayerLoc[9][0],app.offplayerLoc[9][1]):
            app.offplayerLoc[9][0] -= 2
        else:
            app.offplayerLoc[9][1] -= 0.5
            app.offplayerLoc[9][0] += 0.5
        if app.offplayerLoc[10][1]>=app.LOS-20:
            app.offplayerLoc[10][1] -= 1
        else:
            app.offplayerLoc[10][1] += 0.2
            app.offplayerLoc[10][0] -= 0.2
        for i in range(7,11):
            app.defplayerLoc[i][0] = app.offplayerLoc[i][0]
            app.defplayerLoc[i][1] = app.offplayerLoc[i][1]-20
        saf(app)

#function for play2 route running
def play2(app):
    if not app.ballCaught:
        if app.offplayerLoc[7][1]>=0:
            app.offplayerLoc[7][1] -= 1
        else:
            app.offplayerLoc[7][1] += 2
        if app.offplayerLoc[10][1]>=0:
            app.offplayerLoc[10][1] -= 1
        else:
            app.offplayerLoc[10][1] += 2
        app.offplayerLoc[6][0] -= 0.5
        if app.offplayerLoc[9][1]>=app.LOS-60:
            app.offplayerLoc[9][1] -= 1
        else:
            app.offplayerLoc[9][1] += 0.2
            app.offplayerLoc[9][0] -= 0.2
        if app.offplayerLoc[8][1]>=app.LOS-100:
            app.offplayerLoc[8][1] -= 1
        elif app.offplayerLoc[8][1]<=0:
            app.offplayerLoc[8][1] += 2
        else:
            app.offplayerLoc[8][1] -= 0.5
            app.offplayerLoc[8][0] += 0.5
        for i in range(7,11):
            app.defplayerLoc[i][0] = app.offplayerLoc[i][0]
            app.defplayerLoc[i][1] = app.offplayerLoc[i][1]-20
        saf(app)

#function for play3 route running
def play3(app):
    for i in range(6,11):
        if app.offplayerLoc[i][1]>=0:
            app.offplayerLoc[i][1] -= 1
        else:
            app.offplayerLoc[i][1] += 2
        if i>6:
            if app.offplayerLoc[i][1]>300:
                app.defplayerLoc[i][0] = app.offplayerLoc[i][0]
                app.defplayerLoc[i][1] = app.offplayerLoc[i][1]-20
            elif app.offplayerLoc[i][1]>200 and app.offplayerLoc[i][1]<300:
                app.defplayerLoc[i][0] = app.offplayerLoc[i][0]+15
                app.defplayerLoc[i][1] = app.offplayerLoc[i][1]
            elif app.offplayerLoc[i][1]<200:
                app.defplayerLoc[i][0] = app.offplayerLoc[i][0]
                app.defplayerLoc[i][1] = app.offplayerLoc[i][1]+15
    saf(app)

#checks if player is tackled or the ball reached a receiver
# (uses distance formula)
def tackled(app,x,y,x1,y1):
    v = ((x-x1)**2+(y-y1)**2)**0.5
    if v<7:
        return True
    return False

#creates pop ups and other canvas creations based on events of games
def storyBoard(app,canvas):
    if app.call:
        canvas.create_rectangle(25,50,775,500,fill="dimgrey")
        canvas.create_text(400,125,text="Choose Play",fill="white",
                        font = "Arial 40")
        canvas.create_rectangle(50,200,250,400,fill="black")
        canvas.create_image(150,300,image=ImageTk.PhotoImage(app.play1))
        canvas.create_rectangle(300,200,500,400,fill="black")
        canvas.create_image(400,300,image=ImageTk.PhotoImage(app.play2))
        canvas.create_rectangle(550,200,750,400,fill="black")
        canvas.create_image(650,300,image=ImageTk.PhotoImage(app.play3))
    if not app.call and not app.ballSnapped and app.ready:
        canvas.create_text(400,125,text="Press Space to Snap",fill="yellow",
                        font = "Arial 40")
        canvas.create_image(app.offplayerLoc[3][0],app.offplayerLoc[3][1],
                        image=ImageTk.PhotoImage(app.football))
    elif not app.call and app.ballSnapped and not app.ready:
        canvas.create_image(app.fx,app.fy,
                            image=ImageTk.PhotoImage(app.football))
    if app.ballCatch:
        canvas.create_rectangle(340,95,460,130,fill="silver")
        canvas.create_rectangle(350,100,390,125,fill="darkred")
        canvas.create_rectangle(390,100,410,125,fill="green")
        canvas.create_rectangle(410,100,450,125,fill="darkred")
        canvas.create_rectangle(app.bx-5,100,app.bx+5,125,fill="silver")
    if app.onOff:
        canvas.create_image(330,580,image=ImageTk.PhotoImage(app.football))
    else:
        canvas.create_image(450,580,image=ImageTk.PhotoImage(app.football))
    if app.quarter==5:
        canvas.create_rectangle(25,50,775,500,fill="dimgrey")
        if app.score<app.oppScore:
            canvas.create_text(400,125,text="Game Over, You Lose",fill="red",
                        font = "Arial 40")
        elif app.score>app.oppScore:
            canvas.create_text(400,125,text="You Win!",fill="lime",
                        font = "Arial 40")
        elif app.score==app.oppScore:
            canvas.create_text(400,125,text="You Tied",fill="white",
                        font = "Arial 40")
        canvas.create_rectangle(300,350,500,400,fill="grey")
        canvas.create_text(400,250,text=f"{app.score}-{app.oppScore}",fill="white",
                        font = "Arial 20")
        canvas.create_text(400,375,text="Home Screen",fill="white",
                        font = "Arial 20")

#draws players in their relative positions
def drawPlayers(app,canvas):
    for i in range(11):
        if app.onOff:
            canvas.create_oval(app.offplayerLoc[i][0]-7,
                            app.offplayerLoc[i][1]-7,app.offplayerLoc[i][0]+7,
                            app.offplayerLoc[i][1]+7,fill="darkred")
            canvas.create_oval(app.defplayerLoc[i][0]-7,
                            app.defplayerLoc[i][1]-7,app.defplayerLoc[i][0]+7,
                            app.defplayerLoc[i][1]+7,fill="blue")
        else:
            canvas.create_oval(app.offplayerLoc[i][0]-7,
                            app.offplayerLoc[i][1]-7,app.offplayerLoc[i][0]+7,
                            app.offplayerLoc[i][1]+7,fill="blue")
            canvas.create_oval(app.defplayerLoc[i][0]-7,
                            app.defplayerLoc[i][1]-7,app.defplayerLoc[i][0]+7,
                            app.defplayerLoc[i][1]+7,fill="darkred")

    keys = ["S","A","W","E","D"]
    if app.onOff:
        for i in range(6,11):
            canvas.create_text(app.offplayerLoc[i][0],app.offplayerLoc[i][1],
                            text=keys[i-6],fill="yellow",font = "Arial 8")

#positions all of the players when the keys are pressed
def pos(app):
    if app.hasBall[0]:
        app.offplayerLoc[0] = [app.mx,app.my]
    for i in range(1,6):
        if app.hasBall[i]:
            app.offplayerLoc[i+5] = [app.mx,app.my]
    app.fx = app.mx
    app.fy = app.my
    if app.fy<=50:
        touchDown(app)
        
#checks if player is in bounds and returns True if they are
def isInBounds(x,y):
    bound = 400-230*((500-y)/500)
    if(x>400-bound and x<400+bound):
        return True
    return False

#draws the field
def drawField(app,canvas):
    canvas.create_polygon(app.oppTD[0],app.oppTD[1],app.oppTD[2],
                        app.oppTD[3],app.oppTD[4],app.oppTD[5],
                        app.oppTD[6],app.oppTD[7],fill="darkred")
    canvas.create_polygon(app.ownTD[0],app.ownTD[1],app.ownTD[2],
                        app.ownTD[3],app.ownTD[4],app.ownTD[5],
                        app.ownTD[6],app.ownTD[7],fill="darkred")
    canvas.create_line(app.lines[0][0],app.lines[0][1],app.lines[0][2],app.lines[0][3],
                    width=2, fill="white")
    canvas.create_line(app.lines[1][0],app.lines[1][1],app.lines[1][2],app.lines[1][3],
                    width=2, fill="white")
    canvas.create_line(app.lines[2][0],app.lines[2][1],app.lines[2][2],app.lines[2][3],
                    width=2, fill="white")
    canvas.create_line(app.lines[3][0],app.lines[3][1],app.lines[3][2],app.lines[3][3],
                    width=2, fill="white")
    canvas.create_line(app.lines[4][0],app.lines[4][1],app.lines[4][2],app.lines[4][3],
                    width=2, fill="white")
    canvas.create_line(app.lines[5][0],app.lines[5][1],app.lines[5][2],app.lines[5][3],
                    width=2, fill="white")
    canvas.create_line(app.lines[6][0],app.lines[6][1],app.lines[6][2],
                    app.lines[6][3], width=2, fill="white")
    canvas.create_line(app.lines[7][0],app.lines[7][1],app.lines[7][2],app.lines[7][3],
                    width=2, fill="white")
    canvas.create_line(app.lines[8][0],app.lines[8][1],app.lines[8][2],app.lines[8][3],
                    width=2, fill="white")
    canvas.create_line(230,0,0,500,width=7)
    canvas.create_line(570,0,800,500,width=7)
    canvas.create_line(app.oppTD[0],app.oppTD[1],
                        app.oppTD[2],app.oppTD[3],width=7)
    canvas.create_line(app.ownTD[4],app.ownTD[5],
                        app.ownTD[6],app.ownTD[7],width=7)

#timer fired for time
def timerFired(app):
    if app.onOff:
        if not app.pauseGame and app.ballSnapped:
            playersMoving(app)
        elif app.ballThrown:
            ballinAir(app)
        if app.ballCatch:
            if app.br:
                app.bx -= 5
            else:
                app.bx += 5
            if app.bx<=350:
                app.br = False
            elif app.bx>=450:
                app.br = True
    else:
        if not app.pauseGame and app.ballSnapped:
            playersMoving(app)
            app.counter += 1
            if app.counter==app.botTime:
                app.pauseGame = True
                app.hasBallT[0] = False
                app.hasBallT[app.botR] = True
                app.rx = app.offplayerLoc[app.botR+5][0]
                app.ry = app.offplayerLoc[app.botR+5][1]
                app.ydis = app.ry-app.fy
                app.xdis = app.rx-app.fx
                app.hasBall[0] = False
                app.hasBallT[1] = True
                app.ballThrown = True
        elif app.ballThrown:
            ballinAir(app)
        if app.ballCatch:
            if app.br:
                app.bx -= 5
            else:
                app.bx += 5
            if app.bx<=350:
                app.br = False
            elif app.bx>=450:
                app.br = True

#checks which keys are pressed in game
def keyPressed(app, event):
    if app.gameStarted:
        if not app.call and not app.ballSnapped and app.ready:
            if(event.key=='Space'):
                app.ready = False
                app.ballSnapped = True
                if not app.onOff:
                    app.play = random.randint(1,3)
                    app.botTime = random.randint(0,250)
                    app.botR = random.randint(1,5)

        if app.onOff:
            if not app.pauseGame and app.ballSnapped:
                if (event.key=='Down'):
                    if app.my <= 590:
                        app.my += 4
                        if not isInBounds(app.mx,app.my):
                            app.my -= 4
                            nextDown(app)
                elif(event.key=='Left'):
                    app.mx -= 4
                    if not isInBounds(app.mx,app.my):
                            app.mx += 4
                            nextDown(app)
                elif(event.key=='Right'):
                    app.mx += 4
                    if not isInBounds(app.mx,app.my):
                            app.mx -= 4
                            nextDown(app)
                elif(event.key=='Up'):
                    if app.my >= 25:
                        app.my -= 4
                        if not isInBounds(app.mx,app.my):
                            app.my += 4
                            nextDown(app)
                if app.my < app.LOS:
                    app.qbrun = True

            if not app.ballThrown and not app.qbrun:
                if (event.key=='s') and app.hasBall[0]:
                    app.rx = app.offplayerLoc[6][0]
                    app.ry = app.offplayerLoc[6][1]
                    app.ydis = app.ry-app.fy
                    app.xdis = app.rx-app.fx
                    app.hasBall[0] = False
                    app.hasBallT[1] = True
                    app.ballThrown = True
                    app.pauseGame = True
                elif (event.key=='a') and app.hasBall[0]:
                    app.rx = app.offplayerLoc[7][0]
                    app.ry = app.offplayerLoc[7][1]
                    app.ydis = app.ry-app.fy
                    app.xdis = app.rx-app.fx
                    app.hasBall[0] = False
                    app.hasBallT[2] = True
                    app.ballThrown = True
                    app.pauseGame = True
                elif (event.key=='w') and app.hasBall[0]:
                    app.rx = app.offplayerLoc[8][0]
                    app.ry = app.offplayerLoc[8][1]
                    app.ydis = app.ry-app.fy
                    app.xdis = app.rx-app.fx
                    app.hasBall[0] = False
                    app.hasBallT[3] = True
                    app.ballThrown = True
                    app.pauseGame = True
                elif (event.key=='e') and app.hasBall[0]:
                    app.rx = app.offplayerLoc[9][0]
                    app.ry = app.offplayerLoc[9][1]
                    app.ydis = app.ry-app.fy
                    app.xdis = app.rx-app.fx
                    app.hasBall[0] = False
                    app.hasBallT[4] = True
                    app.ballThrown = True
                    app.pauseGame = True
                elif (event.key=='d') and app.hasBall[0]:
                    app.rx = app.offplayerLoc[10][0]
                    app.ry = app.offplayerLoc[10][1]
                    app.ydis = app.ry-app.fy
                    app.xdis = app.rx-app.fx
                    app.hasBall[0] = False
                    app.hasBallT[5] = True
                    app.ballThrown = True
                    app.pauseGame = True
            
            if app.ballCatch:
                if(event.key=='Space'):
                    if app.bx<410 and app.bx>390:
                        app.ballCaught = True
                        app.pauseGame = False
                        app.hasBall = app.hasBallT
                        app.mx = app.rx
                        app.my = app.ry
                        app.fx = app.mx
                        app.fy = app.my
                        if app.ballCaught and app.fy<=50:
                            touchDown(app)
                        else:    
                            app.ballThrown = False
                            app.ballCatch = False
                    else:
                        app.ballCaught = False
                        app.hasBall[0] = True
                        for i in range(1,6):
                            app.hasBall[i] = False
                        nextDown(app)
            pos(app)

        else:
            if app.ballCatch:
                if(event.key=='Space'):
                    app.chance = random.uniform(0,1)
                    if app.bx<410 and app.bx>390:
                        app.ballCaught = False
                        app.hasBall[0] = True
                        for i in range(1,6):
                            app.hasBall[i] = False
                        nextDown(app)
                    else:
                        app.ballCaught = True
                        app.pauseGame = False
                        app.hasBall = app.hasBallT
                        app.rx = app.offplayerLoc[app.botR+5][0]
                        app.ry = app.offplayerLoc[app.botR+5][1]
                        app.fx = app.rx
                        app.fy = app.ry
                        app.ballThrown = False
                        app.ballCatch = False
                    if app.ballCaught and app.fy<=50:
                        touchDown(app)    

#checks which clicks are needed in game
def mousePressed(app, event):
    y = event.y
    x = event.x

    if app.gameOver:
        if x<500 and x>300 and y<400 and y>350:
            appStarted(app)

    if app.call and app.gameStarted:
        if y>200 and y<400:
            if x>50 and x<250:
                app.play = 1
            elif x>300 and x<500:
                app.play = 2
            elif x>550 and x<750:
                app.play = 3
        if app.play>0:
            app.call = False
            app.ready = True

    if app.homeScreen:
        if x>app.width/2-app.buttonlen and x<app.width/2+app.buttonlen:
            if y<250 and y>200:
                app.homeScreen = False
                app.startScreen = True
            
    elif app.startScreen:
        if x>50 and x<150 and y>25 and y<75:
            app.homeScreen = True
            app.startScreen = False
        elif x>app.width/2-app.buttonlen and x<app.width/2+app.buttonlen:
            if y<250 and y>200:
                app.gameMode = 1
                app.call = True
                app.gameStarted = True
                app.startScreen = False
            elif y>300 and y<350:
                app.gameMode = 2
                app.call = True
                app.gameStarted = True
                app.startScreen = False
            elif y<450 and y>400:
                app.gameMode = 3
                app.call = True
                app.gameStarted = True
                app.startScreen = False

    if app.gameStarted:  
        if x<70 and y<25:
            app.pauseGame = True
            app.wantsToQuit = True

    if app.wantsToQuit:
        if y<350 and y>300:
            if x>150 and x<350:
                appStarted(app)
            elif x>450 and x<650:
                app.pauseGame = False
                app.wantsToQuit = False
    
    if app.play==2:
        pass

#draws the home screen
def drawHomeScreen(app,canvas):
    canvas.create_rectangle(0,0,800,600,fill="mediumseagreen")
    canvas.create_text(app.width/2,70,text="CMU-112 Football",fill="white",
                        font = "Arial 40 bold")
    canvas.create_rectangle(app.width/2-app.buttonlen,200,
                    app.width/2+app.buttonlen,250,fill="seagreen")
    canvas.create_text(app.width/2,225,text="Start Game",fill="white",
                        font = "Arial 20")

#draws the start screen
def drawStartScreen(app,canvas):
    canvas.create_rectangle(0,0,800,600,fill="mediumseagreen")
    canvas.create_text(app.width/2,70,text="CMU-112 Football",fill="white",
                        font = "Arial 40 bold")
    canvas.create_text(app.width/2,150,text="Select Mode:",fill="white",
                        font = "Arial 30")
    canvas.create_rectangle(50,25,150,75,fill="seagreen")
    canvas.create_text(100,50,text="Back",fill="white",font = "Arial 20")
    canvas.create_rectangle(app.width/2-app.buttonlen,200,
                    app.width/2+app.buttonlen,250,fill="seagreen")
    canvas.create_text(app.width/2,225,text="Rookie",fill="white",
                        font = "Arial 20")
    canvas.create_rectangle(app.width/2-app.buttonlen,300,
                    app.width/2+app.buttonlen,350,fill="seagreen")
    canvas.create_text(app.width/2,325,text="Pro",fill="white",
                        font = "Arial 20")
    canvas.create_rectangle(app.width/2-app.buttonlen,400,
                    app.width/2+app.buttonlen,450,fill="seagreen")
    canvas.create_text(app.width/2,425,text="All-Pro",fill="white",
                        font = "Arial 20")

#draws the game
def drawGame(app,canvas):
    canvas.create_rectangle(0,0,800,600,fill="mediumseagreen")
    drawField(app,canvas)
    drawPlayers(app,canvas)
    canvas.create_rectangle(app.width/2-150,560,
            app.width/2+150,600,fill="darkgrey")
    canvas.create_rectangle(0,0,70,25,fill="darkgrey")
    canvas.create_text(35,12,text="Exit Game",fill="white",font = "Arial 10")
    if app.quarter<5:
        canvas.create_text(app.width/2,570,text=f"Quarter {app.quarter}",
                            fill="white",font = "Arial 10")
    else:
        canvas.create_text(app.width/2,570,text=f"Quarter 4",
                            fill="white",font = "Arial 10")
    canvas.create_text(app.width/2-110,580,text=f"CMU: {app.score}",
                        fill="white",font = "Arial 15")
    canvas.create_text(app.width/2+100,580,text=f"Opponent: {app.oppScore}",
                        fill="white",font = "Arial 15")
    canvas.create_text(app.width/2,590,text=f"Down: {app.down}",
                        fill="white",font = "Arial 10")
    storyBoard(app,canvas)

#draws quitgame option in corner
def drawWantsToQuit(app,canvas):
    canvas.create_rectangle(100,100,700,400,fill="darkgrey")
    canvas.create_text(app.width/2,200,text="Do you want to exit the game?",
                        fill="white",font = "Arial 30")
    canvas.create_rectangle(150,300,350,350,fill="lightgrey")
    canvas.create_text(250,325,text="Exit Game",
                        fill="red",font = "Arial 20")
    canvas.create_rectangle(450,300,650,350,fill="lightgrey")
    canvas.create_text(550,325,text="Return To Game",
                        fill="green",font = "Arial 20")

#draws everything
def redrawAll(app,canvas):
    if app.homeScreen:
        drawHomeScreen(app,canvas)
    elif app.startScreen:
        drawStartScreen(app,canvas)
    elif app.gameStarted:
        drawGame(app,canvas)
        if app.wantsToQuit:
            drawWantsToQuit(app,canvas)

def main():
    runApp(width=800, height=600)

if __name__ == '__main__':
    main()
