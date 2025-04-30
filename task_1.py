def find_lps(needle):
    i = 1
    j = 0
    lps = [0]*len(needle)
    while i < len(needle):
        if needle[j] == needle[i]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j - 1]
    return lps

def indexes_dfa(haystack, needle):
    lps = find_lps(needle)
    current_state = 0
    indexes = []

    for i, char in enumerate(haystack):
        while char != needle[current_state] and current_state > 0:
            current_state = lps[current_state - 1]

        if char == needle[current_state]:
            current_state += 1

        if current_state == len(needle):
            index = i + 1 - len(needle)
            indexes.append(index)
            current_state = lps[current_state - 1]

    return indexes

res = indexes_dfa("ababacab", "ab")
print(res) 