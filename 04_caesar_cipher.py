def caesar_cipher(text, lang='eng', shift=3):
    alphabet = {
        'eng': ['a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x',
                'y', 'z'],
        'ru':  ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
                'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                'ч' 'ш' 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    }

    char_list = [char for char in text]
    encrypted_char_list = []
    for char in char_list:
        if char.lower() in alphabet[lang]:
            new_char = alphabet[lang][alphabet[lang].index(char.lower()) - shift]
            if char.isupper():
                new_char = new_char.upper()
            encrypted_char_list.append(new_char)
        else:
            encrypted_char_list.append(char)

    return ''.join(encrypted_char_list)


if __name__ == '__main__':
    print(caesar_cipher(text="Hello world! Life is good!"))
