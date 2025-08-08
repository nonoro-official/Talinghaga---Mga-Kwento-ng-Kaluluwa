# Characters
define a = Character("Abraham")

# Image declarations
image donmarciano desperate = "images/characters/richman/desperate.png"
image lazarus neutral = "images/characters/lazarus/neutral.png"
image abraham = "images/characters/abraham.png"

image bg chasm = "images/bg/chasm.png"

# Transforms for dual-character positioning with highlighting
transform left_focused:
    xalign 0.2
    yalign 1.0
    alpha 1.0
    xzoom -1.0

transform left_dim:
    xalign 0.2
    yalign 1.0
    alpha 0.5
    xzoom -1.0

transform right_focused:
    xalign 0.8
    yalign 1.0
    alpha 1.0

transform right_dim:
    xalign 0.8
    yalign 1.0
    alpha 0.5

# ACT 3 START
label act3_start:

    scene bg chasm with fade
    play sound "audio/act3/act3_firesound.ogg"

    show donmarciano desperate at right_dim
    show abraham at left_focused

    a "Anak, alalahanin mong sa buhay mo, tinanggap mo na ang mabubuting bagay..."
    a "samantalang si Lazaro ay pawang masasama."
    a "Ngayo’y siya ang inaaliw, at ikaw ang pinahihirapan."

    play sound "audio/act3/act3_earthcrumbling.ogg"
    pause 2

    a "Bukod pa rito, may malaking bangin sa pagitan natin."
    a "Hindi pwedeng tumawid ang sinuman mula rito patungo sa inyo, ni mula sa inyo patungo rito."

    show donmarciano desperate at right_focused
    show abraham at left_dim

    d "Kung gayon, Ama Abraham, ipadala mo na lang si Lazaro sa aking ama’t bahay!"
    d "Mayroon akong limang kapatid."
    d "Paalalahanan mo sila upang hindi rin sila mapunta rito sa kapighatian!"

    show donmarciano desperate at right_dim
    show abraham at left_focused

    a "Nasa kanila si Moises at ang mga Propeta. Pakinggan nila ang mga iyon."

    show donmarciano desperate at right_focused
    show abraham at left_dim

    d "Hindi po, Ama Abraham!"
    d "Ngunit kung may isang bumangon mula sa mga patay, sila’y maniniwala!"

    show donmarciano desperate at right_dim
    show abraham at left_focused

    a "Kung hindi sila makikinig kay Moises at sa mga Propeta..."
    a "...hindi rin sila mahihikayat kahit may bumangon mula sa mga patay."

    stop sound fadeout 2.0
    scene black with fade
    play sound "audio/act3/act3_intensefiresound.ogg"
    pause 2

    jump act4_start
