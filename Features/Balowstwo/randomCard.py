import random

shapes = ("Spades", "Hearts", "Diamonds", "Clubs")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Jack", "Queen", "Ace")


def select_a_card():
    shape = random.choices(shapes)
    rank = random.choices(ranks)
    return f"The {rank} of {shape}"


print(select_a_card())
