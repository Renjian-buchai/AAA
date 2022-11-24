define u = "[username]" 
define a = "Feng Qiuyue" 

label start:

    scene bglogin
    $ username = renpy.input("Login:{w=0.5}\nPlease insert username: {w=0.5}", length=10, copypaste=False)
    $ username = username.strip() 
    if username == "": 
        $ username = "Yu Wen" 
    
    #Game start
    call neg1 

    return
