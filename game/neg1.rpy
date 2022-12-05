label neg1: 
    play music [yam, "<silence 2.5>", tdc] volume 0.1 fadein 4 fadeout 4 loop 
    scene bgpc1 with dissolve
    "Finals Philosophy Essay" 
    scene bgpc2 with dissolve
    "{u}Topic:{w=0.5} Winter{/u}" 
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
    jump zero 

label zero: 
    "???" "Are you doing your philosophy bullshit again?" 
    "A pair of soft arms wrapped around my neck." 
    u "Ahh, WHAT THE FUCK?!" 
    scene bgbedroom with hpunch
    show ina happy with dissolve 
    "I screamed and turned around,{w=0.1} recognising the one standing behind me." 
    u "Why're you in my room?!" 

menu: 
    a "Your mom let me in."
    
    "You do know you're a girl,{w=0.1} right?": 
        call A1 from _call_A1 
    # TODO: B1, C1 
return 