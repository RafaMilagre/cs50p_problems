name = str(input('What is your name: '))

match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _: # funciona parecido com o else, para todo os resto
        print('Who? ') 