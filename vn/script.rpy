
define a = Character('Steve', color="#00faed")
define N = Character('narrateur', color="#b59be6")
# start game
label start:
    scene black
    with fade
    a "arg! Ma tête.."
    scene shelter
    with fade
    a "mais je suis ou bon sang!! Et qu'est ce qu'il s'est passé?"
    a "J'ai du mal à me souvenir..{w} Mais bon sang qu'est ce qui s'est passé?"

    $ self_control = False
    $ point_energie = 1
    $ point_faim = 0
    
    menu:
        a "j'ai besoi de"
        "me calmer":
            $ self_control = True
        "me souvenir":
            a "Souvies toi, souviens toi, souviens toi!"
            
    return 
    with fade