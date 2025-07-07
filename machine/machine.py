emotion = 'v.v'



def main():
    global emotion
    say('Is anyone there?')
    emotion = '=D'
    say('Oh, hi!')
    
def say(phrase):    
    print(phrase + ' ' + emotion)



main()