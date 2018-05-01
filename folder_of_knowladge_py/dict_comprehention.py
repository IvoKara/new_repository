numb = ['one', 'two', 'theee', 'four']
print({numb[i]:i+1 for i in range(4)})

def wordPower(word):
    num = {ch: numb for numb, ch in enumerate('abcdefghijklmnopqrstuvwxyz', start=1)}
    return sum([num[ch] for ch in word])
