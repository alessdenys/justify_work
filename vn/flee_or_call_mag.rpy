label flee_mag:
    menu:
        "pris de panique, vous décider de : "
        "partir en courant pour sauver votre vie":
            jump courage_fuyons
        "hurler aux filles de se dépĉher et essayer de vous cacher":
            N "après avoir prévenu les filles du danger, vous décider de vous cacher dans un bac à ordures en espérant leurs échapper et vous mettez à pleurer"
    a "pitié je ne veux pas mourir la dedans!"

label courage_fuyons:
    N "emporté par la terreur, vous commencer à courire sans vous retourner. Vous courez le long d'une route plusieurs minutes durant jusqu'a attendre un batiment dans le quel vous entrez en trombe, vous vous éffondrer au sol épuiser et tenter de reprendre votre souffle"
    scene batiment
    with fade
    N "alors que vous commencez"
