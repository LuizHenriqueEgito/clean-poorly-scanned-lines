labels_dict = {
    0: 'good_text',
    1: 'bad_text'
}

# depara_emb =  {
#     'vowels': 1,
#     'consonants': 2,
#     'espace': 10,
#     'digits': 3,
#     'punctuations': 4,
#     'pad': 5,
#     'unk': 6
# }

depara_emb =  {
    'vowels': 1,
    'consonants': 2,
    'espace': 0,
    'digits': 3,
    'punctuations': 4,
    'pad': -2,
    'unk': -1
}

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
digits = '0123456789'
punctuations = '.,;:!?@#$%&*(){}[]_-+='