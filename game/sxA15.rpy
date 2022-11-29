label sxA15: 
    "In the heart of the Christmas Market, there was a competition stage." 
    "On the competition stage was held a giftwrapping competition." 
    "Emcee" "Alright! Is there anyone else who wants to come up?!" 
    "Emcee" "The current record is 20.3 seconds by Mister Lu Hua!" 
    a "Wow, so fast!" 
    u "..." 
    "To be honest, I wasn't very interested." 
    "According to a screen by the side of the stage, the top ten fastest gift wrappers would get vouchers." 
    "The top three would get vouchers and a medal." 
    "The champion gets vouchers and a 'secret gift', whatever that was." 
    "The tenth place had a time of 25.8 seconds." 
    a "Why don't we participate?" 
    u "I don't really want to, though." 
    a "...Alright, then." 
    "She walks up onto the stage." 
    "Emcee" "We have a new competitor!" 
    "Emcee" "What's your name, little miss?" 
    a "Hehe, hi, I'm [a]." 
    a "I'm honoured to come to a competition like this!" 
    "Emcee" "Alright, let's start." 
    "Emcee" "Do you know what you need to do in this competition?" 
    a "We wrap a present, right?" 
    "There was a sound of laughter." 
    "Emcee" "Of course we must wrap a present!" 
    "Emcee" "You must wrap that box over there with the wrapping paper and tape provided." 
    "[a] walked to the table where the tape and wrapping paper lay." 
    "Emcee" "Are you ready?!" 
    a "Yes!" 
    "Emcee" "Then you may start in 3...{w=1} 2...{w=1} 1...{w=1} you may start now!" 
    "[a] hastily attempts to wrap the tape."
    "She manages to completely wrap the present in 22.6 seconds." 
    "Emcee" "Aww, such a shame. You couldn't beat Mr. Lu's record." 
    "Emcee" "But now, you're the new 6th place!" 
    "Emcee" "So... You get a 150 RMB voucher at XX bookstore!" 
    a "Yay!" 
    jump sxA16 

label sxA16: 
    "[a] jumps off the competition stage, walking up to me." 
    a "Did you see?" 
    u "See what?" 
    "She knocked me lightly on my head." 
    a "I wrapped it in 22.6 seconds." 
    u "I know." 
    a "Hmph." 
    "What the hell's wrong with her?" 
    "She seemed to be in a bad mood." 
    "But her bad mood didn't last for very long." 
    a "Isn't there a game district? Let's go." 
    u "Alright." 
    jump sxA17 

label sxA17: 
    "There was a game district in the market." 
    "We headed to the game district." 
    a "What game do you mant to play?" 
    u "No clue. What do you want?" 
    a "I want to play... Oh, a shiba inu plushy..." 
    a "I want it!" 
    u "Oh, OK." 
    "We went to the stall that hung up the shiba inu toy." 
    "Shopkeeper" "Do you want to play?" 
    a "Yup!" 
    "Shopkeeper" "Then, how many balls do you want?" 
    a "How many do you think we need to win it?" 
    u "Dunno. Maybe 5 for now." 
    "Shopkeeper" "Then, that'll be 25 RMB." 
    u "Oh." 
    "Shopkeeper" "Are you a couple?" 
    u "Yes..." 
    "I'm still not used to calling [a] my girlfriend." 
    "Not that we're a couple, anyways." 
    "The shopkeeper seemed unconvinced." 
    "Shopkeeper" "Then, prove it." 
    a "Uhm.. Alright." 
    "I felt a soft feeling on my cheek." 
    $ renpy.music.set_pause(True, channel="music") 
    "The world seemed to stop." 
    "After a moment, I finally understood what happened." 
    $ renpy.music.set_pause(False, channel="music") 
    "Flushing red, I glared at her." 
    "Her face was entirely red." 
    "The store owner guffawed." 
    "Shopkeeper" "I was just kidding." 
    u "Oh." 
    "Then why didn't you say that before she kissed me?" 
    "Then again, she acted so quickly that it was unreasonable to expect him to react on time." 
    "The owner handed over 2.5 RMB along with 6 balls." 
    "Shopkeeper" "One free for putting on such a good show." 
    "We both reddened after being reminded of the incident." 
    a "Oh..." 
    u "Uhm... shall we... try to win the shiba inu?" 
    a "Alright..." 
    a "Three and three, right?" 
    a "The balls, I mean." 
    u "That's fine." 
    a "Alright, shiba inu, I'm coming for you!" 
    "On a table in the centre of the stall were a few moving targets to be knocked down." 
    "Each target had a number written on it, representing the number of points recieved per target." 
    "Points could be exchanged for rewards." 
    "The shiba inu was worth 500 points." 
    "[a] threw a ball at a target." 
    "It missed." 
    "She threw another ball at the same target." 
    "She knocked it down, gaining 100 points." 
    "[a] threw another ball at another target." 
    "She was fortunate, and barely managed to knock down a 200-point target." 
    a "Haih, how sad." 
    a "It's your turn." 
    Owner D "Go on, impress your girlfriend." 
    "Both a and I blushed." 
    jump sxA18 

