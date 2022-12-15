label BwA15: 
    scene bgblack with fade 
    hide a mischievous with dissolve 
    "There was a game district in the market." 
    "We headed to the game district."
    scene bgchristmasmarket with fade 
    show a happy with dissolve 
    a "What game do you want to play?" 
    u "No clue." 
    hide a happy with dissolve 
    show a contemplative with dissolve 
    a "I want to..." 
    "She looked up and down the district." 
    "Suddenly,{w=.1} she exclaimed." 
    hide a contemplative with dissolve 
    show a excited with dissolve 
    a "Is that a shiba inu plushie?" 
    "The sudden change it topic caught me off-guard." 
    u "Uhm...{w=.3} Yeah,{w=.1} why?" 
    a "I want it!" 
    u "..." 
    "Sounds troublesome,{w=.1} but it'll probably be fun." 
    hide a excited with dissolve 
    scene bgblack with fade 
    "We walked up to the stall that had the shiba inu hung from its roof as a prize." 
    scene bggamestall with fade 
    show skpr at left with dissolve 
    u "Erm...{w=.3} We want...{w=.3} 5 balls." 
    "Shopkeeper" "Oh,{w=.1} OK." 
    "Shopkeeper" "Are you a couple?" 
    show a excited with dissolve 
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
    show a flustered with dissolve 
    "I glared at her,{w=.1} my face hot." 
    "[a] smiled back sheepishly,{w=.1} a slight blush tinting her cheek." 
    "She seemed happy,{w=.1} although it might've just been an act." 
    "Her degree ultimately {i}was{/i} acting." 
    show skpr at left with dissolve 
    "The store owner covered his mouth as he chuckled." 
    "Shopkeeper" "I was just kidding..." 
    "Shopkeeper" "But damn,{w=.1} boy,{w=.1} you really snagged a good girlfriend,{w=.1} 233." 
    hide a flustered with dissolve 
    show a happy with dissolve 
    u "Oh." 
    "I want to die." 
    "I want to bury myself in a hole and never come out for the rest of my life!" 
    "Shopkeeper" "Here,{w=.1} take the balls." 
    "He handed over 5 balls." 
    "Shopkeeper" "That'll be 23.5 RMB,{w=.1} after discount...Pft!" 
    "He was unable to keep his laughter in." 
    hide a happy with dissolve 
    show a excited with dissolve  
    "Shopkeeper" "You should look in the mirror,{w=.1} your face is so damn red!" 
    u "Shaddup." 
    hide a excited with dissolve 
    show a mischievous with dissolve 
    a "Haha,{w=.1} that's what's cute about him." 
    u "Cute my ass!" 
    "Shopkeeper" "Shut up,{w=.1} you normie!" 
    a "Haha." 
    "I feel offended..." 
    hide a mischievous with dissolve 
    show a excited with dissolve 
    a "How do we split the balls?" 
    u "You're better than me at sports,{w=.1} so you should take 3 of them." 
    "Playing games is troublesome." 
    "Might as well give it to someone else who likes games." 
    "Also,{w=.1} it's true that she's better than me,{w=.1} a homebody,{w=.1} in terms of sports." 
    a "No,{w=.1} the one who's worse at sports should get more tries." 
    u "But the one who's better at sports would win more points with more opportunities." 
    hide a excited with dissolve 
    hide skpr with dissolve 
    scene bgblack with fade 
    "We argued back and forth for a minute." 
    "As a student of philosophy,{w=.1} I was naturally great at arguing." 
    "In the end,{w=.1} I got my way.{w=.3} She gets 3 balls while I get 2 balls." 
    scene gamestall with fade 
    show a excited with dissolve 
    a "Alright~ Shiba inu,{w=.1} I'm coming for ya~!" 
    "On a table in the centre of the stall,{w=.1} there were a few moving targets to be knocked down." 
    "Each target had a number written on it,{w=.1} representing the number of points recieved per target." 
    "Points could be exchanged with rewards." 
    "The shiba inu was worth 500 points."
    hide a excited with dissolve 
    scene bgblack with fade 
    "[a] threw a ball at the target." 
    "It hit a 100-pointer." 
    "[a] threw another ball at another target." 
    "She knocked it down,{w=.1} getting us 200 points." 
    "[a] threw {i}another{/i} ball at {i}another{/i} target." 
    "She missed,{w=.1} but the ball bounced and knocked down another target worth 100 points." 
    "She doesn't have any balls left." 
    scene bggamestall with fade 
    show a disappointed with dissolve 
    a "Haih,{w=.1} how sad..." 
    a "It's your turn." 
    show skpr at left with dissolve 
    "Shopkeeper" "Go on,{w=.1} impress your girlfriend." 
    hide a disappointed with dissolve 
    show a flustered with dissolve 
    "Both of us blushed." 
    jump BwA16 
