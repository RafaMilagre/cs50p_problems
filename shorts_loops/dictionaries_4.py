WORDS = {'PAIR': 4, 'HAIR': 4, 'CHAIR': 5, 'GRAPHIC': 7}


def main():
    """for key, value in WORDS.items():
        print(f'{key} was worth {value} points.')"""
    print('Welcome to spelling Bee!')
    print('Your letters are: A I P C R H G')


    while len(WORDS) > 0:
        print(f'{len(WORDS)} words left')
        guess = input('Guess a word: ')
        
        if guess == 'GRAPHIC':
            WORDS.clear() # REMOVE TODOS OS ITENS DO DICIONARIO
            print(f'The game is over! You WON!')

        if guess in WORDS.keys(): # KEYS SÃO AS PRIMEIRAS PALAVRAS
            points = WORDS.pop(guess) # POP É O METODO PARA APAGAR UM ITEM DO DICIONARIO
            print(f'Good job! You scored {points} points!')
            # print(f'Good job! You scored {WORDS[guess]} points!')
        

    
    print("That's the game!")



main()
