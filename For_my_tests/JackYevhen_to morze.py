from time import sleep
dialog_mode = False
text = 0
# Text - input too tramslate to morze
ukr_morze = { "а":'•⁃', 
                 "б":'⁃••', 
                 "в":'•⁃',
                 "г":'••••',
                 "ґ":'⁃⁃•',
                 "д":'⁃••',
                 "е":'•',
                 "є":'••⁃••',
                 "ж":'•••⁃',
                 "з":'⁃⁃••',
                 "и":'⁃•⁃⁃',
                 "і":'••',
                 "ї":'•⁃⁃⁃•',
                 "й":'•⁃⁃⁃',
                 "к":'⁃•⁃',
                 "л":'•⁃••',
                 "м":'⁃⁃',
                 "н":'⁃•',
                 "о":'⁃⁃⁃',
                 "п":'•⁃⁃•',
                 "р":'•⁃•',
                 "с":'•••',
                 "т":'⁃',
                 "у":'••⁃',
                 "ф":'••⁃•',
                 "х":'⁃⁃⁃⁃',
                 "ц":'⁃•⁃•',
                 "ч":'⁃⁃⁃•',
                 "ш":'⁃⁃•⁃',
                 "щ":'⁃⁃•⁃⁃',
                 "ь":'⁃••⁃',
                 "ю":'••⁃⁃',
                 "я":'•⁃•⁃'}
special = {".":'••••••',
                 ",":'•⁃•⁃•⁃',
                 "?":'••⁃⁃••',
                 "!":'⁃⁃••⁃⁃',
                 ":":'⁃⁃⁃•••',
                 "-":'⁃••••⁃',
                 " ":'   '}
output_ = ""
while True:
    while True:
        if dialog_mode == False:
            print("\n"*45)
        print("Ця програма піттримує декілька режимів:")
        print("1. режим з вибраної мови в морзе")
        print("2. режим з морзе у вибрану мову")
        print("3. налаштування терміналу")
        mode = input("Ваш вибір: ")
        if mode == "1" or mode == "2" or mode == "3":
            break
        else:
            print("Ви ввели не той символ!")
            print("Спробуйте ще раз...")
            sleep(10)
    if dialog_mode == False:
        print("\n"*45)
    else:
        print("")
    if mode == "2":
        print("WIFP")
        print("Wait In Future Please")
        print("")
        if dialog_mode == False:
            check = input("Натиснініть ENTER щоб вийти в меню")
    elif mode == "1":
        output_ = ""
        morze = []
        while True:
            print("Виберіть мову:")
            print("1. Українська")
            print("2. Англіська")
            language = input("Ваша мова: ")
            if language == "1":
                morze.append(ukr_morze)
                if dialog_mode == False:
                     print("\n"*45)
                     print("Українська")
                     print("")
                break
            elif language == "2":
                print("")
                print("WIFP")
                print("Wait In Future Please")
                if dialog_mode == False:
                    print("")
                    check = input("Натиснініть ENTER щоб вийти в меню")
            else:
                print("Ви ввели не \"1\" чи \"2\"")
            if dialog_mode == False:
                print("\n"*45)
            else:
                print("")
        text = input("Що транслювати: ")
        text = text.lower()
        for i in text:
            if i in morze[0]:
                output_ = output_ + morze[0][i] + "  "
            elif i in special:
                output_ = output_ + special[i] + "  "
            else:
                print("\n"*45)
                print("Помилка № 404 !!!")
                print("Error code: unexpected symbol")
                exit()
        output_ = output_[0:-1]
        print("це буде: " + output_)
        print("")
        if dialog_mode == False:
            check = input("Натиснініть ENTER щоб вийти в меню")
    elif mode == "3":
        while True:
            if dialog_mode == False:
                print("\n"*45)
            print("Налаштування:")
            print("1. Режим діалогу:")
            if dialog_mode == False:
                print("Ввімкнено")
            else:
                print("Вимкнено")
            print("2. Різні вибори:")
            print("Цифрами")
            choosen_setting = input("Введіть число щоб пермкнути або \"-\" щоб вийти: ")
            if choosen_setting == "1" or choosen_setting == "2" or choosen_setting == "-":
                if dialog_mode == False:
                    print("\n"*45)
                break
            else:
                print("Вибачте ви ввели не число і не \"-\"")
                print("")
                if dialog_mode == False:
                    check = input("Натиснініть ENTER щоб вийти в налаштуввання")
        if choosen_setting == "1":
            if dialog_mode == True:
                dialog_mode = False
            else:
                dialog_mode = True
        elif choosen_setting == "2":
            print("")
            print("WIFP")
            print("Wait In Future Please")
            if dialog_mode == False:
                print("")
                check = input("Натиснініть ENTER щоб вийти в меню")
