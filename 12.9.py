#Mohamed Hamed
#1644926
user_input = input().split()
name = user_input[0]
while name != '-1':
    try:
        age = int(user_input[1]) + 1
    except ValueError as v:
        age = 0
    print('{} {}'.format(name, age))
    user_input = input().split()
    name = user_input[0]

