label road:
    scene road
    a "J'espère ne pas devoir marché trop longtemps, j'ai déja chaud et l'air est tellement sec"
    "..."
    "..."
    scene batiment
    a "j'ai réussis enfin.."
    scene black
    with fade
    " "
    "???" "il respire toujours?" 
    "???" "oui on dirait qu'il a juste perdu connaissance"
    "???" "il a eu de la chance, encore un peu et il y passait.{w} bon allez, on va le ramener à.."
    scene maison
    with fade
    a "j'ai soif..{w} mais que.. comment je suis arriver la?!"
    "???" "du calmes mon garçon, tout vas bien tu es en sécurité ne t'en fais pas, dis moi, comment tu t'appelle?"
    a "je.. Steve, je m'appelle Steve"
    show vieu at left
    doc "moi c'est Robert, je suis médecin, tu t'es évanoui avec la désydratation. Heureusement notre équipe de ravitaillement t'as trouvé à temps. Tu as surements des questions, poses les"
    menu:
        "ou sommes nous?":
            doc "Chez moi, dans un petit village à quelques kilomètres de la ville. On s'est réfugier ici quand tout à commencer.."
        "votre équipe de ravitaillement?":
            doc "oui, quand tout à commencé, c'était le chaos et avec mon age je ne pouvait pas me réaprovisioné ni me défendre donc j'ai recueillit des personnes, je les soignes et les héberges et en échange, elles m'aide à entretenir et réaprovisioner le camp"
    a "Quand quoi à commencé?"
    doc "   {w}la pandémie enfin! Vous êtes sur que ça va?!"
    a "excusé moi, pour tout vous dire, je me suis réveiller il y a quelques jours près d'une usine sans aucun souvenir, je ne sais pas ou je suis ni ce qu'il s'est passé"
    N "un voile passa sur le visage du vieil homme, une immense peine semblat s'emparer de lui l'espace d'un instant avant de laissez place au sourir qu'il vous offre depuis votre réveil"
    doc "ça s'est passé il y a quelques années, un jour un nouveau virus est apparu il avait un nom de bière et s'était déclarer loin de chez nous alors les gens en plaisantait candidement"
    doc "puis des personnes infecter sont apparues dans des pays voisins et les morts ont commencé à se multiplié, le virus à se répandre jusqu'a dépasser la grande peste"
    doc "les gens ont tenté de s'isolé, l'armée de contenir le virus et les labos de trouvé un remède en vain"
    doc "puis un jour quelque choses s'est produit, on ne sais ni pourquoi ni comment mais les morts on commencé à se relever et à attaquer les survivants, à ce moment ce qu'il restait de la société s'est éffondré.."
    "???" "Ha le nouveau est réveillé!!"
    show happy_oz at right
    with dissolve
    doc "je vais vous laissez j'ai des choses à faire. Et essayez de le ménager"
    hide vieu with dissolve
    show base_sarah at left
    with dissolve
    "???" "Salut, je suis Sarah et la boule d'énergie qui est entrée juste avant c'est Oz"
    a "Ha enchanter Je m'appelle Steve. Et votre voix m'est famillière, on s'est déja rencontré?"
    oz "Eh bien c'est nous qui t'avons ramener donc d'une certaine façon oui"
    a "c'est vous l'équipe de ravitaillement? Merci beaucoup"
    sarah "ne nous remercie pas trp vite, on compte bien te mettre à profit. on te laisses te reposer aujourd'hui, oz vas te montrer les endroits importants et demain tu nous accompagnera pour récupérer de l'eau"
    hide base_sarah with dissolve
    oz "à nous deux, suis moi je vais te montrer la cuisine pour commencer et t'expliquer les règles"
    scene cuisine_maison
    oz "voila donc c'est ici que l'on mange, les vivres sont partagés par le nombre de personnes. Pour le moment il y a moi, Sarah, le doc et l'équipe d'exploration et de néttoyage composé de Loris et Léa"
    oz "on te les présentera à leurs retours et selon comment tu te débrouillera demain tu sera répartis dans une des deux équipes."
    oz "tu as déja vu ta chambre, reste la salle de bain et la piece la plus importante"
    scene douche_maison
    oz "je sais ce n'est pas le grand luxe et l'eau viens de cuve qui récupère la pluie donc pas d'eau chaude et pas des douches de plus de 5 minutes!"
    oz "Et enfin.."
    scene bunker
    with fade
    oz "le bunker! {w} alors?! tu en pense quoi?!"
    $oz_love = 1
    menu:
        "c'est.. en bordel?":
            $oz_love -= 1
            oz "..."
        "whaw! c'est super!":
            $oz_love += 1
            oz "Je sais, j'adore cette endroit!"
    oz "c'est ici qu'on se réfugie en derniers recours, on y a stocké suffisement de vivre pour tenir mais interdiction d'y toucher! Et pour le moment, tu ne dois pas y entrer seul compris?"
    a "heu d'accord de toutes façons, c'est pas comme si j'avais des choses à faire ici"
    oz "bon allez, va te reposer demain on se lève à l'aube"
    a "d'accord bonne nuit à toi"
    scene maison
    with fade
    a "je ferais mieux de dormir directement"
    scene black 
    with fade
    "..."
    "..."
    a "yaaawn {w} Bon je ferait bien de me préparer et d'allez voir ce qu'il m'attends"
    scene cuisine_maison
    with fade
    show base_sarah at left
    with dissolve
    sarah "Tiens je ne m'attendait pas à ce que tu arrives à te lever"
    show happy_oz at right with dissolve
    oz "Ha je te l'avais dit sarah, tu me dois une ration!"
    a "Bonjour les filles, alors, c'est quoi le programme pour aujourd'hui?"
    oz "déja on déjeune! {w} Bon pour aujourd'hui tu auras une de mes rations comme tu as su te lever seul mais les autres jours tu auras intérêts à mérité de rester!"
    $point_faim = 0
    sarah "Ce qu'elle veut dire c'est que nos ressources ne sont pas infinies et on a déja du sacrifier beaucoup d'eau pour te sauver donc tu vas devoir nous aider et nous prouvez qu'on a eu raison"
    a "j'y compte bien et déolé de vous avoir causé du soucis"
    hide base_sarah
    show loris at left
    loris "c'est donc toi le nouveau?! Bon ne perdons pas de temps, on a trouvé un super endroit, on l'a néttoyer et vous votre boulot ça va être d'allez récupérer un maximum de choses à l'intérieur et sans te blesser"
    hide happy_oz
    show lea at right
    lea "laisses le faire ses preuves avant de te moquer, il pourrait te surprendre le petit"
    hide loris 
    show oz with dissolve
    oz "Bon! on va peut être se mettre en route, c'est quoi cet endroit que vous avez trouvé?"
    lea "on est tombé sur un magasin plus loin sur la route et la bonne nouvlle c'est qu'il n'a pas l'aire d'avoir été piller"
    sarah "bien on se met en route immédiatement Stev Oz on y va"
    scene road
    with fade
    "  "
    scene magasin
    with fade
    a "comment on procède?"
    oz "on fait le tour pour vérifier qu'il n'y a pas de danger, on trouve une entrée puis sarah et moi on va remplir nos sac pendant que tu surveilles que rien ne s'approche puis a notre retour on inverse"
    a "d'accord mais si il y a un danger je fait quoi?"
    sarah "tu aviseras sur le moment. Allez on y vas"
    "..."
    sarah "ça à l'aire désert, on va rentré par la porte de devant et essayer de faire vite"
    "..."
    "..."
    "groarrr" 
    show zombie02
    a "mais c'est quoi cette chose!!"
    menu:
        "attaquer":
            a "yaaaaaah"
            if oz_love < 1:
                jump first_mag_exploration_death
            else:
                jump attaque_mag_win
        "fuir":
            jump flee_mag

    return 
    with fade