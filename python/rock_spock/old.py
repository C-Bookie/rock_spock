"""
'Ello Lewis and future Latifah :)
Just to warn you, I may state the obvious a lot in this,
or I won't be obvious enough. One of those. I hope it's
actually understandable/helpful either way.


This is the Rock-paper-scissors-lizard-Spock template


The key idea of this program is to equate the strings
"rock", "paper", "scissors", "lizard", "Spock" to numbers
as follows:

0 - rock
1 - Spock <--- Don't forget to capitalise the 's' in Spock!
2 - paper
3 - lizard
4 - scissors

^^ Thanks goodness they gave the corresponding numbers
for each name. Hell no would I have wanted to work that
out.
############################################################

Ok, since we saw on the brief that this programme includes
'random.randrange() and we don't know wtf it is, it's probable
that we need to import (especially since it is random.something)
It's best to check the 'Docs'tab to see random's syntax and
how it is used before importing. Also, it's best for imported
things to be placed at the very beginning so that the rest of
the code will actually have something to reference from the start.
"""

import random

"""
helper functions

here we define name_to_number(), where it converts the strings
into the numbers stated above. Quite straightforward so far,
but figuring out the syntax and how to do it exactly was annoying.
I will include the template's instructions as we go along.
"""


def name_to_number(name: str) -> int | str:
    """
    ##################################################################
                            FIRST INSTRUCTIONS
                convert name to number using if/elif/else
                don't forget to return the result!
    ##################################################################
    Ok, the instructions suggest that boolean logic will be included in
    this first step. That's a start. How do we start converting names to
    numbers though? Let's break it down. Since it is meant to convert names
    to numbers, and there are 5 names to define, it makes sense to begin
    writing at least 5 if/elif/else words to get a better idea of the
    function's structure until we figure out how to fill it all in.
            def name_to_number(name):
                if
                    return
                elif
                    return
                elif
                    return
                elif
                    return
                elif
                    return
    The base looks promising, but 'if' what, and 'return' what exactly?
    How do we actually start turning it into numbers? This function has
    only one parameter, which is (name), and the purpose of the function
    is to convert a name to a number, so it's highly probable that we have
    to write name after the if/else statements.
            def name_to_number(name):
                if name
                    return
                elif name
                    return
                    etc
    We have 5 names to use here; 'rock', 'paper', 'scissors', 'lizard'
    and 'Spock' so we need to include these names for each if/elif
    statement. For the sake of simplicity and easy reference, I'll
    write them in the order stated at the beginning of this document.
    Now we have to figure out what to return. The numbers next to the
    names at the beginning suggests that we need to assign each name
    to their corresponding numbers.
    In case any names other than the 5 listed come up in the code for
    whatever reason, I'll add an 'else' statement to define what should
    be returned.
    The code should be looking like this now:
    """
    if name == "rock":  # <---DON'T FORGET THE COLONS. You know how
        # many times I forgot them? Many frustrating times.

        return 0  # Notice how the 0 isn't a string here
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Invalid name."


def number_to_name(number: int) -> str:
    """
    ##################################################################
                          SECOND INSTRUCTIONS
              convert number to name using if/elif/else
              don't forget to return the result!
    ##################################################################
    The second step is basically step one, with name and number reversed.
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Invalid number."


def rpsls(player_choice: str) -> None:
    """
    ##################################################################
                          THIRD INSTRUCTIONS
              print a blank line to separate consecutive games
              print out the message for the player's choice
              convert the player's choice to
              player_number using the function name_to_number()
    ##################################################################
    Now we get to the part where the function we've just created needs
    to be implemented.
    I'll go ahead and do those instructions in order. Ok, so, print a
    blank line. Sure.
          print ""
    Now print out the message for the player's choice.
    There are two parts to the message for the player's choice, the
    string "Player chooses" (that was given in the project's brief)
    and the actual choice. The print out should look a bit like this:
          print "Player chooses " + player_choice
    Remember to type in a space after the word 'chooses', else
    there would be no space between "Player chooses" and player_choice.
    Using a comma instead of a + sign would also work in this instance,
    and it would create a space automatically too. I just used the +
    sign because its purpose looked more straightforward than a comma.
    All right, next we convert the player's choice to player number
    using name_to_number(). Figuring out how to lay this out tripped
    me up a bit until I did a bit of trial and error. Anyway, it makes
    sense to start it off with 'player_number =' since it is the thing
    that we need to figure out. 'name_to_number()' should also come
    after it. So far we have:
          player_number = name_to_number()
    """
    print("")
    print("Player chooses " + player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 4)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses " + comp_choice)
    winner = (player_number - comp_number) % 5
    if winner == 0:
        print("Player and computer tie!")
    elif (winner == 1) or (winner == 2):
        print("Player wins!")
    elif (winner == 3) or (winner == 4):
        print("Computer wins!")
    else:
        print("Invalid modulo calculation.")

    # compute random the difference of comp_number and player_number modulo five
    # use if/elif/else to determine winner, print winner message


# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
def main() -> None:
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")


# always remember to check your completed program against the grading rubric
if __name__ == "__main__":
    main()
