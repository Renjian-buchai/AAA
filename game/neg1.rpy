label neg1: 
    $ renpy.block_rollback()
    play music [yam, "<silence 2.5>", tdc] volume 0.1 fadein 4 fadeout 4 loop 
    scene bgpc1 with dissolve
    "Finals Philosophy Essay" 
    scene bgpc2 with dissolve
    "{u}Topic:{w=0.1} Winter{/u}" 
    scene bgpc3 with dissolve
    "Winter..." 
    scene bgpc4 with dissolve
    "The most beautiful yet dangerous of the four seasons." 
    scene bgpc5 with dissolve
    "The rich enjoy winter." 
    scene bgpc6 with dissolve
    "The poor fear winter." 
    scene bgpc7 with dissolve
    "How scary must the prospect of frostbite and starvation be for those who can't even afford to survive?" 
    scene bgpc8 with dissolve
    "Maybe—" 
    python: 
        boolean_values = [value for value in Persistent_paths.values()] 
        if all(boolean_values):
            Cpath = True
    jump zero 
label zero: 
    "???" "Are you doing your philosophy bullshit again?" 
    "A pair of soft arms wrapped around my neck." 
    u "Ahh,{w=0.05} WHAT THE FUCK?!" 
    scene bgbedroom with hpunch
    show ina happy  
    "I screamed and turned around,{w=0.05} recognising the one standing behind me." 
    u "Why're you in my room?!" 
    python: 
        if Cpath: 
            renpy.say(who=a, what="Your mom let me in.", interact=False) 
            val = result = renpy.display_menu([("You do know you're a girl, right?", "A1")\
            # , ("{i}Sigh{/i}", "B1"), ("Oh.", "C1")\
            ]) 
            renpy.call(val)
        else: 
            renpy.say(who=a, what="Your mom let me in.", interact=False) 
            val = result = renpy.display_menu([("You do know you're a girl, right?", "A1"), \
            # ("{i}Sigh{/i}", "B1")\
            ])   
            renpy.call(val)
            #TODO: C1 
return 