#!/usr/bin/env python3
import csv
import random
import argparse
import sys

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
        print(f"\nTerm:\n {term}\n")
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
            print("Correct!\n")
        else:
            print(f"WRONG, correct answer: {true_def}\n")

        # show current grade
        pct = correct / total * 100
        print(f"Current grade: {correct}/{total} ({pct:.2f}%)")

    # final summary
    print("\nQuiz complete!")
    final_pct = correct / total * 100
    print(f"Final score: {correct}/{total} ({final_pct:.2f}%)")

def main():
    parser = argparse.ArgumentParser(
        description="Study Buddy: multiple-choice quiz on term/definitions CSV"
    )
    parser.add_argument(
        'csvfile',
        help="Path to CSV file (term,definition)"
    )
    args = parser.parse_args()

    terms = load_terms(args.csvfile)
    quiz(terms)

if __name__ == '__main__':
    main()

