﻿label wA13: 
    u "I want to eat roast beef sandwich." 
    a "Huh,{w=.1} that sounds great." 
    a "I'll try it,{w=.1} too!"
    "We walk up to the stall."
    "Shopkeeper A" "Hey,{w=.1} do you want to try some roast beef?{w=.3} I have some samples!" 
    "He reveals a plate with multiple pieces of roast beef impaled by toothpicks." 
    "Without hesitation,{w=.1} [a] picks one up and tries it." 
    a "Wow,{w=.1} this is great." 
    a "Honey,{w=.1} I want to eat this." 
    u "..." 
    "I was completely thrown off-guard." 
    "I completely forgot about the bullshit with the couple's discount." 
    "Shopkeeper A" "You're dating?{w=.3} Then I'll give you a 10\% discount." 
    u "Alright,{w=.1} umm..." 
    u "Then,{w=.1} get me 4 pieces." 
    "Shopkeeper A" "A'ight,{w=.1} 28 RMB." 
    "The sale price of the sandwich is 30 RMB." 
    u "Do you think I can't do basic math?" 
    u "90\% of 30 is 27." 
    "Shopkeeper A" "Alright,{w=.1} I'll make a loss and sell it for 27." 
    "I'm speechless." 
    "How can anyone be so shameless?" 
    jump wA14 

label wA14: 
    "We sat down by a side with food." 
    a "Ahh,{w=.1} how warm!" 
    "She squeezed on the sandwich like it was a hand warmer." 
    u "..." 
    u "Just eat it." 
    a "Don't wanna,{w=.1} we ran out of hand warmers at home!" 
    u "So?" 
    a "So,{w=.1} I'm cold!" 
    u "Then bear with it." 
    u "Oh,{w=.1} I almost forgot." 
    u "You owe me 13.5 RMB." 
    a "Huuh?{w=.3} Why?" 
    u "Because I bought the sandwich for you." 
    a "Hmph,{w=.1} how stingy." 
    "She hands over one of her two sandwiches." 
    "To be more specific,{w=.1} the one she squished to leech the warmth off of." 
    a "Now,{w=.1} I owe you 6.75 RMB." 
    u "...Fine." 
    "I reluctantly accepted the sandwich." 
    u "Can you really be full with just that?" 
    a "Of course." 
    "Sure enough,{w=.1} she seemed satisfied after eating that sandwich. " 
    "Her expression was cute." 
    a "Ahh,{w=.1} I'm so full!" 
    u "Nice." 
    a "I'll buy a log cake!" 
    u "...{w=.3}Aren't you full?" 
    a "Haven't you heard that a girl has a second stomach for sweets?" 
    u "..." 
    "I gave up reasoning with her. " 
    u "We can't really eat a log cake here,{w=.1} so it'd be better if you got something more portable." 
    a "Fine,{w=.1} I'll get an ice cream." 
    u "Ice cream?{w=.3} It's...{w=.3} winter...{w=.3} you know?" 
    a "It's exactly because it's winter that I'm eating ice cream!" 
    a "The ice cream won't melt so fast anymore." 
    u "..." 
    u "Whatever." 
    a "Come with me." 
    u "Why?" 
    a "C{w=.3}-o{w=.3}-u{w=.3}-p{w=.3}-l{w=.3}-e{w=.3}'s{w=.3} d{w=.3}-i{w=.3}-s{w=.3}-c{w=.3}-o{w=.3}-u{w=.3}-n{w=.3}-t." 
    u "{i}Sigh.{/i}" 
    u "After I'm done with my sandwiches." 
    a "OK." 
    a "..." 
    a "Right,{w=.1} no one asked us for proof when we bought the sandwiches." 
    a "Pft,{w=.1} you thought waayy too much about the couple's discount thing!" 
    u "Whatever." 
    "Her laughter was annoying. " 
    "I bought her ice cream later." 
    "Naturally,{w=.1} she had to return the cost of the ice cream to me later." 
    "I guess she completely forgot about eggnog." 

menu: 
    a "What're we going to do now?" 

    "We should go to the competition stage.": 
        call sxA15 
    #TODO BwA15 
return 