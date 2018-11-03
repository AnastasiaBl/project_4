s = input("Введите строку: ")
x = input()
while x =='с' or x=='б' or x =='з' or x =='ф' or x =='к':
    for i in range(len(s)):
        if (s[i] == 'а' or s[i] == 'я' or s[i] == 'е' or s[i] == 'и' or s[i] == 'ё' or s[i] == 'о' or s[i] == 'у' or s[i] == 'ы' or s[i] == 'э' or s[i] == 'ю' or s[i] == 'А' or s[i] == 'Я' or s[i] == 'И' or s[i] == 'У' or s[i] == 'О' or s[i] == 'Ю' or s[i] == 'Ы' or s[i] == 'Э' or s[i] == 'Ё' or s[i] == 'Е') and x =='с':
                print(s[i]+'c'+s[i],end='')
        elif (s[i] == 'а' or s[i] == 'я' or s[i] == 'е' or s[i] == 'и' or s[i] == 'ё' or s[i] == 'о' or s[i] == 'у' or s[i] == 'ы' or s[i] == 'э' or s[i] == 'ю' or s[i] == 'А' or s[i] == 'Я' or s[i] == 'И' or s[i] == 'У' or s[i] == 'О' or s[i] == 'Ю' or s[i] == 'Ы' or s[i] == 'Э' or s[i] == 'Ё' or s[i] == 'Е') and x =='б':
                print(s[i]+'б'+s[i],end='')
        elif (s[i] == 'а' or s[i] == 'я' or s[i] == 'е' or s[i] == 'и' or s[i] == 'ё' or s[i] == 'о' or s[i] == 'у' or s[i] == 'ы' or s[i] == 'э' or s[i] == 'ю' or s[i] == 'А' or s[i] == 'Я' or s[i] == 'И' or s[i] == 'У' or s[i] == 'О' or s[i] == 'Ю' or s[i] == 'Ы' or s[i] == 'Э' or s[i] == 'Ё' or s[i] == 'Е') and x =='з':
                print(s[i]+'з'+s[i],end='')
        elif (s[i] == 'а' or s[i] == 'я' or s[i] == 'е' or s[i] == 'и' or s[i] == 'ё' or s[i] == 'о' or s[i] == 'у' or s[i] == 'ы' or s[i] == 'э' or s[i] == 'ю' or s[i] == 'А' or s[i] == 'Я' or s[i] == 'И' or s[i] == 'У' or s[i] == 'О' or s[i] == 'Ю' or s[i] == 'Ы' or s[i] == 'Э' or s[i] == 'Ё' or s[i] == 'Е') and x =='ф':
                print(s[i]+'ф'+s[i],end='')
        elif (s[i] == 'а' or s[i] == 'я' or s[i] == 'е' or s[i] == 'и' or s[i] == 'ё' or s[i] == 'о' or s[i] == 'у' or s[i] == 'ы' or s[i] == 'э' or s[i] == 'ю' or s[i] == 'А' or s[i] == 'Я' or s[i] == 'И' or s[i] == 'У' or s[i] == 'О' or s[i] == 'Ю' or s[i] == 'Ы' or s[i] == 'Э' or s[i] == 'Ё' or s[i] == 'Е') and x =='к':
                print(s[i]+'к'+s[i],end='')
        else:
                print(s[i],end='')
    s = input("\nВведите строку: ")
    x = input()
