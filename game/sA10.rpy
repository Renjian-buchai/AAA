label sA10: 
    hide a pout 
    show a smirk 
    a "Hehe,{w=0.05} I knew it." 
    "There was a radiant smile on her face." 
    "She's so pretty,{w=0.05} but her personality..." 
    u "{i}Sigh{/i},{w=0.05} what a shame." 
    hide a smirk 
    show a curious 
    a "What's a shame?" 
    a "The fact that I'm too good for you?" 
    u "No,{w=0.05} not at all." 
    u "You're not even my type." 
    hide a curious 
    show a happy 
    a "OK. Anyways,{w=0.05} the Christmas market..."
    u "Where's it?"
    a "It's a few blocks away." 
    u "Alright,{w=0.05} let's go." 
    jump sA11 
label sA11: 
    scene bgblack with fade 
    "We walked to where the Christmas market was held." 
    scene bgchristmasmarket with fade 
    hide a happy 
    show a incredulous 
    a "...{w=0.1}Crowded." 
    u "Yes,{w=0.05} it's very crowded." 
    "Few people celebrated Christmas in China,{w=0.05} and the 25th of December is still a working day." 
    "Thus,{w=0.05} we'd expected the market to be quite empty,{w=0.05} especially considering how it was still working hours." 
    "Yet,{w=0.05} the market was still full of shoppers." 
    a "I think we underestimated the pull of Christmas markets." 
    u "I think calling it {w=0.055}'underestimated'{w=0.055} is still an understatement." 
    a "Right." 
menu: 
    a "What should we do now?" 
    "I think we should get something to eat.": 
        call siA12 from _call_siA12  
    # TODO: BsA12, CsA12; 
return 