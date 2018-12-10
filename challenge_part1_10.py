
import random

def hangman():
    word_list = ['cat','dog','iwai','yamada','tree','yamazi','ziyama','want']
    number = random.randint(0,7)
    word = word_list[number]
    
    wrong = 0
    stages = ['',
              '________        ',
              '|       |       ',
              '|       |       ',
              '|       O       ',
              '|     / |\      ',
              '|      / \      ',
              '|               '
              ]
    rletters = list(word)   # ['o','r','a','n','g','e']
    board = ['_'] * len(word)   # ['_','_','_','_','_','_']
    win = False
    print('ハングマンへようこそ！')

    while wrong < len(stages) - 1:
        print('\n')
        msg = 'アルファベット一文字を予想してね'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'  # ['o','r','$','n','g','e']
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))

        if '_' not in board:
            print('あなたの勝ち！')
            print(' '.join(board))
            win = True
            break

    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け！正解は {}.'.format(word))



hangman()
