screen tbc:
    add "screens/tbc.png"

screen wiproute:
    add "screens/wip-route.png"

screen demothx:
    add "screens/demo-thx.png"

screen credits:
    add "screens/credits.png"

# Journal entries data
default journal_entries = [
    { "id": "childhood", "title": "Ang Aking Kabataan", "image": "images/memories/childhood_cg.png" },
    { "id": "suffering", "title": "Ang Aking Pagkakasakit", "image": "images/memories/sickness_cg.png" },
    { "id": "faith", "title": "Pananalig sa Gitna ng Gutom", "image": "images/memories/faith_cg.png" },
    { "id": "forgiveness", "title": "Pagpapaumanhin", "image": "images/memories/forgiveness_cg.png" }
]

# Styled journal screen (drawn box, no PNG)
screen memory_journal():
    tag menu
    modal True

    add Solid("#0008")  # semi-transparent overlay

    frame:
        background Solid("#222")
        xalign 0.5
        yalign 0.5
        padding (18, 18)
        xminimum 760

        vbox:
            spacing 8
            text "Memory Journal" size 32 color "#fff" xalign 0.5

            # Compute count for interpolation safely
            $ found_count = len(persistent.found_journal)
            text "{size=20}{color=#ccc}%d out of %d entries found{/color}{/size}" % (found_count, len(journal_entries)) xalign 0.5

            null height 8

            # Entries list inside a drawn box
            frame:
                background Solid("#333")
                padding (12, 12)
                xminimum 700
                vbox:
                    spacing 6
                    for entry in journal_entries:
                        if journal_entry_unlocked(entry["id"]):
                            textbutton entry["title"] action [Hide("memory_journal"), Show("journal_entry_viewer", entry=entry)]
                        else:
                            $ title_text = entry["title"]
                            text "???" color "#888"

            null height 8
            hbox:
                spacing 10
                textbutton "Balik" action Return()

# Entry viewer: show title + cg and allow going back to journal
screen journal_entry_viewer(entry):
    tag menu
    modal True
    # dark background so CG stands out
    add Solid("#000C")

    frame:
        background Solid("#111")
        padding (16, 16)
        xalign 0.5
        yalign 0.5
        xmaximum 900
        vbox:
            spacing 10
            text entry["title"] size 30 color "#fff" xalign 0.5
            null height 6
            if entry["image"]:
                add entry["image"] xalign 0.5
            null height 8
            hbox:
                spacing 8
                textbutton "Back to Journal" action [Hide("journal_entry_viewer"), Show("memory_journal")]
                textbutton "Close" action [Hide("journal_entry_viewer"), Return()]

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