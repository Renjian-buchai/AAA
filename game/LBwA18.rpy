label LBwA18: 
    "The competition stage,{w=.1}  situated in the heart of the Christmas Market,{w=.1}  was bustling as many people crowded around the stage." 
    "Emcee" "Does anyone want to try?{w=.3} We only have 3 prizes left." 
    "Noticing a poster nearby,{w=.1}  I commented," 
    u "Oh,{w=.1}  it seems to be a giftwrapping competition." 
    a "Really?{w=.3} That's interesting." 
    "No,{w=.1}  it isn't." 
    a "You look like you're thinking that it's lame." 
    u "..." 
    "How did she know?" 
    u "Since you already know about my thoughts,{w=.1}  care to explain why it's wrong?"
    a "Haha,{w=.1}  it's obviously because I'm good at giftwrapping." 
    a "My parents used to force me to wrap presents for everyone." 
    a "So to get back to watching anime quickly,{w=.1}  I learnt to wrap presents quickly." 
    u "You're just excited about winning,{w=.1}  huh?" 
    a "Of course!" 
    u "...I understand,{w=.1}  you'd rather cry on a BMW than smile on a bike." 
    a "Who're you calling a golddigger?" 
    a "How do you even know that reference?{w=.3} I thought that you only watched anime." 
    u "Are you retarded?{w=.3} Do you think that I was like 3 when the phrase became viral?" 
    a "...Anyways,{w=.1}  let's join the competition now!" 
    "She pulled me along as she jumped onto the stage." 
    "Emcee" "We have two more participants here!" 
    "Why did {i}she{/i} have to drag {i}me{/i} into this?" 
    "[a] seemed to notice my misgivings." 
    a "Don't worry about it." 
    a "Pfft,{w=.1}  we can't get out of it anyways." 
    u "That's exactly what I'm worrying about." 
    "Emcee" "Wow,{w=.1}  such a lively couple we have here." 
    u "..." 
    "Emcee" "Why don't you introduce yourself?" 
    "He held up a mic up to [a]'s face first." 
    a "Hii~I'm [a],{w=.1}  a student at China University of Fine Arts!" 
    u "And I'm her boyfriend." 
    a "Hey,{w=.1}  introduce yourself." 
    u "I'm her boyfriend." 
    a "No,{w=.1}  I mean...{w=.3} Your name!" 
    u "My name is her boyfriend." 
    a "I give up.{w=.3} Mr.{w=.3} Emcee,{w=.1}  can we continue?" 
    "Emcee" "Haha,{w=.1}  how boisterous! Let's explain the rules!" 
    "Emcee" "You are to wrap the present with the materials provided." 
    "Emcee" "You'll get a reward if you're in the top 10." 
    "Emcee" "The current tenth place has a time of 25.8 seconds,{w=.1}  whilst the record stands at 20.3 seconds." 
    "I looked at the leaderboard." 
    "The top ten fastest gift wrappers would get vouchers." 
    "The top three gift wrappers would get vouchers and a medal." 
    "The champion vouchers and a 'secret gift',{w=.1}  whatever that was." 
    a "Wow,{w=.1}  so fast! I might even have to concentrate for this!" 
    "Her sarcastic comment drew amused chuckles from the audience." 
    u "Oh." 
    "My dull reply drew no interest from anyone else." 
    "Emcee" "Well,{w=.1}  then,{w=.1}  miss [a] and her boyfriend,{w=.1}  will you go to your respective stations to prepare?" 
    a "OK!" 
    u "Oh." 
    "We sat at a table placed on the stage,{w=.1}  and prepared to wrap the gift." 
    jump LBwA19
label LBwA19: 
    "When the MC announced 'start',{w=.1}  I begun unwrapping." 
    $ T0 = time.perf_counter() 
label game_n1: 
menu: 
    "What should I do now?" 
    "Wrap present": 
        "I tore out some wrapping paper." 
        "I taped the wrapping paper to the present." 
        "I folded the wrapping paper to encase the present." 
        "I taped the wrapping paper closed." 
        jump game_0 
    "Tie ribbon": 
        "I took out a ribbon." 
        "I set it aside." 
        jump game_1 
    "Submit present": 
        "That doesn't sound quite right..." 
        jump game_n1 
