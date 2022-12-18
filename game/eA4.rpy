label eA4: 
    u "Hmm..." 
    u "It's Saturday,{w=.1} why?" 
    hide ina happy with dissolve
    show ina disdainful with dissolve 
    a "Are you an idiot?" 
    u "No,{w=.1} I'm actually at the top of my class." 
    a "What the fuck?!"  
    a "You know what I mean." 
    u "?" 
    u "Really?" 
    hide ina disdainful with dissolve
    show ina playful with dissolve 
    a "It's C{w=0.2}-H{w=0.2}-R{w=0.2}-I{w=0.2}-S{w=0.2}-T{w=0.2}-M{w=0.2}-A{w=0.2}-S{w=0.2} E{w=0.2}-V{w=0.2}-E." 
    u "Can you speak English?" 
    u "Why're you just reciting the letters—" 
    u "Ohh,{w=.1} Christmas Eve." 
    jump eA5 
label eA5: 
    u "And?" 
    hide ina playful with dissolve
    show ina confused with dissolve 
    a "'And?'?" 
    u "How does that explain anything?" 
    hide ina confused with dissolve
    show ina smirk with dissolve 
    a "You see..." 
    a "Ufufu~" 
    a "I'll give you the honour of going to the Christmas Market with you!" 
    "She definitely has an ulterior motive." 
    u "What's the {i}real{/i} reason you need me to come?" 
    jump eA6 
label eA6: 
    hide ina smirk with dissolve
    show ina sarcastic with dissolve 
    a "Oh no,{w=.1} you saw through me!" 
    "She spoke in an overly-exaggerated manner." 
    hide ina sarcastic with dissolve
    show ina happy with dissolve 
    a "The Christmas market has a couple's discount,{w=.1} so I need you to pretend to be my boyfriend." 
    u "{i}Sigh...{/i}" 
    u "Please.{w=.3} What if they want us to prove it?" 
    hide ina happy with dissolve
    show ina confused with dissolve 
    a "Then we just prove it." 
    hide ina confused with dissolve
    show ina disdainful with dissolve 
    a "Even if they ask us to kiss each other as proof,"
    a "It's not like either of us haven't had our first kisses yet,{w=.1} right?" 
    "Why's she looking at me like I'm the one who's brain damaged?" 
    u "Haha,{w=.1} yeah,{w=.1} right." 
    u "Regardless,{w=.1} I won't go just because you say so. " 
    hide ina disdainful with dissolve 
    show ina mischievous with dissolve
    a "Hehe,{w=.1} too bad,{w=.1} your mom already agreed to it." 
    u "What the fuck?!" 
    a "She asked you to make good use of the discount." 
    u "..." 
    u "{i}Sigh{/i}" 
    jump eA7 
label eA7: 
    u "So,{w=.1} when and where do we meet up?" 
    hide ina disdainful with dissolve 
    show ina flustered with dissolve
    a "Uhm...{w=.3} Call me later." 
    a "I haven't thought of that." 
    u "Are you stupid?" 
    hide ina flustered with dissolve
    show ina smirk with dissolve 
    a "No,{w=.1} I'm actually at the top of the class." 
    "Did she really use my own retort against me?" 
    u "When do I call you?" 
    a "Around 5 p.m-ish?" 
    u "..." 
    u "Alright,{w=.1} I'll call you at 17:00."  
    jump eA8 
label eA8: 
    scene bgblack with fade 
    stop music fadeout 5.0
    "Around 5 p.m." 
    scene bgbedroom with fade
    a "Hello,{w=.1} who's this?" 
    u "It's me." 
    "Beep—{w=.3} {p}She ended the call." 
    "What the hell?"
    "I dialled her number again." 
    a "Are you {i}really{/i} bored enough to call the same person twice?" 
    u "No,{w=.1} it's me,{w=.1} [u]." 
    a "Oh,{w=.1} wait..." 
    a "Shit{w=.1} I thought you were another 'it's me' scammer." 
    u "Weren't you the one who asked me to call you?" 
    a "Right!" 
    a "I forgot!"
    a "Erm... uhm..." 
    a "{size=20}Why's Baidu so slow all of a sudden?{/size}" 
    a "Ah,{w=.1} we should meet up around Zhejiang Exhibition Hall." 
    "She really forgot..." 
    "I'm speechless." 
    u "Around when?" 
    a "Ahh..." 
    a "Around 5:30...?" 
    u "No problem." 
    u "See you later."
    scene bgblack with fade 
    jump eA9 
label eA9: 
    scene bgzhejiangexhibitionhall with fade 
    play music [ttt, "<silence 5>", tot, "<silence 5>", sct, "<silence 5>", lgt, "<silence 5>", tdc, "<silence 5>", yam] volume 0.1 fadein 5 fadeout 5
    "I arrived outside Zhejiang Exhibition Hall." 
    "I couldn't see [a] anywhere." 
    "Dialling her phone number,{w=.1} I gave her a call." 
    a "Hello?" 
    u "Where're you?" 
    a "Sorry,{w=.1} I'm still on my way!" 
    u "Then,{w=.1} where are you on your way?" 
    a "I'm... {w=.5}right behind you!" 
    scene bgzhejiangexhibitionhall with fade  
    "I turned around." 
    u "No,{w=.1} you're not." 
    a "..." 
    u "What?" 
    a "You know,{w=.1} sometimes,{w=.1} you're an idiot." 
    u "And you're an idiot all the time." 
    a "{i}Sigh...{w=.3}{/i} Anyways,{w=.1} I've arrived." 
    u "Are you right behind me?" 
    "I felt a finger tap me on my shoulder." 
    scene bgzhejiangexhibitionhall with fade  
    show a happy peace with dissolve 
    a "Yep,{w=.1} I am!" 
    "She makes a peace sign as she hangs up." 
    a "Are you surprised?" 
    u "Not at all." 
    a "Liar." 
    hide a happy peace with dissolve
    show a pout with dissolve 
    "I was plenty surprised,{w=.1} so..." 
    "Had it been showing on my face?" 
menu: 
    "Fine,{w=.1} I was surprised.": 
        call sA10 from _call_sA10 
    # TODO: BeA4; 
return 