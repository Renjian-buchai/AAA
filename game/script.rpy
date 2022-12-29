label start: 
    call DD from _call_DD 
    $ A_name = _("Feng Qiuyue")

    python: 
        if persistent.username == None: 
            renpy.scene()
            renpy.show("bglogin")
            persistent.username = renpy.input("Login:{w=0.5}\nPlease insert username: {w=0.5}", length=10, copypaste=False)
            persistent.username = persistent.username.strip() 
        if persistent.username is None and not persistent.username is "" or persistent.username is '': 
            persistent.username = "Yu Wen" 
        if persistent.username != None: 
            renpy.jump("label1") 
    
    $ completioncheck() 
    
label label1: 
    call neg1 from _call_neg1 
    return