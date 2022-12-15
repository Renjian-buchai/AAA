label siA12: 
    scene bgchristmasmarket 
    hide a incredulous with dissolve
    show a happy with dissolve
    a "You just reminded me that I'm hungry." 
    a "Let's go!" 
    scene bgblack with fade 
    "We walk to the food district of the Christmas Market." 
    scene bgchristmasmarket with fade 
    u "What do you want to eat?" 
    hide a happy with dissolve
    show a confused with dissolve
    a "Hmm..." 
    a "Eggnog!"  
    u "I asked what you wanted to eat." 
    u "We can drink it later." 
    hide a confused with dissolve
    show a disappointed with dissolve
    a "Oh,{w=.1} then..." 
    hide a disappointed with dissolve
    show a happy with dissolve
    a "Log cake!" 
    u "Are you a pig?" 
    hide a happy with dissolve
    show a serious with dissolve
    "She looked at me and deadass said:" 
    a "No,{w=.1} I'm a human." 
    u "{i}Sigh{/i},{w=.1} We should've eaten something before coming here." 
    hide a serious with dissolve
    show a curious with dissolve
    a "What about you?{w=.3} What do you want to eat?" 
    "She just ignored my comment." 
    "Looking up and down the street,{w=.1} I heard three owner's calls." 
    hide a curious with dissolve
    show shkpra at left with dissolve
    "Shopkeeper A" "Roast beef sandwich,{w=.1} cheap and easy to eat!" 
    show shkprb with dissolve
    "Shopkeeper B" "Delicious mini toad-in-the-hole!{w=.3} If you share it with your crush before confessing,{w=.1} you'll definitely succeed!" 
    show shkprc at right with dissolve
    "Shopkeeper C" "Roasted spring chicken,{w=.1} roasted to perfection!{w=.3} You'll be losing out if you don't try it now!" 
menu: 
    a "(What about you? What do you want to eat?)" 
    "Roast beef sandwich.": 
        call wA13 from _call_wA13      
    "Mini Toad-in-the-hole.": 
        call BsiA13 from _call_BsiA13  
    "Roasted Spring Chicken.": 
        call CsiA13 from _call_CsiA13 
return 