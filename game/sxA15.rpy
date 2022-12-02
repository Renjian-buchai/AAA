﻿label sxA15: 
    scene bgblack with fade 
    hide a mischievous  
    "In the heart of the Christmas Market,{w=.1} there was a competition stage." 
    scene bgstage with fade 
    show a happy   
    "On the competition stage was held a giftwrapping competition." 
    show mc   
    "Emcee" "Alright!{w=.3}Is there anyone else who wants to come up?!" 
    "Emcee" "The current record is 20.3 seconds by Mister Lu Hua!" 
    hide mc 
    hide a happy 
    show a shocked 
    a "Wow,{w=.1} so fast!" 
    u "..." 
    "To be honest,{w=.1} I wasn't very interested." 
    "According to a screen by the side of the stage,{w=.1} the top ten fastest gift wrappers would get vouchers." 
    "The top three would get vouchers and a medal." 
    "The champion gets vouchers and a 'secret gift',{w=.1} whatever that was." 
    "The tenth place had a time of 25.8 seconds." 
    hide a shocked 
    show a excited 
    a "Why don't we participate?" 
    u "I don't really want to,{w=.1} though." 
    a "...{w=.3}Alright,{w=.1} then." 
    hide a excited 
    show stagea excited   
    "She walks up onto the stage." 
    show mc   
    "Emcee" "We have a new competitor!" 
    "Emcee" "What's your name,{w=.1} little miss?" 
    hide stagea excited 
    show stagea happy   
    a "Hehe,{w=.1} hi,{w=.1} I'm [a]." 
    a "I'm honoured to come to a competition like this!" 
    "Emcee" "Alright,{w=.1} let's start." 
    "Emcee" "Do you know what you need to do in this competition?" 
    a "We wrap a present,{w=.1} right?" 
    "There was a sound of laughter." 
    "Emcee" "Of course we must wrap a present!" 
    "Emcee" "You must wrap that box over there with the wrapping paper and tape provided." 
    scene bgblack with fade 
    "[a] walked to the table where the tape and wrapping paper lay." 
    scene bgstage with fade 
    "Emcee" "Are you ready?!" 
    hide stagea happy 
    show stagea excited   
    a "Yes!" 
    "Emcee" "Then you may start in 3...{w=1} 2...{w=1} 1...{w=1} you may start now!" 
    scene bgblack with fade 
    "[a] hastily attempts to wrap the tape."
    "She manages to completely wrap the present in 22.6 seconds." 
    scene bgstage with fade 
    "Emcee" "Aww,{w=.1} such a shame.{w=.3} You couldn't beat Mr. Lu's record." 
    "Emcee" "But now,{w=.1} you're the new 6th place!" 
    "Emcee" "So...{w=.3} You get a 150 RMB voucher at XX bookstore!" 
    hide stagea excited 
    show stagea happy   
    a "Yay!" 
    jump sxA16 

label sxA16: 
    scene bgchristmasmarket with fade 
    "[a] jumps off the competition stage,{w=.1} walking up to me." 
    hide stagea happy 
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
    a "Isn't there a game district?{w=.3}Let's go." 
    u "Alright." 
    scene bgblack with fade 
    jump sxA17 

label sxA17: 
    scene bggamestall with fade 
    hide a mischievous 
    show a playful 
    "There was a game district in the market." 
    "We headed to the game district." 
    a "What game do you mant to play?" 
    u "No clue.{w=.3} What do you want?" 
    a "I want to play...{w=.3} Oh,{w=.1} a shiba inu plushie..." 
    hide a playful 
    show a excited 
    a "I want it!" 
    u "Oh,{w=.1} OK." 
    "We went to the stall that hung up the shiba inu toy." 
    show skpr   
    hide a excited 
    show a excited   
    "Shopkeeper" "Do you want to play?" 
    a "Yup!" 
    "Shopkeeper" "Then,{w=.1} how many balls do you want?" 
    a "How many do you think we need to win it?" 
    u "Dunno.{w=.3} Maybe 5 for now." 
    "Shopkeeper" "Then,{w=.1} that'll be 25 RMB." 
    u "Oh." 
    "Shopkeeper" "Are you a couple?" 
    u "Yes..." 
    "I'm still not used to calling [a] my girlfriend." 
    "Not that we're a couple,{w=.1} anyways." 
    "The shopkeeper seemed unconvinced." 
    "Shopkeeper" "Then,{w=.1} prove it." 
    a "Uhm..{w=.3} Alright." 
    "I felt a soft feeling on my cheek." 
    $ renpy.music.set_pause(True, channel="music") 
    "The world seemed to stop." 
    "After a moment,{w=.1} I finally understood what happened." 
    $ renpy.music.set_pause(False, channel="music") 
    "Flushing red,{w=.1} I glared at her." 
    hide a excited 
    show a flustered   
    "Her face was entirely red." 
    "The store owner guffawed." 
    "Shopkeeper" "I was just kidding." 
    u "Oh." 
    "Then why didn't you say that before she kissed me?" 
    "Then again,{w=.1} she acted so quickly that it was unreasonable to expect him to react on time." 
    "The owner handed over 2.5 RMB along with 6 balls." 
    "Shopkeeper" "One free for putting on such a good show." 
    "We both reddened after being reminded of the incident." 
    a "Oh..." 
    u "Uhm...{w=.3} shall we...{w=.3} try to win the shiba inu?" 
    a "Alright..." 
    a "Three and three,{w=.1} right?" 
    a "The balls,{w=.1} I mean." 
    u "That's fine." 
    hide a flustered 
    show a excited   
    a "Alright,{w=.1} shiba inu,{w=.1} I'm coming for you!" 
    "On a table in the centre of the stall were a few moving targets to be knocked down." 
    "Each target had a number written on it,{w=.1} representing the number of points recieved per target." 
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
    "She knocked it down,{w=.1} gaining 100 points." 
    scene bgblack with fade 
    "[a] threw another ball at another target." 
    scene bggamestall with fade 
    "She was fortunate,{w=.1} and barely managed to knock down a 200-point target." 
    show a depressed   
    show skpr   
    a "Haih,{w=.1} how sad." 
    a "It's your turn." 
    "Shopkeeper" "Go on,{w=.1} impress your girlfriend." 
    hide a depresesd 
    show a flustered   
    "Both [a] and I blushed." 
    jump sxA18 

