from collections import Counter

def checkMagazine(magazine, note):
    word_counts = Counter(magazine)
    for word in note:
        if word_counts[word] > 0:
            word_counts[word] -= 1
        else:
            print("No")
            return

    print('Yes')
    return