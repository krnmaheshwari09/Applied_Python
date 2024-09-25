from translate import Translator

file = open('Sample.txt', 'r')
new_content = file.read()
file.close()
translating = Translator(to_lang='hi')
result = translating.translate(new_content)
file1 = open('Sample.txt', 'w', encoding='utf-8')
file1.write(result)
file1.close()
print(result)