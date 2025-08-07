# Characters
define d = Character("Don Marciano")
define l = Character("Lazaro")
define s = Character("Servant")

# Route Variable
default journal_memory = "none"

# Transition
define slow_fade = Fade(0.5, 0.0, 0.3)  # 3 seconds fade 

label start:

    scene bg room

    # OPENING PROLOGUE  
    

    # Act 1
    call act1_start from act1

    # This ends the game.

    return
