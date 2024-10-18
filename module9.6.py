def all_variants(text):
    for value in range(len(text)):
        for m in range(len(text) - value):
            yield text[m:m + value + 1]




a = all_variants('abc')
for i in a:
    print(i)
