# Sarah Grobe
# CS 021
# Final project

# This program creates a board game in which two players can roll dice and draw cards that can move them forwards or
# backwards. The first to reach the end wins, and the winner is recorded and saved in a file.


# import necessary modules
import turtle
import random

# clone turtle so that each player has their own marker
p1 = turtle.Turtle()
p2 = p1.clone()

# length of one space on the board
SPACE_LENGTH = 70

# create the "deck of cards"
cards = ["Move forward 2 spaces", "Move forward 2 spaces", "Move forward 2 spaces",
         "Move forward 2 spaces", "Move forward 2 spaces", "Move back 1 space",
         "Move back 1 space", "Move back 1 space", "Move back 1 space",
         "Move back 1 space", "Move back 1 space", "Move back 2 spaces",
         "Move back 2 spaces", "Move back 2 spaces", "Move back 2 spaces",
         "Move back 2 spaces", "Move forward 3 spaces", "Move forward 3 spaces",
         "Move forward 3 spaces", "Move back 3 spaces", "Move back 3 spaces",
         "Move back 3 spaces","Move forward 4 spaces", "Move backward 4 spaces",
         "Move your OPPONENT back 5 spaces!"]


# the main function dictates the flow of the gameplay. First, information is gathered from each player. It then calls
# the gameplay functions such as roll_dice and draw_card to organize the gameplay.
def main():
    # draw the game board
    start_position = draw_game_board()
    # briefly explain game
    input('Welcome to my board game! (Press Enter to continue)')
    input('The object of the game is to make it once around the board before your opponent. (Press Enter to continue)')
    input("You'll move each turn by rolling a die and drawing cards, which can move you\n" +
          "forwards or backwards. (Press Enter to continue)")
    input("At the end, the winner's name will be saved to a file. (Press Enter to continue)")
    input('The first step is to enter your name and choose a color! (Press Enter to continue)')
    # obtain player 1 name and color choice
    player1 = input("Player 1's name: ")
    # validate color choice
    valid = 'no'
    while valid == 'no':
        p1color = input("Player 1, choose a color, red, blue, green, or gray: ")
        if p1color == 'red' or p1color == 'blue' or p1color == 'green' or p1color == 'gray':
            valid = 'yes'
        else:
            print("Color must be red, blue, green, or gray.")

    # obtain player 2 name and color choice
    player2 = input("Player 2's name: ")
    # validate color choice (an acceptable color & different from player 1's)
    valid = 'no'
    while valid == 'no':
        p2color = input("Player 2, choose a color, red, blue, green, or gray: ")
        if p2color == 'red' or p2color == 'blue' or p2color == 'green' or p2color == 'gray':
            if p1color != p2color:
                valid = 'yes'
            else:
                print("Color must be different from Player 1's.")
        else:
            print("Color must be red, blue, green, or gray.")

    # begin playing!
    go = 'yes'  # go = 'yes' indicates that there is currently no winner
    p1total = 0  # total number of spaces player 1 has moved
    # player 1 rolls dice
    input(player1 + ', hit Enter to roll!')
    roll = roll_dice()
    # print results of the roll
    print("You rolled ", roll, "!", sep='')
    # move player according to the roll
    direction = 'forward'
    p1position, p1total = move_gamepiece(p1color, roll, start_position, p1total, player1, p1, direction, go)

    # draw extra card if player lands on the special space
    if p1total == 5:
        input(player1 + ', hit Enter to draw an EXTRA card!')
        direction, roll = draw_card()
        if direction == 'opponent':
            print('Opponent cannot move back!')
        else:
            p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)

    # player 1 draws a card
    input(player1 + ', hit Enter to draw a card!')
    direction, roll = draw_card()
    # move player according to the results of the card
    if direction == 'opponent':
        print('Opponent cannot move back!')
    else:
        p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)

    # draw extra card if player lands on the special space
    if p1total == 5:
        input(player1 + ', hit Enter to draw an EXTRA card!')
        direction, roll = draw_card()
        if direction == 'opponent':
            print('Opponent cannot move back!')
        else:
            p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)

    print()  # print blank line to separate the turns
    p2total = 0  # total number of spaces player 2 has moved
    # player 2 rolls dice
    input(player2 + ', hit Enter to roll!')
    roll = roll_dice()
    # print results of roll
    print("You rolled ", roll, "!", sep='')
    # move player according to the roll
    direction = 'forward'
    p2position, p2total = move_gamepiece(p2color, roll, start_position, p2total, player2, p2, direction, go)

    # draw extra card if player lands on the special space
    if p2total == 5:
        input(player2 + ', hit Enter to draw an EXTRA card!')
        direction, roll = draw_card()
        # move player according to the results of the card
        if direction == 'opponent':
            direction = 'backward'
            p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)
        else:
            p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction, go)

    # player 2 draws a card
    input(player2 + ', hit Enter to draw a card!')
    direction, roll = draw_card()
    # move player according to the results of the card
    if direction == 'opponent':
        direction = 'backward'
        p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)

    else:
        p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction, go)

    # draw extra card if player lands on the special space
    if p2total == 5:
        input(player2 + ', hit Enter to draw an EXTRA card!')
        direction, roll = draw_card()
        # move player according to the results of the card
        if direction == 'opponent':
            direction = 'backward'
            p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)
        else:
            p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction, go)

    # while loop: keep playing until someone reaches the end
    while go == 'yes':
        print()  # print blank line to separate the turns
        # player 1 rolls
        input(player1 + ', hit Enter to roll!')
        roll = roll_dice()
        # print results of the roll
        print("You rolled ", roll, "!", sep='')
        # player 1 moves according to the roll
        direction = 'forward'
        p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)

        # draw extra card if player lands on the special space
        if p1total == 5 or p1total == 14 or p1total == 23 or p1total == 32:
            input(player1 + ', hit Enter to draw an EXTRA card!')
            direction, roll = draw_card()

            if direction == 'opponent':
                direction = 'backward'
                p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction, go)

            else:
                p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)

        # if player 1 wins, go = 'no' and it falls out of the while loop
        if p1total >= 36 or p2total >= 36:
            go = 'no'

        # continues on if player 1 did not win on the roll
        if go == 'yes':
            # player 1 draws a card
            input(player1 + ', hit Enter to draw a card!')
            direction, roll = draw_card()

            # move player according to the result of the card
            if direction == 'opponent':
                direction = 'backward'
                p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction, go)
            else:
                p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction, go)

            # draw extra card if player lands on the special space
            if p1total == 5 or p1total == 14 or p1total == 23 or p1total == 32:
                input(player1 + ', hit Enter to draw an EXTRA card!')
                direction, roll = draw_card()

                if direction == 'opponent':
                    direction = 'backward'
                    p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction,
                                                         go)

                else:
                    p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction,
                                                         go)

            # if player 1 wins, go = 'no' and it falls out of the while loop
            if p1total >= 36 or p2total >= 36:
                go = 'no'

            # continues on if player 1 did not win
            if go == 'yes':
                print()  # print blank line to separate the turns
                # player 2 rolls
                input(player2 + ', hit Enter to roll!')
                roll = roll_dice()
                # prints results of the roll
                print("You rolled ", roll, "!", sep='')
                # player moves according to the roll
                direction = 'forward'
                p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction, go)

                # draw extra card if player lands on the special space
                if p2total == 5 or p2total == 14 or p2total == 23 or p2total == 32:
                    input(player2 + ', hit Enter to draw an EXTRA card!')
                    direction, roll = draw_card()
                    # move player according to the results of the card
                    if direction == 'opponent':
                        direction = 'backward'
                        p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction,
                                                             go)
                    else:
                        p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction,
                                                             go)

                # if player 2 wins, go = 'no' and it falls out of the loop
                if p1total >= 36 or p2total >= 36:
                    go = 'no'

                # continues on if player 2 did not win yet
                if go == 'yes':
                    # player 2 draws a card
                    input(player2 + ', hit Enter to draw a card!')
                    direction, roll = draw_card()

                    # move player according to the result of the card
                    if direction == 'opponent':
                        direction = 'backward'
                        p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1, direction,
                                                             go)
                    else:
                        p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2, direction,
                                                             go)

                    # draw extra card if player lands on the special space
                    if p2total == 5 or p2total == 14 or p2total == 23 or p2total == 32:
                        input(player2 + ', hit Enter to draw an EXTRA card!')
                        direction, roll = draw_card()
                        # move player according to the results of the card
                        if direction == 'opponent':
                            direction = 'backward'
                            p1position, p1total = move_gamepiece(p1color, roll, p1position, p1total, player1, p1,
                                                                 direction, go)
                        else:
                            p2position, p2total = move_gamepiece(p2color, roll, p2position, p2total, player2, p2,
                                                                 direction, go)

                    # falls out of the loop if player 2 wins
                    if p1total >= 36 or p2total >= 36:
                        go = 'no'

    # this occurs once the game ends and one of the players has won
    # prepare winning player information to be written to file
    if p1total >= 36:
        winning_player = 'Player 1'
        winning_name = player1

    else:
        winning_player = 'Player 2'
        winning_name = player2

    # see if file exists by trying to read it
    try:
        # if file exists, no error occurs, so put it into append mode
        winners = open('winners.txt')
        winners.close()
        winners = open('winners.txt', 'a')

    # if exception is raised, then file does not exist
    except IOError:
        # create file, put in append mode
        winners = open('winners.txt', 'a')
        # create the heading of the file
        winners.write('Player number   Player name\n')
        winners.write('---------------------------\n')

    # now that file definitely exists, write in the winning player number and name
    winners.write(winning_player + '        ' + winning_name + '\n')
    # close the file
    winners.close()

    # allow players to see the file
    what_next = input('Type "winners" to see the list of winners, or type "quit" to close the game. ')

    # validate input
    while what_next != 'winners' and what_next != 'quit':
        print('Please type either "winners" or "quit"')
        what_next = input('Type "winners" to see the list of winners, or type "quit" to close the game. ')

    # if they choose to see the file
    if what_next == 'winners':
        # open in read mode
        winners = open('winners.txt')
        print()

        # strip newline character and print each line
        for line in winners:
            line = line.rstrip('\n')
            print(line)

        # close the file
        winners.close()

    # skips to here if they choose not to see the file
    print()
    # close turtle window
    turtle.bye()
    print('Thanks for playing!')


