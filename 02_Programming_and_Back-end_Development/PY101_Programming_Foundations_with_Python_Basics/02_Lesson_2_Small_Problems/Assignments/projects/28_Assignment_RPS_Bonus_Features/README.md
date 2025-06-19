# The python files within this directory contain different refactoring options for adding extra moves and keeping score of the player and the computer.

# rock_paper_scissors_spock_lizard_1.py
    Includes the extra moves: spock and lizard

# rock_paper_scissors_spock_lizard_2&3.py
    Includes integers (immutable object) assigned to the player and computer to keep score. This results in having to implement global statements in the functions that depend on these variables in order to reassign through augmentation.

# rock_paper_scissors_spock_lizard_2&3_A.py
    Includes a list (mutable object) assigned to the player and computer which allows for mutation to occur in the functions that depend on these variables. This result in not having to implement global statements.

# rock_paper_scissors_spock_lizard_2&3_B.py
    Includes a dictionary to keep track of both the player and the computer score. This dictionary can be updated by mutating the score values assigned to the 'player' and 'computer' keys.
