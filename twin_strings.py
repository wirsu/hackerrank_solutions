def twins(a, b):
    # Input: a and b are arrays of strings (of equal length)
    # Return an array of length equal to length of a with "Yes and "No"s

    # n number of strings to process
    n = len(a)

    output = [None] * n

    for i in range(0, n):
        ai_odd = []
        ai_even = []

        bi_odd = []
        bi_even = []

        length_ai = len(a[i])
        length_bi = len(b[i])

        if length_ai != length_bi:
            # Case where the lengths of the strings aren't equal. Thus certiantly not twins
            output[i] = 'No'

        else:
            for j in range(0, length_ai):
                # Gather the letters from each string that are in odd / even indexes.
                if j % 2 == 1:
                    ai_odd.append(a[i][j])
                    bi_odd.append(b[i][j])
                else:
                    ai_even.append(a[i][j])
                    bi_even.append(b[i][j])
                # aslong as the sets for each are equal, we can swap characters to obtain the other string
                if (set(ai_even) == set(bi_even)) & (set(ai_odd) == set(bi_odd)):
                    output[i] = 'Yes'
                else:
                    output[i] = 'No'

    return output



def main():
    #call function
    #define inputs

    firstString = ["cdab", "dcba", "abcd"]
    secondString = ["abcd", "abcd", "abcdcd"]
    x = twins(firstString, secondString)
    print(x)

main()