# This function draws out the gameboard itself, based on the global variable of the length of a single space
def draw_game_board():
    # starting location
    turtle.speed(0)
    turtle.penup()
    turtle.left(225)
    turtle.forward(500)
    turtle.pendown()
    turtle.right(-135)

    # outer edges of the board
    for i in range(4):
        turtle.forward(SPACE_LENGTH * 10)
        turtle.left(90)

    # inner edges
    turtle.forward(SPACE_LENGTH)
    turtle.left(90)
    turtle.forward(SPACE_LENGTH * 9)
    turtle.right(90)
    turtle.forward(SPACE_LENGTH * 8)
    turtle.right(90)
    turtle.forward(SPACE_LENGTH * 8)
    turtle.right(90)
    turtle.forward(SPACE_LENGTH * 9)
    turtle.right(90)
    turtle.forward(SPACE_LENGTH)

    # left side spaces
    for i in range(4):
        turtle.right(90)
        turtle.forward(SPACE_LENGTH)
        turtle.left(90)
        turtle.forward(SPACE_LENGTH)
        turtle.left(90)
        turtle.forward(SPACE_LENGTH)
        turtle.right(90)
        turtle.forward(SPACE_LENGTH)

    turtle.right(90)
    turtle.forward(SPACE_LENGTH)

    # top spaces
    for i in range(4):
        turtle.right(90)
        turtle.forward(SPACE_LENGTH)
        turtle.left(90)
        turtle.forward(SPACE_LENGTH)
        turtle.left(90)
        turtle.forward(SPACE_LENGTH)
        turtle.right(90)
        turtle.forward(SPACE_LENGTH)

    turtle.right(90)
    turtle.forward(SPACE_LENGTH)
    turtle.left(90)
    turtle.forward(SPACE_LENGTH)

    # right side spaces
    for i in range(4):
        turtle.right(90)
        turtle.forward(SPACE_LENGTH)
        turtle.right(90)
        turtle.forward(SPACE_LENGTH)
        turtle.left(90)
        turtle.forward(SPACE_LENGTH)
        turtle.left(90)
        turtle.forward(SPACE_LENGTH)

    turtle.right(180)
    turtle.forward(SPACE_LENGTH)
    turtle.left(90)
    turtle.forward(SPACE_LENGTH)

    # bottom spaces
    for i in range(4):
        turtle.right(90)
        turtle.forward(SPACE_LENGTH)
        turtle.right(90)
        turtle.forward(SPACE_LENGTH)
        turtle.left(90)
        turtle.forward(SPACE_LENGTH)
        turtle.left(90)
        turtle.forward(SPACE_LENGTH)

    # obtain starting position
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.write("Start", font=16)
    turtle.right(90)
    start = turtle.pos()

    # write in special spaces
    # bottom
    turtle.forward(5 * SPACE_LENGTH - 5)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.write("Draw\nanother\ncard!", font=12)
    turtle.forward(4 * SPACE_LENGTH)
    turtle.left(90)  # turn the corner
    # right side
    turtle.forward(5 * SPACE_LENGTH - 5)
    turtle.write("Draw\nanother\ncard!", font=12)
    turtle.forward(4 * SPACE_LENGTH)
    turtle.left(90)  # turn the corner
    # top
    turtle.forward(5 * SPACE_LENGTH - 5)
    turtle.write("Draw\nanother\ncard!", font=12, align="left")
    turtle.forward(4 * SPACE_LENGTH)
    turtle.left(90)  # turn the corner
    # left side
    turtle.forward(5 * SPACE_LENGTH - 5)
    turtle.write("Draw\nanother\ncard!", font=12, align="left")
    turtle.hideturtle()

    # finish by returning the value
    return start


