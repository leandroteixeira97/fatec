text = '''
The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.
'''.split()
newText = []

for pos in text:
    p = list(pos)
    if p[0] in 'python' or p[0] in 'PYTHON' or p[len(p)-1] in 'python' or p[len(p)-1] in 'PYTHON':
        newText.append(pos)
print(newText)