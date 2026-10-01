"""The infinite monkey theorem states that a monkey hitting keys at random on a
typewriter keyboard for an infinite amount of time will almost surely type any
given text, such as the complete works of William Shakespeare.
"""

import random
import string
import time


def get_targeted_string():
    """Get a string from the user."""
    
    print(
        "*" * 5
        + " This program will tell you how long it would take a monkey "
          "to type some words if the monkey was playing with random keyboard keys. "
        + "*" * 5
    )

    phrase = input("What phrase/word do you want the monkey to generate? ")

    return phrase


def generate_string(the_phrase, current_phrase):
    """Generate a new phrase while keeping characters that are already correct."""

    characters = string.ascii_letters + string.punctuation + " "
    new_phrase = []

    for target_char, current_char in zip(the_phrase, current_phrase):

        if target_char == current_char:
            # Keep characters that are already correct.
            new_phrase.append(current_char)
        else:
            # Generate a new random character for incorrect positions.
            new_phrase.append(random.choice(characters))

    return "".join(new_phrase)


def score_generated_strings(the_phrase):
    """Generate strings until every character matches the target."""

    attempts = 0
    start_time = time.time()

    # Start with a completely random phrase.
    characters = string.ascii_letters + string.punctuation + " "
    current_phrase = "".join(
        random.choice(characters) for _ in range(len(the_phrase))
    )

    while True:
        attempts += 1

        current_phrase = generate_string(the_phrase, current_phrase)

        matches = sum(1 for char1, char2 in zip(current_phrase, the_phrase) if char1 == char2)
        score = (matches / len(the_phrase)) * 100

        if score == 100:
            end_time = time.time()

            print(f"\nSuccess after {attempts} generations.")
            print(f"The generated phrase is: {current_phrase}")
            print(f"Time taken is: {end_time - start_time:.4f} seconds.")
            break

        elif attempts % 100 == 0:
            print(f"\nAttempts: {attempts}, Score: {score:.2f}%")
            print(f"The best generated phrase is: {current_phrase}")


the_phrase = get_targeted_string()
score_generated_strings(the_phrase)