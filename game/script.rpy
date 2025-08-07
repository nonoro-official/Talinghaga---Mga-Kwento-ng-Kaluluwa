# Characters
define d = Character("Don Marciano")
define l = Character("Lazaro")

# Route Variable
default journal_memory = "none"

init python:
    renpy.music.set_volume(1.0, delay=0, channel='music')
    renpy.music.set_volume(1.0, delay=0, channel='sound')

# Transition
define slow_fade = Fade(0.5, 0.0, 0.3)  # 3 seconds fade 

label start:

    # OPENING PROLOGUE  
    

    # Act 1
    call act1_start from act1

    # This ends the game.

    return
