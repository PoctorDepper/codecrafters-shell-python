import sys


def main():
    builtin_commands = ["exit", "echo", "type"]

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
                print(*args)
            case "type":
                sys.stdout.write(args[0])
                if args[0] in builtin_commands:
                    sys.stdout.write(" is a shell builtin\n")
                else:
                    sys.stdout.write(" not found\n")
            case _:
                sys.stdout.write(f"{command}: command not found\n")
        continue



if __name__ == "__main__":
    main()
