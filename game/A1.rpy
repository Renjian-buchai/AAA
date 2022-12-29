label A1: 
    $ del val 
    $ renpy.block_rollback()
    u "You do know that you're a girl,{w=0.05} right?" 
    u "Also, you do know that I'm a guy,{w=0.05} right?" 
    a "Haha,{w=0.05} you don't say?" 
    a "Besides,{w=0.05} we're friends!" 
    hide ina happy  
    show ina smirk 
    a "You don't look at your {i}friend{/i} with {i}pervy eyes{/i},{w=0.05} correct?" 
    u "..." 
    "Now that I think of it..." 
    "How did she know I was doing philosophy?" 
    "Was I reading aloud as I typed?" 
    u "How did you know I was doing philosophy?" 
    hide ina smirk 
    show ina happy  
    a "It was{w=0.3} just~{w=0.3} a~{w=0.3} guess!" 
    "Her guesses are way too accurate." 
    "Then again,{w=0.05} it's not like I have anything else to do other than work." 
    jump A2 
label A2: 
    "[a] is my best female friend from university." 
    "She majors in acting and minors in literature,{w=0.05} while I major in philosophy and minor in maths." 
    "Our relationship used to be terrible,{w=0.05} because she kept insulting me unprovoked when I was doing work in the library." 
    "Speaking of which,{w=0.05} humans really are strange creatures." 
    "When they stay with something long enough,{w=0.05} they can even grow fond of a chihuahua,{w=0.05} not to mention a beauty like [a]." 
    "Wait,{w=0.05} I've digressed." 
    "My point was,{w=0.05} we became friends after we insulted each other for a long enough time." 
    jump A3 
label A3: 
    u "Why have you come here anyways?"
menu: 
    a "Hehe,{w=0.05} do you know what day it is?" 
    "It's Saturday.": 
        call eA4 from _call_eA4 
    # TODO: BA4 
return 