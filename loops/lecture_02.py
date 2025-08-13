for i in [0, 1, 2]:
    print('Meow!')

print('...')

for i in range(3):
    print('Meow!')

print('...')

print('Meow!\n' * 3, end='')

print('...')

while True:
    n = int(input('What is n? '))
    if n > 0:
        break


for _ in range(n):
    print('Meow!')

