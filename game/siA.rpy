label siA12: 
    $ renpy.block_rollback()
    scene bgchristmasmarket 
    hide a incredulous 
    show a happy 
    a "You just reminded me that I'm hungry." 
    a "Let's go!" 
    scene bgblack with fade 
    "We walk to the food district of the Christmas Market." 
    scene bgchristmasmarket with fade 
    u "What do you want to eat?" 
    hide a happy 
    show a confused 
    a "Hmm..." 
    a "Eggnog!"  
    u "I asked what you wanted to eat." 
    u "We can drink it later." 
    hide a confused 
    show a disappointed 
    a "Oh,{w=.05} then..." 
    hide a disappointed 
    show a happy 
    a "Log cake!" 
    u "Are you a pig?" 
    hide a happy 
    show a serious 
    "She looked at me and deadass said:" 
    a "No,{w=.05} I'm a human." 
    u "{i}Sigh{/i},{w=.05} We should've eaten something before coming here." 
    hide a serious 
    show a curious 
    a "What about you?{w=.1} What do you want to eat?" 
    "She just ignored my comment." 
    "Looking up and down the street,{w=.05} I heard three owner's calls." 
    scene bgchristmasmarket
    show shkpra at left 
    "Shopkeeper A" "Roast beef sandwich,{w=.05} cheap and easy to eat!" 
    show shkprb 
    "Shopkeeper B" "Delicious mini toad-in-the-hole!{w=.1} If you share it with your crush before confessing,{w=.05} you'll definitely succeed!" 
    show shkprc at right   
    "Shopkeeper C" "Roasted spring chicken,{w=.05} roasted to perfection!{w=.1} You'll be losing out if you don't try it now!" 

    menu: 
        a "(What about you? What do you want to eat?)" 
        "Roast beef sandwich.": 
            jump wA13 
        "Mini Toad-in-the-hole.": 
            jump BsiA13
        "Roasted Spring Chicken.": 
            jump CsiA13 
    

label wA13: 
    $ renpy.block_rollback()
    hide shkpra 
    hide shkprb 
    hide shkprc 
    scene bgchristmasmarket 
    u "I want to eat roast beef sandwich." 
    show a contemplative 
    a "Huh,{w=.05} that sounds great." 
    show a happy 
    a "I'll try it,{w=.05} too!"
    scene bgblack with fade 
    "We walk up to the stall."
    scene bgchristmasmarket with fade 
    show shkpra 
    "Shopkeeper A" "Hey,{w=.05} do you want to try some roast beef?{w=.1} I have some samples!" 
    "He reveals a plate with multiple pieces of roast beef impaled by toothpicks." 
    "Without hesitation,{w=.05} [a] picks one up and tries it." 
    hide a happy 
    show a excited 
    a "Wow,{w=.05} this is great." 
    a "Honey,{w=.05} I want to eat this." 
    u "..." 
    "I was completely thrown off-guard." 
    "I completely forgot about the bullshit with the couple's discount." 
    "Shopkeeper A" "You're dating?{w=.1} Then I'll give you a 10\% discount." 
    u "Alright,{w=.05} umm..." 
    u "Then,{w=.05} get me 4 pieces." 
    "Shopkeeper A" "A'ight,{w=.05} 28 RMB." 
    "The sale price of the sandwich is 30 RMB." 
    u "Do you think I can't do basic math?" 
    u "90\% of 30 is 27." 
    "Shopkeeper A" "Alright,{w=.05} I'll make a loss and sell it for 27." 
    "I'm speechless." 
    "How can anyone be so shameless?" 
    jump wA14 

label wA14: 
    scene bgchristmasmarket with fade 
    "We sat down by a side with food." 
    hide a excited 
    show a happy 
    a "Ahh,{w=.05} how warm!" 
    "She squeezed on the sandwich like it was a hand warmer." 
    u "..." 
    u "Just eat it." 
    hide a happy 
    show a sarcastic 
    a "Don't wanna,{w=.05} we ran out of hand warmers at home!" 
    u "So?" 
    hide a sarcastic 
    show a smirk 
    a "So,{w=.05} I'm cold!" 
    u "Then bear with it." 
    u "Oh,{w=.05} I almost forgot." 
    u "You owe me 13.5 RMB." 
    hide a smirk 
    show a confused 
    a "Huuh?{w=.1} Why?" 
    u "Because I bought the sandwich for you." 
    hide a confused 
    show a disdainful 
    a "Hmph,{w=.05} how stingy." 
    "She hands over one of her two sandwiches." 
    "To be more specific,{w=.05} the one she squished to leech the warmth off of." 
    a "Now,{w=.05} I owe you 6.75 RMB." 
    u "...{w=.1}Fine." 
    "I reluctantly accepted the sandwich." 
    hide a disdainful 
    show a happy 
    u "Can you really be full with just that?" 
    a "Of course." 
    "Sure enough,{w=.05} she seemed satisfied after eating that sandwich." 
    hide a happy 
    show a satisfied 
    "Her expression was cute." 
    a "Ahh,{w=.05} I'm so full!" 
    u "Nice." 
    hide a satisfied 
    show a excited 
    a "I'll buy a log cake!" 
    u "...{w=.1}Aren't you full?" 
    hide a excited 
    show a sarcastic 
    a "Haven't you heard that a girl has a second stomach for sweets?" 
    u "..." 
    "I gave up reasoning with her." 
    u "We can't really eat a log cake here,{w=.05} so it'd be better if you got something more portable." 
    hide a sarcastic 
    show a happy 
    a "Fine,{w=.05} I'll get an ice cream." 
    u "Ice cream?{w=.1} It's...{w=.1} winter...{w=.1} you know?" 
    a "It's exactly because it's winter that I'm eating ice cream!" 
    a "The ice cream won't melt so fast anymore." 
    u "..." 
    u "Whatever." 
    a "Come with me." 
    u "Why?" 
    hide a happy 
    show a disdainful 
    a "C{w=.1}-o{w=.1}-u{w=.1}-p{w=.1}-l{w=.1}-e{w=.1}'s{w=.1} d{w=.1}-i{w=.1}-s{w=.1}-c{w=.1}-o{w=.1}-u{w=.1}-n{w=.1}-t." 
    u "{i}Sigh.{/i}" 
    u "After I'm done with my sandwiches." 
    hide a disdainful 
    show a playful   
    a "OK." 
    a "..." 
    a "Right,{w=.05} no one asked us for proof when we bought the sandwiches." 
    a "Pft,{w=.05} you thought waayy too much about the couple's discount thing!" 
    hide a playful 
    show a mischievous 
    u "Whatever." 
    "Her laughter was annoying." 
    scene bgblack with fade 
    "I bought her ice cream later." 
    "Naturally,{w=.05} she had to return the cost of the ice cream to me later." 
    "I guess she completely forgot about eggnog." 
    scene bgchristmasmarket with fade 

    menu: 
        a "What're we going to do now?" 
        "We should go to the competition stage.": 
            jump sxA15 
        "We should go to the game district.": 
            jump BwA15 
    

label BsiA13: 
    $ renpy.block_rollback()
    hide shkpra 
    hide shkprb 
    hide shkprc 
    scene bgchristmasmarket 
    u "I want to eat mini toad-in-the-hole."
    show a confused 
    a "Mini toad-in-the-hole? What a 'toad-in-the-hole'?" 
    u "It's just sausages in Yorkshire pudding batter,{w=.05} seasoned with onion gravy and vegetables." 
    a "That sounds...{w=.1}strange." 
    a "Is it good?" 
    u "Dunno,{w=.05} depends on the store." 
    hide a confused 
    show a excited 
    a "Alright,{w=.05} I'll try it!" 
    "We walked up to the store." 
    show shkprbl at left 
    "Shopkeeper B" "Boy,{w=.05} girl,{w=.05} do you want mini toad-in-the-hole." 
    a "Yep." 
    u "...{w=.1}Well,{w=.05} what she said." 
    a "Yeay!" 
    "Shopkeeper B" "Are you dating?" 
    u "Yep." 
    hide a excited 
    show a happy peace 
    a "Yes!" 
    "Shopkeeper B" "Alright,{w=.05} then I'll give you a discount."
    hide a happy peace 
    show a confused 
    a "Don't you need proof?" 
    "Shopkeeper B" "Nah,{w=.05} just a part-time worker.{w=.1} Can't be bothered." 
    "I guess it doesn't matter where you work.{w=.1} As long as you're a part-time worker,{w=.05} you won't give a fuck about work." 
    hide a confused 
    show a disappointed 
    a "Oh,{w=.05} OK." 
    "She put on a disappointed act." 
    "Her act was realistic.{w=.1} Well,{w=.05} it {i}is{/i} her degree." 
    u "Alright,{w=.05} we want 2 of them." 
    "Each toad-in-the-hole was around 6-inches across,{w=.05} even though they were supposedly 'mini'." 
    "Part-timer" "74.8 RMB." 
    u "Expensive." 
    "Part-timer" "No,{w=.05} it's normal." 
    u "70 RMB." 
    "Part-timer" "I didn't set the price." 
    u "{i}Sigh,{w=.05}{/i} Fine." 
    hide a disappointed 
    show a happy 
    a "I love you honey!" 
    u "Same." 
    "The part-timer glared at us like,{w=.05} 'Go die,{w=.05} normies',{w=.05} then took out two mini toad-in-the-hole and two spoons." 
    "Part-timer" "Here.{w=.1} Now,{w=.05} fuck off." 
    hide a happy 
    show a mischievous 
    a "So mean." 
    u "Very mean." 
    "Part-timer" "Shut up,{w=.05} you normies." 
    jump BsiA14 

