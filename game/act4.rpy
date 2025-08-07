label act4_start:

    # Scene 1: Memory Journal Unlocks

    "Bilang gantimpala sa iyong pananampalataya at pagtitiis, ikaw ay dadalhin sa kapahingahan."

    "Ngunit alalahanin mo ang iyong landas, upang ito’y maging liwanag sa iba."

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
    # “Ang Aking Kabataan” – A scene where Lazarus worked in a vineyard with joy
    jump act4_cont

label memory_suffering:
    # “Ang Aking Pagkakasakit” – He collapses in the street; no one helps
    jump act4_cont

label memory_faith:
    # “Pananalig sa Gitna ng Gutom” – He prays even while starving
    jump act4_cont

label memory_childhood:
    # “Pagpapaumanhin” – He forgives the rich man in his heart before dying
    jump act4_cont

label act4_cont:
    l "Sa kahirapan, hindi ako nawalan ng pananampalataya. Sa sakit, hindi ko isinuko ang aking kaluluwa. Ngayo’y ako’y nasa kapahingahan... at ang Panginoon ay tapat." 

    # lazarus walks towards the light with music swelling

    return