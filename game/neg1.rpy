label neg1: 
    
    play music ["./audio/You and Me.mp3", "<silence 2.5>", "./audio/10dC.mp3"] volume 0.1 fadein 4 fadeout 4 
    scene bgpc1 
    "Finals Philosophy Essay" 
    scene bgpc2 
    "{u}Topic:{w=0.5} Winter{/u}" 
    scene bgpc3 
    "Winter..." 
    scene bgpc4 
    "The most beautiful yet dangerous of the four seasons." 
    scene bgpc5 
    "The rich enjoy winter." 
    scene bgpc6 
    "The poor fear winter." 
    scene bgpc7 
    "How scary must the prospect of frostbite and starvation be for those who can't even afford to survive?" 
    scene bgpc8 
    "Maybe—" 
    jump zero 

label zero: 
    "???" "Are you doing your philosophy bullshit again?" 
    "A pair of soft arms wrapped around my neck." 
    u "Ahh, WHAT THE FUCK?!" 
    scene bgbedroom
    show a happy
    "I screamed and turned around,{w=0.1} recognising the one standing behind me." 
    u "Why're you in my room?!" 

menu: 
    a "Your mom let me in."
    
    "You do know you're a girl,{w=0.1} right?": 
        call A1 


return 