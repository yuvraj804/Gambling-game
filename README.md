# Slot Machine 

## I do not condone gambling, but if you really want to, you can do it here!

## Mechanism

This simulates a slot machine commonly found in casinos.
The program will ask you to deposit fake dollars, which must be a positive integer. Then, it will prompt you to choose the number of lines—that is, the number of rows (from top to bottom) you would like to bet on.
Next, it will ask how much you want to bet on each line, with some predefined lower and upper limits.
For example, if you choose 2 lines and bet $60 per line, your total bet will be:
60 × 2 = $120.

You win money if a row (that you bet on) contains the same character across all columns.
Each character has a different frequency (rarity), and therefore offers a different reward multiplier.

### Default values
CHARACTER | FREQUENCY | MULTIPLIER =
A        |     3     |    8,
B        |     6     |    4,
C        |     12    |    2,
D        |     16    |    1,

MAX BET = 10000 and MIN BET=20

The values can easily be changed by changing constants 

