screen tbc:
    add "screens/tbc.png"

screen wiproute:
    add "screens/wip-route.png"

screen demothx:
    add "screens/demo-thx.png"

screen credits:
    add "screens/credits.png"

screen memory_journal():

    if not journal_open:
        add "journal_closed.png"
        imagebutton:
            xpos 0.5 ypos 0.5 anchor (0.5, 0.5)
            idle "journal_closed.png"
            action SetVariable("journal_open", True)

    else:
        add "journal_open.png"

        # Calculate what to show
        $ start = journal_page * 2
        $ end = start + 2
        $ visible = memory_entries[start:end]

        for i, entry in enumerate(visible):
            if unlocked_memory == entry["id"]:  # show only if it's unlocked
                textbutton entry["title"]:
                    xpos 120
                    ypos 180 + i * 100
                    style "memory_entry_button"
                    action [Hide("memory_journal"), Jump("memory_" + entry["id"])]
            else:
                text entry["title"] + " (Locked)":
                    xpos 120
                    ypos 180 + i * 100
                    style "memory_locked_style"

        # Arrows
        if journal_page > 0:
            imagebutton:
                xpos 50 ypos 420
                idle "arrow_left.png"
                action SetVariable("journal_page", journal_page - 1)

        if end < len(memory_entries):
            imagebutton:
                xpos 700 ypos 420
                idle "arrow_right.png"
                action SetVariable("journal_page", journal_page + 1)

        # Close button
        textbutton "Close":
            xpos 700 ypos 60
            action SetVariable("journal_open", False)

style memory_entry_button is default:
    size 32
    color "#ffffff"
    hover_color "#facc15"  # highlight color on hover
    underline True
    bold True

style memory_locked_style is default:
    size 28
    color "#777777"
    italic True

label demoend:
    hide window
    show screen tbc with fade
    pause

    show screen demothx with fade
    pause

    show screen credits with fade
    pause

    hide screen tbc 
    hide screen demothx 
    hide screen credits with fade
    
    return