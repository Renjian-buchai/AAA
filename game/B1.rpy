label B1: 
    $ del val 
    $ renpy.block_rollback()
    scene bgbedroom 
    a "Hehe, isn't it good that your gorgeous friend came here out of nowhere?" 
    u "Narcissist." 
    jump B2 
    
label B2: 
    "This is [a], my best friend and a narcissist." 
    "She takes a different degree from me." 
    "I'm studying philosophy at University, minoring in maths whilst [a] studies acting, majoring in literature." 
    "We were initially something like enemies because she always made fun of me when I write essays in the library." 
    "After we insulted each other for a long enough time, we became friends." 
    "Even if she's a narcissist, she (shockingly) has the capital to brag, since she really is quite beautiful." 
    jump B3 

label B3: 
    hide ina happy 
    show ina sarcastic 
    a "If it's about being narcissistic, you're even worse than me." 
    u "Agreed." 
    "I'm bad at being a narcissist." 
    "[a] was caught off guard." 
    hide ina sarcastic 
    show ina suspicious 
    a "What're you even agreeing with?" 
    u "I'm bad at being a narcissist." 
    hide ina suspicious 
    show ina annoyed 
    a "Fuck off." 
    "When it comes to personality, I'm definitely the humble type." 
    "In fact, I'm so humble that perhaps even Obama would bow down to me when it came to humility." 
    "Really. I'm extremely humble." 
    hide ina annoyed 
    show ina pout 
    a "{i}Sigh{/i}, Why're you so taciturn? Cheer up!" 
    hide ina pout 
    show ina mischievous 
    a "What happened to {i}Ahh, what the fuck?! Why're you in my room?{/i}" 
    u "..." 
    "I had been panicking, so I accidentally shouted out my thoughts."
    "That was the exception, not the norm." 
    hide ina mischievous 
    show ina happy 
    a "Right, for why I came here, you should already know." 
    u "No I don't." 
    hide ina happy 
    show ina playful 
    a "Then, what day is it?" 
    jump B4 

label B4: 
    "I look at the calendar hanging on the wall." 
    u "It's Christmas Eve." 
    hide ina playful 
    show ina smirk 
    a "Hehe, and what's on Christmas Eve?" 
    u "Dunno." 
    "Was there some holiday I had forgotten about?" 
    "Or was there something bored people on SNS created?" 
    hide ina smirk 
    show ina pout 
    a "{i}Of course{/i}, you don't know." 
    a "{i}Sigh{/i} I really don't understand how you can live like this." 
    "The fuck is she even talking about?" 
    jump B5 

label B5: 
    u "..." 
    a "So silent..." 
    hide ina pout 
    show ina happy 

    menu: 
        a "Anyways, Christmas Market. Come with me." 
        "No.": 
            call AB6 from _call_AB6 
        #TODO: eB6; 
return 