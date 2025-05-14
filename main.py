# Tarasidou Anna
from graph_checker.generator import sequence_generator
from graph_checker.checker import is_graphic
from graph_checker.constructor import construct_graph


def run_once():
    sequence = None
    while True:
        choice = input("Do you want to (1) enter your own degree sequence or (2) generate a random one? ")
        if choice == "1":
            raw_input = input("Enter your degree sequence separated by spaces (e.g., 3 3 2 2 2 2): ")
            try:
                sequence = [int(x) for x in raw_input.strip().split()]
            except ValueError:
                print("Invalid input. Please enter only integers.")
                continue
            break
        elif choice == "2":
            order = int(input("Give the order (number of nodes) of the graph: "))
            sequence = sequence_generator(order)
            print("Generated sequence of degrees:", sequence)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    result = is_graphic(sequence)
    print("Is the sequence graphic:", result)

    if result == "YES":
        construct_graph(sequence)
    else:
        print("The sequence is not graphic.")


def main():
    while True:
        run_once()
        while True:
            again = input("\nDo you want to check another sequence? (y/n): ").lower()
            if again in ('y', 'n'):
                break
            print("Please enter 'y' or 'n'.")
        if again == 'n':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
