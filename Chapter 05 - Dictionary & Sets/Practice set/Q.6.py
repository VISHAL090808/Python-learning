d = {}

name = input('Enter your name:')
lang = input('Enter your lang:')
d.update({name:lang})

name = input('Enter your name:')
lang = input('Enter your lang:')
d.update({name:lang})

name = input('Enter your name:') # 1. do baar ek hi naam (key) daal diya to last main jo value doge vo print hogi
lang = input('Enter your lang:') # 2. agar value same daal di (lang) do baar to wah dono baar print hogi
d.update({name:lang})

name = input('Enter your name:')
lang = input('Enter your lang:')
d.update({name:lang})

print(d)