import sys


def main():

    while True:
        # Clear terminal
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Get user input
        args = input().split()
        match command := args.pop(0):
            case "exit" if args[0] == "0":
                sys.exit(0)
            case "echo":
                print(*args[0:])
            case _:
                sys.stdout.write(f"{command}: command not found\n")
        continue



if __name__ == "__main__":
    main()