label sxA18: 
    "Ignoring the store owner's uproarious laughter, I went up to the line behind which I had to stand." 
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
    "Shopkeeper" "Fuck, you're a great shot, boy!" 
    u "Haha, can I exchange my points for the shiba inu?" 
    "Shopkeeper" "Alright, no problem." 
    "He hoisted down the shiba inu toy, handing it over to me." 
    "The shiba inu plushie was very soft." 
    "Without another word, I handed the plushie to [a]." 
    a "Hehe, thanks!" 
    u "No problem." 
    "Shopkeeper" "What other things do you want?" 
    "Shopkeeper" "You still have some points left." 
    u "Don't want anything." 
    "I wasn't interested in anything else in the stall." 
    "Shopkeeper" "Hah, then so be it." 
    u "Haha." 
    a "Bye!" 
    "We left." 
    "It's late, so I want to go home..." 
    u "Should we leave now?" 
    a "No, there's still a fireworks show." 
    u "Oh, OK." 
    u "..." 
    u "There's no couple's discount during the fireworks show, so I can go home first, right?" 
    a "No, of course not!" 
    u "{i}Sigh,{/i} Alright." 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh, alright." 
    "We strolled around the market, looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    u "Oh, OK." 
    call sxA20 

label XsxA19: 
    "Shopkeeper" "You did great, boy." 
    u "Hehe, I want to exchange it for a shiba inu doll." 
    "Shopkeeper" "A'ight, getting it now." 
    "He down the shiba inu toy, handing it over to me." 
    "Without another word, I handed the shiba inu toy to A." 
    a "Hehe, thanks!" 
    u "You're welcome." 
    u "Well, then, bye." 
    "Shopkeeper" "Bye." 
    "We left" 
    "It's late, so I want to go home." 
    u "Should we go home now?" 
    a "No, there'st still a fireworks show." 
    u "Oh, OK." 
    u "There's no couple's discount during the fireworks show, so I can go home first, right?" 
    a "No, of course not!" 
    u "{i}Sigh,{/i} Alright." 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh, alright." 
    "We strolled around the market, looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    u "Oh, OK." 
    call sxA20 


label LsxA19: 
    "Shopkeeper" "Well, that's a shame." 
    "[a] shook her head in disappointment." 
    u "{i}Sigh,{/i}Three more balls, please." 
    "Shopkeeper" "Alright." 
    "I played the game until we got 500 points." 
    "It somehow took me 700 balls." 
    "{b}Fuck.{/b}" 
    "The shopkeeper exasperatedly took down the plushie, handing it over to me." 
    "I passed it over to [a]." 
    a "Thanks..." 
    u "No problem." 
    a "I'll pay you back." 
    u "No need." 
    "We walked away from the booth." 
    "It's late, so I want to go home." 
    u "Should we go home now?" 
    a "No, there'st still a fireworks show." 
    u "Oh, OK." 
    u "There's no couple's discount during the fireworks show, so I can go home first, right?" 
    a "No, of course not!" 
    u "{i}Sigh,{/i} Alright." 
    u "Should we find somewhere to sit and wait for the show to start?" 
    a "Oh, alright." 
    "We strolled around the market, looking for somewhere to sit." 
    "[a] suddenly pointed at a park next to the market right as we passed by." 
    u "Oh, OK." 
    call sxA20 
return 