label sAB13: 
    $ renpy.block_rollback() 
    scene bgblack with fade 
    "Game district in the Christmas market." 
    scene bggamestall with fade 
    show a happy 
    a "What game do you want to play?" 
    u "...They're all the same (to me)."
    hide a happy 
    show a annoyed 
    a "You... Geez, you're way too indifferent." 
    u "I'm not." 
    hide a annoyed 
    show a smirk 
    a "You are!" 
    u "Whatever." 
    u "You choose." 
    "The games seemed to all be lame." 
    "Wait, guessing the riddles?" 
    "Isn't that a Mid-autumn Festival game?" 
    u "How retarded." 
    hide a smirk 
    show a annoyed 
    a "What?" 
    u "There's a riddle guessing game here." 
    hide a annoyed 
    show a contemplative 
    a "Oh, that's quite ironic." 
    "Neverthless, festivals are just excuses to have fun." 
    "Ultimately, it didn't matter what game is included, since all that matters is that everyone has fun." 
    "And everyone earns money, I guess." 
    hide a contemplative 
    show a excited 
    a "Let's try it!" 
    "Just as I expected."
    "I fucking knew that she'd choose the most retarded option." 
    "Now, I can make fun of her, because guessing riddles is my advantage, whilst things requiring the brain is her disadvantage." 
    scene bggamestall with fade 
    show ladyboss 
    "Lady Boss" "Hi, beauty, handsome, do you want to guess some riddles?" 
    hide ladyboss 
    show ladyboss at left 
    show a excited 
    a "Yep!" 
    hide a excited 
    show a curious 
    a "Are there any... prizes?" 
    "There wasn't anything that indicated that there was a reward." 
    "Lady Boss" "None, if you want, you can play the ball toss booth or something." 
    hide a curious 
    show a disappointed 
    a "Oh." 
    hide a disappointed 
    show a curious 
    a "Do we need to pay to play?" 
    "Lady Boss" "No need, just take one from the box there. We also sell keychains, if you want them." 
    "So that's how they're trying to turn a profit." 
    hide a curious 
    show a excited 
    a "Why don't we get a matching pair?" 
    u "OK." 
    "I wasn't very opposed to the idea." 
    "A few RMB is a cheap price to pay to maining something as fragile as a platonic, opposite gender relationship." 
    u "How much does it cost?" 
    "Lady Boss" "25 RMB per, 22.50 with the couple's discount." 
    a "We're a couple!" 
    "She made half of a heart shape with her hand." 
    "Reluctantly, I completed the heart shape." 
    "The lady boss seemed to notice my reluctance." 
    u "This is embarrassing." 
    hide a excited 
    show a smirk 
    "[a] looked at me with an expression that said, 'Nice save'." 
    "Lady Boss" "Alright, you two can flirt as much as you want at home." 
    "She handed over two keychains, one black and red, and one white and blue." 
    "[a] liked winter, so she naturally picked the white and blue one." 
    "Without an option, I had to choose the black and red one." 
    "I stuffed it into my pocket." 
    "Lady Boss" "Just take a riddle from the box, and write your answers down on a piece of paper." 
    "SHe pointed at a box that contained multiple strips of paper." 
    "Lady Boss" "Then show me your riddle and answer." 
    a "Alright!" 
    "She drew a piece of paper, following which I drew one, too." 
    scene bggamestall with fade 
    python: 
        indx = randint(0, 4) 
        if indx in Riddle0: 
            Riddle = Riddle0[indx] 
        else: 
            Riddle = ('Five brothers, living together, with different names and uneven heights.', "Quintuplets", 'Fingers', 'Siblings') 
        Q, W1, C, W2 = Riddle 
        del indx, Riddle
    menu: 
        "Question: [Q]" 
        "[W1]": 
            $ W = W1 
            jump riddlewrong
        "[C]": 
            jump riddlecorrect
        "[W2]": 
            $ W = W2
            jump riddlewrong 

