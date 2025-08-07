# Characters
define d = Character("Don Marciano")
define l = Character("Lazaro")
define n = Character("Narrator", what_italic=True)

# Image declarations
image donmarciano shocked = "images/characters/richman/shocked.png"
image lazarus distressed = "images/characters/lazarus/distressed.png"

# ACT 2 START
label act2_start:

    # Scene 1: Lazarus’s Final Breath
    scene black with slow_fade
    play sound "audio/act2/act2_coldwind.ogg"

    show lazarus distressed with dissolve
    l "Panginoon... kung ito na po ang wakas, ako'y handa."
    l "Sa gutom at kirot, di Mo ako iniwan."
    l "Nawa'y matagpuan Ko ang Inyong liwanag."

    # Angelic transition
    play music "audio/act2/act2_angelchoirmusic.ogg"
    pause 2
    hide lazarus with dissolve

    n "At siya'y kinuha ng mga anghel at dinala sa piling ni Abraham."

    stop music fadeout 2.0
    scene black with fade
    pause 1

    # Scene 2: The Rich Man’s Sudden Death
    play sound "audio/act2/act2_grouplaughing.ogg"
    pause 2
    stop sound

    play sound "audio/act2/act2_heartbeat.ogg"
    pause 2

    show donmarciano shocked with dissolve
    d "Anong... anong nangyayari? Hindi... hindi ako pwedeng mamatay ngayon!"

    play sound "audio/act2/act2_bodycollapse.ogg"
    pause 1
    hide donmarciano with dissolve

    n "At ang mayamang lalaki'y namatay rin, at siya'y inilibing."

    scene black with fade
    pause 1

    # Scene 3: The Great Divide (Afterlife)
    play sound "audio/act2/act2_scaryambience.ogg"
    pause 2

    show donmarciano shocked with dissolve
    d "Ama Abraham! Mahabag ka sa akin!"
    d "Ipadala mo si Lazaro upang isawsaw ang dulo ng kanyang daliri sa tubig at palamigin ang aking dila!"
    d "Ako’y pinahihirapan sa apoy na ito!"

    stop sound fadeout 2.0
    scene black with fade

    jump act3_start