label BsiA14: 
    hide a mischievous 
    hide shkprb 
    scene bgblack with fade 
    "We sat down to a side with the toad-in-the-hole." 
    scene bgchristmasmarket with fade 
    show a happy 
    "[a] plucks a sausage out of the toad-in-the-hole,{w=.05} before biting into it slowly." 
    a "{i}Ahh!{/i},{w=.05} the sausage screams as the monster eats it piece by piece." 
    u "Don't play with your food." 
    "If I did that at home,{w=.05} my parents would've beaten me half to death." 
    "In fact,{w=.05} they did beat me half to death when I was 4 years old." 
    hide a happy 
    show a annoyed  
    a "Shut up; unless you want me to break up with you." 
    u "..." 
    u "What's there to break up?" 
    hide a annoyed 
    show a mischievous 
    a "Our relationship." 
    a "Until the director says cut,{w=.05} we must continue our act." 
    a "That's the first thing I was taught." 
    u "Haha." 
    "There isn't a director here,{w=.05} for fuck's sake." 
    "Well,{w=.05} why don't I try..." 
    u "Cut." 
    hide a mischievous 
    show a disdainful 
    a "You're not the director." 
    u "Figured so." 
    u "Well,{w=.05} let's eat it quickly.{w=.1} The crowds will be fucking crazy when working time ends." 
    hide a disdainful 
    show a happy 
    a "A'ight!" 
    "We wolfed down the toad-in-the-hole." 
    "[a] only ate half of it before being full." 
    "I was forced to eat the rest of it." 

    menu: 
        a "Well,{w=.05} where should we go now?"
        "We should go to the competition stage.": 
            jump sxA15 
        "We should go to the game district": 
            jump BwA15 
    

label CsiA13: 
    $ renpy.block_rollback()
    hide shkpra 
    hide shkprb 
    hide shkprc 
    u "I want to eat roasted spring chicken." 
    show a happy 
    a "Ah,{w=.05} OK." 
    a "I was thinking so,{w=.05} too." 
    u "Then why didn't you mention this earlier when I asked what you wanted?" 
    hide a happy 
    show a mischievous 
    a "Tehe." 
    u "...{w=.1}Don't 'Tehe' me." 
    hide a mischievous 
    show a smirk 
    a "..." 
    u "Let's go." 
    hide a smirk 
    show a happy 
    a "Alright." 
    show shkprcl at left 
    "Shopkeeper C" "D'you want'a eat some spring chick'n?" 
    "She spoke in the Sichuan dialect." 
    "I did not understand the Sichuan dialect." 
    "Fortunately,{w=.05} [a]'s hometown was Chengdu,{w=.05} so she understood and spoke it perfectly." 
    u "What did that mean?" 
    a "She said,{w=.05} 'Do you want to eat spring chicken?'."
    u "Tell her,{w=.05} 'Yes,{w=.05} 2 of them.'" 
    a "OK." 
    a "Ye'h,{w=.05} 2." 
    "Shopkeeper C" "A'ight,{w=.05} less get'cha couple o' spring chick'n." 
    u "Baidu translate,{w=.05} please help me translate." 
    a "He said,{w=.05} 'Alright,{w=.05} let's get you some spring chicken.'" 
    u "I asked for Baidu translate,{w=.05} not you." 
    hide a happy 
    show a smirk 
    a "Haha,{w=.05} fuck off." 
    "Shopkeeper C" "Thah's 21.60 RMB." 
    hide a smirk 
    show a happy 
    a "Weh're a cou'le." 
    u "What'd you just say?" 
    a "We're a couple."  
    "This is getting tedious." 
    "Shopkeeper C" "Yah,{w=.05} then I'll get'cha thi discount." 
    "Shopkeeper C" "19.45." 
    u "Alright."
    a "A'ight." 
    "This is {i}really{/i} getting tedious." 
    "The shopkeeper handed over two spring chickens after a slight delay." 
    hide a happy 
    hide shkprc 
    scene bgblack with fade 
    "I thanked her,{w=.05} then we went over to a side to eat." 
    jump CsiA14 

label CsiA14: 
    "We ate the spring chicken in silence." 
    scene bgchristmasmarket with fade 
    show a contemplative 
    "[a] seemed to be thinking about something." 
    u "What're you thinking about?" 
    hide a contemplative 
    show a smirk 
    a "Nothing." 
    u "Whenever a girl says nothing,{w=.05} she means something." 
    hide a smirk 
    show a annoyed 
    a "Alright,{w=.05} then treat me as a guy friend instead." 
    u "Alright." 
    hide a annoyed 
    show a contemplative 
    u "What're you thinking about?" 
    a "Nothing." 
    u "Lies." 
    hide a contemplative 
    show a angry 
    a "You said you'd treat me like a guy friend." 
    u "I was treating you like a guy friend." 
    a "Haha." 
    "She stabbed the stick that impaled her spring chicken at me." 
    "The half-eaten chicken fell off the stick when she stopped the stick just shy of it poking me." 
    hide a angry 
    show a shocked 
    a "Ah." 
    u "Oh." 
    u "Do you want mine?" 
    "I still had a good half of mine left." 
    hide a shocked 
    show a excited 
    a "Can I?"   
    u "If I wanted this little bit,{w=.05} I wouldn't bring it up anyways." 
    a "Then,{w=.05} alright!" 
    "She ate a bit of it from the opposite side from where I was eating from until she was full." 
    "I ate the rest of it,{w=.05} including the parts from which she ate from." 
    hide a excited 
    show a smirk 
    a "Isn't that an indirect kiss?" 
    u "Huh?" 
    "She said what was likely the most comic-book-esque comment." 
    u "Oh,{w=.05} just that?" 
    u "It doesn't matter,{w=.05} does it?" 
    u "Anyways,{w=.05} I swallowed the parts that you ate from." 
    u "If it were applied to the logic of kissing,{w=.05} it would be like I bit her lips off,{w=.05} then swallowed it." 
    hide a smirk 
    show a scared 
    "[a] shuddered." 
    a "Don't give me that imagery." 
    u "Haha,{w=.05} should we go somewhere else now?" 
    hide a scared 
    show a happy 
    a "Alright,{w=.05} then..." 

    menu: 
        a "Where do you want to go?" 
        "We should go to the competition stage.": 
            jump sxA15 
        "We should go to the game district.": 
            jump BwA15 
    

label BwA15: 
    $ renpy.block_rollback()
    scene bgblack with fade 
    hide a mischievous  
    "There was a game district in the market." 
    "We headed to the game district."
    scene bgchristmasmarket with fade 
    show a happy  
    a "What game do you want to play?" 
    u "No clue." 
    hide a happy  
    show a contemplative  
    a "I want to..." 
    "She looked up and down the district." 
    "Suddenly,{w=.05} she exclaimed." 
    hide a contemplative  
    show a excited  
    a "Is that a shiba inu plushie?" 
    "The sudden change it topic caught me off-guard." 
    u "Uhm...{w=.1} Yeah,{w=.05} why?" 
    a "I want it!" 
    u "..." 
    "Sounds troublesome,{w=.05} but it'll probably be fun." 
    hide a excited  
    scene bgblack with fade 
    "We walked up to the stall that had the shiba inu hung from its roof as a prize." 
    scene bggamestall with fade 
    show skpr at left  
    u "Erm...{w=.1} We want...{w=.1} 5 balls." 
    "Shopkeeper" "Oh,{w=.05} OK." 
    "Shopkeeper" "Are you a couple?" 
    show a excited  
    a "Yes!" 
    u "Yep." 
    "The shopkeeper smirks." 
    "Shopkeeper" "Show me proof." 
    u "Huh..." 
    hide a excited 
    hide skpr 
    scene bgblack with fade 
    $ renpy.music.set_pause(True, channel="music")
    "I was about to refuse when I felt a soft feeling on my cheek." 
    "Time seemed to pause." 
    $ renpy.music.set_pause(False, channel="music") 
    scene bggamestall with fade 
    show a flustered  
    "I glared at her,{w=.05} my face hot." 
    "[a] smiled back sheepishly,{w=.05} a slight blush tinting her cheek." 
    "She seemed happy,{w=.05} although it might've just been an act." 
    "Her degree ultimately {i}was{/i} acting." 
    show skpr at left  
    "The store owner covered his mouth as he chuckled." 
    "Shopkeeper" "I was just kidding..." 
    "Shopkeeper" "But damn,{w=.05} boy,{w=.05} you really snagged a good girlfriend,{w=.05} 233." 
    hide a flustered  
    show a happy  
    u "Oh." 
    "I want to die." 
    "I want to bury myself in a hole and never come out for the rest of my life!" 
    "Shopkeeper" "Here,{w=.05} take the balls." 
    "He handed over 5 balls." 
    "Shopkeeper" "That'll be 23.5 RMB,{w=.05} after discount...Pft!" 
    "He was unable to keep his laughter in." 
    hide a happy  
    show a excited   
    "Shopkeeper" "You should look in the mirror,{w=.05} your face is so damn red!" 
    u "Shaddup." 
    hide a excited  
    show a mischievous  
    a "Haha,{w=.05} that's what's cute about him." 
    u "Cute my ass!" 
    "Shopkeeper" "Shut up,{w=.05} you normie!" 
    a "Haha." 
    "I feel offended..." 
    hide a mischievous  
    show a excited  
    a "How do we split the balls?" 
    u "You're better than me at sports,{w=.05} so you should take 3 of them." 
    "Playing games is troublesome." 
    "Might as well give it to someone else who likes games." 
    "Also,{w=.05} it's true that she's better than me,{w=.05} a homebody,{w=.05} in terms of sports." 
    a "No,{w=.05} the one who's worse at sports should get more tries." 
    u "But the one who's better at sports would win more points with more opportunities." 
    hide a excited  
    hide skpr  
    scene bgblack with fade 
    "We argued back and forth for a minute." 
    "As a student of philosophy,{w=.05} I was naturally great at arguing." 
    "In the end,{w=.05} I got my way.{w=.1} She gets 3 balls while I get 2 balls." 
    scene bggamestall with fade 
    show a excited  
    a "Alright~{w=.1} Shiba inu,{w=.05} I'm coming for ya~!" 
    "On a table in the centre of the stall,{w=.05} there were a few moving targets to be knocked down." 
    "Each target had a number written on it,{w=.05} representing the number of points received per target." 
    "Points could be exchanged with rewards." 
    "The shiba inu was worth 500 points."
    hide a excited  
    scene bgblack with fade 
    "[a] threw a ball at the target." 
    "It hit a 100-pointer." 
    "[a] threw another ball at another target." 
    "She knocked it down,{w=.05} getting us 200 points." 
    "[a] threw {i}another{/i} ball at {i}another{/i} target." 
    "She missed,{w=.05} but the ball bounced and knocked down another target worth 100 points." 
    "She doesn't have any balls left." 
    scene bggamestall with fade 
    show a disappointed  
    a "Haih,{w=.05} how sad..." 
    a "It's your turn." 
    show skpr at left  
    "Shopkeeper" "Go on,{w=.05} impress your girlfriend." 
    hide a disappointed  
    show a flustered  
    "Both of us blushed." 
    jump BwA16 