label riddlewrong: 
    $ renpy.block_rollback() 
    scene bggamestall with fade 
    show ladyboss 
    "Lady Boss" "Wrong. The correct answer is [C], but you answered [W]." 
    $ del Q, C, W, W1, W2
    u "..." 
    "I was quite confident in my answer." 
    "I guess my instincts aren't as accurate as I would've thought." 
    hide ladyboss 
    "Oh, [a] is also having a hard time." 
    show a contemplative 
    u "Do you need help?" 
    hide a contemplative 
    show a disdainful 
    a "Nope, you got it wrong too; what help can you give?" 
    u "Haha." 
    "How incisive." 
    python: 
        indx = randint(0, 4)     
        if indx in Riddle1: 
            Riddle = Riddle1[indx] 
        else: 
            Riddle = ('The hunchbacked old man has great strength; he likes to carry whatever when everyone is busy (guess an item).', 'Bridge', 'Table', 'Hook')
        Q, C, W1, W2 = Riddle 
        del indx, Riddle 
        if randint(0, 1) is 1: 
            W = W1 
        else: 
            W = W2 
    "Question: [Q]"
    "..." 
    hide a disdainful 
    show a excited 
    a "I know! It's [W]." 
    u "Huh?" 
    "That's obviously wrong." 
    "I think it should be [C]." 
    show ladyboss at left 
    "Lady Boss" "Wrong, it's [C]." 
    $   del Q, C, W, W1, W2 
    "Oh, I guessed it right." 
    "Shame I didn't say it aloud, else I could tease her with 'Told you so'." 
    hide a excited 
    show a disappointed 
    a "Aww... How sad." 
    "Lady Boss" "Hehe." 
    "[a]'s disappointed expression was quite adorable." 
    hide a disappointed 
    show a annoyed 
    a "What're you laughing at?" 
    "She glared at me."
    u "Nothing." 
    "She'd probably smack me if I said, 'you' or something similar." 
    "Wait, I wasn't even laughing aloud!" 
    a "Hmph, do you need to laugh aloud for me to know you're laughing?" 
    a "Think how long we've known each other." 
    a "You'd better not be laughing at me, or you'll get it."
    "She must be a damn mind-reader." 
    u "..." 
    "Nonetheless, she can't say anything if she has no proof." 
    hide a annoyed 
    show a smirk 
    a "That {i}is{/i} what you're thinking, right?" 
    a "Or else, you'd deny it." 
    "Shit, she found out." 
    scene bggamestall with hpunch 
    "Ow." 
    "She punched me in the gut." 
    "How painful." 
    "Was I really {i}that{/i} predictable?" 
    "She didn't seem to be in a good mood. Either that, or she's drunk." 
    "Actually, the latter possibility is likelier." 
    "Lady Boss" "How long are you going to flirt here?" 
    "Lady Boss" "Shoo!" 
    u "OK." 
    "Damn it, how much force did that gorilla use?" 
    "Even talking is fucking painful!" 
    hide a smirk 
    show a suspicious  
    "Ever the mind-reader, [a] glared at me for an instant before replying to the Lady Boss." 
    hide a suspicious 
    show a smirk 
    a "Yes!" 
    scene bgblack with fade 
    "We left." 
    scene bgchristmasmarket with fade 
    a "Where should we go now?" 
    "There's really just one place we haven't visited, I think." 
    u "Christmas tree." 
    a "OK!" 
    call sAB14 from _call_sAB14 

label riddlecorrect: 
    $ renpy.block_rollback() 
    $ del Q, C, W, W1, W2 
    show ladyboss 
    "Lady Boss" "Huh, surprising." 
    "Lady Boss" "It's correct." 
    u "Yay..." 
    "How lame." 
    "I'm not even excited after getting it correct." 
    "Also, what's with that backhanded compliment?" 
    "..." 
    hide ladyboss 
    "I suddenly noticed that [a] also seemed to be having a hard time." 
    show a contemplative 
    u "Do you need help?" 
    python: 
        indx = randint(0, 4) 
        if indx in Riddle1: 
            Riddle = Riddle1[indx] 
        else: 
            Riddle = ('The hunchbacked old man has great strength; he likes to carry whatever when everyone is busy (guess an item).', 'Bridge', 'Table', 'Hook')
        Q, C, W1, W2 = Riddle 
        del indx, Riddle 
        indx = randint(0, 2)
        if indx is 0: 
            A = C 
        elif indx is 1: 
            A = W1 
        else: 
            A = W2 
    hide a contemplative 
    show a curious 
    a "Yep. [Q], what do you think it is?" 
    a "I think it's [A]" 
    $ del indx, A 
    
    menu: 
        "[Q]" 
        "[C]": 
            call riddle1correct from _call_riddle1correct 
        "[W1]": 
            $ B = W1 
            call riddle1wrong from _call_riddle1wrong 
        "[W2]": 
            $ B = W2 
            call riddle1wrong from _call_riddle1wrong_1 
    
