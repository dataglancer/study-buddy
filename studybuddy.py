#!/usr/bin/env python3
import csv
import random
import argparse
import sys
from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init(autoreset=True)

def load_terms(csv_path):
    """Load terms and definitions from a two-column CSV."""
    terms = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                term, definition = row[0].strip(), row[1].strip()
                terms.append((term, definition))
    if len(terms) < 4:
        sys.exit("Need at least 4 term-definition pairs to generate options.")
    return terms


def quiz(terms):
    """Run the quiz: present each term once in random order."""
    random.shuffle(terms)
    total = 0
    correct = 0

    for term, true_def in terms:
        # pick three other definitions as distractors
        distractors = random.sample([d for (_t, d) in terms if d != true_def], 3)
        options = distractors + [true_def]
        random.shuffle(options)

        # display question
        print(f"\nTerm:\n{Style.BRIGHT}{Fore.CYAN}{term}{Style.RESET_ALL}\n")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")

        # get answer
        while True:
            choice = input("\nYour answer (1-4): ").strip()
            if choice in ('1','2','3','4'):
                idx = int(choice) - 1
                break
            print("\nPlease enter a number between 1 and 4.\n")

        total += 1
        if options[idx] == true_def:
            correct += 1
            print(f"\n{Style.BRIGHT}{Fore.GREEN}Correct!{Style.RESET_ALL}\n")
        else:
            print(f"{Style.BRIGHT}{Fore.RED}\nWRONG!{Style.RESET_ALL} Correct answer: {true_def}\n")

        # show current grade
        pct = correct / total * 100
        print(f"Current grade: {correct}/{total} ({pct:.2f}%)")

    # final summary
    print("\nQuiz complete!")
    final_pct = correct / total * 100
    print(f"Final score: {correct}/{total} ({final_pct:.2f}%)")


def flashcards(terms):
    """Run flashcard mode: show term, wait for key, then definition."""
    random.shuffle(terms)
    for term, definition in terms:
        # show term
        print(f"\nTerm:\n{Style.BRIGHT}{Fore.CYAN}{term}{Style.RESET_ALL}\n")
        input("Press Enter to see definition...")
        # show definition
        print(f"\nDefinition: {Style.BRIGHT}{Fore.GREEN}{definition}{Style.RESET_ALL}\n")
        input("Press Enter to continue...")
    print("\nFlashcards complete!")


def main():
    parser = argparse.ArgumentParser(
        description="Study Buddy: multiple-choice quiz or flashcards on term/definitions CSV"
    )
    parser.add_argument(
        'csvfile',
        help="Path to CSV file (term,definition)"
    )
    args = parser.parse_args()

    terms = load_terms(args.csvfile)

    # mode selection
    print("Select mode:")
    print("  1) Quiz mode")
    print("  2) Flashcard mode")
    while True:
        mode = input("Enter 1 or 2: ").strip()
        if mode in ('1','2'):
            break
        print("Please enter 1 or 2.")

    if mode == '1':
        quiz(terms)
    else:
        flashcards(terms)

if __name__ == '__main__':
    main()
