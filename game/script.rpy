# Characters
define d = Character("Don Marciano")
define l = Character("Lazaro")

# Route Variables
default journal_memory = "none"

init python:
    if not hasattr(persistent, "found_journal"):
        persistent.found_journal = []

    renpy.music.set_volume(1.0, delay=0, channel='music')
    renpy.music.set_volume(1.0, delay=0, channel='sound')

    def unlock_journal_entry(entry_id):
        if entry_id not in persistent.found_journal:
            persistent.found_journal.append(entry_id)
            renpy.save_persistent()

    def journal_entry_unlocked(entry_id):
        return entry_id in persistent.found_journal

# Transition
define slow_fade = Fade(0.5, 0.0, 0.3)  # 3 seconds fade 

label start:

    # OPENING PROLOGUE  
    

    # Act 1
    call act1_start from act1

    # This ends the game.

    return
