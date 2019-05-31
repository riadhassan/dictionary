import json
from difflib import get_close_matches


def translate(word):
    word = word.lower()
    file_url = 'asset/data.json'
    data = json.load(open(file_url))

    #key properly maatch with word
    if word in data:
        meaning = data[word]
        return meaning

#if the case of word does not match with key
    data_keys = data.keys()
    for data_key in data_keys:
        if(data_key.lower()) == word:
            meaning = data[data_key]
            return meaning

    expected_words = get_close_matches(word, data_keys)

    if len(expected_words) > 0:
        print('Do you want to search')
        word_position = 0
        for expected_word in expected_words:
            word_position = int(word_position + 1)
            print(str(word_position) + ' -> ' + expected_word)

        yn = int(input('Enter corresponding number for that word (0 for none): '))
        if yn != 0:
            try:
                meaning = data[expected_words[yn-1]]
                return meaning
            except:
                return ['we don\'t understand your word']

    return ['we don\'t understand your word']
