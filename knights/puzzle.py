from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says "I am both a knight and a knave."
AStatement0 = And(AKnight, AKnave)
knowledge0 = And(

    # A can be knight or knave
    Or(AKnight, AKnave),

    # A cannot be both
    Not(And(AKnight, AKnave)),

    # If A is a knight statement is true.
    # If A is a knave, statement is false
    Implication(AKnight, AStatement0),
    Implication(AKnave, Not(AStatement0)),

)

print('knowledge0 logic is', knowledge0.formula())
print(model_check(knowledge0, AKnave))

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
AStatement1 = And(AKnave, BKnave)
knowledge1 = And(

    # A can be knight or knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B can be knight or knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If A is a knight statement is true.
    # If A is a knave, statement is false
    Implication(AKnight, AStatement1),
    Implication(AKnave, Not(AStatement1)),

)

print('knowledge1 logic is', knowledge1.formula())

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
AStatement2 = Or(And(AKnave, BKnave), And(AKnight, BKnight))
BStatement0 = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(

    # Using Biconditional to represent 'X' can be knight or knave, but not both
    Not(Biconditional(AKnave, AKnight)),
    Not(Biconditional(BKnave, BKnight)),

    # If A is a knight statement is true. Same for B statements
    # If A is a knave, statement is false. Same for B statements
    Implication(AKnight, AStatement2),
    Implication(AKnave, Not(AStatement2)),
    Implication(BKnight, BStatement0),
    Implication(BKnave, Not(BStatement0))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
AStatement3 = Or(AKnight, AKnave)
BStatement1 = Implication(AKnight, AKnave)
BStatement2 = CKnave
CStatement0 = AKnight
knowledge3 = And(

    # Using Biconditional to represent 'X' can be knight or knave, but not both
    Not(Biconditional(AKnave, AKnight)),
    Not(Biconditional(BKnave, BKnight)),
    Not(Biconditional(CKnave, CKnight)),


    Implication(AKnight, AStatement3),
    Implication(AKnave, Not(AStatement3)),
    Implication(BKnight, BStatement1),
    Implication(BKnave, Not(BStatement1)),
    Implication(BKnight, BStatement2),
    Implication(BKnave, Not(BStatement2)),
    Implication(CKnight, CStatement0),
    Implication(CKnave, Not(CStatement0)),


)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
