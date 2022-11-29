python: 
    import math 

define randoma = 0
define randomb = 0 
define randomc = 0 
define randomd = 0 

#Characters 
define u = Character("[username]") 
define a = Character("Feng Qiuyue") 

#Music 
define ttt = "./audio/2.23 AM.mp3" 
define tot = "./audio/3.03 PM.mp3" 
define tdc = "./audio/10dC.mp3" 
define sct = "./audio/Santa Claus is coming by Train.mp3"
define lgt = "./audio/The lonely ghost and the moon of Tokyo.mp3"
define yam = "./audio/You and Me.mp3" 

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

    scene bglogin with fade 
    $ username = renpy.input("Login:{w=0.5}\nPlease insert username: {w=0.5}", length=10, copypaste=False)
    $ username = username.strip() 
    if username == "": 
        $ username = "Yu Wen" 
    
    #Game start
    call neg1 

    return