label sxA18: 
    "Ignoring the store owner's uproarious laughter,{w=.1} I went up to the line behind which I had to stand." 
    hide a flustered 
    hide skpr 
    scene bggamestall1 with dissolve 
    $ score = 300
python: 
    randoma = random.randint(0, 1) 
    randomb = random.randint(0, 3)

menu: 
    "" "Which target should I aim for?" 
    "100 point": 
        if randoma == 1: 
            $ score = score + 100 
            $ randoma = 0 
            jump game0 
        else: 
            $ randoma = 0 
            jump game1 

    "200 point": 
        if randomb == 3: 
            $ score = score + 200 
            $ randomb = 0 
            jump game2 
        else: 
            $ randomb = 0 
            jump game3 

label game0: 
    "I knocked down the 100 point target." 
    "Our current score is [score]." 
    jump game4 

label game1: 
    "I missed." 
    "Our current score is [score]." 
    jump game4 

label game2: 
    "I knocked down the 200 point target." 
    "Our current score is [score]." 
    jump game4 

label game3: 
    "I missed." 
    "Our current score is [score]." 
    jump game4 

label game4: 

python: 
    randoma = random.randint(0, 1) 
    randomb = random.randint(0, 3)

menu: 
    "" "Which target should I aim for?" 
    "100 point": 
        if randoma == 1: 
            $ score = score + 100 
            $ randoma = 0 
            jump game5 
        else: 
            $ randoma = 0 
            jump game6 

    "200 point": 
        if randomb == 3: 
            $ score = score + 200 
            $ randomb = 0 
            jump game7 
        else: 
            $ randomb = 0 
            jump game8 

label game5: 
    "I knocked down the 100 point target." 
    "Our current score is [score]." 
    jump game9 

label game6: 
    "I missed." 
    "Our current score is [score]." 
    jump game9 

label game7: 
    "I knocked down the 200 point target." 
    "Our current score is [score]." 
    jump game9 

label game8: 
    "I missed." 
    "Our current score is [score]." 
    jump game9 

label game9: 

python: 
    randoma = random.randint(0, 1) 
    randomb = random.randint(0, 3)

menu: 
    "" "Which target should I aim for?" 
    "100 point": 
        if randoma == 1: 
            $ score = score + 100 
            $ randoma = 0 
            jump game10 
        else: 
            $ randoma = 0 
            jump game11 

    "200 point": 
        if randomb == 3: 
            $ score = score + 200 
            $ randomb = 0 
            jump game12 
        else: 
            $ randomb = 0 
            jump game13 

label game10: 
    "I knocked down the 100 point target." 
    "Our current score is [score]." 
    jump game14 

label game11: 
    "I missed." 
    "Our current score is [score]." 
    jump game14 

label game12: 
    "I knocked down the 200 point target." 
    "Our current score is [score]." 
    jump game14 

label game13: 
    "I missed." 
    "Our current score is [score]." 
    jump game14 

label game14: 
    if score > 800: 
        jump WsxA19 
    elif score >500: 
        jump XsxA19 
    else: 
        jump LsxA19 

