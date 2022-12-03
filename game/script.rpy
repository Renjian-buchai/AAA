init python: 
    import math 
    import random 

#Variables
define randoma = 0
define randomb = 0 
define randomc = 0 
define randomd = 0 
define score = 0 

#Persistent 
define persistent.sxA23 = False
define persistent.username = None
define persistent.gameState = 0 

#Characters 
define u = Character("[persistent.username]") 
define a = Character("Feng Qiuyue") 

#Music 
define ttt = "./audio/2.23 AM.mp3" 
define tot = "./audio/3.03 PM.mp3" 
define tdc = "./audio/10dC.mp3" 
define sct = "./audio/Santa Claus is coming by Train.mp3"
define lgt = "./audio/The lonely ghost and the moon of Tokyo.mp3"
define yam = "./audio/You and Me.mp3" 
define ctd = "./audio/Cassette_Tape_Dream.mp3"
define st = "./audio/SUMMER_TRIANGLE.mp3" 
define m1 = "./audio/しゅわしゅわハニーレモン350ml.mp3"
define m2 = "./audio/ローファイ少女は今日も寝不足.mp3"
define m3 = "./audio/極東の羊、テレキャスターと踊る.mp3"

#Movies
define fireworks = Movie(fps=24, size=None, channel=u'sound', play="./movie/mvfireworks", loop=True) 

#Transitions
define wiperight = CropMove(1.0, "wiperight")
define wipeleft = CropMove(1.0, "wipeleft")
define wipeup = CropMove(1.0, "wipeup")
define wipedown = CropMove(1.0, "wipedown")
define slideright = CropMove(1.0, "slideright")
define slideleft = CropMove(1.0, "slideleft")
define slideup = CropMove(1.0, "slideup")
define slidedown = CropMove(1.0, "slidedown")
define slideawayright = CropMove(1.0, "slideawayright")
define slideawayleft = CropMove(1.0, "slideawayleft")
define slideawayup = CropMove(1.0, "slideawayup")
define slideawaydown = CropMove(1.0, "slideawaydown")
define irisout = CropMove(1.0, "irisout")
define irisin = CropMove(1.0, "irisin")

label start: 
    python: 
        if persistent.username == None: 
            renpy.scene("bglogin") 
            persistent.username = renpy.input("Login:{w=0.5}\nPlease insert username: {w=0.5}\n(This cannot be changed)", length=10, copypaste=False)
            persistent.username = persistent.username.strip() 
        if persistent.username == "" and persistent.username == None: 
            persistent.username = "Yu Wen" 
        if persistent.username != None: 
            renpy.jump("label1") 
label label1: 
    call neg1 
    return
