define u = "[username]" 
define a = "a" 

label start:

    scene bglogin
    $ username = renpy.input("Login:\nPlease insert username: ", length=10, copypaste=False)
    $ username = username.strip() 
    if username == "": 
        $ username = "Yu Wen" 
    
    #Game start
    call neg1 

    return
