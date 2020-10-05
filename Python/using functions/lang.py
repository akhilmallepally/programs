def greet(lang):
    if lang == 'tel':
        return 'Namasthe'
    elif lang == 'tam':
        return 'Vanakkam'
    else:
        return 'Hello'

print(greet('tel'), 'Akhil')