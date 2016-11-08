def lowit(line):
    line = line.lower()
    sentences = line.split('. ')
    sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    string2 = '. '.join(sentences2)
    return string2

def capcico(line, allKeywords):
    allWords = line.split(' ')
    original = line.split(' ')

    for i,words in enumerate(allWords):
        words = words.rstrip('\r\n')
        words = words.replace(',', '')
        words = words.replace('.', '')
        words = words.replace(';', '')
        words = words.replace('.', '')
        
        if words in allKeywords:
            original[i] = original[i].capitalize()

    return ' '.join(original)

def main():
    dfile = open('XXXX.txt', 'w') 
    f = open('allist.txt', 'r')
    allKeywords = f.read().split('\n')

    with open('YYYYYY.txt', 'r') as fileinput:
        for line in fileinput:
            low_line = lowit(line)
            dfile.write('\n' + capcico(low_line, allKeywords))
    dfile.close()

if __name__ == '__main__':
    main()
