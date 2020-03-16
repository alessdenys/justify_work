label caught:
    a "Hey! Je ne vous veux aucun mal, je.. je ne sais pas trop ou je suis, vous pourriez m'aider?"
    "..."
    a "Heu madame?"
    "???" "groaar"
    a "J'aurai juste besoin d'.. elle est partie"
    a "{i}Je ferai surement mieux de rentrer, elle m'a un peu fait flipper avec ces grognement{/i}"
    scene sleep with fade
    a "{i}Je vais dormir un peu et j'irait explorer l'endroit demain{/i}"
    scene black with fade
    scene shelter with fade
    a "yhaaa. J'spère que je trouvais un meilleur lit, mon dos commence à me faire mal"
    $point_energie = 3
    jump day_2

    return
    with fade

label safe_than_sorry:
    a "snaaaaake!"
    return 
    with fade

label sneak_shadow:
    N "petit filou"
    return
    with fade