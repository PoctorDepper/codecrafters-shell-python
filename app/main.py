import sys


def main():

    while True:
        # Clear terminal
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Get user input
        command = input()
        match command:
            case "exit 0":
                break
            case _:
                sys.stdout.write(f"{command}: command not found\n")
        continue



if __name__ == "__main__":
    main()
