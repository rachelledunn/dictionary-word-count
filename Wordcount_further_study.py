from collections import Counter

import operator

with open("test.txt") as poem:
    
    poem_dict = {}

    poem_comb = poem.read().replace(".","").replace(",","").replace("?","").lower().split()


    print poem_comb

    counter = Counter(poem_comb)

    for word in poem_comb:

        poem_dict[word] = counter[word]
    
    # poem_dict_alpha = sorted(poem_dict)

    sorted_dict = sorted(poem_dict.items(),key=operator.itemgetter(1), reverse=True)

    print sorted_dict

    for word,count in sorted_dict: 
        print "%s %d" % (word, poem_dict[word])