label game_0: 
menu: 
    "What should I do now?" 
    "Tie ribbon": 
        "I took out a ribbon." 
        "I taped the ribbon to the present." 
        "I tied the ribbon tightly."  
        jump game_2 
    "Submit present": 
        "That doesn't sound quite right..." 
        jump game_0 
label game_1: 
menu: 
    "What should I do now?" 
    "Wrap present": 
        "I tore out some wrapping paper." 
        "I taped the wrapping paper to the present." 
        "I folded the wrapping paper to encase the present." 
        "I taped the wrapping paper closed." 
        jump game_3 
    "Submit present": 
        "That doesn't sound quite right..." 
        jump game_1 
label game_3: 
menu: 
    "What should I do now?" 
    "Tie ribbon": 
        "I taped the ribbon to the present." 
        "I tied the ribbon tightly." 
        jump game_4 
    "Submit present": 
        "That doesn't sound quite right..." 
        jump game_3 
label game_2: 
menu: 
    "What should I do now?" 
    "Submit present": 
        jump LBwA20g
label game_4: 
menu: 
    "What should I do now?" 
    "Submit present": 
        jump LBwA20g
label LBwA20g: 
    python: 
        T1 = time.perf_counter() 
        T = (T1 - T0) * 4.5
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
    "After the competition,{w=.1}  we collected our winnings." 
    "I recieved [Reward]."
    "[a] managed to eke out second place,{w=.1}  qualifying herself for a voucher and a gold medal." 
    "It's quite amusing,{w=.1}  since she recieved gold for as a runner up." 
    "That makes TMD a lot of sense." 
    u "Can I go home now?" 
    a "What?{w=.3} Am I really {i}that{/i} annoying to be with?" 
    u "More or less." 
    u "Also,{w=.1}  there's no place like home." 
    a "Isn't that from {i}The Wizard of Oz{/i}?{w=.3} You know,{w=.1}  I take literature as my minor." 
    u "Are you an idiot?" 
    u "It's just a quote." 
    a "Whatever." 
    a "You can't go home." 
    u "{font=SIMSUN.ttf}囧{/font}" 
    a "Why're you making that face?" 
    a "Who leaves their 'girlfriend' on their own on a date?" 
    u "Me,{w=.1}  that's who." 
    a "Dumbass." 
    a "Please~?" 
    u "Don't act cute." 
    u "The weather forecast says it's about to rain,{w=.1}  so we should probably go back." 
    a "Huh?{w=.3} How sad..." 
    jump LBwA21 
label LBwA21: 
    "[a] also checked the weather." 
    a "It's not going to rain! It's already at -2 Celcius!" 
    u "Well,{w=.1}  it could be freezing rain." 
    "The weather this week was unusually cold,{w=.1}  considering it was still in December." 
    "Perhaps it was just a cold snap." 
    u "Either way,{w=.1}  you don't want to get cold,{w=.1}  right?" 
    u "You still have the whole winter hols ahead." 
    a "Huh...{w=.3} But the Christmas market will close after tomorrow..." 
    u "Then we can come back tomorrow before it closes." 
    a "Alright..." 
    "Reluctantly,{w=.1}  she decided to leave." 
    a "But there's a fireworks festival later!" 
    u "There is?{w=.3} But it might be cancelled if it rains later." 
    a "Hmph,{w=.1}  there doesn't even seem to be clouds in the sky." 
    u "The sky's pitch black.{w=.3} How can you see any clouds?" 
    u "And anyways,{w=.1}  we've already made the decision.{w=.3} There's no point in questioning your previous decision." 
    u "There'll probably be a fireworks festival tomorrow,{w=.1}  too." 
    a "Hmph,{w=.1}  cold hearted." 
    u "What the fuck?" 
    u "If you're going to do this,{w=.1}  so be it." 
    u "If you were a number,{w=.1}  you would be 250." 
    a "Who're you calling half-crazy?" 
    u "Haha." 
    a "Don't just laugh it off!" 
    a "When did 250 come to represent half-crazy,{w=.1}  though?" 
    u "If I recall correctly,{w=.1}  it came from imperial China." 
    u "Then,{w=.1}  banks would denote 500 taels of silver as a 'feng'." 
    u "So,{w=.1}  250 taels of silver would be half a 'feng'." 
    u "Since 'feng' is also the pronunciation of 'crazy',{w=.1}  250 can also be said as half-crazy." 
    a "Never knew that." 
    u "Because you never studied." 
    a "Are you retarded?{w=.3} Of course I've studied!" 
    a "I'm at the top of my class!" 
    u "Top of what class?" 
    a "Acting." 
    u "How study intensive." 
    a "Yes,{w=.1}  it's very study intensive..." 
    u "It's sarcasm,{w=.1}  you idiot." 
    a "You're correct,{w=.1}  you're an idiot." 
    "She used my own insult against me." 
    "Normally,{w=.1}  I would casually say 'you're right,{w=.1}  you're a <insult>' when someone calls me an '<insult>'." 
    "Usually,{w=.1}  they would reply,{w=.1}  'I know',{w=.1}  before realising what they agreed to." 
    "With such meaningless conversation,{w=.1}  we made our way back home." 
    jump LBwA22 