label BwA16: 
    "Ignoring the shopkeeper's uproarious laughter,{w=.05} I went up to the line behind which I was to stand."
    hide a flustered  
    hide skpr  
    $ score0 = 400 
    python: 
        randoma = randint(0, 1) 
        randomb = randint(0, 3)

    menu: 
        "Which target should I aim for?" 
        "100 point": 
            if randoma == 1: 
                $ score0 = score0 + 100 
                $ randoma = 0 
                jump gametw 
            else: 
                $ randoma = 0 
                jump gametsx 
        "200 point": 
            if randomb == 3: 
                $ score0 = score0 + 200 
                $ randomb = 0 
                jump gametq 
            else: 
                $ randomb = 0 
                jump gametb
    

label gametw: 
    $ renpy.block_rollback()
    "I knocked down the 100 point target." 
    "Our current score is [score0]." 
    jump gametj 
    

label gametsx: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score0]." 
    jump gametj 
    

label gametq: 
    $ renpy.block_rollback()
    "I knocked down the 200 point target." 
    "Our current score is [score0]." 
    jump gametj 
    

label gametb: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score0]." 
    jump gametj 
    

label gametj:
    $ renpy.block_rollback()
    python: 
        randoma = randint(0,1)
        randomb = randint(0,3) 

    menu: 
        "Which target should I aim for?" 
        "100 point": 
            if randoma == 1: 
                $ score0 = score0 + 100 
                $ randoma = 0 
                jump gameet
            else: 
                $ randoma = 0 
                jump gameety 
        "200 point": 
            if randomb == 3: 
                $ score0 = score0 + 200 
                $ randomb = 0 
                jump gameete 
            else: 
                $ randomb = 0 
                jump gameets
    

label gameet: 
    $ renpy.block_rollback()
    "I knocked down the 100 point target." 
    "Our current score is [score0]." 
    jump gameetsi
    

label gameety: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score0]." 
    jump gameetsi 
    

label gameete: 
    $ renpy.block_rollback()
    "I knocked down the 200 point target." 
    "Our current score is [score0]." 
    jump gameetsi 
    

label gameets: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score0]." 
    jump gameetsi 
    

label gameetsi: 
    $ renpy.block_rollback()
    if score0 == 800: 
        jump WBwA17 
    elif score0 >= 500: 
        jump XBwA17 
    else: 
        jump LBwA17 
    

label WBwA17: 
    $ renpy.block_rollback()
    scene bgblack with fade 
    pause 1.0 
    scene bggamestall with fade 
    show skpr at left  
    "The owner whistles seeing my aim." 
    "Shopkeeper" "Damn,{w=.05} both of your aim are cracked." 
    u "She plays overwatch; her aim {i}has{/i} to be good." 
    show a annoyed  
    a "Shut up." 
    "Shopkeeper" "Fuck you,{w=.05} overwatch player." 
    hide a annoyed  
    show a angry  
    "[a] glared at me." 
    a "You didn't have to say that." 
    u "Sorry,{w=.05} a CS:GO player like me can't understand having to be ashamed of doing what I like." 
    hide a angry  
    show a annoyed  
    a "Shut up." 
    u "Haha." 
    u "Well,{w=.05} we'll get the shiba inu plushie." 
    "Shopkeeper" "A'ight,{w=.05} I'll bring it down." 
    hide a annoyed  
    hide skpr  
    scene bgblack with fade 
    "He hoisted down the plushie before passing it over to me." 
    scene bggamestall with fade 
    "Shopkeeper" "Here's it." 
    u "Alright,{w=.05} thanks." 
    "I handed the plushie over to [a]." 
    show asi happy 
    a "Thanks!" 
    u "You're welcome." 
    a "No,{w=.05} really,{w=.05} thank you." 
    u "What the fuck?" 
    "I still can't understand women even after speaking to her for almost a year." 
    "She's already thanked me once,{w=.05} hadn't she?" 
    u "Anyways,{w=.05} bye." 
    "Shopkeeper" "Bye." 
    hide asi happy  
    hide skpr  
    scene bgblack with fade 
    "We walked away from the stall." 
    scene bgchristmasmarket with fade 
    u "Where should we go now?" 
    a "I don't know." 
    u "Isn't there a competition going on at the competition stage?" 
    "I remember seeing it on a flyer on the way to the exhibition hall." 
    a "Huh?{w=.1} That sounds interesting." 
    a "Let's go!" 
    jump BwA18

label XBwA17: 
    $ renpy.block_rollback()
    scene bgblack with fade 
    pause 1.0 
    scene bggamestall with fade 
    show skpr at left  
    show a smirk  
    "Shopkeeper" "Your aim's great,{w=.05} boy." 
    u "Haha,{w=.05} I want the shiba inu plushie." 
    a "Hehe,{w=.05} your aim's better than I remember." 
    u "Shut up." 
    u "It has always been this good." 
    u "I was just playing the pig to eat the tiger." 
    "That was a lie." 
    "It was just luck." 
    hide a smirk  
    show a disdainful  
    a "No,{w=.05} you weren't." 
    a "Remember during our university's sports day,{w=.05} you were a part of the baseball team,{w=.05} and when you pitched,{w=.05} it became a homerun even before the batter hit the ball." 
    u "Fuck,{w=.05} I just gave the other team a ball three times." 
    "That is,{w=.05} I missed the strike zone thrice." 
    hide a disdainful  
    show a confused  
    a "What does that even mean?" 
    "It was apparent that she didn't know the rules of baseball." 
    "The shopkeeper laughed at our childish display,{w=.05} handing over the shiba inu plushie that he hoisted down." 
    hide a confused  
    show a happy  
    "[a] received it,{w=.05} then hugged it tightly." 
    u "Alright,{w=.05} bye!" 
    a "Bye!" 
    "The shopkeeper did not respond,{w=.05} just waving back." 
    hide skpr  
    hide asi happy  
    scene bgblack with fade 
    "We left the game district." 
    scene bgchristmasmarket with fade 
    show asi happy  
    u "Where do we go now?" 
    a "Isn't there a competition going on at the competition stage?" 
    a "Why don't we go check it out?" 
    u "Alright." 
    scene bgblack with fade 
    jump BwA18

label BwA18:
    "There was a competition stage situated in the heart of the Christmas market." 
    "Arriving at the competition stage,{w=.05}  we suddenly realised that the area was quite empty." 
    scene bgstage with fade 
    u "I think that we're too late." 
    show asi confused  
    a "Huh?" 
    "I had noticed a sign posted on the stage." 
    "\'Gift Wrapping competition concluded early as all prizes have been distributed.\'" 
    hide asi confused  
    show asi disappointed  
    a "Aww..." 
    a "The competition really sounded fun." 
    u "Not really." 
    "It actually,{w=.05}  it sounds {i}really{/i} lame." 
    a "I'm actually great at gift wrapping." 
    u "That's the {i}real{/i} reason you find it fun,{w=.05}  huh." 
    hide asi disappointed  
    show asi smirk  
    a "Of course.{w=.1} If I can't win,{w=.05}  what's the point?" 
    u "How competitive." 
    hide asi smirk  
    show asi happy  
    a "Well...{w=.1} then,{w=.05}  what should we do now?" 
    u "Dunno." 
    "I noticed an empty bench near the stage." 
    u "Why don't we sit there at the bench?" 
    hide asi happy  
    show asi confused  
    a "Why?{w=.1} It's not like I sprained my ankle while walking in sandals." 
    u "Who wears sandals in this weather?" 
    u "Regardless,{w=.05}  you watch too many shows; you're thinking too deeply." 
    hide asi confused  
    show asi smirk  
    a "Why?" 
    a "Anime is fun to watch!" 
    u "Hehe." 
    a "What does that \'Hehe\' mean?" 
    hide asi smirk  
    show asi annoyed  
    a "Are you judging me?" 
    u "No,{w=.05}  of course not.{w=.1} I,{w=.05}  too,{w=.05}  watch anime occasionally." 
    a "Then you have no grounds to judge me." 
    u "Didn't I just say that I wasn't judging you?" 
    a "Oh,{w=.05}  right." 
    hide asi annoyed  
    show asi awkward  
    "The conversation up and died right there." 
    "I really can't understand girls' thoughts."
    "How awkward..." 
    jump BwA19 

