# Characters
define a = Character("Anghel", what_italic=True)

# Image declarations
image lazarus neutral = "images/characters/lazarus/neutral.png"
image lazarus distressed = "images/characters/lazarus/distressed.png"

# ACT 4 START
label act4_start:
    scene black with fade
    play music "audio/act4/act4_softcalmmusic.ogg"

    "Bilang gantimpala sa iyong pananampalataya at pagtitiis, ikaw ay dadalhin sa kapahingahan."
    "Ngunit alalahanin mo ang iyong landas, upang ito’y maging liwanag sa iba."

    # DO NOT unlock all entries here!
    # Only show the memory journal screen to display unlocked entries

    "Bubukas ang Memory Journal..."
    call screen memory_journal

    # Final Reflection
    l "Sa kahirapan, hindi ako nawalan ng pananampalataya."
    l "Sa sakit, hindi ko isinuko ang aking kaluluwa."
    l "Ngayo’y ako’y nasa kapahingahan... at ang Panginoon ay tapat."

    scene white with fade
    "Lazarus walks toward the light. Peaceful music swells."

    call screen credits

    return