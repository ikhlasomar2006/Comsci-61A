"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls > 0, "Must roll at least once."
    "*** YOUR CODE HERE ***"
    counter = 0
    was_one = False

    while num_rolls != 0:
        track_dice_result = dice()

        if track_dice_result == 1:
            was_one = True

        counter += track_dice_result
        num_rolls -= 1

    if was_one == True:
        return 1
    
    return counter

def boar_brawl(player_score, opponent_score):
    """Return the points scored when the current player rolls 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    "*** YOUR CODE HERE ***"
    value_to_add = 0
    if opponent_score >= 100:
        value_to_add = (3 * abs((opponent_score - (opponent_score // 100 * 100)) // 10 - player_score % 10))
    else:
        value_to_add = (3 * abs(opponent_score // 10 - player_score % 10))

    if value_to_add == 0:
        return 1
    return value_to_add



def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    current player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls >= 0, "Cannot roll a negative number of dice in take_turn."
    assert num_rolls <= 10, "Cannot roll more than 10 dice."
    "*** YOUR CODE HERE ***"
    score = 0
    if num_rolls == 0:
        score += boar_brawl(player_score, opponent_score)
    else:
        score += roll_dice(num_rolls, dice)
    return score


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score


def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    "*** YOUR CODE HERE ***"
    num_of_prime = 0
    num = 1
    while n >= num:
        if n % num == 0:
            num_of_prime += 1
        num += 1
    return num_of_prime


def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    "*** YOUR CODE HERE ***"
    if num_factors(score) == 3 or num_factors(score) == 4:
        score_copy = score
        while num_factors(score_copy) > 2:
            score_copy += 1
        return score_copy
    return score
        
        


def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    "*** YOUR CODE HERE ***"
    roll_boar_score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    final_score = sus_points(roll_boar_score)
    return final_score



def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update, score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    "*** YOUR CODE HERE ***"
    who = 0
    while score0 < goal and score1 < goal:
        if who == 0:
            num_rolls = strategy0(score0, score1)
            score0 = update(num_rolls, score0, score1, dice)
        if who == 1:
            num_rolls = strategy1(score1, score0)
            score1 = update(num_rolls, score1, score0, dice)
        who = 1 - who
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10

    "*** YOUR CODE HERE ***"
    def helper_func(x, y):
        return n
    return helper_func



def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> catch_up(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    for every possible combination of score and opponent_score
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    "*** YOUR CODE HERE ***"
    i = 0
    goal_copy = goal
    is_const = strategy(0, 0)
    while goal_copy >= 0:
        while i < goal + 1:
            if strategy(goal_copy, i) != is_const:
                return False
            i += 1
        i = 0
        goal_copy -= 1
    return True


    


def make_averaged(func_to_average, iterations=1000):
    """Return a function that returns the average value of func_to_average
    called iterations times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """

    "*** YOUR CODE HERE ***"

    
    def helper_func(*args):
        total = 0
        for _ in range(iterations):
            total += func_to_average(*args)
        return total / iterations
    
    return helper_func


def max_scoring_num_rolls(dice=six_sided, iterations=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    "*** YOUR CODE HERE ***"
    best_score = 0
    best_num = 1
    for i in range(1, 11):
        score_arrgae = make_averaged(roll_dice, iterations)
        score_result = score_arrgae(i, dice)

        if score_result > best_score:
            best_score = score_result
            best_num = i
    return best_num



def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print("Max scoring num rolls for six-sided dice:", six_sided_max)

    print("always_roll(6) win rate:", average_win_rate(always_roll(6)))  # near 0.5
    print("catch_up win rate:", average_win_rate(catch_up))
    print("always_roll(3) win rate:", average_win_rate(always_roll(3)))
    print("always_roll(8) win rate:", average_win_rate(always_roll(8)))

    print("boar_strategy win rate:", average_win_rate(boar_strategy))
    print("sus_strategy win rate:", average_win_rate(sus_strategy))
    print("final_strategy win rate:", average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"




def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore the Sus Fuss rule.
    """
    "*** YOUR CODE HERE ***"
    num_rolls = num_rolls

    if boar_brawl(score, opponent_score) >= threshold:
        num_rolls = 0
    return num_rolls  # Remove this line once implemented.


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when rolling 0 increases the score by at least
    THRESHOLD points, and returns NUM_ROLLS otherwise. Consider both the Boar Brawl and
    Sus Fuss rules."""
    "*** YOUR CODE HERE ***"
    if sus_update(0,score,opponent_score) - score >= threshold:
        num_rolls = 0
    return num_rolls  # Remove this line once implemented.


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    "*** YOUR CODE HERE ***"
    return 6  # Remove this line once implemented.


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument(
        "--run_experiments", "-r", action="store_true", help="Runs strategy experiments"
    )

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
