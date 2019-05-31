import translator


word = '1'
print('For exit press enter(without any word)')
while '' != word:
    word = input('Enter the word: ')
    if '' != word:
        meanings = translator.translate(word)
        for meaning in meanings:
            print(meaning)

print('----------Thank you for using this dictionary---------------')