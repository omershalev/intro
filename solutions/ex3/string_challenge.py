def string_challeng(sentence):
    bang_split = sentence.split('!')
    sentence_to_be_modified = bang_split[-2].split(' ')
    word_to_modfify = sentence_to_be_modified[-1]
    modified_word = word_to_modfify.upper()
    modified_sentence = ' '.join(sentence_to_be_modified[0:-1] + [modified_word])
    new_sentence = '!'.join(bang_split[0:-2] + [modified_sentence] + [bang_split[-1]])
    return new_sentence

if __name__ == '__main__':
    sentence = 'Hey! Hooray! This Python course is awesome! We enjoy it very much.'
    print sentence
    print string_challeng(sentence)