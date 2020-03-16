
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
        
    if self_control == True:
        scene meditation
        with fade
        N "Au fil de ta vie tu as appris à maitriser tes émotion et ton énergie, cela te sera bénéfique."
        $ point_energie += 1 
    else: 
        a "ça ne sers à rien à part empirer mes migraines, je ferais mieux de dormir un peu.."
        $ point_faim += 1

    scene shelter    
    with fade

    if point_faim > 0:
        a " Je commence à avoir faim, je ferait bien de chercher si il y a de la nourriture ici."
    else:
        a "Bon je ferait bien de jeter un oeil aux alentours {w} déja, j'ai un.. \"lit\"."
    $ tuyau = False
    menu: 
        a "Je vais commencer par fouiller :"
        "la cuisine":
            scene black
            a "deux boites de haricots super.."
            $ point_faim -= 1
            $point_energie -=1
        "la chambre" if point_faim < 1:
            scene radiateur
            a "Ce tuyau n'as pas l'aire bien fixé, je devrait peut être le garder au cas ou."
            $ tuyau = True
            $ point_energie -= 1
    scene shelter
    menu:
        a "bon il commence à se faire tard, je ferais mieux de :"
        "me reposer directement":
            scene sleep with fade
            jump first_death
        "faire un tour rapide avant de dormir" if point_energie > 0:
            scene gaz with fade
            a "ha le gaz marche! bon à savoir,{w} tiens, je n'avais pas vu cette fenêtre."
    scene vitre_shelter with fade
    a "on dirait que je suis prêt d'une usine ou d'un entrepot. {w}c'était quoi ce bruit?!"
    "..."
    show ombre_femme at right 
    menu:
        a "ha super il y a d'autres gens!! je devrais : "
        "leurs faire savoir que je suis la, ils pourraient m'aider":
            jump caught
        "les suivre, ils ont peut être des chose intéressantes":
            jump sneak_shadow
        "les observer, ils pourraient être dangereux":
            jump safe_than_sorry
    return 
    with fade