label BwA19: 
    "We both sat at the bench in an awkward silence." 
    a "There's a fireworks festival later." 
    u "Oh,{w=.05}  I guess?" 
    u "There's nothing to pay for during some fireworks,{w=.05}  right?" 
    u "So,{w=.05}  can I go home?" 
    hide asi awkward  
    show asi playful  
    "[a] laughed." 
    a "Of course not,{w=.05}  you dumbass." 
    u "Huh?{w=.1} But I need to do my holiday project." 
    hide asi playful  
    show asi sarcastic  
    a "Do you really not want a life?" 
    u "Of course not." 
    a "Do you not want to not have a life,{w=.05}  or do you not want a life?" 
    u "I don't want a life." 
    a "You idiot." 
    hide asi sarcastic  
    show asi annoyed  
    "She hit me in the shoulder playfully." 
    "I really want to go home." 
    hide asi annoyed  
    show asi contemplative 
    "The earlier incident aside,{w=.05}  we sat in silence." 
    a "Remember the first time we met?" 
    u "The first time we met..." 
    "The first time we met was at the university's library last year during the summer hols." 
    hide asi contemplative  
    "Being the time of year that it was,{w=.05}  it was mostly empty." 
    scene bgblack with fade 
    "At the time,{w=.05}  [a] suddenly came up to me while I was reading for research purposes and writing an essay on the side." 
    jump BwA20 

label BwA20: 
    scene bglibrary with fade 
    show ina curious 
    a "What're you doing here?" 
    u "Is there anything that says I can't be here?" 
    u "I could return the question to you,{w=.05}  if so." 
    a "Hmm...{w=.1} Good point." 
    "She sat down opposite me." 
    a "What're you reading?"  
    "I lifted up my book to reveal the cover." 
    "{i}The laws of thought{/i},{w=.05}  by George Boole"
    hide ina curious  
    show ina disdainful  
    a "Ew,{w=.05}  philosophy." 
    u "Huh?" 
    u "Is that how you speak to everyone?" 
    "How rude." 
    hide ina disdainful  
    show ina mischievous  
    a "No,{w=.05}  but you're a philosophy student." 
    "Then,{w=.05}  could it be because she doesn't like humanities students?" 
    "She's pretty,{w=.05}  but I never thought that she was a STEM student." 
    "Why would she be in an arts university if so,{w=.05}  though?" 
    u "I'm also a math student,{w=.05}  so..." 
    hide ina mischievous  
    show ina disdainful  
    a "Eww." 
    "I can't understand what she's thinking." 
    u "What?" 
    a "Math is philosophy,{w=.05}  right?" 
    u "More or less,{w=.05}  but why do you hate philosophy students?" 
    hide ina disdainful  
    show ina sarcastic  
    a "I mean,{w=.05}  if you're going to think about goodness or justice or knowledge,{w=.05}  why don't you become a scientist or sociologist to learn more concrete facts?" 
    u "Don't compare me to those bastard axiologists,{w=.05}  metaphysists and epistemologists." 
    u "I'm learning logic." 
    hide ina sarcastic  
    show ina curious  
    a "There are branches to philosophy?" 
    u "Of course." 
    hide ina curious  
    show ina disdainful  
    a "Either way,{w=.05}  logicians can't be good anyways." 
    a "You'll probably preach to me about good arguments and whatnot." 
    u "Huh..." 
    "This conversation's getting tiresome." 
    hide ina disdainful  
    show ina annoyed  
    a "Har?!{w=.1} You picking a fight?" 
    u "No,{w=.05}  I'm not picking a fight." 
    u "Either way,{w=.05}  I can't understand how you got a challenge declaration from my 'huh'." 
    hide ina annoyed  
    show ina disdainful  
    a "You can't understand because you're an idiot for studying philosophy." 
    u "Well,{w=.05}  then,{w=.05}  what do {i}you{/i} study?" 
    hide ina disdainful  
    show ina playful  
    a "Acting,{w=.05}  a much better degree than yours." 
    u "Oh,{w=.05}  so you're a narcissist." 
    hide ina playful  
    show ina angry  
    a "What did'ya just say?!" 
    hide ina angry  
    "Needless to mention,{w=.05} we started off on the wrong foot." 
    scene bgblack with fade 
    "Since then,{w=.05}  she would come to the library every day just to insult me." 
    "I wasted my entire summer holidays because I couldn't study due to our diss wars." 
    jump BwA21

label BwA21: 
    scene bgstage with fade 
    u "Of course I remember." 
    show asi smirk  
    a "Haha,{w=.05}  do you remember how you called me every time we met?" 
    u "..." 
    u "Nope." 
    "I remember clearly." 
    "It was \'Supporting Cast\'." 
    "She got heated every time I called her that,{w=.05}  and would constantly bug me to change it." 
    "Since she hated that form of address,{w=.05}  it was only natural that I would continue to call her that." 
    hide asi smirk  
    show asi sarcastic  
    a "Haha." 
    "She doesn't seem to believe me." 
    hide asi sarcastic  
    show asi mischievous  
    a "Is it so~?" 
    "She {i}definitely{/i} doesn't believe me." 
    u "Hehe." 
    u "So,{w=.05}  what's your point?" 
    hide asi mischievous  
    show asi contemplative  
    a "You know..." 
    a "We got quite close after insulting each other for a long time,{w=.05}  right?" 
    u "You don't say?" 
    u "Who'd have thought that we would now be going on (platonic) Christmas dates?" 
    hide asi contemplative  
    show asi flustered  
    "[a] blushed." 
    a "Stop it." 
    u "You don't like me calling it that?" 
    a "Not really..." 
    u "Oh." 
    "Silence once again." 
    a "You know,{w=.05}  I—"
    jump BwA22

label BwA22: 
    "She was interrupted by an announcement." 
    "Announcement" "The fireworks show is starting.{w=.1} Please do not approach the competition stage." 
    hide asi flustered  
    show asi annoyed  
    "[a] looked frustrated,{w=.05}  but that was soon replaced by awe as a glowing trail snaked into the air."
    hide asi annoyed  
    show asi excited 
    scene bgfireworks with fade 
    $ renpy.music.set_volume(0.5, delay=0.3)
    a "Beautiful." 
    u "Yes,{w=.05}  very beautiful." 
    "I was just responding randomly because I was wondering what she was planning to say just now." 
    "My eyes didn't leave her face even as I spoke,{w=.05}  something that [a] seemed to vaguely notice." 
    hide asi excited 
    show asi flustered 
    "Coloured slightly red,{w=.05}  [a] turned to face me." 
    "She took a deep breath." 
    a "You know,{w=.05}  I really l-like you.{w=.1} Could you be my..." 
    "Her voice trailed off." 
    "She averted her gaze in embarrassment,{w=.05}  staring at the competition stage." 
    "I got the gist of her words." 
    "Taking a deep breath,{w=.05}  too,{w=.05}  I started." 
    u "I—"
    hide asi flustered 
    scene bgblack with fade 
    show disableskip
    $ renpy.movie_cutscene("mvcutscene.webm", delay=3, loops=0, stop_music=True)
    scene bgmov45 
    pause 5
    scene bgblack with fade 
    pause 10 
    jump BwA23 

label BwA23: 
    "During the Christmas festival,{w=.05}  there was an accident." 
    "During the fireworks festival,{w=.05}  a multi-shot firework abruptly tilted to the reaction force of the fireworks." 
    "The resulting explosion caused the death of three workers and a woman who was sitting at a nearby park bench." 
    "The man who was with the deceased woman was permanently blinded in his right eye by the chemicals emitted." 
    "Based on eyewitness accounts,{w=.05}  18-year-old [a] was first to notice the firework's tilt,{w=.05}  prompting her to jump in front of 18-year-old [u],{w=.05}  saving his life at the sacrifice of hers." 
    "I listened to the news broadcasted on Christmas as I looked for [a]'s gravestone." 
    "Due to my injuries,{w=.05}  I was unable to attend [a]'s funeral." 
    "On the day of my discharge,{w=.05}  I directly headed to H City Xiaoshan Cemetery." 
    "Finally seeing the gravestone planted in the middle-class grave,{w=.05}  my vision grew blurry." 
    "To the one who I never realised I loved until it was too late," 
    "goodbye." 
    $ end('BwA23')

