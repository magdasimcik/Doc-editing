# Doplnit: smazat cislovani otazek; smazat prazdne radky


doc_name = input("Zadej název dokumentu (bez přípony .txt): ")
repeat = True


while repeat:
    search_char = input("Zadej řetězec, který chceš vyhledat: ")
    char_location = input("Pokud se řetězec nachází na začátku řádku, napiš 'z', pokud na konci, napiš 'k': ")
    char_action = input("Napiš: \n'del' vymaže celý řádek, \n'rem' vymaže zadaný řetězec, \n'rep' zadaný řetězec nahradí jiným řetězcem, \n'add' zapíše zadaný řetězec za hledaný, \n'new' vloží nový řádek a zapíše na něj '--': \n")

    if search_char:
        with open(doc_name + '.txt', 'r+', encoding="utf8") as f: 
            lines = f.readlines()
            # Delete whole line
            if char_action == 'del':
                if char_location == 'z':
                    lines = [line for line in lines if not line.startswith(search_char)]
                elif char_location == 'k':
                    lines = [line for line in lines if not line.rstrip().endswith(search_char)]
            # Remove the string
            elif char_action == 'rem':
                if char_location == 'z':
                    lines = [line.replace(search_char, '') if line.startswith(search_char) else line for line in lines]
                elif char_location == 'k':
                    lines = [line.replace(search_char, '') if line.rstrip().endswith(search_char) else line for line in lines]
            # Replace the string with new one
            elif char_action == 'rep':
                replace_char = input("Zadej řetězec, který chceš vložit místo hledaného: ")
                if char_location == 'z':
                    lines = [line.replace(search_char, replace_char, 1) if line.startswith(search_char) else line for line in lines]
                elif char_location == 'k':
                    lines = [line.rstrip()[:-len(search_char)] + replace_char + '\n' if line.rstrip().endswith(search_char) else line for line in lines]
            # Adds a new line with string '--'
            elif char_action == 'new':
                new_lines = []
                for line in lines:
                    new_lines.append(line)
                    if char_location == 'z' and line.startswith(search_char):
                        new_lines.append('--\n')
                    elif char_location == 'k' and line.rstrip().endswith(search_char):
                        new_lines[-1] = line.rstrip() + '\n--\n'
                lines = new_lines
            # Adds a new string after the searched one
            elif char_action == 'add':
                add_string = input("Zadej řetězec, který chceš přidat za hledaný: ")
                if char_location == 'z':
                    lines = [line.replace(search_char, search_char + add_string, 1) if line.startswith(search_char) else line for line in lines]
                elif char_location == 'k':
                    lines = [line.rstrip() + add_string + '\n' if line.rstrip().endswith(search_char) else line for line in lines]

            f.seek(0)
            f.truncate()
            for line in lines:
                f.write(line)
    
    if input("Chceš pokračovat v úpravách? ('a' nebo 'n'): ") == 'n':
        repeat = False
    
    print()


