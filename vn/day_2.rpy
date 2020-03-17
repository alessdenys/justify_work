label day_2:
    $usine_expl = False
    a "Il est temps d'explorer la zone, je n'ai même pas encore vu l'extérieur"
    scene usine
    a "J'étais surement dans la loge du gardien, l'endroit à l'aire immense mais aussi abandonné Tss"
    menu:
        a "Bon si je veux survivre et comprendre ce qui m'arrive, je doit explorer, mais par ou commencer?"
        "l'usine serait le plus logique vu qu'elle est juste devant mais je n'ai pas d'équipement":
            a "Tampis, je trouverai surement dedans"
            $usine_expl = True
            jump usine_first
        "Tiens un container, il contient peut être des choses utiles":
            jump containeur
        "Sinon je peut suivre cette route et espéré tomber sur une ville":
            jump road
    return
    with fade