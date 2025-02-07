import csv
import sys


def main():
    # Check for correct command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)


    database = []
    with open(sys.argv[1], "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            database.append(row)


    with open(sys.argv[2], "r") as txtfile:
        sequence = txtfile.read()

    # Get the STRs (Short Tandem Repeats) from the CSV header
    strs = list(database[0].keys())[1:]


    str_counts = {}
    for str_seq in strs:
        str_counts[str_seq] = longest_match(sequence, str_seq)

    #
    for person in database:
        match = all(str_counts[str_seq] == int(person[str_seq]) for str_seq in strs)
        if match:
            print(person['name'])
            return

    #
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    #
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    #
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence

        while True:


            start = i + count * subsequence_length
            end = start + subsequence_length


            if sequence[start:end] == subsequence:
                count += 1


            else:
                break


        longest_run = max(longest_run, count)


    return longest_run



if __name__ == "__main__":
    main()
