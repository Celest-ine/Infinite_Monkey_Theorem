"""The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text,
such as the complete works of William Shakespeare.
"""
import random
import string
import time

def get_targeted_string():
    """Get a string from the user"""
    print("*" * 5 + "This program will tell you how long it would take a monkey to type some words if the monkey was playing with random keyboard keys." + "*" * 5)

    phrase = input("What phrase/word do you want the monkey to generate?")
    
    return phrase


def generate_string(the_phrase):
    """Generate a string that is as long as the string that the user typed in, 
    by choosing random letters from alphabets
    """

    phrase_length = len(the_phrase)
    random_generation = "".join(random.choice(string.ascii_letters) for _ in range(phrase_length))
    
    return random_generation

def score_generated_strings(the_phrase):
    """Score the generated strings aganist the random string."""

    attempts = 0
    start_time = time.time()

    while True:
        generated_phrase = generate_string(the_phrase)
        attempts += 1

        matches = sum(1 for char1, char2 in zip(generated_phrase, the_phrase) if char1 == char2)
        score = (matches / len(the_phrase)) * 100

        if score == 100: # If we have a match, breakthe loop and print the results
            end_time = time.time()
            print(f"\nSuccess after {attempts} generations.")
            print(f"The generated phrase is: {generated_phrase}")
            print(f"Time taken is: {end_time - start_time:.4f} seconds.")
            break

        elif attempts % 1000 == 0: # Print the score every 1000 attempts
            print(f"\nAttempts: {attempts}, Score: {score:.2f}%")
            print(f"The best generated phrase is: {generated_phrase}")


the_phrase = get_targeted_string()
generated_phrase = generate_string(the_phrase)
score_generated_strings(the_phrase)