label WsxA19: 
    scene bggamestall with dissolve 
    show skpr   
    "Shopkeeper" "Fuck,{w=.1} you're a great shot,{w=.1} boy!" 
    u "Haha,{w=.1} can I exchange my points for the shiba inu?" 
    "Shopkeeper" "Alright,{w=.1} no problem." 
    "He hoisted down the shiba inu toy,{w=.1} handing it over to me." 
    "The shiba inu plushie was very soft." 
    "Without another word,{w=.1} I handed the plushie to [a]." 
    show asi happy   
    a "Hehe,{w=.1} thanks!" 
    u "No problem." 
    "Shopkeeper" "What other things do you want?" 
    "Shopkeeper" "You still have some points left." 
    u "Don't want anything." 
    "I wasn't interested in anything else in the stall." 
    "Shopkeeper" "Hah,{w=.1} then so be it." 
    u "Haha." 
    a "Bye!" 
    scene bgblack with fade 
    hide asi happy 
    hide skpr 
    "We left." 
    "It's late,{w=.1} so I want to go home..." 
    show bgchristmasmarket 
    show asi happy 
    u "Should we leave now?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.1} there's still a fireworks show." 
    u "Oh,{w=.1} OK." 
    hide asi disdainful 
    show asi happy 
    u "..." 
    u "There's no couple's discount during the fireworks show,{w=.1} so I can go home first,{w=.1} right?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.1} of course not!" 
    u "{i}Sigh,{w=.1}{/i} Alright." 
    hide asi disdainful  
    show asi happy 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh,{w=.1} alright." 
    scene bgblack with fade 
    "We strolled around the market,{w=.1} looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    scene bgchristmasmarketpark with fade 
    u "Oh,{w=.1} OK." 
    call sxA20 from _call_sxA20 

label XsxA19: 
    scene bggamestall with dissolve 
    show skpr   
    "Shopkeeper" "You did great,{w=.1} boy." 
    u "Hehe,{w=.1} I want to exchange it for a shiba inu doll." 
    "Shopkeeper" "A'ight,{w=.1} getting it now." 
    "He down the shiba inu toy,{w=.1} handing it over to me." 
    "Without another word,{w=.1} I handed the shiba inu toy to A." 
    show asi happy   
    a "Hehe,{w=.1} thanks!" 
    u "You're welcome." 
    u "Well,{w=.1} then,{w=.1} bye." 
    "Shopkeeper" "Bye." 
    scene bgblack with fade 
    hide asi happy 
    hide  skpr 
    "We left" 
    "It's late,{w=.1} so I want to go home." 
    scene bgchristmasmarket with fade 
    show asi happy 
    u "Should we go home now?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.1} there'st still a fireworks show." 
    u "Oh,{w=.1} OK." 
    hide asi disdainful 
    show asi happy 
    u "There's no couple's discount during the fireworks show,{w=.1} so I can go home first,{w=.1} right?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.1} of course not!" 
    u "{i}Sigh,{w=.1}{/i} Alright." 
    hide asi disdainful 
    show asi happy 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh,{w=.1} alright." 
    scene bgblack with fade 
    "We strolled around the market,{w=.1} looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    scene bgchristmasmarketpark with fade 
    u "Oh,{w=.1} OK." 
    call sxA20 from _call_sxA20_1 

label LsxA19: 
    scene bggamestall with dissolve 
    show skpr   
    "Shopkeeper" "Well,{w=.1} that's a shame." 
    "[a] shook her head in disappointment." 
    u "{i}Sigh,{w=.1}{/i}Three more balls,{w=.1} please." 
    "Shopkeeper" "Alright." 
    hide skpr 
    scene bgblack with fade 
    "I played the game until we got 500 points." 
    "It somehow took me 7 more balls." 
    "{b}Fuck.{/b}" 
    show skpr 
    scene bggamestall with fade 
    "The shopkeeper exasperatedly took down the plushie,{w=.1} handing it over to me." 
    "I passed it over to [a]." 
    show asi apologetic 
    a "Thanks..." 
    u "No problem." 
    a "I'll pay you back." 
    u "No need." 
    scene bgblack with fade 
    "We walked away from the booth." 
    "It's late,{w=.1} so I want to go home." 
    hide asi apologetic 
    show asi happy 
    scene bgchristmasmarket with fade 
    u "Should we go home now?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.1} there'st still a fireworks show." 
    u "Oh,{w=.1} OK." 
    hide asi disdainful 
    show asi happy 
    u "There's no couple's discount during the fireworks show,{w=.1} so I can go home first,{w=.1} right?" 
    hide asi happy 
    show asi disdainful 
    a "No,{w=.1} of course not!" 
    u "{i}Sigh,{w=.1}{/i} Alright." 
    hide asi disdainful 
    show asi happy 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh,{w=.1} alright." 
    scene bgblack with fade 
    hide asi happy 
    "We strolled around the market,{w=.1} looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    scene bgchristmasmarketpark with fade 
    u "Oh,{w=.1} OK." 
    call sxA20 from _call_sxA20_2 
return 