label riddle1correct:
    $ renpy.block_rollback() 
    $ del Q, C, W1, W2 
    show ladyboss at left 
    "Lady Boss" "Correct."
    hide a curious 
    show a sarcastic  
    a "I didn't know you were so good at riddles." 
    u "Don't underestimate a logic student." 
    hide a sarcastic 
    show a mischievous 
    a "Are you retarded?" 
    hide a mischievous 
    show a sarcastic 
    a "There're farmers who can get this correct, and you're bragging about it being because you're studying logic?" 
    u "Of course." 
    "I obviously understood that my comment was meaningless, but fuck you, I'm not admitting it." 
    hide a sarcastic 
    show a suspicious 
    a "..." 
    hide a suspicious 
    show a resigned 
    a "{i}Sigh.{/i}" 
    u "..."
    hide a resigned 
    show a happy 
    a "Ah, Lady Boss, thanks!" 
    "Lady Boss" "No problem." 
    "Lady Boss" "Have a nice date, you two." 
    hide a happy 
    show a flustered 
    "We both blushed slightly." 
    "It was a common understanding between the two of us that we look like we're on a date." 
    "But having it pointed out was a completely different matter from pointing it out ourselves." 
    "Lady Boss" "Haha, look how cute you two are." 
    "Lady Boss" "Don't worry, your secret's safe with me." 
    "So she already knew from the beginning." 
    "Fuck." 
    a "Thanks..." 
    hide a flustered 
    u "..." 
    scene bgblack with fade 
    "We left." 
    scene bgchristmasmarket with fade 
    show a contemplative 
    a "Where should we go now..." 
    u "..." 
    hide a contemplative 
    show a pout 
    a "Don't be so silent; just say something randomly." 
    u "Ho—" 
    hide a pout 
    show a annoyed 
    a "If you say 'home', I'll make sure you can't sit for the rest of the holidays." 
    "Geez, how violent." 
    u "Christmas tree." 
    hide a annoyed 
    show a happy 
    a "Right, let's go!" 
    call sAB14 from _call_sAB14_1 

label riddle1wrong: 
    $ renpy.block_rollback() 
    show ladyboss at left 
    "Lady Boss" "Is that your answer or his." 
    python: 
        if A == B: 
            python.hide('a curious')  
            python.show('a happy')  
            renpy.say(who='Feng Qiuyue', what="Ours.") 
        else: 
            python.hide('a curious') 
            python.show('a smirk') 
            renpy.say(who='Feng Qiuyue', what="His.") 
    "Lady Boss" "Oh, OK." 
    "Lady Boss" "Anyways, it's wrong." 
    hide a smirk 
    show a disappointed 
    a "Har?" 
    a "Can you check again?" 
    "Lady Boss" "Huh?" 
    "Lady Boss" "I've already memorised the answers, you don't need to bother trying to muddle through this." 
    u "..." 
    "How embarrassing." 
    "What the hell did I expect when I'm going out with this shameless girl?" 
    hide a disappointed 
    show a annoyed 
    a "But still—"
    "Lady Boss" "Nope. Scram." 
    hide a annoyed 
    show a resigned 
    a "Alright..." 
    "Why's she being so competitive?" 
    "I'm so damn embarrassed..." 
    scene bgblack with fade 
    "We left." 
    scene bgchristmasmarket with fade 
    show a curious 
    a "Where do you want to go now?" 
    "Her mood was quite low from being shouted at by the Lady Boss." 
    u "Don't know." 
    hide a curious 
    show a disdainful 
    a "Of course, you don't." 
    a "Uhm... Let's just go to the Christmas tree!" 
    hide a disdainful 
    show a excited 
    "Her previous upbeat mood was restored." 
    u "{i}Sigh{/i}." 
    hide a excited 
    show a annoyed 
    a "What's that sigh supposed to mean?" 
    u "..." 
    "It means that I'm tired of being with you." 
    "Not that I would ever say that, though." 
    $ del Q, W1, W2, C, B 
    call sAB14 from _call_sAB14_2 

label sAB14: 
    ""
return 