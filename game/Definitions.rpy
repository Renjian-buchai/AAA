label Definitions: 
    init python: 
        import math 
        import random 
        import time 
        import threading 
    
    init: 
        # Characters 
        define u = Character("[persistent.username]")   
        define a = DynamicCharacter("A_name")

        # Persistent
        default persistent.sxA23 = False
        default persistent.BwA23 = False 
        default persistent.LBwA23 = False 
        default persistent.username = None
        default persistent.gameState = 0 

        # Movies 

        # Music 
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
return 