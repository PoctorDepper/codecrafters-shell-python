import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Get user input
    command = input()
    sys.stdout.write(f"{command}: command not found \n")


if __name__ == "__main__":
    main()
