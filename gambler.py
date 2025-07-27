import random

MAX_LINE=3
MAX_BET=1000
MIN_BET=20
ITEMS =3
WHEEL =3

sym_f = {
    'A':3,
    'B':6,
    'C':8,
    'D':16,
}
sym_v = {
    'A':8,
    'B':4,
    'C':2,
    'D':1,
}

def outcome(cols,numlin,Bet,multi):
    win=0
    w_ln = []
    for line in range(numlin):
        symb = cols[0][line]
        for c in cols:
            symb_c = c[line]
            if symb != symb_c:
                break
        else:
            win+=multi[symb]*Bet
            w_ln.append(line+1)
    return win,w_ln



def slot_outcome(ro,co,syms):
    sym_c=[]
    for sym, sym_f in syms.items():
        for _ in range(sym_f):
            sym_c.append(sym)
    cols = []
    for _ in range(co):
        column = []
        cur_sym = sym_c[:]
        for _ in range(ro):
          pick = random.choice(cur_sym)
          cur_sym.remove(pick)
          column.append(pick)
        cols.append(column)
    return cols

def display(cols):
    for row in range(len(cols[0])):
        for i, column in enumerate(cols):
            if i != len(cols) - 1:
              print(column[row],end=" | ")
            else:
              print(column[row],end="")
        print()



def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        try:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Amount must be an integer")

    return amount


def no_of_lines():
   while True:
    lines = input(f"Enter the number of lines you want to bet on (1-{MAX_LINE}): ")
    try:
        lines = int(lines)
        if lines >= 1 and lines <= MAX_LINE:
            break
        else:
            print(f"Number of lines must be between 1 and {MAX_LINE}")
    except ValueError:
        print("Number of lines must be an integer")
   return lines

def bet():
    while True:
        Bet = input("Enter the amount you want to bet per line: $")
        try:
            Bet = int(Bet)
            if Bet >= MIN_BET and Bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between {MIN_BET} and {MAX_BET}")
        except ValueError:
            print("Bet must be an integer")

    return Bet

def mechanic(resources):

    numlin = no_of_lines()

    while True:
        Bet = bet()
        total_bet = numlin * Bet
        if total_bet <= resources:
            break
        else:
            print(f"Total bet must be less than ${resources}. You are short by ${total_bet - resources}")

    print(f"You have bet ${Bet} on {numlin} lines. So, your total bet is: {total_bet}")
    out = slot_outcome(ITEMS, WHEEL, sym_f)
    display(out)
    win, w_ln = outcome(out, numlin, Bet, sym_v)
    print(f"You have won a total of ${win} on {numlin} lines.")
    print(f"You won on line:", *w_ln)
    return win - total_bet

def main():
    resources = deposit()
    while True:
        print(f"You have ${resources} ")
        navi = input(f"Press 'Enter' or Q to quit: ")

        if navi.lower() == 'q':
           break

        resources += mechanic(resources)

main()

