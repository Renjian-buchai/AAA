label start: 
    call Definitions
    call Dictionaries 
    $ A_name = _("Feng Qiuyue")
    python:  
        if persistent.username is None: 
            renpy.scene()
            renpy.show("bglogin")
            persistent.username = renpy.input("Login:{w=0.5}\nPlease insert username: {w=0.5}", length=10, copypaste=False)
            persistent.username = persistent.username.strip()
        if persistent.username in (None, ''):
            persistent.username = "Yu Wen"
        if persistent.username is not None:
            renpy.jump("label1")
label label1: 
    call neg1 from _call_neg1 
    return