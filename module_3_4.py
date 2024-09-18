def single_root_words(root_word,*other_words):
    same_words = []
    for a in other_words:
        if root_word.lower() in a.lower() or a.lower() in root_word.lower():
            same_words += {a}
    return same_words
result1 = single_root_words('rich','richiest','orichalcum','cheers','riches')
result2 = single_root_words('Disablement','Able','Mable','Disable','Bagel')
print(result1)
print(result2)