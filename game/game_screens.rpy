screen tbc:
    add "screens/tbc.png"

screen wiproute:
    add "screens/wip-route.png"

screen demothx:
    add "screens/demo-thx.png"

screen credits:
    add "screens/credits.png"

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