code = ''
print('Please set the code for a lock')
code = input()
while not code.isdigit():
    print('Code can only contain digits!')
    print('Please set the code again')
    code = input()

print('=====CODE SET=====')
print('Enter the code to unlock a safe')

for i in range(3):
    codeIn = input()
    if codeIn == code:
        print('ACCESS GRANTED')
        break
    else:
        print('Wrong code, ' + str(2-i) + ' trials left')
