label A1: 
    u "You do know that you're a girl,{w=0.1} right?" 
    u "Also, you do know that I'm a guy,{w=.1} right?" 
    a "Haha,{w=.1} you don't say?" 
    a "Besides,{w=.1} we're friends!" 
    hide a happy 
    show a smirk 
    a "You don't look at your {i}friend{/i} with {i}pervy eyes{/i},{w=.1} correct?" 
    u "..." 
    "Now that I think of it..." 
    "How did she know I was doing philosophy?" 
    "Was I reading aloud as I typed?" 
    u "How did you know I was doing philosophy?" 
    hide a smirk 
    show a happy 
    a "It was{w=1} just{w=1} a{w=1} guess!" 
    "Her guesses are way too accurate." 
    "Then again,{w=.1} it's not like I have anything else to do other than work." 
    jump A2 

label A2: 
    "[a] is my best female friend from university." 
    "She majors in music and minors in literature,{w=.1} while I major in philosophy and minor in maths." 
    "Our relationship used to be terrible,{w=.1} because she kept insulting me unprovoked when I was doing work in the library." 
    "Speaking of which,{w=.1} humans really are strange creatures." 
    "When they stay with something long enough,{w=.1} they can even grow fond of a chihuahua,{w=.1} not to mention a beauty like [a]." 
    "Wait,{w=.1} I've digressed." 
    "My point was,{w=.1} we became friends after we insulted each other for a long enough time." 
    jump A3 

label A3: 
    u "Why have you come here anyways?"
    
menu: 
    a "Hehe,{w=.1} do you know what day it is?" 
    
    "It's Saturday.": 
        call AA4 
    
return 