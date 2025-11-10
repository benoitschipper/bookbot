def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_characters(text):
    charachters = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char in charachters:
                charachters[char] += 1
            else:
                charachters[char] = 1
    return charachters

def get_sorted_list_of_dictionaries(text):
    sorted_list_of_disctionaries = []
    charachters = get_number_of_characters(text)
    for key, value in charachters.items():
        sorted_list_of_disctionaries.append({"char": key, "num": value})
    sorted_list_of_disctionaries.sort(key=sort_on, reverse=True)
    return sorted_list_of_disctionaries

def sort_on(items):
    return items["num"]