label BwA16: 
    "Ignoring the shopkeeper's uproarious laughter,{w=.1} I went up to the line behind which I was to stand."
    hide a flustered with dissolve 
    hide skpr with dissolve 
    $ store = 400 
    python: 
        randoma = random.randint(0, 1) 
        randomb = random.randint(0, 3)
menu: 
    "Which target should I aim for?" 
    "100 point": 
        if randoma == 1: 
            $ score = score + 100 
            $ randoma = 0 
            jump gametw 
        else: 
            $ randoma = 0 
            jump gametsx 
    "200 point": 
        if randomb == 3: 
            $ score = score + 200 
            $ randomb = 0 
            jump gametq 
        else: 
            $ randomb = 0 
            jump gametb
label gametw: 
    "I knocked down the 100 point target." 
    "Our current score is [score]." 
    jump gametj 
label gametsx: 
    "I missed." 
    "Our current score is [score]." 
    jump gametj 
label gametq: 
    "I knocked down the 200 point target." 
    "Our current score is [score]." 
    jump gametj 
label gametb: 
    "I missed." 
    "Our current score is [score]." 
    jump gametj 
label gametj:
    python: 
        randoma = random.randint(0,1)
        randomb = random.randint(0,3) 
menu: 
    "Which target should I aim for?" 
    "100 point": 
        if randoma == 1: 
            $ score = score + 100 
            $ randoma = 0 
            jump gameet 
        else: 
            $ randoma = 0 
            jump gametety 
    "200 point": 
        if randomb == 3: 
            $ score = score + 200 
            $ randomb = 0 
            jump gametete 
        else: 
            $ randomb = 0 
            jump gametets
label gameet: 
    "I knocked down the 100 point target." 
    "Our current score is [score]." 
    jump gameetsi 
label gameety: 
    "I missed." 
    "Our current score is [score]." 
    jump gameetsi 
label gameete: 
    "I knocked down the 200 point target." 
    "Our current score is [score]." 
    jump gameetsi
label gameets: 
    "I missed." 
    "Our current score is [score]." 
    jump gameetsi 
label gameetsi: 
if score == 800: 
    jump WBwA17 
elif score >= 500: 
    jump XBwA17 
else: 
    jump LBwA17 
label WBwA17: 
    scene bgblack with fade 
    pause 1.0 
    scene bggamestall with fade 
    show skpr at left with dissolve 
    "The owner whistles seeing my aim." 
    "Shopkeeper" "Damn,{w=.1} both of your aim are cracked." 
    u "She plays overwatch; her aim {i}has{/i} to be good." 
    show a annoyed with dissolve 
    a "Shut up." 
    "Shopkeeper" "Fuck you,{w=.1} overwatch player." 
    hide a annoyed with dissolve 
    show a angry with dissolve 
    "[a] glared at me." 
    a "You didn't have to say that." 
    u "Sorry,{w=.1} a CS:GO player like me can't understand having to be ashamed of doing what I like." 
    hide a angry with dissolve 
    show a annoyed with dissolve 
    a "Shut up." 
    u "Haha." 
    u "Well,{w=.1} we'll get the shiba inu plushie." 
    "Shopkeeper" "A'ight,{w=.1} I'll bring it down." 
    hide a annoyed with dissolve 
    hide skpr with dissolve 
    scene bgblack with fade 
    "He hoisted down the plushie before passing it over to me." 
    scene bggamestall with fade 
    show skpr with dissolve 
    "Shopkeeper" "Here's it." 
    u "Alright,{w=.1} thanks." 
    "I handed the plushie over to [a]." 
    show asi happy 
    a "Thanks!" 
    u "You're welcome." 
    a "No,{w=.1} really,{w=.1} thank you." 
    u "What the fuck?" 
    "I still can't understand women even after speaking to her for almost a year." 
    "She's already thanked me once,{w=.1} hadn't she?" 
    u "Anyways,{w=.1} bye." 
    "Shopkeeper" "Bye." 
    hide asi happy with dissolve 
    hide skpr with dissolve 
    scene bgblack with fade 
    "We walked away from the stall." 
    scene bgchristmasmarket with fade 
    u "Where should we go now?" 
    a "I don't know." 
    u "Isn't there a competition going on at the competition stage?" 
    "I remember seeing it on a flyer on the way to the exhibition hall." 
    a "Huh?{w=.3} That sounds interesting." 
    a "Let's go!" 
    call BwA18 from _call_BwA18 
