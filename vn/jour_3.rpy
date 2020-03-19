label jour_3:
    a "yaaaawn"
    if etirement == False:
        a "j'aurai du m'étirer! je n'arrive même pas à me lever"
        jump debt
        
    else:
        a "j'ai bien fait de m'étirer, j'ai moins mal que je ne le pensais"
    scene cuisine_maison
    a "Bonjour tout le monde vous allez bien?"
    "Tous ensembles" "bien et toi?"
    show happy_oz at left with dissolve
    oz "Contente que tu ais su te lever! Sarah, tu me dois encore une ration!"
    a "J'avoue que je pensais avoir plus mal que ça, j'ai bien fait de m'étirer avant de dormir"
    a "Et donc qu'est ce qui est prévu aujourd'hui?"
    oz "Aujourd'hui tu as le choix, tu peux venir t'entrainer avec avec nous pour qu'on te montre quelques trucs et astuces ou tu peux t'entrainer avec l'équipe d'exploration pour pouvoir les suivre ce soir"

    menu:
        "je vais vous suivres":
            scene training
            with fade
            $oz_love += 1
            jump train_with_oz
        "j'aimerai voir comment fonction l'équipe d'exploration":
            scene construct
            N "cette partie n'est pas encore disponible"

    return
    with fade
label debt:
    a "je ne pense pas pouvoir me lever aujourd'hui"
    