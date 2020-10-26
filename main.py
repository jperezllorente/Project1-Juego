
import functions as fn

def game():
    
    select = int(input('Choose game mode between 1 and 2:'))
    if select not in range (1,3):
        print('Choose a valid game mode')
    elif select == 1:
        print('You have chosen to play yourself')
        fn.player()
    elif select == 2:
        print('You have chosen to watch the machine play')
        fn.machine()

game = game()








