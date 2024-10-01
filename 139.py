from typing import List
def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s) + 1
    T = [False] * (n)
    T[0] = True
    for i in range(1,n):
        for j in range(i):
            if T[j] and s[j:i] in word_set:
                T[i] = True
                break
    return T[n - 1]



s = "leetcode"
w = ["leet","code"]
print(wordBreak(s , w))