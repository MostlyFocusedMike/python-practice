player_win_matrix = {
    's': { 'p': True, 'r': False },
    'p': { 'r': True, 's': False },
    'r': { 's': True, 'p': False },
}

computer = 'r'
player = 'r'

if computer == player:
    print('You tied!')
else:
    did_player_win = player_win_matrix[player][computer]
    print(f"You {'won!'if did_player_win else 'lost.'}")