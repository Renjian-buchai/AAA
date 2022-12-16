init python: 
    import math 
    import random 
    import time 
    import threading 
init: 
    define randoma = float(0.0)
    define randomb = float(0.0)
    define randomc = float(0.0)
    define randomd = float(0.0)
    define score0 = float(0.0)
    default persistent.sxA23 = False
    default persistent.BwA23 = False 
    default persistent.LBwA23 = False 
    default persistent.username = None
    default persistent.gameState = 0 
    define cutscene = Movie("mvcutscene.webm", )
    define u = Character("[persistent.username]")   
    define a = DynamicCharacter("A_name")
    define ttt = "./audio/2.23_AM.mp3" 
    define tot = "./audio/3.03_PM.mp3" 
    define tdc = "./audio/10dC.mp3" 
    define sct = "./audio/Santa_Claus_is_coming_by_Train.mp3"
    define lgt = "./audio/The_lonely_ghost_and_the_moon_of_Tokyo.mp3"
    define yam = "./audio/You_and_Me.mp3" 
    define ctd = "./audio/Cassette_Tape_Dream.mp3"
    define st = "./audio/SUMMER_TRIANGLE.mp3" 
    define m1 = "./audio/Fizzy_Honey_Lemon_Soda_350ml.mp3"
    define m2 = "./audio/Lo-fi_girl_always_lacks_sleep.mp3"
    define m3 = "./audio/Sheep_of_the_Far_East_Dancing_with_the_Telecaster.mp3"
    define Cutsceney = Movie(fps=15, size=None, channel=u'sound', play="./movie/mvbadendcutscene.webm", loop=False) 
    define T = float(0.0)
    define T0 = float(0.0)
    define T1 = float(0.0)
    define Reward = "Reward" 
    define position = "Position"
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
    $ A_name = _("Feng Qiuyue")
    python: 
        if persistent.username == None: 
            renpy.scene()
            renpy.show("bglogin")
            persistent.username = renpy.input("Login:{w=0.5}\nPlease insert username: {w=0.5}", length=10, copypaste=False)
            persistent.username = persistent.username.strip() 
        if persistent.username == "" and persistent.username == None: 
            persistent.username = "Yu Wen" 
        if persistent.username != None: 
            renpy.jump("label1") 
label label1: 
    call neg1 from _call_neg1 
    return