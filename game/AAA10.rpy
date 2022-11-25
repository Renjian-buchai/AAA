label sA10: 
    hide a pout 
    show a smirk 
    a "Hehe,{w=.1} I knew it." 
    "There was a radiant smile on her face." 
    "She's so pretty,{w=.1} but her personality..." 
    u "{i}Sigh{/i},{w=.1} what a shame." 
    hide a smirk 
    show a curious 
    a "What's a shame?" 
    a "The fact that I'm too good for you?" 
    u "No,{w=.1} not at all." 
    u "You're not even my type." 
    hide a curious 
    show a happy 
    a "OK. Anyways,{w=.1} the Christmas market..."
    u "Where's it?"
    a "It's a few blocks away." 
    u "Alright,{w=.1} let's go." 
    jump sA11 

label sA11: 
    scene bgblack with fade 
    "We walked to where the Christmas market was held." 
    scene bgchristmasmarket with fade 
    hide a happy 
    show a incredulous 
    a "...{w=.3}Crowded." 
    u "Yes,{w=.1} it's very crowded." 
    "Few people celebrated Christmas in China,{w=.1} and the 25th of December is still a working day." 
    "Thus,{w=.1} we'd expected the market to be quite empty,{w=.1} especially considering how it was still working hours." 
    "Yet,{w=.1} the market was still full of shoppers." 
    a "I think we underestimated the pull of Christmas markets." 
    u "I think calling it {w=.15}'underestimated'{w=.15} is still an understatement." 
    a "Right." 

menu: 
    a "What should we do now?" 

    "I think we should get something to eat.": 
        call siA12  
return 