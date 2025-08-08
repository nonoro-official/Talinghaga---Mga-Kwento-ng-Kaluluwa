# Characters
define a = Character("Anghel", what_italic=True)

# Image declarations
image lazarus neutral = "images/characters/lazarus/neutral.png"
image lazarus distressed = "images/characters/lazarus/distressed.png"

image bg heaven = "images/bg/heaven.png"

# ACT 4 START
label act4_start:
    scene bg heaven with fade
    play music "audio/act4/act4_softcalmmusic.ogg"

    a "Bilang gantimpala sa iyong pananampalataya at pagtitiis, ikaw ay dadalhin sa kapahingahan."
    a "Ngunit alalahanin mo ang iyong landas, upang ito’y maging liwanag sa iba."

    "Bubukas ang Memory Journal..."
    call screen memory_journal

    # Final Reflection
    l "Sa kahirapan, hindi ako nawalan ng pananampalataya."
    l "Sa sakit, hindi ko isinuko ang aking kaluluwa."
    l "Ngayo’y ako’y nasa kapahingahan... at ang Panginoon ay tapat."

    window hide

    pause 1.0

    call screen credits

    return