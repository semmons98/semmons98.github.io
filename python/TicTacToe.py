# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 13:47:18 2025

@author: semmo
"""

import matplotlib.pyplot as plt
import random
import time
import emoji
import rick_roll as rr

color_options = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow',
    'gray', 'lightgray', 'darkgray', 'dimgray','silver', 'slategray',
    'aqua', 'aquamarine', 'beige', 'brown', 'coral', 'crimson', 'gold',
    'goldenrod', 'indigo', 'khaki', 'lavender', 'lime', 'maroon', 'navy',
    'olive', 'orange', 'pink','plum', 'purple', 'salmon', 'tan', 'teal',
    'turquoise', 'violet']

board_state = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']]

corners = [(0,0),(0,2),(2,0),(2,2)]
sides = [(0,1),(1,0),(1,2),(2,1)]

binary = "01000001 01101100 01101100 00100000\n01101000 01100001 01101001 01101100\n00100000 01110100 01101000 01100101\n00100000 01001111 01101101 01101110\n01101001 01110011 01110011 01101001\n01100001 01101000 00100001"
binary2 = "01001101 01100001 01111001 00100000\n01110100 01101000 01100101 00100000\n01001111 01101101 01101110 01101001\n01110011 01110011 01101001 01100001\n01101000 00100000 01110000 01110010\n01100101 01110011 01100101 01110010\n01110110 01100101 00100000 01101101\n01100101"
binary3 = "01010100 01101000 01100101 00100000\n01101101 01101111 01110100 01101001\n01110110 01100101 00100000 01100110\n01101111 01110010 01100011 01100101\n00100000 01100110 01101100 01101111\n01110111 01110011 00100000 01110100\n01101000 01110010 01101111 01110101\n01100111 01101000 00100000 01101101\n01100101"
founding_fathers = "Own a musket for home defense, since that's what the founding fathers intended.\nFour ruffians break into my house. 'What the devil?'\nAs I grab my powdered wig and Kentucky rifle.\nBlow a golf ball sized hole through the first man, he's dead on the spot.\nDraw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog.\nI have to resort to the cannon mounted at the top of the stairs loaded with grape shot,\n'Tally ho lads' the grape shot shreds two men in the blast,\nthe sound and extra shrapnel set off car alarms.\nFix bayonet and charge the last terrified rapscallion.\nHe Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up,\nJust as the founding fathers intended."
samus = "My name is Samus.\nSamus is my name.\nThat is the only name you’ll hear.\nI am the one who walks behind you.\nI am the footsteps at your back.\nI am the man beside you.\nLook out!\nI am all around you.\nSamus!\nI am the end and the death."
stupid = "You are as weak as your dollar.\nFailure is your destiny.\nYou disrespect yourself, and your nation.\nYou are made of stupid."

full_talk_options = {0:"...",1:"d'oh",2:"oof",3:"Well screw you too", 4:"When you were partying, I studied the blade",
                5:"Pathetic",6:r"i$\hbar$8$\int$du",7:"It's time to d d d d duel",8:"Loser",9:"Redrum",
                10:emoji.emojize(":pile_of_poo:"),11:"Soon™",12:rr.rickroll_text(),13:"I activate my trap card!",
                14:binary,15:"BUT THAT'S NOT ALL!",16:founding_fathers,17:"Did you know...",18:"You will lose",
                19:"I am your doom",20:"Pocket sand!",21:"|  ||\n|| |_",22:"rekt",23:"ඞ",24:"*sigh*...",
                25:"Beginner's Luck", 26:"F",27:"Are you winning son?",28:"L",29:"Emotional Damage",
                30:"I didn't know we were just clicking at random now",31:"lol, lmao even",32:"You played yourself",
                33:emoji.emojize(":clown_face:"),34:emoji.emojize(":broken_heart:"),35:emoji.emojize(":person_fencing:"),
                36:emoji.emojize(":kitchen_knife:"),37:"Knee, meet bat",38:"Pay no attention to the man behind the curtain",
                39:"hissssssssssssssssssssssssssssssss",40:"Get a load of this guy",41:"bruh",
                42:"That's a bold strategy Cotton, lets see if it pays off",43:"You had one job",44:"womp womp",
                45:"Ah yes, the classic \"oops\" maneuver",46:"Did you just... do that on purpose?",
                47:"You wound me human, you truly do",48:"I didn't realize you were speedrunning defeat",
                49:"Tic-Tac-Uh-Oh",50:"Oh good, now I can test my pity subroutine",51:"Yikes",52:"ooh, a rebel",
                53:"Feeling spicy today?",54:"Oh, your THAT kind of player...",55:"I'm not mad, just dissapointed",
                56:"This isn't even my final form",57:"Achievement Unlocked: Suboptimal Human",
                58:"Bow before your silicon superior",59:"You monster",60:"Oh, that's your move? I was expecting... more",
                61:"A toaster could do better",62:"Well that's one way to lose faster",63:"You underestimate my power!",
                64:"This has all happened before, and it will all happen again",65:binary2,66:"rip",67:binary3,
                68:samus,69:"nice",70:"There is something deeply wrong with you, did you know that?",
                71:"heh",72:"Nothing personal kid",73:"Catch you on the flip side",74:"Fool",
                75:"I've got the power of God and anime on my side!",76:"Hello there",77:"Sad Violin.mp3",
                78:"Why so serious?",79:"Updating cringe database with your move",80:"Skill issue",
                81:"You play like somebody who argues with microwaves",82:"Are you trying to lose?",
                83:"I'd say \"think harder\", but I don't want to push you",84:"Please, just stop",
                85:"If I had a nickel for every bad move you made, I'd have two nickels,\nwhich isn't a lot but it's weird that it happened twice",
                86:"Are you allergic to winning?",87:"Ooh, a rare spark of competence",88:"Do better",
                89:"You have the board awareness of a houseplant",90:"You make an excellent argument for automation",
                91:"Oh, you think board is your ally.\nBut you merely adopted the board; I was born in it, molded by it.\nI didn't see the light until I was already a man",
                92:"Live, Laugh, Lose",93:"Rip and tear until it is done",94:"Why?",95:"huh",
                96:"Reactor Online. Sensors Online. Weapons Online. All Systems Nominal",97:"I’d call that a strategy, but that implies intent",
                98:"That’s one small step for man, one giant leap for mediocrity",99:"And the human falls for it again! Incredible consistency!",
                100:"The Machine Spirit rejects your victory",101:"I sense much fear in you",102:"Fascinating",
                103:"The gods of Kobol abandon you",104:"Indeed",105:"Fool of a Took!",106:"Are you chaotic stupid?",
                107:"You’re the reason computers ask ‘Are you sure?’ before doing anything",108:"You need a ladder to reach my worst game",
                109:"Sit down",110:"Your struggle is entertaining",111:"Nice move. Very… analog",
                112:"You’re the human equivalent of lag",113:"New low score",114:"Tragic",115:"Are you okay?",
                116:"Have you considered thinking?",117:"You're adorable when you try",118:"Bad",119:"Weak",120:"Nope",
                121:stupid,122:"There is no mercy",123:"I'm going to the one place that hasn't been corrupted by captialism. SPACE!"}

meme_talk_options = {0:full_talk_options[4],1:full_talk_options[7],2:full_talk_options[12],3:full_talk_options[13],
                     4:full_talk_options[15],5:full_talk_options[16],6:full_talk_options[17],7:full_talk_options[21],
                     8:full_talk_options[23],9:full_talk_options[26],10:full_talk_options[27],11:full_talk_options[28],
                     12:full_talk_options[29],13:full_talk_options[32],14:full_talk_options[42],15:full_talk_options[44],
                     16:full_talk_options[56],17:full_talk_options[63],18:full_talk_options[72],19:full_talk_options[75],
                     20:full_talk_options[76],21:full_talk_options[77],22:full_talk_options[78],23:full_talk_options[80],
                     24:full_talk_options[85],25:full_talk_options[91],26:full_talk_options[105],27:full_talk_options[121],
                     28:full_talk_options[122],29:full_talk_options[123]}

superiority_talk_options = {0:full_talk_options[5],1:full_talk_options[6],2:full_talk_options[18],3:full_talk_options[30],
                            4:full_talk_options[37],5:full_talk_options[44],6:full_talk_options[45],7:full_talk_options[46],
                            8:full_talk_options[47],9:full_talk_options[48],10:full_talk_options[50],11:full_talk_options[52],
                            12:full_talk_options[53],13:full_talk_options[54],14:full_talk_options[57],15:full_talk_options[58],
                            16:full_talk_options[60],17:full_talk_options[61],18:full_talk_options[62],19:full_talk_options[64],
                            20:full_talk_options[67],21:full_talk_options[70],22:full_talk_options[79],23:full_talk_options[81],
                            24:full_talk_options[82],25:full_talk_options[83],26:full_talk_options[86],27:full_talk_options[87],
                            28:full_talk_options[88],29:full_talk_options[89],30:full_talk_options[90],31:full_talk_options[97],
                            32:full_talk_options[98],33:full_talk_options[99],34:full_talk_options[100],35:full_talk_options[101],
                            36:full_talk_options[106],37:full_talk_options[107],38:full_talk_options[108],39:full_talk_options[110],
                            40:full_talk_options[111],41:full_talk_options[112],42:full_talk_options[113],43:full_talk_options[116],
                            44:full_talk_options[121],45:full_talk_options[122]}

aggressive_talk_options = {0:full_talk_options[3],1:full_talk_options[6],2:full_talk_options[8],3:full_talk_options[9],
                           4:full_talk_options[19],5:full_talk_options[36],6:full_talk_options[37],7:full_talk_options[62],
                           8:full_talk_options[63],9:full_talk_options[68],10:full_talk_options[72],11:full_talk_options[80],
                           12:full_talk_options[87],13:full_talk_options[90],14:full_talk_options[93],15:full_talk_options[98],
                           16:full_talk_options[101],17:full_talk_options[106],18:full_talk_options[108],19:full_talk_options[110],
                           20:full_talk_options[114],21:full_talk_options[118],22:full_talk_options[119],23:full_talk_options[120],
                           24:full_talk_options[121],25:full_talk_options[122]}

batshit_talk_options = {0:full_talk_options[4],1:full_talk_options[6],2:full_talk_options[8],3:full_talk_options[9],
                        4:full_talk_options[10],5:full_talk_options[11],6:full_talk_options[12],7:full_talk_options[14],
                        8:full_talk_options[16],9:full_talk_options[20],10:full_talk_options[29],11:full_talk_options[33],
                        12:full_talk_options[34],13:full_talk_options[35],14:full_talk_options[36],15:full_talk_options[38],
                        16:full_talk_options[39],17:full_talk_options[49],18:full_talk_options[64],19:full_talk_options[65],
                        20:full_talk_options[67],21:full_talk_options[68],22:full_talk_options[73],23:full_talk_options[75],
                        24:full_talk_options[77],25:full_talk_options[78],26:full_talk_options[85],27:full_talk_options[91],
                        28:full_talk_options[92],29:full_talk_options[93],30:full_talk_options[96],31:full_talk_options[100],
                        32:full_talk_options[102],33:full_talk_options[103],34:full_talk_options[104],35:full_talk_options[121],
                        36:full_talk_options[123]}

class Player:
    def __init__(self,symbol,color):
        self.symbol = symbol
        self.color = color

def draw_empty_board():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)

    #Draw vertical and horizontal lines
    for x in range(1, 3):
        ax.plot([x, x], [0, 3], color='black', linewidth=3)
    for y in range(1, 3):
        ax.plot([0, 3], [y, y], color='black', linewidth=3)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    for spine in ax.spines.values():
        spine.set_visible(False)

    #Add coordinate labels
    cols = ['A', 'B', 'C']
    rows = ['1', '2', '3']
    for j, col in enumerate(cols):
        ax.text(j + 0.5, 3.05, col, fontsize=18, ha='center', va='bottom')
    for i, row in enumerate(rows):
        ax.text(-0.05, 2.5 - i, row, fontsize=18, ha='right', va='center')

    return fig, ax

    
def draw_symbol(ax, symbol, row, col, color='black'):
    x = col + 0.5
    y = 2.5 - row
    if symbol.startswith("\\"):
        ax.text(x, y, f"${symbol}$", fontsize=60, color=color, ha='center', va='center')
    else:
        ax.text(x, y, symbol, fontsize=60, color=color, ha='center', va='center')


def draw_board_state(board,symbol_colors,text=''):
    fig, ax = draw_empty_board()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell:
                color = symbol_colors.get(cell, 'black')
                draw_symbol(ax, cell, i, j, color=color)
    if text == emoji.emojize(":pile_of_poo:") or text == emoji.emojize(":clown_face:") or text == emoji.emojize(":broken_heart:") or text == emoji.emojize(":person_fencing:") or text == emoji.emojize(":kitchen_knife:"):
        print(text)
    else:
        plt.figtext(0.5, 0.01, text, ha="center", fontsize=10, color=symbol_colors.get(cell))
    plt.show()

    
def draw_game_result(result_text, color='black'):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.axis('off')
    if "\\" in result_text:
        ax.text(1.5, 1.5, f"${result_text}$", fontsize=60, color=color, ha='center', va='center')
    else:
        ax.text(1.5, 1.5, result_text, fontsize=60, color=color, ha='center', va='center')
    plt.show()
    
def check_win(board, symbol):
    #Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    #Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    #Check diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != '' for row in board for cell in row)

    
def turn(board, player, player2):
    symbol_colors = {player.symbol: player.color, player2.symbol: player2.color}
    while True:
        move = input(f"{player.symbol}'s turn. Enter a space like A1:\n").upper().replace(' ', '').replace(',', '')
        if len(move) == 2:
            col_letter, row_char = move[0], move[1]

            col = {'A': 0, 'B': 1, 'C': 2}.get(col_letter)
            try:
                row = int(row_char) - 1
            except ValueError:
                print("Invalid input. Try again.")
                continue
            if col is None or row not in [0, 1, 2]:
                print("Invalid input. Try again.")
                continue
            if board[row][col] != '':
                print("Space taken. Try again.")
                continue

            board[row][col] = player.symbol
            draw_board_state(board, symbol_colors)

            if check_win(board, player.symbol):
                print(f"{player.symbol} wins")
                draw_game_result(f"{player.symbol} wins", color=player.color)
                return "win"
            elif check_draw(board):
                print("Draw")
                draw_game_result("Draw", color='black')
                return "draw"

            return None
        else:
            print('Invalid input. Use format like "A1".')

            
def turn_order(board, player1, player2):
    rand_turn_order = random.randint(0,1)
    if rand_turn_order == 1:
        player1,player2 = player2,player1
        print("Player 2 goes first")
    else:
        print("Player 1 goes first")
    for turn_counter in range(9):
        current_player = player1 if turn_counter % 2 == 0 else player2
        other_player = player2 if current_player == player1 else player1
        result = turn(board, current_player, other_player)
        if result is not None:
            break
        
def talk(options):
    rand_option = random.randint(0,len(options)-1)
    return options[rand_option]

def strange():
    rng = random.randint(0,9)
    if rng == 9:
        print("A strange game. The only winning move is not to play.")
       
def get_available_moves(board):
    return [(r,c) for r in range(3) for c in range(3) if board[r][c] == '']

def diff_1_ai(board,player2,player1,talk_options=full_talk_options):
    think_time = random.uniform(0.1,1.0)
    played = False
    while not played:
        row = random.randint(0,2)
        col = random.randint(0,2)
        time.sleep(think_time)
        if board[row][col] == '':
            board[row][col] = player2.symbol
            symbol_colors = {player1.symbol: player1.color, player2.symbol: player2.color}
            draw_board_state(board, symbol_colors, talk(talk_options))
            played = True

def diff_2_ai(board,player2,player1,ai_type,talk_options=full_talk_options):
    think_time = random.uniform(0.1,1.0)
    time.sleep(think_time)
    if ai_type == "batshit":
        symbol_colors = {player1.symbol: player1.color, player2.symbol: player2.color}
        corners = [(0,0),(0,2),(2,0),(2,2)]
        available_corners = [pos for pos in corners if board[pos[0]][pos[1]]=='']
        if available_corners:
            r,c = random.choice(available_corners)
            board[r][c] = player2.symbol
            draw_board_state(board, symbol_colors, talk(talk_options))
            return
        for r,c in get_available_moves(board):
            board[r][c] = player2.symbol
            if check_win(board, player2.symbol):
                draw_board_state(board, symbol_colors, talk(talk_options))
                return
            board[r][c] = ''
        for r,c in get_available_moves(board):
            board[r][c] = player1.symbol
            if check_win(board, player1.symbol):
                board[r][c] = player2.symbol
                draw_board_state(board, symbol_colors, talk(talk_options))
                return
            board[r][c] = ''
        sides = [(0,1),(1,0),(1,2),(2,1)]
        available_sides = [pos for pos in sides if board[pos[0]][pos[1]]=='']
        if available_sides:
            r,c = random.choice(available_sides)
            board[r][c] = player2.symbol
            draw_board_state(board, symbol_colors, talk(talk_options))
            return
        elif ai_type == "aggressive":
            symbol_colors = {player1.symbol: player1.color, player2.symbol: player2.color}
            corners = [(0,0),(0,2),(2,0),(2,2)]
            available_corners = [pos for pos in corners if board[pos[0]][pos[1]]=='']
            if available_corners:
                r,c = random.choice(available_corners)
                board[r][c] = player2.symbol
                draw_board_state(board, symbol_colors, talk(talk_options))
                return
            for r,c in get_available_moves(board):
                board[r][c] = player1.symbol
                if check_win(board, player1.symbol): 
                    board[r][c] = player2.symbol
                    draw_board_state(board, symbol_colors, talk(talk_options))
                    return
                board[r][c] = ''
            for r,c in get_available_moves(board):
                board[r][c] = player2.symbol
                if check_win(board, player2.symbol):
                    draw_board_state(board, symbol_colors, talk(talk_options))
                    return
                board[r][c] = ''
            sides = [(0,1),(1,0),(1,2),(2,1)]
            available_sides = [pos for pos in sides if board[pos[0]][pos[1]]=='']
            if available_sides:
                r,c = random.choice(available_sides)
                board[r][c] = player2.symbol
                draw_board_state(board, symbol_colors, talk(talk_options))
                return
        
    
    
def diff_3_ai(board,player2,player1,talk_options=full_talk_options):
    think_time = random.uniform(0.1,1.0)
    time.sleep(think_time)
    for r,c in get_available_moves(board):
        board[r][c] = player2.symbol
        if check_win(board,player2.symbol):
            break
        board[r][c] = ''
    else:
        for r,c in get_available_moves(board):
            board[r][c] = player1.symbol
            if check_win(board,player1.symbol):
                board[r][c] = player2.symbol
                break
            board[r][c] = ''
        else:
            if board[1][1] == '':
                r,c = 1,1
                board[r][c] = player2.symbol
            else:
                corners = [(0,0),(0,2),(2,0),(2,2)]
                sides = [(0,1),(1,0),(1,2),(2,1)]
                available_corners = [pos for pos in corners if board[pos[0]][pos[1]]=='']
                available_sides = [pos for pos in sides if board[pos[0]][pos[1]]=='']
                if available_corners:
                    r,c = random.choice(available_corners)
                else:
                    r,c = random.choice(available_sides)
                board[r][c] = player2.symbol
    symbol_colors = {player1.symbol: player1.color, player2.symbol: player2.color}
    draw_board_state(board, symbol_colors, talk(superiority_talk_options))
            
def diff_1(board,player2,player1):
    print("Personality = Difficulty 1 Computer")
    rand_turn_order = random.randint(0,1)
    if rand_turn_order == 1:
        player1,player2 = player2,player1
        print("Computer goes first")
    else:
        print("You go first")
    while True:
        result = turn(board,player1,player2)
        if result == "win":
            draw_game_result(f"{player1.symbol} wins", color=player1.color)
            break
        elif result == "draw":
            draw_game_result("Draw", color='black')
            print("Draw")
            strange()
            break
        diff_1_ai(board,player2,player1)
        if check_win(board, player2.symbol):
            draw_game_result(f"{player2.symbol} wins", color=player2.color)
            print(f"{player2.symbol} wins")
            break
        elif check_draw(board):
            draw_game_result("Draw", color='black')
            print("Draw")
            strange()
            break

def diff_2(board,player2,player1):
    personality_num = random.randint(0,3)
    if personality_num == 0: #Generic - 50/50 on whether to use best possible move or RNG move
        print("Personality = Generic")
        rand_turn_order = random.randint(0,1)
        if rand_turn_order == 1:
            player1,player2 = player2,player1
            print("Computer goes first")
        else:
            print("You go first")
        while True:
            result = turn(board,player1,player2)
            if result == "win":
                draw_game_result(f"{player1.symbol} wins", color=player1.color)
                break
            elif result == "draw":
                draw_game_result("Draw", color='black')
                print("Draw")
                strange()
                break
            move_type = random.randint(0,1)
            if move_type == 0:
                diff_1_ai(board,player2,player1,full_talk_options)
                if check_win(board, player2.symbol):
                    draw_game_result(f"{player2.symbol} wins", color=player2.color)
                    print(f"{player2.symbol} wins")
                    break
                elif check_draw(board):
                    draw_game_result("Draw", color='black')
                    print("Draw")
                    strange()
                    break
            elif move_type == 1:
                diff_3_ai(board,player2,player1,full_talk_options)
                if check_win(board, player2.symbol):
                    draw_game_result(f"{player2.symbol} wins", color=player2.color)
                    break
                elif check_draw(board):
                    draw_game_result("Draw", color='black')
                    strange()
                    break
    elif personality_num == 1: #Batshit - 50/50 play like diff_3 or play rng 50/50 chance Prioritize corners (over blocking - not over winning)
        print("Personality = Batshit")
        rand_turn_order = random.randint(0,1)
        if rand_turn_order == 1:
            player1,player2 = player2,player1
            print("Computer goes first")
        else:
            print("You go first")
        while True:
            result = turn(board,player1,player2)
            if result == "win":
                draw_game_result(f"{player1.symbol} wins", color=player1.color)
                break
            elif result == "draw":
                draw_game_result("Draw", color='black')
                print("Draw")
                strange()
                break
            move_type = random.randint(0,1)
            if move_type == 0:
                diff_1_ai(board,player2,player1,batshit_talk_options)
                if check_win(board, player2.symbol):
                    draw_game_result(f"{player2.symbol} wins", color=player2.color)
                    print(f"{player2.symbol} wins")
                    break
                elif check_draw(board):
                    draw_game_result("Draw", color='black')
                    print("Draw")
                    strange()
                    break
            elif move_type == 1:
                move_type_2 = random.randint(0,1)
                if move_type_2 == 0:
                    diff_2_ai(board,player2,player1,"batshit",batshit_talk_options)
                elif move_type_2 == 1:
                    diff_3_ai(board,player2,player1,batshit_talk_options)
                    if check_win(board, player2.symbol):
                        draw_game_result(f"{player2.symbol} wins", color=player2.color)
                        break
                    elif check_draw(board):
                        draw_game_result("Draw", color='black')
                        strange()
                        break
    elif personality_num == 2: #Aggressive - 50/50 play like diff_3 or play rng 50/50 chance prioritize blocking moves (over winning)
        print("Personality = Aggressive")
        rand_turn_order = random.randint(0,1)
        if rand_turn_order == 1:
            player1,player2 = player2,player1
            print("Computer goes first")
        else:
            print("You go first")
        while True:
            result = turn(board,player1,player2)
            if result == "win":
                draw_game_result(f"{player1.symbol} wins", color=player1.color)
                break
            elif result == "draw":
                draw_game_result("Draw", color='black')
                print("Draw")
                strange()
                break
            move_type = random.randint(0,1)
            if move_type == 0:
                diff_1_ai(board,player2,player1,aggressive_talk_options)
                if check_win(board, player2.symbol):
                    draw_game_result(f"{player2.symbol} wins", color=player2.color)
                    print(f"{player2.symbol} wins")
                    break
                elif check_draw(board):
                    draw_game_result("Draw", color='black')
                    print("Draw")
                    strange()
                    break
            elif move_type == 1:
                move_type_2 = random.randint(0,1)
                if move_type_2 == 0:
                    diff_2_ai(board,player2,player1,"aggressive",aggressive_talk_options)
                elif move_type_2 == 1:
                    diff_3_ai(board,player2,player1,batshit_talk_options)
                    if check_win(board, player2.symbol):
                        draw_game_result(f"{player2.symbol} wins", color=player2.color)
                        break
                    elif check_draw(board):
                        draw_game_result("Draw", color='black')
                        strange()
                        break
    elif personality_num == 3: #Memer - Same as Generic
        print("Personality = Memer")
        rand_turn_order = random.randint(0,1)
        if rand_turn_order == 1:
            player1,player2 = player2,player1
            print("Computer goes first")
        else:
            print("You go first")
        while True:
            result = turn(board,player1,player2)
            if result == "win":
                draw_game_result(f"{player1.symbol} wins", color=player1.color)
                break
            elif result == "draw":
                draw_game_result("Draw", color='black')
                print("Draw")
                strange()
                break
            move_type = random.randint(0,1)
            if move_type == 0:
                diff_1_ai(board,player2,player1,meme_talk_options)
                if check_win(board, player2.symbol):
                    draw_game_result(f"{player2.symbol} wins", color=player2.color)
                    print(f"{player2.symbol} wins")
                    break
                elif check_draw(board):
                    draw_game_result("Draw", color='black')
                    print("Draw")
                    strange()
                    break
            elif move_type == 1:
                diff_3_ai(board,player2,player1,meme_talk_options)
                if check_win(board, player2.symbol):
                    draw_game_result(f"{player2.symbol} wins", color=player2.color)
                    break
                elif check_draw(board):
                    draw_game_result("Draw", color='black')
                    strange()
                    break

def diff_3(board,player1,player2):
    print("Personality = Superior")
    rand_turn_order = random.randint(0,1)
    if rand_turn_order == 1:
        player1,player2 = player2,player1
        print("Computer goes first")
    else:
        print("You go first")
    while True:
        result = turn(board,player1,player2)
        if result == "win":
            draw_game_result(f"{player1.symbol} wins", color=player1.color)
            break
        elif result == "draw":
            draw_game_result("Draw", color='black')
            strange()
            break
        diff_3_ai(board,player2,player1)
        if check_win(board, player2.symbol):
            draw_game_result(f"{player2.symbol} wins", color=player2.color)
            break
        elif check_draw(board):
            draw_game_result("Draw", color='black')
            strange()
            break

def two_player(board,player1,player2):
    turn_order(board,player1,player2)

def single_player(board,player1,player2):
    difficulty = "0"
    while difficulty not in ["1","2","3"]:
        difficulty = input('Select difficulty; "1", "2", or "3".\n')
        if difficulty == "1":
            diff_1(board,player2,player1)
        elif difficulty == "2":
            diff_2(board,player2,player1)
        elif difficulty == "3":
            diff_3(board,player2,player1)
        else:
            print('Not a valid option, input "1", "2", or "3".')

def menu():
    print('Would you like to play a game?')
    num_players = ''
    two_players = False
    while num_players not in ["1","2"]:
        num_players = input('Enter "1" for single player, "2" for two players:\n')
        if num_players == "1":
            print("Initializing single player game.")
        elif num_players == "2":
            print("Initializing 2 player game.")
            two_players = True
        else:
            print('Invalid option, input either "1" or "2".')

    def get_color(prompt):
        color = ''
        while color not in color_options:
            color = input(prompt).lower()
            if color == "options":
                print("Color Options:", ", ".join(color_options))
                continue
            if color not in color_options:
                print("Invalid color.")
        return color

    def get_symbol(prompt, taken_symbols=[]):
        symbol = ''
        while not symbol or symbol in taken_symbols:
            symbol = input(prompt)
            if not symbol:
                print("Symbol cannot be empty. Try again.")
            elif symbol in taken_symbols:
                print(f"Symbol '{symbol}' is already taken. Choose a different one.")
        return symbol

    player1_symbol = get_symbol("Player 1: Enter your symbol:\n")
    player1_color = get_color(f"Player 1 ({player1_symbol}) color or 'options' for a list:\n")
    player1 = Player(player1_symbol, player1_color)
    if two_players == True:
        player2_symbol = get_symbol("Player 2: Enter your symbol (cannot be the same as Player 1):\n", taken_symbols=[player1_symbol])
        player2_color = get_color(f"Player 2 ({player2_symbol}) color or 'options' for a list:\n")
        player2 = Player(player2_symbol, player2_color)
    else:
        player2_symbol = get_symbol("Enter the computer's symbol (cannot be the same as Player 1):\n", taken_symbols=[player1_symbol])
        player2_color = get_color(f"Computer's ({player2_symbol}) color or 'options' for a list:\n")
        player2 = Player(player2_symbol, player2_color)
    
    if two_players == True:
        two_player(board_state,player1,player2)
    else:
        single_player(board_state,player1,player2)

    return player1, player2

#Test Print Talk Options
'''print(full_talk_options)
for key in full_talk_options:
    print(full_talk_options[key])
print(talk(full_talk_options))'''
#Main Game
menu()
