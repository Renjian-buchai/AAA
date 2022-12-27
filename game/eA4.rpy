label eA4: 
    $ renpy.block_rollback()
    u "Hmm..." 
    u "It's Saturday,{w=0.05} why?" 
    hide ina happy 
    show ina disdainful  
    a "Are you an idiot?" 
    u "No,{w=0.05} I'm actually at the top of my class." 
    a "What the fuck?!"  
    a "You know what I mean." 
    u "?" 
    u "Really?" 
    hide ina disdainful 
    show ina playful  
    a "It's C{w=0.15}-H{w=0.15}-R{w=0.15}-I{w=0.15}-S{w=0.15}-T{w=0.15}-M{w=0.15}-A{w=0.15}-S{w=0.15} E{w=0.15}-V{w=0.15}-E." 
    u "Can you speak English?" 
    u "Why're you just reciting the letters—" 
    u "Ohh,{w=0.05} Christmas Eve." 
    jump eA5 

label eA5: 
    u "And?" 
    hide ina playful 
    show ina confused  
    a "'And?'?" 
    u "How does that explain anything?" 
    hide ina confused 
    show ina smirk  
    a "You see..." 
    a "Ufufu~" 
    a "I'll give you the honour of going to the Christmas Market with you!" 
    "She definitely has an ulterior motive." 
    u "What's the {i}real{/i} reason you need me to come?" 
    jump eA6 

label eA6: 
    hide ina smirk 
    show ina sarcastic  
    a "Oh no,{w=0.05} you saw through me!" 
    "She spoke in an overly-exaggerated manner." 
    hide ina sarcastic 
    show ina happy  
    a "The Christmas market has a couple's discount,{w=0.05} so I need you to pretend to be my boyfriend." 
    u "{i}Sigh...{/i}" 
    u "Please.{w=0.1} What if they want us to prove it?" 
    hide ina happy 
    show ina confused  
    a "Then we just prove it." 
    hide ina confused 
    show ina disdainful  
    a "Even if they ask us to kiss each other as proof,"
    a "It's not like either of us haven't had our first kisses yet,{w=0.05} right?" 
    "Why's she looking at me like I'm the one who's brain damaged?" 
    u "Haha,{w=0.05} yeah,{w=0.05} right." 
    u "Regardless,{w=0.05} I won't go just because you say so. " 
    hide ina disdainful  
    show ina mischievous 
    a "Hehe,{w=0.05} too bad,{w=0.05} your mom already agreed to it." 
    u "What the fuck?!" 
    a "She asked you to make good use of the discount." 
    u "..." 
    u "{i}Sigh{/i}" 
    jump eA7 

label eA7: 
    u "So,{w=0.05} when and where do we meet up?" 
    hide ina disdainful  
    show ina flustered 
    a "Uhm...{w=0.1} Call me later." 
    a "I haven't thought of that." 
    u "Are you stupid?" 
    hide ina flustered 
    show ina smirk  
    a "No,{w=0.05} I'm actually at the top of the class." 
    "Did she really use my own retort against me?" 
    u "When do I call you?" 
    a "Around 5 p.m-ish?" 
    u "..." 
    u "Alright,{w=0.05} I'll call you at 17:00."  
    jump eA8 

label eA8: 
    scene bgblack with fade 
    stop music fadeout 5.0
    "Around 5 p.m." 
    scene bgbedroom with fade
    a "Hello,{w=0.05} who's this?" 
    u "It's me." 
    "Beep—{w=0.1} {p}She ended the call." 
    "What the hell?"
    "I dialled her number again." 
    a "Are you {i}really{/i} bored enough to call the same person twice?" 
    u "No,{w=0.05} it's me,{w=0.05} [u]." 
    a "Oh,{w=0.05} wait..." 
    a "Shit{w=0.05} I thought you were another 'it's me' scammer." 
    u "Weren't you the one who asked me to call you?" 
    a "Right!" 
    a "I forgot!"
    a "Erm... uhm..." 
    a "{size=20}Why's Baidu so slow all of a sudden?{/size}" 
    a "Ah,{w=0.05} we should meet up around Zhejiang Exhibition Hall." 
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
    "Dialling her phone number,{w=0.05} I gave her a call." 
    a "Hello?" 
    u "Where're you?" 
    a "Sorry,{w=0.05} I'm still on my way!" 
    u "Then,{w=0.05} where are you on your way?" 
    a "I'm... {w=.5}right behind you!" 
    scene bgzhejiangexhibitionhall with fade  
    "I turned around." 
    u "No,{w=0.05} you're not." 
    a "..." 
    u "What?" 
    a "You know,{w=0.05} sometimes,{w=0.05} you're an idiot." 
    u "And you're an idiot all the time." 
    a "{i}Sigh...{w=0.1}{/i} Anyways,{w=0.05} I've arrived." 
    u "Are you right behind me?" 
    "I felt a finger tap me on my shoulder." 
    scene bgzhejiangexhibitionhall with fade  
    show a happy peace with dissolve 
    a "Yep,{w=0.05} I am!" 
    "She makes a peace sign as she hangs up." 
    a "Are you surprised?" 
    u "Not at all." 
    a "Liar." 
    hide a happy peace 
    show a pout  
    "I was plenty surprised,{w=0.05} so..." 
    "Had it been showing on my face?" 

    menu: 
        "Fine,{w=0.05} I was surprised.": 
            call sA10 from _call_sA10 
        # TODO: BeA4; 
return 