label LBwA22: 
    "I walked [a] back home,{w=.1}  before returning home myself." 
    "It was fortunate that we left early,{w=.1}  because just as I was about to arrive back home,{w=.1}  the first snowflakes begun to fall." 
    "Obviously,{w=.1}  I rushed back into my house,{w=.1}  then hid under my blanket to warm myself." 
    "Soon,{w=.1}  I recieved a call from [a]." 
    a "It's snowing!" 
    u "Yes,{w=.1}  it's snowing." 
    "What else am I supposed to say?" 
    "Deny that it's snowing?" 
    a "Do you want to build a snowman?" 
    u "Nope." 
    a "How cruel,{w=.1}  abandoning me like that after toying with me for the whole day." 
    u "Shut up." 
    u "Well,{w=.1}  at least we left early,{w=.1}  so we could go home just in time." 
    a "What do you mean?{w=.3} After I came back,{w=.1}  it was like half-an-hour before it started snowing." 
    u "{i]I{/i} made it back just in time." 
    a "You don't matter." 
    u "..." 
    "I'm speechless." 
    u "Well,{w=.1}  anyways,{w=.1}  goodbye." 
    a "Bye bye!" 
    "I hung up." 
    "That night,{w=.1}  I slept terribly." 
    jump LBwA23 
label LBwA23: 
    "25th December." 
    "I was woken up by a phone call." 
    "With tired eyes,{w=.1}  I looked  at the Caller ID." 
    u "[a]! What do you think you're doing?" 
    a "I'm calling you." 
    u "Fuck,{w=.1}  do you know what time it is?" 
    a "It's 6:03 A.M." 
    u "Do you think you're Sakuta Azusagawa?" 
    u "Why did you even call me?" 
    a "Because the news was played at 6:00." 
    u "But I don't watch the news." 
    "Newspaper superiority." 
    a "But I do!" 
    u "What does that have to do with me,{w=.1}  then?" 
    a "You don't matter." 
    "Fucking—" 
    "Whatever,{w=.1}  I won't argue with a retard." 
    a "Anyways,{w=.1}  the fireworks at the Christmas markets exploded last night,{w=.1}  right after we left." 
    u "You see,{w=.1}  it was the correct choice to leave." 
    "How lucky..." 
    a "Hmph,{w=.1}  but still..." 
    a "Now,{w=.1}  the Christmas market was cancelled..." 
    u "Then that's just that." 
    a "How heartless..." 
    a "Anyways,{w=.1}  now that you know about it,{w=.1}  bye~" 
    u "Erm...{w=.3} then," 
    "Goodbye." 
    "Ending." 
    python: 
        if persistent.LBwA23 = False: 
            persistent.LBwA23 = True 
            persistent.gamestate += 1 
    "Number of endings completed: [persistent.gamestate]" 
menu: 
    "What would you like to do now?" 
    "Quit": 
        return 
    "Try another path": 
        call start 