# The roll_dice function simulates rolling a die by choosing a random number between 1 and 6 and returning it to
# the main function.
def roll_dice():
    # select random number between 1 and 6
    roll = random.randint(1, 6)
    # return the value
    return roll


# the move_gamepiece function accepts input for player color, roll, player's position, player's total, player's name,
# direction of movement, and whether or not someone has won. It uses this to then move the appropriate player's
# gamepiece the correct number of spaces based on their roll and location.
def move_gamepiece(color, roll, position, total, player, p, direction, go):
    p.penup()
    # ensure correct starting position for moving the gamepiece
    p.goto(position)
    # assign color of gamepiece
    p.pencolor(color)
    i = 1

    # goes through while loop as long as no one has won and the number of spaces moved hasn't exceeded the roll
    while go == 'yes' and i <= roll:
        p.speed(0)
        p.setheading(0)

        # for forward moving pieces
        if direction == 'forward':

            # if forward on second to last space:
            if total == 35:
                # orient gamepiece down
                p.setheading(270)
                p.speed(1)
                # move forward one
                p.forward(SPACE_LENGTH)
                # declare player as the winner
                go = 'no'
                total += 1
                print()
                print(player, 'wins!')

            # if on left side of the board
            elif total >= 27:
                # orient gamepiece down
                p.setheading(270)
                p.speed(1)
                # move forward one
                p.forward(SPACE_LENGTH)
                # increase count and space total by 1
                i += 1
                total += 1

            # if on top of game board
            elif total >= 18:
                # orient gamepiece to the left
                p.setheading(180)
                p.speed(1)
                # move forward one
                p.forward(SPACE_LENGTH)
                # increase count and space total by 1
                i += 1
                total += 1

            # if on right side of game board
            elif total >= 9:
                # orient gamepiece up
                p.setheading(90)
                p.speed(1)
                # move forward one
                p.forward(SPACE_LENGTH)
                # increase count and space total by 1
                i += 1
                total += 1

            # otherwise, gamepiece is on the bottom of the board
            else:
                p.speed(1)
                # move forward one space
                p.forward(SPACE_LENGTH)
                # increase count and space total by 1
                i += 1
                total += 1

        # for backward moving gamepieces
        elif direction == 'backward':

            # if on the left side of the board
            if total > 27:
                # orient gamepiece up
                p.setheading(90)
                p.speed(1)
                # move forward (which is really backwards) one space
                p.forward(SPACE_LENGTH)
                # increase count by 1
                i += 1
                # decrease space total by 1
                total = total - 1

            # if on the top of the board
            elif total > 18:
                # orient gamepiece to the right
                p.setheading(0)
                p.speed(1)
                # move forward (which is really backwards) one space
                p.forward(SPACE_LENGTH)
                # increase count total by 1
                i += 1
                # decrease space total by 1
                total = total - 1

            # if on the right side of the board
            elif total > 9:
                # orient the gamepiece down
                p.setheading(270)
                p.speed(1)
                # move forward (which is really backwards) one space
                p.forward(SPACE_LENGTH)
                # increase count total by 1
                i += 1
                # decrease space total by 1
                total = total - 1

            # otherwise gamepiece is on the bottom of the board
            else:
                # only move backwards if the player has space to move backwards
                if total > 0:
                    # orient gamepiece to the left
                    p.setheading(180)
                    p.speed(1)
                    # move forward (which is really backwards) one space
                    p.forward(SPACE_LENGTH)
                    # increase count by 1
                    i += 1
                    # decrease total spaces by 1
                    total = total - 1
                # fall out of loop if player can't move back anymore
                else:
                    go = 'no'

    # state position as the player's current position
    position = p.pos()
    # return the necessary values
    return position, total


# This function chooses a random card from the "deck" (list) above, prints it, determines its contents, and removes
# the card from the deck, before finally returning the necessary information to the main function.
def draw_card():
    # if cards is not empty:
    if cards != []:
        # randomly select a card in the deck
        card = random.randint(0, len(cards) - 1)
        result = cards[card]
        # print the resulting card
        print('Your card:', result)
        # cycle through the characters in the card and extract the digit
        for letter in result:
            if letter.isdigit():
                # turn digit into an integer
                spaces = int(letter)

        # determine direction stated in the card
        if result[5] == 'f':
            direction = 'forward'

        elif result[5] == 'b':
            direction = 'backward'

        else:
            direction = 'opponent'

        # remove the card from the deck
        del cards[card]

    # if cards is empty (all cards have been drawn):
    else:
        print('Out of cards!')
        # no change occurs since no card was drawn
        direction = 'forward'
        spaces = 0

    # return the values
    return direction, spaces


main()
