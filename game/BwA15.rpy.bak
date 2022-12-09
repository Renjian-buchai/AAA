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
    "Suddenly, she exclaimed." 
    hide a contemplative 
    show a excited 
    a "Is that a shiba inu plushie?" 
    "The sudden change it topic caught me off-guard." 
    u "Uhm... Yeah, why?" 
    a "I want it!" 
    u "..." 
    "Sounds troublesome, but it'll probably be fun." 
    hide a excited 
    scene bgblack with fade 
    "We walked up to the stall that had the shiba inu hung from its roof as a prize." 
    scene bggamestall with fade 
    show skpr at left 
    u "Erm... We want... 5 balls." 
    "Shopkeeper" "Oh, OK." 
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
    "I glared at her, my face hot." 
    "[a] smiled back sheepishly, a slight blush tinting her cheek." 
    "She seemed happy, although it might've just been an act." 
    "Her degree ultimately {i}was{/i} acting." 
    "The store owner covered his mouth as he chuckled." 
    "Shopkeeper" "I was just kidding..." 
    "Shopkeeper" "But damn, boy, you really snagged a good girlfriend, 233." 
    u "Oh." 
    "I want to die." 
    "I want to bury myself in a hole and never come out for the rest of my life!" 
    "Shopkeeper" "Here, take the balls." 
    "He handed over 5 balls." 
    "Shopkeeper" "That'll be 23.5 RMB, after discount...Pft!" 
    "He was unable to keep his laughter in." 
    "Shopkeeper" "You should look in the mirror, your face is so damn red!" 
    u "Shaddup." 
    a "Haha, that's what's cute about him." 
    u "Cute my ass!" 
    "Shopkeeper" "Shut up, you normie!" 
    a "Haha." 
    "I feel offended..." 
    a "How do we split the balls?" 
    u "You're better than me at sports, so you should take 3 of them." 
    "Playing games is troublesome." 
    "Might as well give it to someone else who likes games." 
    "Also, it's true that she's better than me, a homebody, in terms of sports." 
    a "No, the one who's worse at sports should get more tries." 
    u "But the one who's better at sports would win more points with more opportunities." 
    "We argued back and forth for a minute." 
    "As a student of philosophy, I was naturally great at arguing." 
    "In the end, I got my way. She gets 3 balls while I get 2 balls." 
    a "Alright~ Shiba inu, I'm coming for ya~!" 
    "On a table in the centre of the stall, there were a few moving targets to be knocked down." 
    "Each target had a number written on it, representing the number of points recieved per target." 
    "Points could be exchanged with rewards." 
    "The shiba inu was worth 500 points."
    "[a] threw a ball at the target." 
    "It hit a 100-pointer." 
    "[a] threw another ball at another target." 
    "She knocked it down, getting us 200 points." 
    "[a] threw {i}another{/i} ball at {i}another{/i} target." 
    "She missed, but the ball bounced and knocked down another target worth 100 points." 
    "She doesn't have any balls left." 
    a "Haih, how sad..." 
    a "It's your turn." 
    "Shopkeeper" "Go on, impress your girlfriend." 
    "Both of us blushed." 
    jump BwA16 

label BwA16: 
    "Ignoring the shopkeeper's uproarious laughter, I went up to the line behind which I was to stand."
    $ store = 400 
    python: 
        randoma = random.randint(0, 1) 
        randomb = random.randint(0, 3)
menu: 
    "" "Which target should I aim for?" 
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
    "" "Which target should I aim for?" 
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
    jump WBwA16 
elif score >= 500: 
    jump XBwA16 
else: 
    jump LBwA16 
label WBwA16: 
    "The owner whistles seeing my aim." 
    "Shopkeeper" "Damn, both of your aim are cracked." 
    u "She plays overwatch; her aim {i}has{/i} to be good." 
    a "Shut up." 
    "Shopkeeper" "Fuck you, overwatch player." 
    "[a] glared at me." 
    a "You didn't have to say that." 
    u "Sorry, a CS:GO player like me can't understand having to be ashamed of doing what I like." 
    a "Shut up." 
    u "Haha." 
    u "Well, we'll get the shiba inu plushie." 
    "Shopkeeper" "A'ight, I'll bring it down." 
    "He hoisted down the plushie before passing it over to me." 
    "Shopkeeper" "Here's it." 
    u "Alright, thanks." 
    "I handed the plushie over to [a]." 
    a "Thanks!" 
    u "You're welcome." 
    a "No, really, thank you." 
    u "What the fuck?" 
    "I still can't understand women even after speaking to her for almost a year." 
    "She's already thanked me once, hadn't she?" 
    u "Anyways, bye." 
    "Shopkeeper" "Bye." 
    "We walked away from the stall." 
    u "Where should we go now?" 
    a "I don't know." 
    u "Isn't there a competition going on at the competition stage?" 
    "I remember seeing it on a flyer on the way to the exhibition hall." 
    a "Huh? That sounds interesting." 
    a "Let's go!" 
    call BwA18 
label XBwA16: 
    "Shopkeeper" "Your aim's great, boy." 
    u "Haha, I want the shiba inu plushie." 
    a "Hehe, your aim's better than I remember." 
    u "Shut up." 
    u "It has always been this good." 
    u "I was just playing the pig to eat the tiger." 
    "That was a lie." 
    "It was just luck." 
    a "No, you weren't." 
    a "Remember during our university's sports day, you were a part of the baseball team, and when you pitched, it became a homerun even before the batter hit the ball." 
    u "Fuck, I just gave the other team a ball three times." 
    "That is, I missed the strike zone thrice." 
    a "What does that even mean?" 
    "It was apparent that she didn't know the rules of baseball." 
    "The shopkeeper laughed at our childish display, handing over the shiba inu plushie that he hoisted down." 
    "[a] recieved it, then hugged it tightly." 
    u "Alright, bye!" 
    a "Bye!" 
    "The shopkeeper did not respond, just waving back." 
    "We left the game district." 
    u "Where do we go now?" 
    a "Isn't there a competition going on at the competition stage?" 
    a "Why don't we go check it out?" 
    u "Alright." 
    call BwA18 
label LBwA16: 
    #Not sad ending. 
return 