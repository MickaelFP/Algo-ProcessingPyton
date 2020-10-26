ballX = 0
ballY = 0
ballSpeedX = 0.5
ballSpeedY = 0.1

ballSpeed = 0.3
ballAngle = PI/6
ballAngleMax = PI/1.9

ballRadius = 5

racketWidth = 50
racketHeight = 10
racketX = 0
racketY = 0

lastFrameTime = 0
deltaTime = 0

#ici on définit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    global ballX, ballY, racketX, racketY, racketWidth, racketHeight
    global LastFrameTime, deltaTime
    
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on définit la taille de la fenêtre
    size(400, 400)
    #vide la fenêtre
    clear()
    #on change la frameRate de l'application
    frameRate(60)
    ballX = width/2
    ballY = height/2
    
    racketX = mouseX - (racketWidth/2)
    racketY = height - 50
    
    lastFrameTime = millis()

def draw():
    global deltaTime, lastFrameTime
    
    clear()
    
    deltaTime = millis() - lastFrameTime
    lastFrameTime = millis()
    
    drawRacket()
    drawBall()

def drawRacket():
    global racketX, racketY, racketWidth, racketHeight
    
    fill(255)
    #draw a rectangle in coords
    # x : mouseX minus half of width
    # y : height of the window minus 20
    # width : 50
    # height : 10
    racketX = mouseX - (racketWidth/2)
    rect(racketX, racketY, racketWidth, racketHeight)

def drawBall():
    global ballX, ballY, ballRadius, ballSpeed, ballAngle, ballAngleMax
    global racketX, racketY, racketWidth, racketHeight
    global deltaTime
    
    #draw circle
    #circle(ballX, height/2, 10);
    #circle(ballX, ballY, 10)
    
    #ballX = ballX + ballSpeedX
    #ballY = ballY + ballSpeedY
    speedX = cos(ballAngle) * ballSpeed * deltaTime
    speedY = sin(ballAngle) * ballSpeed * deltaTime
    ballX += speedX
    ballY -= speedY
    
    #haut et bas
    if(ballY-ballRadius < 0):
        ballAngle = - ballAngle
        ballY = ballRadius
    elif(ballY+ballRadius > height):
        ballAngle = - ballAngle
        ballY = height-ballRadius
    
    #droite et gauche
    if(ballX+ballRadius > width):
        ballAngle = - PI - ballAngle
        ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
        ballAngle = - PI - ballAngle
        ballX = ballRadius
        
    if(racketY < ballY+ballRadius < racketY+racketHeight and speedY < 0):
        if(racketX < ballX < racketX + racketWidth):
            ratio = (ballX - racketX - racketWidth/2) /  (racketWidth/2)
            #print("position de la balle sur la raquette : ")
            #print(ratio)
            ballAngle = PI/2 - ratio * ballAngleMax
            ballY = racketY-ballRadius
    
    #if(racketY < ballY+ballRadius < racketY+racketHeight
    
    #haut racket
    #if(racketY + 10 >= ballY+ballRadius >= racketY)and(racketX <= ballX+ballRadius <= racketX + racketWidth):
        #ballSpeedY *= -1
    
     
    
    circle(ballX, ballY, 2*ballRadius);
    
