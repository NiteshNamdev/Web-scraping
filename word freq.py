import string


print('Word count from text:')

word_freq= open('web scraping.txt', 'r')
data = word_freq.read().lower()
word_freq.close()

special_char = ',.?/\!-'
for sc in special_char:
    if sc in data:
        data = data.replace(sc," ")
        
word_list = data.split()
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1
    
for key, value in word_count.items():
    print(f"{key}: {value}")