label LBwA17: 
    scene bgblack with fade 
    pause 1.0 
    scene bggamestall with fade 
    show a disappointed  
    a "Well,{w=.05} what did I even expect from you?" 
    u "Probably more than what I could actually achieve." 
    a "That's for sure." 
    a "Haha." 
    show skpr at left  
    "Shopkeeper" "Then...{w=.1} What do you want to redeem?" 
    u "Erm...{w=.1} Let's put that on hold." 
    u "I want another ball."
    "Shopkeeper" "Alright." 
    "He passes a ball to me after I paid for it." 
    hide a disappointed  
    show a happy  
    "I tossed the ball to [a]." 
    u "You're much better than me,{w=.05} so you should throw it." 
    hide a happy  
    show a disdainful  
    "[a] scoffs." 
    a "How pathetic~" 
    u "Shut it." 
    hide a disdainful  
    hide skpr  
    scene bgblack with fade 
    "She threw the ball with quite some strength,{w=.05} knocking down a 200-point target." 
    scene bggamestall with fade 
    show a mischievous  
    a "You can feel free to worship me." 
    u "No,{w=.05} I won't." 
    hide a mischievous  
    show a smirk  
    a "Haha,{w=.05} then so be it." 
    a "I want the shiba inu doll." 
    scene bgblack with fade 
    "The shopkeeper hoisted down the plushie and passed it to [a]." 
    scene bggamestall with fade 
    hide a smirk  
    show asi smirk  
    show skpr at left  
    a "Then,{w=.05} bye!" 
    "Shopkeeper" "Bye!" 
    hide skpr  
    hide asi smirk  
    scene bgblack with fade 
    "We walked away from the stall." 
    scene bgchristmasmarket with fade 
    u "Where do we go now?" 
    show asi excited  
    a "There's a competition going on at the stage,{w=.05} right?{w=.1} "
    u "I would assume so." 
    u "That's what the market's website says." 
    a "Sounds interesting!"
    a "Let's go!" 
    scene bgblack with fade 
    jump LBwA18 

label LBwA18: 
    "The competition stage,{w=.05} situated in the heart of the Christmas Market,{w=.05} was bustling as many people crowded around the stage." 
    scene bgstage with fade 
    "Emcee" "Does anyone want to try?{w=.1} We only have 3 prizes left." 
    show Emcee at left  
    "Noticing a poster nearby,{w=.05} I commented," 
    u "Oh,{w=.05} it seems to be a gift-wrapping competition." 
    show asi happy  
    a "Really?{w=.1} That's interesting." 
    "No,{w=.05} it isn't." 
    hide asi happy  
    show asi smirk  
    a "You look like you're thinking that it's lame." 
    u "..." 
    "How did she know?" 
    u "Since you already know about my thoughts,{w=.05} care to explain why it's wrong?"
    hide asi smirk  
    show asi excited  
    a "Haha,{w=.05} it's obviously because I'm good at gift-wrapping." 
    a "My parents used to force me to wrap presents for everyone." 
    a "So to get back to watching anime quickly,{w=.05} I learnt to wrap presents quickly." 
    u "You're just excited about winning,{w=.05} huh?" 
    hide asi excited  
    show asi disdainful  
    a "Of course!" 
    u "...I understand,{w=.05} you'd rather cry on a BMW than smile on a bike." 
    hide asi disdainful  
    show asi annoyed  
    a "Who're you calling a gold-digger?" 
    a "How do you even know that reference?{w=.1} I thought that you only watched anime." 
    u "Are you retarded?{w=.1} Do you think that I was like 3 when the phrase became viral?" 
    hide asi annoyed  
    show asi excited  
    a "...Anyways,{w=.05} let's join the competition now!" 
    hide asi excited  
    hide Emcee  
    scene bgstage with fade 
    "She pulled me along as she jumped onto the stage." 
    show Emcee at left
    "Emcee" "We have two more participants here!" 
    "Why did {i}she{/i} have to drag {i}me{/i} into this?" 
    "[a] seemed to notice my misgivings." 
    show asi smirk  
    a "Don't worry about it." 
    a "Pfft,{w=.05} we can't get out of it anyways." 
    u "That's exactly what I'm worrying about." 
    "Emcee" "Wow,{w=.05} such a lively couple we have here." 
    u "..." 
    "Emcee" "Why don't you introduce yourself?" 
    hide asi smirk  
    show asi excited  
    "He held up a mic up to [a]'s face first." 
    a "Hii~{w=.1} I'm [a],{w=.05} a student at China University of Fine Arts!" 
    u "And I'm her boyfriend." 
    a "Hey,{w=.05} introduce yourself." 
    u "I'm her boyfriend." 
    hide asi excited  
    show asi annoyed  
    a "No,{w=.05} I mean...{w=.1} Your name!" 
    u "My name is her boyfriend." 
    hide asi annoyed  
    show asi sarcastic  
    a "I give up.{w=.1} Mr.{w=.1} Emcee,{w=.05} can we continue?" 
    "Emcee" "Haha,{w=.05} how boisterous! Let's explain the rules!" 
    "Emcee" "You are to wrap the present with the materials provided." 
    "Emcee" "You'll get a reward if you're in the top 10." 
    "Emcee" "The current tenth place has a time of 25.8 seconds,{w=.05} whilst the record stands at 20.3 seconds." 
    "I looked at the leaderboard." 
    "The top ten fastest gift wrappers would get vouchers." 
    "The top three gift wrappers would get vouchers and a medal." 
    "The champion vouchers and a 'secret gift',{w=.05} whatever that was." 
    hide asi sarcastic  
    show asi excited  
    a "Wow,{w=.05} so fast! I might even have to concentrate for this!" 
    "Her sarcastic comment drew amused chuckles from the audience." 
    u "Oh." 
    "My dull reply drew no interest from anyone else." 
    "Emcee" "Well,{w=.05} then,{w=.05} miss [a] and her boyfriend,{w=.05} will you go to your respective stations to prepare?" 
    a "OK!" 
    u "Oh." 
    "We sat at a table placed on the stage,{w=.05} and prepared to wrap the gift." 
    jump LBwA19

label LBwA19: 
    hide asi excited with fade 
    hide Emcee with fade 
    scene bgstage with fade 
    "When the emcee announced 'start',{w=.05} I begun unwrapping." 
    $ T0 = perf_counter() 

label game_n1: 
    $ renpy.block_rollback()

    menu: 
        "What should I do now?" 
        "Wrap present": 
            "I tore out some wrapping paper." 
            "I taped the wrapping paper to the present." 
            "I folded the wrapping paper to encase the present." 
            "I taped the wrapping paper closed." 
            $ renpy.pause(1.0, hard=True)
            jump game_0 
        "Tie ribbon": 
            "I took out a ribbon." 
            "I set it aside." 
            $ renpy.pause(1.0, hard=True)
            jump game_1 
        "Submit present": 
            "That doesn't sound quite right..." 
            $ renpy.pause(1.0, hard=True)
            jump game_n1 

label game_0: 
    $ renpy.block_rollback()

    menu: 
        "What should I do now?" 
        "Tie ribbon": 
            "I took out a ribbon." 
            "I taped the ribbon to the present." 
            "I tied the ribbon tightly."  
            $ renpy.pause(1.0, hard=True)
            jump game_2
        "Submit present": 
            "That doesn't sound quite right..." 
            $ renpy.pause(1.0, hard=True)
            jump game_0 

label game_1: 
    $ renpy.block_rollback()

    menu: 
        "What should I do now?" 
        "Wrap present": 
            "I tore out some wrapping paper." 
            "I taped the wrapping paper to the present." 
            "I folded the wrapping paper to encase the present." 
            "I taped the wrapping paper closed." 
            $ renpy.pause(1.0, hard=True)
            jump game_3
        "Submit present": 
            "That doesn't sound quite right..." 
            $ renpy.pause(1.0, hard=True)
            jump game_1 

label game_3: 
    $ renpy.block_rollback()

    menu: 
        "What should I do now?" 
        "Tie ribbon": 
            "I taped the ribbon to the present." 
            "I tied the ribbon tightly." 
            $ renpy.pause(1.0, hard=True)
            jump game_4 
        "Submit present": 
            "That doesn't sound quite right..." 
            $ renpy.pause(1.0, hard=True)
            jump game_3 

label game_2: 
    $ renpy.block_rollback()

    menu: 
        "What should I do now?" 
        "Submit present": 
            $ renpy.pause(1.0, hard=True)
            jump LBwA20g 

label game_4: 
    $ renpy.block_rollback()

    menu: 
        "What should I do now?" 
        "Submit present": 
            $ renpy.pause(1.0, hard=True)
            jump LBwA20g 

label LBwA20g: 
    $ renpy.block_rollback()
    python: 
        T1 = perf_counter() 
        T = (T1 - T0) * 4.0
    if T < 20.3: 
        $ Reward = "a voucher and a keychain" 
        $ Position = "1st" 
        jump LBwA20 
    elif T < 22.5: 
        $ Reward = "a voucher and a medal"
        $ Position = "3rd" 
        jump LBwA20
    elif T < 25.8: 
        $ Reward = "a voucher" 
        $ Position = "5th" 
        jump LBwA20
    else: 
        $ Reward = "nothing" 
        $ Position = "23rd" 
        jump LBwA20 

