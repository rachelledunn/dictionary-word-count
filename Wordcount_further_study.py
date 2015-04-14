from collections import Counter

with open("test.txt") as poem:
    
    poem_dict = {}

    poem_comb = poem.read().replace(".","").replace(",","").replace("?","").lower().split()


    print poem_comb

    counter = Counter(poem_comb)

    for word in poem_comb:

        poem_dict[word] = counter[word]

    for word in poem_dict:
        print "%s %d" % (word, poem_dict[word])
