def sort_strings(string_list):
    string_list.sort(key=len)
    print("Сортировка по возрастанию:", string_list) # Печатает: Сортировка по возрастанию: ['apple', 'cherry', 'blueberry', 'banana', 'grapefruit']
    string_list.reverse()
    print("Сортировка по убыванию:", string_list) # Печатает: Сортировка по убыванию: ['grapefruit', 'banana', 'blueberry', 'cherry', 'apple']

    return string_list

# Пример использования:
words = ["cherry", "apple", "banana", "grapefruit", "blueberry", ]
print('Исходный: ', words)
sorted_words = sort_strings(words)