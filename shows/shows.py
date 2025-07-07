shows = [' Avatar, the last airbender',
         'Ben 10',
         'arthur', 
         ' Spongebob squarepants',
         'Phineas and ferb',
         'Kim possible',
         'Jimmy Neutron',
         'the Proud family'
]



def main():
    cleaned_shows = []
    for show in shows:
        cleaned_shows.append(show.strip().title())

    print('\n'.join(cleaned_shows))
    print(', '.join(cleaned_shows))

main()