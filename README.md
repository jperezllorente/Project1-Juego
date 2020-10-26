# Guess the number   

### Game objective: 

The objective of the game is to guess a number that has been randomly chosen

### Development:

*The development of the game will be explained step by step as it would be played, but the complete code will be available at the end of this file*

In order to develop the code for this game the following steps have been taken:

1. The first thing the player has to choose is if he wants to either play the game, or would rather watch the machine play. This choice can be made using:

        select = int(input('Choose game mode:'))
        if select not in range (1,3):
            print('Choose a valid game mode')
        elif select == 1:
            print('You have chosen to play yourself')
            player()
        elif select == 2:
            print('You have chosen to watch the machine play')
            machine()

2. Once the game mode has been chosen, the computer will ask the player what level of the game he wants to play, that will set the range between which the number to be guessed will be randomly chosen from. 

        Level 1 sets the range between 1 and 20
        Level 2 sets the range between 1 and 30
        Level 3 sets the range between 1 and 40

        The level can be chosen using **level = int(input('Choose the difficulty level you want to face:'))** that returns the following results:
        
            if level == 1:
                print('What a chicken!')
                num = rn.randint(1,20)
            elif level == 2:
                print('Not a complete waste. I guess...')
                num = rn.randint(1,30)
            elif level == 3:
                print('Someone proper looking a for a challenge. I like it!')
                num = rn.randint(1,40)

    The number is chosen using the **.randint()** function of the **random** library, which gives a random number between a range. The idea is to not know the number until the end. 

3. #### Game mode:
    If the user has chosen game mode 1 (the player gets to play the game) the computer will ask the player to guess the number that has been randomly chosen, returning a **HIGHER** message if the player has enter a number lower that the guessed one; and a **LOWER** message if the number entered if higher. The player will have a maximun of five tries to get the right answer. In case the player spends all five tries without guessing the right number, the computer will stop the game as a **GAME OVER**. On the contrary, if the player is able to guess the number, the computer will stop the game and print a **CONGRATULATIONS** message and the number of the try in which the playe has guessed the number. The code goes as follow: 

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
            print('Someone proper looking a for a challenge. I like it!')
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
                print('Good job! The number was',num)
                break
            
        if guess == num:
            print('Congratulations!! You guessed the number on your try number ', chance)
        if guess != num:
            print('Game over! The number was' ,num)

    In case the chosen game mode is 2 (watch the machine play), the same instructions are apllied, but with the exeption that the computer is constanly entering a random number usin the **.randint()** function.In order to close the range of the guess, if the computer entered a number than the guessed one, its next random choice will be made betweem the **first option + 1** and the maximum point of the range from which the to guess number has been chosen. The same applies to a number lower than the one to be guessed, but with **first option - 1**. The reason to use a (+-) 1 is to avoid repeating the same number. 
    
        import random as rn

        print("""The difficulty level determines the range between which you have to guess:
                    - Level 1 -> (1,20)
                    - Level 2 -> (1,30)
                    - Level 3 -> (1,40)""")
        
        level = int(input('Choose the difficulty level you want to face:'))
        
        if level == 1:
            print('What a chicken!')
            min_bound=1
            max_bound = 20
        elif level == 2:
            print('Not a complete waste. I guess...')
            min_bound=1
            max_bound = 30
        elif level == 3:
            print('Someone proper looking a for a challenge. I like it!')
            min_bound=1
            max_bound = 40
        
        chances = 0
        tries = 5   
        num = rn.randint(min_bound,max_bound)
        guess = rn.randint(min_bound,max_bound)
        
        while chances < tries:
            
            chances += 1
            if guess == num:
                print('Good job! The number was',num)
                break
            elif guess < num:
                print(guess,'Try higher')
                guess = rn.randint(guess+1,max_bound)
            elif guess > num:
                print(guess,'Try lower')
                guess = rn.randint (min_bound,guess-1)
                
        if guess == num:
            print('Congratulations!! You guessed the number on your try number ', chances)
        if guess != num:
            print('Game over! The number was' ,num)


### Conclusions:

- This game offers two game modes, one that allows us to be the player and another that allows to be spectators. 
- The number to be guessed is randomly chosen in order to offer a better experience
- There are three dificulty levels that set tha range between which the number can be guessed
- The player enters the number he believes are the answer, while the computer chosses randomly with a range that closes with each guess so that it  resembles the actions of a person.
- The whole code ca be found next:

    1. We define the function for the player:

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
            print('Someone proper looking a for a challenge. I like it!')
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
                print('Good job! The number was',num)
                break
            
        if guess == num:
            print('Congratulations!! You guessed the number on your try number ', chance)
        if guess != num:
            print('Game over! The number was' ,num)

    2. We define the function for the machine:

    def machine():

        import random as rn
        
        level = int(input('Choose the difficulty level you want to face:'))
        
        if level == 1:
            print('What a chicken!')
            min_bound=1
            max_bound = 20
        elif level == 2:
            print('Not a complete waste. I guess...')
            min_bound=1
            max_bound = 30
        elif level == 3:
            print('Someone proper looking a for a challenge. I like it!')
            min_bound=1
            max_bound = 40
        
        chances = 0
        tries = 5   
        num = rn.randint(min_bound,max_bound)
        guess = rn.randint(min_bound,max_bound)
        
        while chances < tries:
            
            chances += 1
            if guess == num:
                print('Good job! The number was',num)
                break
            elif guess < num:
                print(guess,'Try higher')
                guess = rn.randint(guess+1,max_bound)
            elif guess > num:
                print(guess,'Try lower')
                guess = rn.randint (min_bound,guess-1)
                
        if guess == num:
            print('Congratulations!! You guessed the number on your try number ', chances)
        if guess != num:
            print('Game over! The number was' ,num)

3. We combine both a define the game function:

    def game():

        select = int(input('Choose game mode:'))
        if select not in range (1,3):
            print('Choose a valid game mode')
        elif select == 1:
            print('You have chosen to play yourself')
            player()
        elif select == 2:
            print('You have chosen to watch the machine play')
            machine()



        

