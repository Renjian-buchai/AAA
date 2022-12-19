label DD: 
label Definitions: 
    init python: 
        import math 
        import random 
        import time 
        import threading 
    
    init: 
        # Characters 
        define u = Character("[persistent.username]")   
        define a = DynamicCharacter("A_name")

        # Persistent
        default persistent.sxA23 = False
        default persistent.BwA23 = False 
        default persistent.LBwA23 = False 
        default persistent.username = None
        default persistent.gameState = 0 

        # Movies 

        # Music 
        define ttt = "./audio/2.23_AM.mp3" 
        define tot = "./audio/3.03_PM.mp3" 
        define tdc = "./audio/10dC.mp3" 
        define sct = "./audio/Santa_Claus_is_coming_by_Train.mp3"
        define lgt = "./audio/The_lonely_ghost_and_the_moon_of_Tokyo.mp3"
        define yam = "./audio/You_and_Me.mp3" 
        define ctd = "./audio/Cassette_Tape_Dream.mp3"
        define st = "./audio/SUMMER_TRIANGLE.mp3" 
        define m1 = "./audio/Fizzy_Honey_Lemon_Soda_350ml.mp3"
        define m2 = "./audio/Lo-fi_girl_always_lacks_sleep.mp3"
        define m3 = "./audio/Sheep_of_the_Far_East_Dancing_with_the_Telecaster.mp3"

label Dictionaries: 
    python: 
        # Riddle Guessing Game 
        Riddle0 = {  
        0: ('Five brothers, living together, with different names and uneven heights.', "Quintuplets", 'Fingers', 'Siblings'), 
        1: ('A black boy who never speaks. When he does, his tongue falls out.', 'An African peasant', 'Sunflower seeds', 'Leaking pens'), 
        2: ('When people take off their clothes, it wears clothes. When people wear their clothes, they take off their clothes', 'Voyeurs', 'Clothes racks', 'The \'toys\' in [a]\'s drawers'), 
        3: ('The square house has doors not windows, keeping it frosty outside and warm inside.', 'Ice house', 'Freezers', 'Igloos'), 
        4: ('Tall buildings made of single wood, no tiles or bricks, people walk under the water, and the water flows up the people.', 'Wooden shack', 'Umbrella', 'Raincoats')} 

        Riddle1 = {  
        0: ('The hunchbacked old man has great strength; he likes to carry whatever when everyone is busy (guess an item).', 'Bridge', 'Table', 'Hook'), 
        1: ('The head of a sheep and the neck of a goose, it can endure thirst and hunger. (guess an animal).', 'Camel', 'Tenghuang', 'Horse'), 
        2: ('Lives on the top of Qingshan Mountain, wears a ragged coir raincoat, often swims in the sky, and loves to eat chickens. (guess an animal)', 'Eagles', 'Pilots', 'Vultures'), 
        3: ('There is a face but no mouth, and feet but no hands. Although there are four legs, they cannot walk by themselves.', 'Table', 'Chair', '2 whole frozen chickens from the supermarket'), 
        4: ('Wearing green clothes, the belly is watery, has many children, and all of them have black faces.', 'Watermelon', 'A cuckold', 'Vegetarians')} 

return 
return 