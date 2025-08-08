# Characters
define s = Character("Servant")

# Images
image donmarciano smug = "images/characters/richman/smug.png"
image donmarciano shocked = "images/characters/richman/shocked.png"
image donmarciano neutral = "images/characters/richman/neutral.png"

image lazarus distressed = "images/characters/lazarus/distressed.png"
image lazarus neutral = "images/characters/lazarus/neutral.png"

image bg richdining = "images/bg/richdining.png"
image bg streetdark = "images/bg/streetdark.png"

# ACT 1 START
label act1_start:

    # Scene 1: Inside the Mansion (Don Marciano POV)
    scene bg richdining with dissolve
    play music "audio/act1/act1_richpeoplemusic.ogg"
    play sound "audio/act1/act1_dinneratmosphere.ogg"

    show donmarciano smug with dissolve
    d "Hah! Isa na namang matagumpay na araw. Ang buhay ay para sa mga may kaya, hindi ba?"

    show donmarciano shocked with dissolve
    d "Nasa labas na naman si Lazaro? Tsk. Lagi na lang siya nandiyan. Ba’t di siya umalis?"

    s "Ginoo, hindi po siya kumakain. May lagnat din yata..."

    show donmarciano neutral with dissolve
    d "Hindi ko problema ‘yan. Ako ba ang Diyos niya?"
    d "Ayokong marinig ang kanyang ungol. Sabihan mo siyang lumayo sa pinto ko."

    stop music fadeout 1.5
    scene bg streetdark with slow_fade

    # Scene 2: Outside the Gate (Lazaro POV)
    play music "audio/act1/act1_sadmusic.ogg"
    play sound "audio/act1/act1_dog.ogg"

    show lazarus distressed with dissolve
    l "{i}Panginoon... gutom na naman ako.{/i}"

    show lazarus neutral with dissolve
    l "{i}Kahit mumo lang sana... kahit kapiraso mula sa hapag ng mayaman.{/i}"
    l "{i}Pero kahit aso, mas pinapansin pa kaysa sa akin.{/i}"

    menu:
        "Patawarin mo sila, Panginoon.":
            $ journal_memory = "forgiveness"
        "Hanggang kailan ang sakit na ito?":
            $ journal_memory = "suffering"
        "Bigyan mo pa po ako ng lakas.":
            $ journal_memory = "faith"
        "...":
            $ journal_memory = "childhood"

    # Unlock only the chosen entry
    $ unlock_journal_entry(journal_memory)

    hide lazarus with dissolve
    stop music fadeout 1.5
    scene black with fade

    "{i}At araw-araw, sila'y nagkikita... ngunit kailanman, hindi sila nagtagpo.{/i}"
    "{i}Ngunit darating ang araw — ang huling araw — na babaligtad ang mundo.{/i}"

    window hide

    jump act2_start
