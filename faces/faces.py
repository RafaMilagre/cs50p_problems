smile_old = ':)'
smile_new = '🙂'
sad_old = ':('
sad_new = '🙁'


def main():
    faces = str(input('Digite: '))
    print(convert(faces))


def convert(frase):
    return frase.replace(smile_old, smile_new).replace(sad_old, sad_new)


main()