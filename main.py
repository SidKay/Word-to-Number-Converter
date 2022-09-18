def parse_int(string):
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3, 
        "four": 4, 
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9, 
        'ten':10, 
        'eleven': 11, 
        'twelve':12, 
        'thirteen':13, 
        'fourteen':14, 
        'fifteen':15,
        'sixteen':16,
        'seventeen':17,
        'eighteen': 18,
        'nineteen':19,
        'twenty':20,
        'thirty':30,
        'forty':40,
        'fifty':50,
        'sixty':60,
        'seventy':70,
        'eighty':80,
        'ninety':90,
        'hundred': 100,
        "thousand": 1000,
        'million': 1000000
    }
    cur_num = 0
    separated_str = ''
    pure_str = []
#     current_val = ''
    result = 0
    
    separated_str = string.split(' ')
    
    for word in separated_str:
        if '-' in word:
            mini_sep_str = word.split('-')
            for word2 in mini_sep_str:
                pure_str.append(word2)
        else:
            pure_str.append(word)
            
    for word3 in pure_str:
        if word3 == 'and':
            continue
        current = numbers[word3]
        
        if current >= 1000:
            cur_num *= current
            result += cur_num
            cur_num = 0
        elif current >= 100:
            cur_num *= current
            result += cur_num
            if pure_str.count("hundred") > 1:
#                 pure_str.pop(pure_str.index("hundred"))
                continue
            else:
                cur_num = 0
        else:
            cur_num += numbers[word3]
    
    return result + cur_num
