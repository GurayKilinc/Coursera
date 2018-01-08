"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    hand_dict = {item: hand.count(item) for item in hand}
#    print(hand_dict)
    max_score = 0
    for key in hand_dict:
#        print(key)
#        print(hand_dict[key])
        hand_dict[key] *= key
        if hand_dict[key] > max_score:
            max_score = hand_dict[key]
#    print(hand_dict)
#    print(max_score)
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    results_list = range(1, num_die_sides + 1)
    roll_results = gen_all_sequences(results_list, num_free_dice)
#    print(roll_results)
    combined_results = []
    score_list = []
    for key in roll_results:
#        print(key)
        combo = key + held_dice
#        print("---")
#        print(key)
        combined_results.append(combo)
#        key += held_dice
#    print(combined_results)
    for hand in combined_results:
        score_list.append(score(hand))
#    print(score_list)
    return sum(score_list) * 1.0 / len(score_list)



def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = set([()])  
    for hand_ele in hand:  
        for hold in all_holds.copy():  
            new_hold = list(hold)  
            new_hold.append(hand_ele)  
            all_holds.add(tuple(new_hold))  
    return all_holds   



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    score_dict = {}
    for hold in all_holds:
        temp_score = expected_value(hold, num_die_sides, len(hand) - len(hold))
        score_dict.update({hold: temp_score})
    max_score = max(score_dict.values())
    for key in score_dict:
        if score_dict[key] == max_score:
            max_hand = key
    return (max_score, max_hand)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    score(hand)
    print(expected_value(hand, num_die_sides, 1))
    print(gen_all_holds((1,1)))
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)
    
    
run_example()
print(strategy((1,), 6))
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)