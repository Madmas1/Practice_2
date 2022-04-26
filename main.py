def ceaser_ecnrypt(step, words, state = 1):
    '''
    Метод по шифровке/дешифровке слова шифром Цезаря для латинских слов.
    step - шаг по алфавиту
    words - строка с набором слов
    state - необязательный аргумент указывающий на статус метода. 1 - метод шифрует слово. 0 - метод дешифрует слово.
    По умолчанию state = e
    '''
    if state == 0:
        step = -step
    encrypt_word = ''
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for word in words:
        for letter in word:
            if letter in abc:
                encrypt_word += abc[(abc.find(letter) + step) % 26]
            elif letter in ABC:
                encrypt_word += ABC[(ABC.find(letter) + step) % 26]
            else:
                encrypt_word += letter
    return encrypt_word


w = input()
s = int(input())

word = ceaser_ecnrypt(s, w)
print(word)
print(ceaser_ecnrypt(s, word, 0))