n = int(input('ENTER n with n is a positive integer: '))
k = int(input('ENTER k with k is also a positive integer and k < n: '))
rounds = []
round_number = 1
players = ['A', 'B']
now_player = 0
error_pA = error_pB = 0
while True:
    if n < 1 or k < 1 or k >= n:
        print('RE-ENTER THE VALUE OF n AND k .')
        n = int(input('INPUT n: '))
        k = int(input('INPUT k: '))
    print(f'ROUND {round_number}')
    while n > 0:
        move = int(input(f'TURN for {players[now_player]}, enter from 1 to {min(n, k)}: '))
        if 1 <= move <= min(n, k):
            n -= move
            now_player = 1 - now_player
        else:
            if (players[now_player] == 'A'):
                error_pA +=1
            else:
                error_pB +=1
        if n <= 0:
            rounds.append(players[now_player])
            print(f'{players[now_player]} is winnerRound {round_number}')
            round_number += 1
    continue_game = input('CONTINUE? YES : NO').upper()
    if continue_game != 'YES':
        break
print('---THE RESULT FOR THIS GAME---')
p1 = rounds.count('A')
p2 = rounds.count('B')
A_win = []
B_win = []
if p1 > p2:
    print('A is winner winner chicken')
    for i in range(len(rounds)):
        if rounds[i] == 'A':
            A_win.append(i+1)
    print("A's winRounds :", ' '.join(str(e) for e in A_win))
elif p2 > p1:
    print('B is winner winner chicken')
    for i in range(len(rounds)):
        if rounds[i] == 'B':
            B_win.append(i+1)
    print("B's winRounds : ", ' '.join(str(e) for e in B_win))
else:
    if error_pA > error_pB:
        print('B is winner winner chicken')
        for i in range(len(rounds)):
            if rounds[i] == 'B':
                B_win.append(i+1)
        print("B's winRounds : ",' '.join(str(e) for e in B_win))
    elif error_pB > error_pA:
        print('A is winner winner chicken')
        for i in range(len(rounds)):
            if rounds[i] == 'A':
                A_win.append(i+1)
        print("A's winRounds :", ' '.join(str(e) for e in A_win))
    else:
        print('---TIE---')
        for i, winner in enumerate(rounds, start=1):
            print(f'Round {i}: {winner}')
