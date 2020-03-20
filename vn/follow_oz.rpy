label train_with_oz:
    show base_oz  at left with dissolve 
    oz "Super! Suis nous"
    " "
    scene training with fade
    oz "bien prends cette épée en bois, on va déja voir comment tu te débrouilles face à un humain"
    show oz_fight at left with dissolve
    $fight = True
    $hp_oz = 3
    $hp_a = 3
    $coups = 0
    while fight == True:
        menu:
            "attaquer":
                if hp_oz == 0:
                    N "après ce dernier coup, Oz lève ss mains en signe de défaite."
                    $win = True
                    fight = False
                elif hp_a == 0:
                    N "après les coups que tu as reçus, tu sens la colère t'envahir et tu frappe de toutes tes forces une dernière fois"
                    "SMACK!!!!"
                    $win = False
                    fight = False
                    
                elif coups % 2 == 0:
                    $hp_oz -= 1
                    $coups += 1 
                    "smack!!"
                    N "Ton épée de bois fend l'air avant de s'abbatre sur ton partenaire"
                else:
                    N "elle part ton coup avant d'attaquer ton flanc laissé libre"
                    $hp_a -= 1
                    $coups += 1
