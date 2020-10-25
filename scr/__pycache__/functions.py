def player():
    import random as rn
    print("""The difficulty level determines the range between which you have to guess:
               - Level 1 -> (1,20)
               - Level 2 -> (1,30)
               - Level 3 -> (1,40)""")
    level = int(input('Choose the difficulty level you want to face:'))
    if level == 1:
        print('What a chicken!')
        num = rn.randint(1,20)
    elif level == 2:
        print('Not a complete waste. I guess...')
        num = rn.randint(1,30)
    elif level == 3:
        print('Someone proper looking for a challenge. I like it!')
        num = rn.randint(1,40)
    tries = 5
    chance = 0
    while chance < tries:
        guess = int(input('Try guessing the number:'))
        chance += 1
        if guess < num:
            print('Try higher')
        elif guess > num:
            print('Try lower')
        else: 
            print('Good job! The number was', num)
    if guess == num:
        print('COngratulations!! You guessed the number on your try number ',chance)
    elif guess != num:
        print('Game over! The number was ',num)


