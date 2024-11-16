verb_dict: list[str] = ['this, chocolate, cake, is, rich, moist, and, full, of, delicious, chocolate, flavor,'
                        'to, make, the, cake,, you, will, need, chocolate, flour, sugar, eggs and butter,'
                        'after, baking, the, chocolate, cake, let, the, cake, cool, before, adding, the,'
                        'chocolate frosting']

# a
# word_count: dict[str] = dict()
# for word in verb_dict:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)

dict_count: dict[str, int] = dict()
dict_count[word] = dict_count.get(word, 0) + 1
print(dict_count)
max_word = max(dict_count, key=dict_count.get)
print(f'the word that appeared the most is: {max_word}')
print(f'the word {dict_count}')



# לא מצליחה לפתור.. אשמח שתרחיב על זה בשיעור

# בשאלה b זה אותו העיקרון רק שבמקום
# sign / char זה word
# min זה max
