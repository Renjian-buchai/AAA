label BsiA13: 
    hide shkpra
    hide shkprb
    hide shkprc 
    scene bgchristmasmarket 
    u "I want to eat mini toad-in-the-hole."
    show a confused 
    a "Mini toad-in-the-hole? What a 'toad-in-the-hole'?" 
    u "It's just sausages in Yorkshire pudding batter,{w=.1} seasoned with onion gravy and vegetables." 
    a "That sounds...{w=.3}strange." 
    a "Is it good?" 
    u "Dunno,{w=.1} depends on the store." 
    hide a confused 
    show a excited 
    a "Alright,{w=.1} I'll try it!" 
    "We walked up to the store." 
    show shkprb 
    "Owner B" "Boy,{w=.1} girl,{w=.1} do you want mini toad-in-the-hole." 
    a "Yep." 
    u "...Well,{w=.1} what she said." 
    a "Yeay!" 
    "Owner B" "Are you dating?" 
    u "Yep." 
    hide a excited 
    show a happy peace 
    a "Yes!" 
    "Owner B" "Alright,{w=.1} then I'll give you a discount."
    hide a happy peace 
    show a confused 
    a "Don't you need proof?" 
    "Owner B" "Nah,{w=.1} just a part-time worker.{w=.3}Can't be bothered." 
    "I guess it doesn't matter where you work.{w=.3}As long as you're a part-time worker,{w=.1} you won't give a fuck about work." 
    hide a confused 
    show a disappointed 
    a "Oh,{w=.1} OK." 
    "She put on a disappointed act." 
    "Her act was realistic.{w=.3}Well,{w=.1} it {i}is{/i} her degree." 
    u "Alright,{w=.1} we want 2 of them." 
    "Each toad-in-the-hole was around 6-inches across,{w=.1} even though they were supposedly 'mini'." 
    "Part-timer" "74.8 RMB." 
    u "Expensive." 
    "Part-timer" "No,{w=.1} it's normal." 
    u "70 RMB." 
    "Part-timer" "I didn't record the price." 
    u "{i}Sigh,{w=.1}{/i} Fine." 
    hide a disappointed 
    show a happy 
    a "I love you honey!" 
    u "Same." 
    "The part-timer glared at us like,{w=.1} 'Go die,{w=.1} normies',{w=.1} then took out two mini toad-in-the-hole and two spoons." 
    "Part-timer" "Here.{w=.3}Now,{w=.1} fuck off." 
    hide a happy 
    show a mischievous 
    a "So mean." 
    u "Very mean." 
    "Part-timer" "Shut up,{w=.1} you normies." 
    jump BsiA14 

label BsiA14: 
    hide a mischievous 
    hide shkprb 
    scene bgblack with fade 
    "We sat down to a side with the toad-in-the-hole." 
    scene bgchristmasmarket with fade 
    show a happy 
    "[a] plucks a sausage out of the toad-in-the-hole,{w=.1} before bititng into it slowly." 
    a "{i}Ahh!{/i},{w=.1} the sausage screams as the monster eats it piece by piece." 
    u "Don't play with your food." 
    "If I did that at home,{w=.1} my parents would've beaten me half to death." 
    "In fact,{w=.1} they did beat me half to death when I was 4 years old." 
    hide a happy 
    show a annoyed  
    a "Shut up; unless you want me to break up with you." 
    u "..." 
    u "What's there to break up?" 
    hide a annoyed 
    show a mischievous 
    a "Our relationship." 
    a "Until the director says cut,{w=.1} we must continue our act." 
    a "That's the first thing I was taught." 
    u "Haha." 
    "There isn't a director here,{w=.1} for fuck's sake." 
    "Well,{w=.1} why don't I try..." 
    u "Cut." 
    hide a mischievous 
    show a disdainful 
    a "You're not the director." 
    u "Figured so." 
    u "Well,{w=.1} let's eat it quickly.{w=.3}The crowds will be fucking crazy when working time ends." 
    hide a disdainful 
    show a happy 
    a "A'ight!" 
    "We wolfed down the toad-in-the-hole." 
    "[a] only ate half of it before being full." 
    "I was forced to eat the rest of it." 
menu: 
    a "Well,{w=.1} where should we go now?"

    "We should go to the competition stage.": 
        call sxA15
    #TODO BwA15 
return 