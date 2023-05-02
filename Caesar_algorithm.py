# finds the shift value for current word (word length)
def length_word(word):
    length = 0
    for i in word:
        if i.isalpha():
            length += 1
    if (operation == 'd') or (operation == 'decrypt'):
        return -length
    return length


# getting the alphabet of the desired language of lower symbols
def get_alpha_lower(language):
    if language == 'en':
        return 'abcdefghijklmnopqrstuvwxyz'

    if language == 'ru':
        return 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


# getting the alphabet of the desired language of upper symbols
def get_alpha_upper(language):
    if language == 'en':
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if language == 'ru':
        return 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


# encrypting your text
def caesar_cipher(text, alphabet_lower, alphabet_upper):
    result = ""
    words = text.split()
    for word in words:
        shift = length_word(word)
        for char in word:
            if char in alphabet_upper:
                index = (alphabet_upper.index(char) + shift) % len(alphabet_upper)
                result += alphabet_upper[index]
            elif char in alphabet_lower:
                index = (alphabet_lower.index(char) + shift) % len(alphabet_lower)
                result += alphabet_lower[index]
            else:
                result += char
        result += ' '
    return result


# check your language for compliance with the list available
def check_language(language):
    while language not in ['en', 'ru']:
        print("I don't know this language :(\nPlease, write any language from this list:")
        print('2, 8, 10, 16')


message = input('Input text, that you want to encrypt/decrypt')
chosen_lang = input('Input the language of your text')
chosen_lang = chosen_lang
operation = input('You want to encrypt or decrypt text? (e/d)')
alpha_lower = get_alpha_lower(chosen_lang)
alpha_upper = get_alpha_upper(chosen_lang)
encrypted_message = caesar_cipher(message, alpha_lower, alpha_upper)
print(encrypted_message)
