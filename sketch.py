from p5 import *
def setup():
  createCanvas(windowWidth,windowHeight)
  global stickman,e1,e2,e3,e4,e5,e6,e7,e8,e9,gameState,stickX,score,level,highscore,soundcount
  soundcount=0
  score=0
  highscore=0
  stickX = 0
  level=1
  loadImage('stickaaron.png','stick')
  noStroke()
  textFont("comic sans ms")
  loadSound('moon.mp3','Happymusic')
  loadSound('error.mp3','Error')
 
#dictionary -> {key:value,key:value,key:value..........}
  #dictionary is a collection of lots of elements which are stored as key:value pairs

  gameState = "play"
  e1={
    'x':random(0,width),
    'y':random(350,height+100)
  }
  e2={
    'x':random(0,width),
    'y':random(0,height)
  }
  e3={
    'x':random(0,width),
    'y':random(0,height)
  }
  e4={
    'x':random(0,width),
    'y':random(0,height)
  }
  e5={
    'x':random(0,width),
    'y':random(0,height)
  }
  e6={
    'x':random(0,width),
    'y':random(0,height)
  }
  e7={
    'x':random(0,width),
    'y':random(0,height)
  }
  e8={
    'x':random(0,width),
    'y':random(0,height)
  }
  e9={
    'x':random(0,width),
    'y':random(0,height)
  }

def draw():
  global stickman,stickX,level,soundcount,highscore,score
  changeBackground()
  # playing the music
  if not(assets['Happymusic'].isPlaying()):
    assets['Happymusic'].play()

  
  
  fill("green")
  rect(0,0,width,20)
  #crosshair()

  image(assets['stick'],stickX,20,50,50)  #image(imgVariable,x,y,w,h)
  # drawTickAxes()

  drawEmoji(e1)
  drawEmoji(e2)
  drawEmoji(e3)
  drawEmoji(e4)
  drawEmoji(e5)
  drawEmoji(e6)
  drawEmoji(e7)
  drawEmoji(e8)
  drawEmoji(e9)
  scoreBoard()
  changelevel()

  if gameState == "over":
    if highscore < score:
      highscore = score
      
    textAlign()
    textSize(50)
    text("Game over",400,350)
    assets['Happymusic'].stop()
    
    if (not(assets['Error'].isPlaying())) and soundcount == 0:
      assets['Error'].play()
      soundcount = 1
  if gameState == "play":
    
    stickX=mouseX
    fallEmoji(e1)
    fallEmoji(e2)
    fallEmoji(e3)
    fallEmoji(e4)
    fallEmoji(e5)
    fallEmoji(e6)
    fallEmoji(e7)
    fallEmoji(e8)
    fallEmoji(e9)

    emojiCollide(e1)
    emojiCollide(e2)
    emojiCollide(e3)
    emojiCollide(e4)
    emojiCollide(e5)
    emojiCollide(e6)
    emojiCollide(e7)
    emojiCollide(e8)
    emojiCollide(e9)








  #calling the function

#creating the function
def drawEmoji(emo):
  global level
  textSize(40)
  if level==1:
    text("😀",emo['x'],emo['y'])
  elif level==2:
    text("😐",emo['x'],emo['y'])
  elif level==3:
    text("😑",emo['x'],emo['y'])
  elif level==4:
    text("😠",emo['x'],emo['y'])
  elif level==5:
    text("😤",emo['x'],emo['y'])
  elif level==6:
    text("🤬",emo['x'],emo['y'])

def fallEmoji(emo):
  global score
  print("fall")
  if level==1:
    emo['y']=emo['y']-5
  elif level==2:
    emo['y']=emo['y']-6
  elif level==3:
    emo['y']=emo['y']-7
  elif level==4:
    emo['y']=emo['y']-8
  elif level==5:
    emo['y']=emo['y']-9
  elif level==6:
    emo['y']=emo['y']-10
  if emo['y']<0:
    score=score+1
    emo['y']=height+50
    emo['x']=random(0,width)

def emojiCollide(emo):
  global gameState
  distX= abs(mouseX-emo['x'])
  distY= abs(20-emo['y'])
  if distX < 20 and distY < 20:
    print("Game over")
    gameState = "over"
    

def scoreBoard():
  global score, highscore
  fill("crimson")
  rect(width-280,height-140,220,130,10)
  fill("yellow")
  textSize(22)
  text(f"Score: {score}",width-270,height-80)
  text(f"HighScore: {highscore}",width-270,height-40)


def changelevel():
  global level,score,highscore
  textSize(22)
  text(f"Level: {level}",width-270,height-110)
  #here write the if -elif statements for changing levels with score
  if score <=20:
    level=1
  elif score<=40:
    level=2
  elif score<=60:
    level=3
  elif score<=80:
    level=4
  elif score<=100:
    level=5
  else:
    level=6

def changeBackground():
  if level==1:
    background(13, 177, 231, 30)
  elif level==2:
    background(26, 107, 230, 30)
  elif level==3:
    background(88, 92, 219, 30)
  elif level==4:
    background(52, 56, 207, 30)
  elif level==5:
    background(33, 36, 181, 30)
  elif level==6:
    background(102, 14, 145, 30)

def mousePressed():
  global gameState,score
  if gameState == "over":
    gameState = "play"
    score = 0








