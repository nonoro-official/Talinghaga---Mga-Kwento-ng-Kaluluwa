define a = Character("Anghel", what_italic=True)

# Image declarations
image lazarus neutral = "images/characters/lazarus/neutral.png"
image lazarus distressed = "images/characters/lazarus/distressed.png"

# ACT 4 START
label act4_start:

    scene black with fade
    play music "audio/act4/act4_softcalmmusic.ogg"

    a "Bilang gantimpala sa iyong pananampalataya at pagtitiis, ikaw ay dadalhin sa kapahingahan."
    a "Ngunit alalahanin mo ang iyong landas, upang ito’y maging liwanag sa iba."

    if journal_memory == "forgiveness":
        jump memory_forgiveness
    elif journal_memory == "suffering":
        jump memory_suffering
    elif journal_memory == "faith":
        jump memory_faith
    elif journal_memory == "childhood":
        jump memory_childhood
    else:
        jump act4_cont

label memory_forgiveness:
    play music "audio/act4/act4_nostalgiamemorymusic.ogg"
    show lazarus neutral with dissolve
    "‘Ang Aking Kabataan’ — Noong ako’y nagtratrabaho sa ubasan. Noon ay may saya pa."
    pause 2
    hide lazarus with dissolve
    jump act4_cont

label memory_suffering:
    play music "audio/act4/act4_nostalgiamemorymusic.ogg"
    show lazarus distressed with dissolve
    "‘Ang Aking Pagkakasakit’ — Ako’y bumagsak sa lansangan, walang sino mang tumulong."
    pause 2
    hide lazarus with dissolve
    jump act4_cont

label memory_faith:
    play music "audio/act4/act4_nostalgiamemorymusic.ogg"
    show lazarus neutral with dissolve
    "‘Pananalig sa Gitna ng Gutom’ — Ako’y nanalangin kahit walang laman ang tiyan."
    pause 2
    hide lazarus with dissolve
    jump act4_cont

label memory_childhood:
    play music "audio/act4/act4_nostalgiamemorymusic.ogg"
    show lazarus neutral with dissolve
    "‘Pagpapaumanhin’ — Pinatawad ko si Don Marciano bago pumikit magpakailanman."
    pause 2
    hide lazarus with dissolve
    jump act4_cont

label act4_cont:
    stop music fadeout 2.0
    play music "audio/act4/act4_peacefulendingmusic.ogg"

    show lazarus neutral with dissolve
    l "Sa kahirapan, hindi ako nawalan ng pananampalataya."
    l "Sa sakit, hindi ko isinuko ang aking kaluluwa."
    l "Ngayo’y ako’y nasa kapahingahan... at ang Panginoon ay tapat."

    hide lazarus with dissolve
    scene black with fade
    pause 2

    return