label XBwA17: 
    scene bgblack with fade 
    pause 1.0 
    scene bggamestall with fade 
    show skpr at left with dissolve 
    show a smirk with dissolve 
    "Shopkeeper" "Your aim's great,{w=.1} boy." 
    u "Haha,{w=.1} I want the shiba inu plushie." 
    a "Hehe,{w=.1} your aim's better than I remember." 
    u "Shut up." 
    u "It has always been this good." 
    u "I was just playing the pig to eat the tiger." 
    "That was a lie." 
    "It was just luck." 
    hide a smirk with dissolve 
    show a disdainful with dissolve 
    a "No,{w=.1} you weren't." 
    a "Remember during our university's sports day,{w=.1} you were a part of the baseball team,{w=.1} and when you pitched,{w=.1} it became a homerun even before the batter hit the ball." 
    u "Fuck,{w=.1} I just gave the other team a ball three times." 
    "That is,{w=.1} I missed the strike zone thrice." 
    hide a disdainful with dissolve 
    show a confused with dissolve 
    a "What does that even mean?" 
    "It was apparent that she didn't know the rules of baseball." 
    "The shopkeeper laughed at our childish display,{w=.1} handing over the shiba inu plushie that he hoisted down." 
    hide a confused with dissolve 
    show a happy with dissolve 
    "[a] recieved it,{w=.1} then hugged it tightly." 
    u "Alright,{w=.1} bye!" 
    a "Bye!" 
    "The shopkeeper did not respond,{w=.1} just waving back." 
    hide skpr with dissolve 
    hide asi happy with dissolve 
    scene bgblack with fade 
    "We left the game district." 
    scene bgchristmasmarket with fade 
    show asi happy with dissolve 
    u "Where do we go now?" 
    a "Isn't there a competition going on at the competition stage?" 
    a "Why don't we go check it out?" 
    u "Alright." 
    scene bgblack with fade 
    call BwA18 from _call_BwA18_1 
label LBwA17: 
    scene bgblack with fade 
    pause 1.0 
    scene bggamestall with fade 
    a "Well,{w=.1} what did I even expect from you?" 
    u "Probably more than what I could actually achieve." 
    a "That's for sure." 
    a "Haha." 
    "Shopkeeper" "Then...{w=.3} What do you want to redeem?" 
    u "Erm...{w=.3} Let's put that on hold." 
    u "I want another ball."
    "Shopkeeper" "Alright." 
    "He passes a ball to me after I paid for it." 
    "I tossed the ball to [a]." 
    u "You're much better than me,{w=.1} so you should throw it." 
    "[a] scoffs." 
    a "How pathetic~" 
    u "Shut it." 
    "She threw the ball with quite some strength,{w=.1} knocking down a 200-point target." 
    a "You can feel free to worship me." 
    u "No,{w=.1} I won't." 
    a "Haha,{w=.1} then so be it." 
    a "I want the shiba inu doll." 
    "The shopkeeper hoisted down the plushie and passed it to [a]." 
    a "Then,{w=.1} bye!" 
    "Shopkeeper" "Bye!" 
    "We walked away from the stall." 
    u "Where do we go now?" 
    a "There's a competiiton going on at the stage,{w=.1} right?{w=.3} "
    u "I would assume so." 
    u "That's what the market's website says." 
    a "Sounds interesting!"
    a "Let's go!" 
    call LBwA18 
return 