label attaque_mag_win: 
    N "Vous vous élancez armé du tuyau récupérer dans votre chambre et lui porté un coup au visage, le faisant vaciller"
    N "Alors que vous vous apprétez a porter un second coup, une main vous agrippe le bras et vous tires vers l'arrière vous entrainant au sol et vous sauvant d'une seconde créature qui vous attaquait par le flanc"
    a "Qu'est ce que.."
    show zombie01 at left with dissolve
    show angry_oz at right with dissolve
    oz "T'es malade?! Tu aurait pu y rester si je t'avais pas garder à l'oeil!{w} Bon, tiens toi prêts, ils nous laisseront pas nous en sortir si facilement, on va devoir les éliminés"
    a "Et Sarah?!"
    oz "elle remplit les sacs mais concentrons nous sur eux déja!"
    N "vous réattaquer ensemble prenant chaqu'un une créature, aubout de plusieurs minutes d'acharnement vous finissez par vaincre votre cible en vous retournant pour aider votre amie, vous vous rendez compte qu'elle vous observes souriante la créature à ses pieds"
    sarah "Bon vous compter m'aider un jour?"
    hide angry_oz with dissolve
    a "Désolé j'arrive tout de suite!"
    N "Vous rentrez tous ensemble vos sac remplis de vivre pour une bonne semaine et avec la confiance de vos nouveaux camarades"
    scene cuisine_maison
    with fade
    show base_sarah at left
    sarah "merci de nous avoir aidé, je vais allez me reposer bonne nuit a vous deux"
    hide base_sarah with dissolve
    show base_oz at left with dissolve
    oz "Suis moi."
    scene bunker with dissolve
    a "Tu voulais me parler?"
    show base_oz at left
    oz "Oui, ce que tu as fait tout à l'heure était dangereux. Tu serais mort si je n'était pas intervenu. Toutefois, tu as fais preuve de courage et tu ne nous as pas abandonner. Tu as gagner notre confiance alors si tu souhaite rejoindre notre équipe, nous t'accepteront."
    oz "Maintenant va te coucher, il est tard et la journée à été longue, dors et réfléchis à ce que je viens de te dire."
    a "Merci je vais y réflechir. Bonne nuit Oz."
    scene maison with fade
    a "je suis épuiser et mes musccles me font souffrir, elle a raison je ferais mieux de me reposer."
    jump jour_3

