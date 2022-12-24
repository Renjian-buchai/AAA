label AB6: 
    $ renpy.block_rollback()
    hide ina happy 
    show ina disappointed 
    a "Why noot~?" 
    u "Busy." 
    hide ina disappointed 
    show ina contemplative 
    a "Hmm? Then what if I told you there's a couple's discount if we pretend to date?" 
    u "Doesn't matter, still busy." 
    hide ina contemplative 
    show ina disdainful 
    a "What're you busy with?" 
    u "I'm busy with not going with you." 
    hide ina disdainful 
    show ina annoyed  
    a "What—{w=.3} Do you hate me {i}that{/i} much?" 
    u "No." 
    "I feel like she's trying to tease me." 
    "Wait, no, she's definitely trying to tease me." 
    hide ina annoyed 
    show ina smirk 
    a "Then, I'll have to use my trump card."
    u "?" 
    "I have a bad feeling about this..." 
    hide ina smirk 
    show ina excited 
    a "Your mom has already agreed to it." 
    u "Why?!" 
    hide ina excited 
    show ina mischievous 
    a "Discounts are always welcome, no?" 
    u "{i}Sigh{/i}, fine." 
    "If I don't take advantage of the discount, Mother will definitely beat me half to death." 
    jump AB7 

label AB7: 
    "I was reluctant, but those who stand under the eaves must bow." 
    u "Where? And when?" 
    hide ina mischievous 
    show ina smirk 
    a "Hmm... I wonder :3" 
    "She smirks evilly." 
    "I felt a vein throb in my forehead, but I forced my feelings of annoyance down." 
    u "Out with it." 
    hide ina smirk 
    show ina contemplative 
    a "Alright, then~{w=.3} Just come to my place at 17:30 hours~" 
    u "Why—{w=.3} Whatever."
    hide ina contemplative 
    scene bgblack with fade 
    jump AB8 

label AB8: 
    $ renpy.pause(1, hard=True)
    scene bgapartment with fade 
    "Around 17:30, I arrived at her apartment." 
    "I knocked on her door." 
    a "Sorry, give me a moment." 
    u "..." 
    "Seriously, weren't you the one who asked me to come here now?" 
    "It's not like I came earlier than appointed."  
    "With a few stumbling sounds, the door finally came out." 
    "Out came [a], wearing her indoor clothes and hugging a plushy." 
    show ina happy 
    u "You..." 
    a "Sorry, still have to change~{w=.3} Come in first." 
    hide ina happy 
    scene bgblack with fade 
    "I guess she thought it was bad for her to wait outside, considering the current temperature outside." 
    "It wasn't the first time I've been to her apartment, but somehow, the knowledge that she was changing into her outdoor clothes right now makes it feel different." 
    "Actually, did she invite me in whilst she's changing {i}because{/i} she just sees me as a friend?" 
    "How sad..." 
    scene bgapartmentint 
    show ina suspicious 
    a "Don't roam around." 
    u "Never intended to." 
    hide ina suspicious 
    show ina happy 
    a "Good." 
    u "..." 
    hide ina happy with dissolve 
    "Seriously, why did she even have to warn me about it?" 
    "I hadn't thought about it earlier, but now..." 
    "No, I'm a gentleman, I'm a buddhist monk, I'm a kind person." 
    "{i}Sigh{/i}, I think I've calmed down enough." 
    scene bgblack with fade 
    jump AB9 

label AB9: 
    $ renpy.pause(3, hard=True) 
    scene bgchristmasmarket with fade 
    "From her apartment, we went directly to the CHristmas market."
    "By the time we arrived there, it was around 18:00." 
    show a shocked 
    a "How crowded." 
    u "..." 
    "What am I supposed to say?" 
    "It's not crowded even though the entire market is teeming with people?" 
    a "It's more crowded than I expected." 
    "Well, I don't know {i}what{/i} you expected, but it is very crowded." 
    "No one celebrates Christmas eve in China, you said." 
    "And under the 996 schedule (9 to 9, 6 days a week), it was still a working day, you said." 
    "So it would not be crowded today, you said." 
    "Then she should also explain why the entire Christmas market was filled with people." 
    hide a shocked 
    show a curious 
    menu: 
        a "Then, what do you think we should we do now?" 
        "Drink": 
            jump eAB10 
        #TODO: BAB10, CAB10;  
return 