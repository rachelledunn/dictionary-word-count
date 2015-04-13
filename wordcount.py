# put your code here.
with open("test.txt") as poem:

    poem_list = []    
    for line in poem:
        words = line.rstrip().split(" ")
        poem_list.extend(words)

    for word in set(poem_list):
        count = poem_list.count(word)
        print "%s %d" % (word, count)

# print "Dictionary Option:"

# # put your code here.
# with open("test.txt") as poem:

#     # poem_list = []    
#     poem_dict = {}

#     poem_comb = poem.read().split()

#     for word in poem_comb:

#         if poem_dict.get(word,0) == 0:
#             poem_dict[word] = poem_comb.count(word)

#     for word in poem_dict:
#         print "%s %d" % (word, poem_dict[word])


print "Dictionary Option 2:"

# put your code here.
with open("test.txt") as poem:
    
    poem_dict = {}

    poem_comb = poem.read().replace(".","").replace(",","").replace("?","").lower().split()

    # poem_comb = poem.read().split()
    # poem_comb_string = " ".join(poem_comb).lower()

    # punctuation = ["?",".",","]
    # for character in punctuation:
    #     if character in poem_comb_string:
    #         poem_comb_string = poem_comb_string.replace(character,"")

    print poem_comb
    
    count = 0

    for word in poem_comb:

        if poem_dict.get(word,0) == 0:
            count = 1
        else:
            count = poem_dict.get(word) + 1

        poem_dict[word] = count


    print poem_dict

    for word in poem_dict:
        print "%s %d" % (word, poem_dict[word])
