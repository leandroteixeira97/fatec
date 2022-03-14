text = '''
The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.
'''.lower().split()

newText = []

for pos in text:
  word = list(pos)
  if len(word) > 4:
    for letter in word:
      if letter in 'python':
        newText.append(pos)
        break

print(f'{len(newText)} palavras')
print(newText)