label LBwA20: 
    $ renpy.block_rollback()
    scene bgblack with fade 
    "After the competition,{w=.05} we collected our winnings." 
    "I received [Reward]."
    "[a] managed to eke out second place,{w=.05} qualifying herself for a voucher and a gold medal." 
    "It's quite amusing,{w=.05} since she received gold for as a runner up." 
    "That makes TMD a lot of sense." 
    scene bgchristmasmarket with fade 
    u "Can I go home now?" 
    show asi pout  
    a "What?{w=.1} Am I really {i}that{/i} annoying to be with?" 
    u "More or less." 
    u "Also,{w=.05} there's no place like home." 
    hide asi pout  
    show asi disdainful  
    a "Isn't that from {i}The Wizard of Oz{/i}?{w=.1} You know,{w=.05} I take literature as my minor." 
    u "Are you an idiot?" 
    u "It's just a quote." 
    hide asi disdainful  
    show asi mischievous  
    a "Whatever." 
    a "You can't go home." 
    u "{font=SIMSUN.ttf}囧{/font}" 
    hide asi mischievous  
    show asi playful  
    a "Why're you making that face?" 
    a "Who leaves their 'girlfriend' on their own on a date?" 
    u "Me,{w=.05} that's who." 
    hide asi playful  
    show asi annoyed  
    a "Dumbass." 
    a "Please~?" 
    u "Don't act cute." 
    u "The weather forecast says it's about to rain,{w=.05} so we should probably go back." 
    hide asi annoyed  
    show asi disappointed  
    a "Huh?{w=.1} How sad..." 
    jump LBwA21 

label LBwA21: 
    "[a] also checked the weather." 
    hide asi disappointed  
    show asi smirk  
    a "It's not going to rain! It's already at -2 Celsius!" 
    u "Well,{w=.05} it could be freezing rain." 
    "The weather this week was unusually cold,{w=.05} considering it was still in December." 
    "Perhaps it was just a cold snap." 
    u "Either way,{w=.05} you don't want to get cold,{w=.05} right?" 
    hide asi smirk  
    show asi disappointed  
    u "You still have the whole winter hols ahead." 
    a "Huh...{w=.1} But the Christmas market will close after tomorrow..." 
    u "Then we can come back tomorrow before it closes." 
    a "Alright..." 
    "Reluctantly,{w=.05} she decided to leave." 
    hide asi disappointed  
    show asi pout  
    a "But there's a fireworks festival later!" 
    u "There is?{w=.1} But it might be cancelled if it rains later." 
    hide asi pout  
    show asi disdainful  
    a "Hmph,{w=.05} there doesn't even seem to be clouds in the sky." 
    u "The sky's pitch black.{w=.1} How can you see any clouds?" 
    u "And anyways,{w=.05} we've already made the decision.{w=.1} There's no point in questioning your previous decision." 
    u "There'll probably be a fireworks festival tomorrow,{w=.05} too." 
    hide asi disdainful  
    show asi disappointed  
    a "Hmph,{w=.05} cold hearted." 
    u "What the fuck?" 
    u "If you're going to do this,{w=.05} so be it." 
    u "If you were a number,{w=.05} you would be 250." 
    hide asi disappointed  
    show asi annoyed  
    a "Who're you calling half-crazy?" 
    u "Haha." 
    a "Don't just laugh it off!" 
    hide asi annoyed  
    show asi contemplative  
    a "When did 250 come to represent half-crazy,{w=.05} though?" 
    u "If I recall correctly,{w=.05} it came from imperial China." 
    u "Then,{w=.05} banks would denote 500 taels of silver as a 'feng'." 
    u "So,{w=.05} 250 taels of silver would be half a 'feng'." 
    u "Since 'feng' is also the pronunciation of 'crazy',{w=.05} 250 can also be said as half-crazy." 
    a "Never knew that." 
    u "Because you never studied." 
    hide asi contemplative  
    show asi annoyed  
    a "Are you retarded?{w=.1} Of course I've studied!" 
    a "I'm at the top of my class!" 
    u "Top of what class?" 
    a "Acting." 
    u "How study intensive." 
    hide asi annoyed  
    show asi sarcastic  
    a "Yes,{w=.05} it's very study intensive..." 
    u "It's sarcasm,{w=.05} you idiot." 
    hide asi sarcastic  
    show asi smirk  
    a "You're correct,{w=.05} you're an idiot." 
    "She used my own insult against me." 
    "Normally,{w=.05} I would casually say 'you're right,{w=.05} you're a <insult>' when someone calls me an '<insult>'." 
    "Usually,{w=.05} they would reply,{w=.05} 'I know',{w=.05} before realising what they agreed to." 
    "With such meaningless conversation,{w=.05} we made our way back home." 
    hide asi smirk  
    scene bgblack  
    jump LBwA22 

label LBwA22: 
    "I walked [a] back home,{w=.05} before returning home myself." 
    "It was fortunate that we left early,{w=.05} because just as I was about to arrive back home,{w=.05} the first snowflakes begun to fall." 
    "Obviously,{w=.05} I rushed back into my house,{w=.05} then hid under my blanket to warm myself." 
    scene bgbedroom with fade 
    "Soon,{w=.05} I received a call from [a]." 
    a "It's snowing!" 
    u "Yes,{w=.05} it's snowing." 
    "What else am I supposed to say?" 
    "Deny that it's snowing?" 
    a "Do you want to build a snowman?" 
    u "Nope." 
    a "How cruel,{w=.05} abandoning me like that after toying with me for the whole day." 
    u "Shut up." 
    u "Well,{w=.05} at least we left early,{w=.05} so we could go home just in time." 
    a "What do you mean?{w=.1} After I came back,{w=.05} it was like half-an-hour before it started snowing." 
    u "{i}I{/i} made it back just in time." 
    a "You don't matter." 
    u "..." 
    "I'm speechless." 
    u "Well,{w=.05} anyways,{w=.05} goodbye." 
    a "Bye bye!" 
    "I hung up." 
    scene bgblack with fade 
    "That night,{w=.05} I slept terribly." 
    $ renpy.pause(2.0, hard=True) 
    jump LBwA23 

label LBwA23: 
    "25th December." 
    "I was woken up by a phone call." 
    scene bgbedroom with fade 
    "With tired eyes,{w=.05} I looked  at the Caller ID." 
    u "[a]! What do you think you're doing?" 
    a "I'm calling you." 
    u "Fuck,{w=.05} do you know what time it is?" 
    a "It's 6:03 A.M." 
    u "Do you think you're Sakuta Azusagawa?" 
    u "Why did you even call me?" 
    a "Because the news was played at 6:00." 
    u "But I don't watch the news." 
    "Newspaper superiority." 
    a "But I do!" 
    u "What does that have to do with me,{w=.05} then?" 
    a "You don't matter." 
    "Fucking—" 
    "Whatever,{w=.05} I won't argue with a retard." 
    a "Anyways,{w=.05} the fireworks at the Christmas markets exploded last night,{w=.05} right after we left." 
    u "You see,{w=.05} it was the correct choice to leave." 
    "How lucky..." 
    a "Hmph,{w=.05} but still..." 
    a "Now,{w=.05} the Christmas market was cancelled..." 
    u "Then that's just that." 
    a "How heartless..." 
    a "Anyways,{w=.05} now that you know about it,{w=.05} bye~" 
    u "Erm...{w=.1} then," 
    "Goodbye." 
    $ end('LBwA23')

label sxA15: 
    scene bgblack with fade 
    hide a mischievous  
    "In the heart of the Christmas Market,{w=.05} there was a competition stage." 
    scene bgstage with fade 
    show a happy   
    "On the competition stage was held a gift-wrapping competition." 
    show mc
    "Emcee" "Alright!{w=.1} Is there anyone else who wants to come up?!" 
    "Emcee" "The current record is 20.3 seconds by Mister Lu Hua!" 
    hide mc 
    hide a happy 
    show a shocked 
    a "Wow,{w=.05} so fast!" 
    u "..." 
    "To be honest,{w=.05} I wasn't very interested." 
    "According to a screen by the side of the stage,{w=.05} the top ten fastest gift wrappers would get vouchers." 
    "The top three would get vouchers and a medal." 
    "The champion gets vouchers and a 'secret gift',{w=.05} whatever that was." 
    "The tenth place had a time of 25.8 seconds." 
    hide a shocked 
    show a excited 
    a "Why don't we participate?" 
    u "I don't really want to,{w=.05} though." 
    a "...{w=.1}Alright,{w=.05} then." 
    hide a excited 
    show a excited   
    "She walks up onto the stage." 
    show mc at left 
    "Emcee" "We have a new competitor!" 
    "Emcee" "What's your name,{w=.05} little miss?" 
    hide a excited 
    show a happy   
    a "Hehe,{w=.05} hi,{w=.05} I'm [a]." 
    a "I'm honoured to come to a competition like this!" 
    "Emcee" "Alright,{w=.05} let's start." 
    "Emcee" "Do you know what you need to do in this competition?" 
    a "We wrap a present,{w=.05} right?" 
    "There was a sound of laughter." 
    "Emcee" "Of course we must wrap a present!" 
    "Emcee" "You must wrap that box over there with the wrapping paper and tape provided." 
    scene bgblack with fade 
    "[a] walked to the table where the tape and wrapping paper lay." 
    scene bgstage with fade 
    "Emcee" "Are you ready?!" 
    hide a happy 
    show a excited   
    a "Yes!" 
    "Emcee" "Then you may start in 3...{w=1} 2...{w=1} 1...{w=1} you may start now!" 
    scene bgblack with fade 
    "[a] hastily attempts to wrap the tape."
    "She manages to completely wrap the present in 22.6 seconds." 
    scene bgstage with fade 
    "Emcee" "Aww,{w=.05} such a shame.{w=.1} You couldn't beat Mr. Lu's record." 
    "Emcee" "But now,{w=.05} you're the new 6th place!" 
    "Emcee" "So...{w=.1} You get a 150 RMB voucher at XX bookstore!" 
    hide a excited 
    show a happy   
    a "Yay!" 
    jump sxA16 

