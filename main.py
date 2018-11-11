
# Encrypt using the da Vinci method.
with open('input.txt') as f_in:
    text = f_in.read()

with open('output.txt', 'w') as f_out:
    f_out.write('Шифр да Винчи:')
    f_out.write(text[::-1])


# Decrypt using the da Vinci method.
with open('output.txt') as f_in:
    text_one = f_in.read()
    text_one_r = text_one[::-1]

with open('record.txt', 'w') as f_out:
    f_out.write('Расшифрованный тескст:')
    f_out.write(text_one_r[:len(text)])
    f_out.write('\n')


# Code  in the second wayю
ENG_LET_1 = ['A', 'E',  'I',  'O',  'U', 'U', 'a', 'e',  'i',  'o',  'u', 'u']

ENG_LET_2 = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
             'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
              'b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm', 'n',
             'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', ]

RUS_LET_2 = ['Б','В','Г','Д','Ж','З','Й','К','Л','М', 'Н','П', 'Р', 'С', 'Т', 'С',
             'Ф', 'Х', 'Ц','Ч', 'Ш','Щ','Ъ','Ь', 'б', 'в', 'г' ,'д','ж','з','й','к','л','м', 'н',  'п', 'р', 'с',
             'т', 'с',  'ф', 'х', 'ц','ч', 'ш','щ','ъ', 'ь']

RUS_LET_1 = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я',
             'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',]

with open('input.txt') as f_in:
    text = f_in.read()
    _replaced = text
with open('output.txt', 'a') as f_out:
    for i in range(len(text)):
        if text[i] in ENG_LET_1:
            _replaced = text.replace((text[i]), '1')
            text = _replaced
        if text[i] in ENG_LET_2:
            _replaced = text.replace((text[i]), '2')
            text = _replaced
        if text[i] in RUS_LET_2:
            _replaced = text.replace((text[i]), '2')
            text = _replaced
        if text[i] in RUS_LET_1:
            _replaced = text.replace((text[i]), '1')
            text = _replaced
    f_out.write('Кодировка заменой:')
    f_out.write(_replaced)