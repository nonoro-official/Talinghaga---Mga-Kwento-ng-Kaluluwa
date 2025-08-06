# Characters
define d = Character("Don Marciano")
define l = Character("Lazaro")
define s = Character("Servant")

# Route Variable
default journal_memory = "none"

# Transition
define slow_fade = Fade(0.5, 0.0, 0.3)  # 3 seconds fade 

label act1_start:

    # Scene 1: Inside the Mansion (Don Marciano POV)

    # play music 

    scene bg banquet with fade

    show don marciano happy with dissolve

    d "Hah! Isa na namang matagumpay na araw. Ang buhay ay para sa mga may kaya, hindi ba?"

    show don marciano annoyed with dissolve

    d "Nasa labas na naman si Lazaro? Tsk. Lagi na lang siya nandiyan. Ba’t di siya umalis?"

    s "Ginoo, hindi po siya kumakain. May lagnat din yata..."

    show don marciano smirks with dissolve

    d "Hindi ko problema ‘yan. Ako ba ang Diyos niya?"

    d "Ayokong marinig ang kanyang ungol. Sabihan mo siyang lumayo sa pinto ko."

    # Scene 2: Outside the Gate (Lazaro POV)

    scene bg street with fade

    l "{i}Panginoon... gutom na naman ako.{/i}"

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

    "At araw-araw, sila'y nagkikita... ngunit kailanman, hindi sila nagtagpo."

    "Ngunit darating ang araw — ang huling araw — na babaligtad ang mundo."

    scene blackscreen with fade

    return
    