label sxA16: 
    hide mc 
    scene bgchristmasmarket with fade 
    "[a] jumps off the competition stage,{w=.05} walking up to me." 
    hide a happy 
    show a happy 
    a "Did you see?" 
    u "See what?" 
    hide a happy 
    show a annoyed 
    "She knocked me lightly on my head." 
    a "I wrapped it in 22.6 seconds." 
    u "I know." 
    a "Hmph." 
    "What the hell's wrong with her?" 
    "She seemed to be in a bad mood." 
    "But her bad mood didn't last for very long." 
    hide a annoyed 
    show a mischievous 
    a "Isn't there a game district?{w=.1} Let's go." 
    u "Alright." 
    scene bgblack with fade 
    jump sxA17 

label sxA17: 
    scene bggamestall with fade 
    hide a mischievous 
    show a playful 
    "There was a game district in the market." 
    "We headed to the game district." 
    a "What game do you want to play?" 
    u "No clue.{w=.1} What do you want?" 
    a "I want to play...{w=.1} Oh,{w=.05} a shiba inu plushie..." 
    hide a playful 
    show a excited 
    a "I want it!" 
    u "Oh,{w=.05} OK." 
    "We went to the stall that hung up the shiba inu toy." 
    show skpr at left 
    hide a excited 
    show a excited   
    "Shopkeeper" "Do you want to play?" 
    a "Yup!" 
    "Shopkeeper" "Then,{w=.05} how many balls do you want?" 
    a "How many do you think we need to win it?" 
    u "Dunno.{w=.1} Maybe 5 for now." 
    "Shopkeeper" "Then,{w=.05} that'll be 25 RMB." 
    u "Oh." 
    "Shopkeeper" "Are you a couple?" 
    u "Yes..." 
    "I'm still not used to calling [a] my girlfriend." 
    "Not that we're a couple,{w=.05} anyways." 
    "The shopkeeper seemed unconvinced." 
    "Shopkeeper" "Then,{w=.05} prove it." 
    a "Uhm..{w=.1} Alright." 
    scene bgblack with fade 
    "I felt a soft feeling on my cheek." 
    $ renpy.music.set_pause(True, channel="music") 
    "The world seemed to stop." 
    "After a moment,{w=.05} I finally understood what happened." 
    $ renpy.music.set_pause(False, channel="music") 
    "Flushing red,{w=.05} I glared at her." 
    scene bggamestall with fade
    hide a excited 
    show a flustered   
    "Her face was entirely red." 
    "The store owner guffawed." 
    "Shopkeeper" "I was just kidding." 
    u "Oh." 
    "Then why didn't you say that before she kissed me?" 
    "Then again,{w=.05} she acted so quickly that it was unreasonable to expect him to react on time." 
    "The owner handed over 2.5 RMB along with 6 balls." 
    "Shopkeeper" "One free for putting on such a good show." 
    "We both reddened after being reminded of the incident." 
    a "Oh..." 
    u "Uhm...{w=.1} shall we...{w=.1} try to win the shiba inu?" 
    a "Alright..." 
    a "Three and three,{w=.05} right?" 
    a "The balls,{w=.05} I mean." 
    u "That's fine." 
    hide a flustered 
    show a excited   
    a "Alright,{w=.05} shiba inu,{w=.05} I'm coming for you!" 
    "On a table in the centre of the stall were a few moving targets to be knocked down." 
    "Each target had a number written on it,{w=.05} representing the number of points received per target." 
    "Points could be exchanged for rewards." 
    "The shiba inu was worth 500 points." 
    hide a excited 
    hide skpr 
    scene bgblack with fade 
    "[a] threw a ball at a target." 
    scene bggamestall with fade 
    "It missed." 
    scene bgblack with fade 
    "She threw another ball at the same target." 
    scene bggamestall with fade 
    "She knocked it down,{w=.05} gaining 100 points." 
    scene bgblack with fade 
    "[a] threw another ball at another target." 
    scene bggamestall with fade 
    "She was fortunate,{w=.05} and barely managed to knock down a 200-point target." 
    show a depressed   
    show skpr at left 
    a "Haih,{w=.05} how sad." 
    a "It's your turn." 
    "Shopkeeper" "Go on,{w=.05} impress your girlfriend." 
    hide a depressed 
    show a flustered   
    "Both [a] and I blushed." 
    jump sxA18 

label sxA18: 
    "Ignoring the store owner's uproarious laughter,{w=.05} I went up to the line behind which I had to stand." 
    hide a flustered 
    hide skpr 
    scene bggamestall  
    $ score = 300

    python: 
        randoma = randint(0, 1) 
        randomb = randint(0, 3)

    menu: 
        "Which target should I aim for?" 
        "100 point": 
            if randoma == 1: 
                $ score = score + 100 
                $ randoma = 0 
                jump gamez 
            else: 
                $ randoma = 0 
                jump game 
        "200 point": 
            if randomb == 3: 
                $ score = score + 200 
                $ randomb = 0 
                jump gamee 
            else: 
                $ randomb = 0 
                jump games 

label gamez: 
    $ renpy.block_rollback()
    "I knocked down the 100 point target." 
    "Our current score is [score]." 
    jump gamesi 

label game: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score]." 
    jump gamesi 

label gamee: 
    $ renpy.block_rollback()
    "I knocked down the 200 point target." 
    "Our current score is [score]." 
    jump gamesi 

label games: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score]." 
    jump gamesi 

label gamesi: 
    $ renpy.block_rollback()

    python: 
        randoma = randint(0, 1) 
        randomb = randint(0, 3)

    menu: 
        "Which target should I aim for?" 
        "100 point": 
            if randoma == 1: 
                $ score = score + 100 
                $ randoma = 0 
                jump gamew 
            else: 
                $ randoma = 0 
                jump gamesx 
        "200 point": 
            if randomb == 3: 
                $ score = score + 200 
                $ randomb = 0 
                jump gameq 
            else: 
                $ randomb = 0 
                jump gameb 

label gamew: 
    $ renpy.block_rollback()
    "I knocked down the 100 point target." 
    "Our current score is [score]." 
    jump gamej 

label gamesx: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score]." 
    jump gamej 

label gameq: 
    $ renpy.block_rollback()
    "I knocked down the 200 point target." 
    "Our current score is [score]." 
    jump gamej 

label gameb: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score]." 
    jump gamej 

label gamej: 
    $ renpy.block_rollback()

    python: 
        randoma = randint(0, 1) 
        randomb = randint(0, 3)

    menu: 
        "Which target should I aim for?" 
        "100 point": 
            if randoma == 1: 
                $ score = score + 100 
                $ randoma = 0 
                jump gamet
            else: 
                $ randoma = 0 
                jump gamety 
        "200 point": 
            if randomb == 3: 
                $ score = score + 200 
                $ randomb = 0 
                jump gamete 
            else: 
                $ randomb = 0 
                jump gamets 

label gamet: 
    $ renpy.block_rollback()
    "I knocked down the 100 point target." 
    "Our current score is [score]." 
    jump gametsi

label gamety: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score]." 
    jump gametsi 

label gamete: 
    $ renpy.block_rollback()
    "I knocked down the 200 point target." 
    "Our current score is [score]." 
    jump gametsi 

label gamets: 
    $ renpy.block_rollback()
    "I missed." 
    "Our current score is [score]." 
    jump gametsi 

label gametsi: 
    $ renpy.block_rollback()
    if score >= 800: 
        jump WsxA19 
    elif score >= 500: 
        jump XsxA19  
    else: 
        jump LsxA19  

label WsxA19: 
    $ renpy.block_rollback()
    scene bggamestall  
    show skpr at left 
    "Shopkeeper" "Fuck,{w=.05} you're a great shot,{w=.05} boy!" 
    u "Haha,{w=.05} can I exchange my points for the shiba inu?" 
    "Shopkeeper" "Alright,{w=.05} no problem." 
    "He hoisted down the shiba inu toy,{w=.05} handing it over to me." 
    "The shiba inu plushie was very soft." 
    "Without another word,{w=.05} I handed the plushie to [a]." 
    show asi happy 
    a "Hehe,{w=.05} thanks!" 
    u "No problem." 
    "Shopkeeper" "What other things do you want?" 
    "Shopkeeper" "You still have some points left." 
    u "Don't want anything." 
    "I wasn't interested in anything else in the stall." 
    "Shopkeeper" "Hah,{w=.05} then so be it." 
    u "Haha." 
    a "Bye!" 
    hide asi happy 
    hide skpr 
    scene bgblack with fade 
    "We left." 
    "It's late,{w=.05} so I want to go home..." 
    scene bgchristmasmarket with fade 
    show asi happy 
    u "Should we leave now?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.05} there's still a fireworks show." 
    u "Oh,{w=.05} OK." 
    hide asi disdainful 
    show asi happy 
    u "..." 
    u "There's no couple's discount during the fireworks show,{w=.05} so I can go home first,{w=.05} right?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.05} of course not!" 
    u "{i}Sigh,{w=.05}{/i} Alright." 
    hide asi disdainful  
    show asi happy 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh,{w=.05} alright." 
    scene bgblack with fade 
    "We strolled around the market,{w=.05} looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    scene bgchristmasmarket with fade 
    u "Oh,{w=.05} OK." 
    jump sxA20

label XsxA19: 
    $ renpy.block_rollback()
    scene bggamestall  
    show skpr at left 
    "Shopkeeper" "You did great,{w=.05} boy." 
    u "Hehe,{w=.05} I want to exchange it for a shiba inu doll." 
    "Shopkeeper" "A'ight,{w=.05} getting it now." 
    "He down the shiba inu toy,{w=.05} handing it over to me." 
    "Without another word,{w=.05} I handed the shiba inu toy to A." 
    show asi happy   
    a "Hehe,{w=.05} thanks!" 
    u "You're welcome." 
    u "Well,{w=.05} then,{w=.05} bye." 
    "Shopkeeper" "Bye." 
    scene bgblack with fade 
    hide asi happy 
    hide  skpr 
    "We left" 
    "It's late,{w=.05} so I want to go home." 
    scene bgchristmasmarket with fade 
    show asi happy 
    u "Should we go home now?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.05} there's still a fireworks show." 
    u "Oh,{w=.05} OK." 
    hide asi disdainful 
    show asi happy 
    u "There's no couple's discount during the fireworks show,{w=.05} so I can go home first,{w=.05} right?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.05} of course not!" 
    u "{i}Sigh,{w=.05}{/i} Alright." 
    hide asi disdainful 
    show asi happy 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh,{w=.05} alright." 
    scene bgblack with fade 
    "We strolled around the market,{w=.05} looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    scene bgchristmasmarketpark with fade 
    u "Oh,{w=.05} OK." 
    jump sxA20

label LsxA19: 
    $ renpy.block_rollback()
    scene bggamestall  
    show skpr at left 
    "Shopkeeper" "Well,{w=.05} that's a shame." 
    "[a] shook her head in disappointment." 
    u "{i}Sigh,{w=.05}{/i} Three more balls,{w=.05} please." 
    "Shopkeeper" "Alright." 
    hide skpr 
    scene bgblack with fade 
    "I played the game until we got 500 points." 
    "It somehow took me 7 more balls." 
    "{b}Fuck.{/b}" 
    show skpr at left 
    scene bggamestall with fade 
    "The shopkeeper exasperatedly took down the plushie,{w=.05} handing it over to me." 
    "I passed it over to [a]." 
    show asi apologetic 
    a "Thanks..." 
    u "No problem." 
    a "I'll pay you back." 
    u "No need." 
    scene bgblack with fade 
    "We walked away from the booth." 
    "It's late,{w=.05} so I want to go home." 
    hide asi apologetic 
    show asi happy 
    scene bgchristmasmarket with fade 
    u "Should we go home now?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.05} there's still a fireworks show." 
    u "Oh,{w=.05} OK." 
    hide asi disdainful 
    show asi happy 
    u "There's no couple's discount during the fireworks show,{w=.05} so I can go home first,{w=.05} right?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.05} of course not!" 
    u "{i}Sigh,{w=.05}{/i} Alright." 
    hide asi disdainful 
    show asi happy 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh,{w=.05} alright." 
    scene bgblack with fade 
    hide asi happy 
    "We strolled around the market,{w=.05} looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    scene bgchristmasmarketpark with fade 
    u "Oh,{w=.05} OK." 
    jump sxA20 

label sxA20: 
    scene bgparkbench with fade 
    stop music fadeout 2 
    "We sat at a bench in the park." 
    "It was much quieter compared to the bustle of the Christmas market." 
    play music [m1, "<silence 5>", m3, "<silence 5>", st, "<silence 5>", lgt, "<silence 5>", tdc, "<silence 5>", m2, "<silence 5>", ctd] volume 0.05 fadein 5 fadeout 5
    show asi excited 
    a "Right,{w=.05} eggnog!" 
    "Her sudden exclamation shocked me." 
    u "Oh...{w=.1} you finally remembered?" 
    "She really is an airhead." 
    hide asi excited 
    show asi apologetic 
    a "Yep,{w=.05} can you help me buy it?" 
    a "Please?" 
    u "What about the couple's discount?" 
    hide asi apologetic 
    show asi smirk 
    a "Lazy.{w=.1} Also,{w=.05} I can't buy anything while holding doge." 
    "Doge was probably the name she gave to the plushie." 
    u "Alright..." 
    hide asi smirk 
    scene bgblack with fade 
    "I reluctantly returned to the food section,{w=.05} bought two cups of eggnog,{w=.05} then headed towards the park." 
    "There seemed to be some kind of ruckus in the park." 
    jump sxA21 

label sxA21: 
    "I quickened my footsteps while trying not to spill the eggnog." 
    scene bgparkbench with fade 
    "At the bench was [a] and another man." 
    show ahole at left
    show asi annoyed 
    "Man" "Why don't you come along with me?" 
    a "No,{w=.05} don't want to." 
    "Man" "Why not? Are you on a date?" 
    "Man" "Why don't you dump him and come with me?" 
    a "I'm not on a date." 
    "She seemed to be very annoyed." 
    "Man" "Then there's no problem,{w=.05} right?" 
    hide asi annoyed 
    show asi angry 
    a "There's definitely a problem,{w=.05} and that's that I don't want to go with you." 
    "Man" "Why not?" 
    "Man" "Come on,{w=.05} I'll show you something much better than your friend can." 
    "The man grabbed onto her arm,{w=.05} pulling her with some strength." 
    hide asi angry  
    show asi scared 
    a "Stop! Erm...{w=.1} Uhm...{w=.1} Help!" 
    "How amusing;{w=.2} she was so flustered she forgot how to say 'help'." 
    "Wait,{w=.05} that's not the point here." 
    "Finally,{w=.05} I have grounds to claim self-defence." 
    u "A'ight,{w=.05} that's enough." 
    "Since his attention was completely on [a],{w=.05} his back was completely open." 
    scene bgparkbench with hpunch 
    "I kicked him diagonally in the ass,{w=.05} so that he fell onto the bench,{w=.05} then dumped a cup of piping hot eggnog onto his face." 
    "Man" "What the fuck—{w=.1} Fuck you!" 
    "I held onto [a]'s hand,{w=.05} poured the other cup of eggnog onto his crotch (Since I can't run while holding it anyways),{w=.05} then ran away,{w=.05} pulling [a] along." 
    hide asi scared 
    show asi relieved 
    a "Finally,{w=.05} you acted." 
    "She probably saw me while I was waiting for an excuse to kick him." 
    u "Sorry,{w=.05} the eggnog..." 
    hide asi relieved 
    show asi happy 
    a "No need,{w=.05} at least I still have doge." 
    u "..." 
    u "Well,{w=.05} let's go somewhere with more people." 
    hide asi happy 
    show asi excited 
    a "Haha!" 
    u "Why're you laughing?" 
    a "Well,{w=.05} it's fun." 
    "My face turned gloomy." 
    u "Then I want to see whatever you don't think is fun." 
    u "It must be like...{w=.1} hell,{w=.05} or something." 
    a "Hehe!" 
    hide asi excited 
    scene bgblack with fade 
    "We returned to the game district,{w=.05} which was the closest area to us." 
    scene bgchristmasmarket with fade 
    show asi happy 
    a "The fireworks show should happen in 5 minutes or so." 
    u "And?" 
    show asi confused 
    a "Dunno,{w=.05} just wanted to say it."    
    u "Oh." 
    hide asi confused 
    jump sxA22 

label sxA22: 
    "Soon,{w=.05} there was an announcement over the intercom system." 
    "Announcer" "The fireworks show is starting.{w=.1} For safety reasons,{w=.05} please do not approach the competition stage." 
    scene bgfireworks with fade 
    $ renpy.music.set_volume(0.5, delay=0.3)
    "Soon,{w=.05} there was a whistling sound as a glowing trail headed towards the heavens,{w=.05} followed by multiple others." 
    "Immediately after,{w=.05} the fireworks exploded into a flower of sparks." 
    "This was actually my first time seeing fireworks in person." 
    "It looks much better than it does on TV." 
    hide fireworks 
    show a excited 
    a "Wow,{w=.05} so beautiful!" 
    u "Yep,{w=.05} it's quite beautiful." 
    a "Wait,{w=.05} why don't we record it?" 
    a "I want to share it on my lecture group chat." 
    u "Good point." 
    "I took out my phone." 
    "The voice recorder was still on." 
    "I started the audio recording when that bastard tried to screw with [a]." 
    "Just in case I need to submit it as evidence if he tried to sue us afterwards." 
    "I stopped the recording,{w=.05} then opened the camera app,{w=.05} recording the fireworks." 
    hide a happy 
    show a disdainful 
    a "You should watch the fireworks too,{w=.05} you know?" 
    a "Don't just look at it through the screen." 
    a "You can't get the full experience like that." 
    u "Oh." 
    hide a disdainful 
    "The fireworks really were beautiful." 
    scene bgblack with fade 
    jump sxA23 

label sxA23: 
    "After the fireworks show,{w=.05} the crowds dispersed and the stalls closed up for the day." 
    scene bgchristmasmarket with fade 
    show a disappointed 
    u "Should I walk you home?" 
    u "It's really quite late." 
    a "Alright." 
    hide a disappointed 
    scene bgblack with fade 
    "I walked her home." 
    "Her house was a little closer to the market than mine." 
    "We exchanged some banter along the way." 
    "Finally,{w=.05} we arrived at her apartment." 
    scene bgapartment with fade 
    "Standing in the fluorescent lightning of the apartment hallway,{w=.05} [a] turned around." 
    show a satisfied 
    a "I had quite a lot of fun today." 
    u "Me too." 
    a "I hope that we can do this next year,{w=.05} too."   
    u "Same." 
    "What she said was quite strange since we both have 2 more years in university,{w=.05} but I didn't think much of it." 
    a "Then,{w=.05} goodbye." 
    u "Goodbye." 
    $ end('sxA23')
    hide a satisfied 