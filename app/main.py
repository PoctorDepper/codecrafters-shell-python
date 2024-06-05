import sys
import os

builtin_commands = ["exit", "echo", "type"]
paths = os.environ.get("PATH").split(":")

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
                print(*args)
            case "type":
                command_path = None
                for path in paths:
                    if os.path.isfile(f"{path}/{args[0]}"):
                        command_path = path
                        break
                sys.stdout.write(f"{args[0]} ")
                if args[0] in builtin_commands:
                    sys.stdout.write("is a shell builtin\n")
                elif command_path:
                    sys.stdout.write(f"is {command_path}/{args[0]}")
                else:
                    sys.stdout.write("not found\n")
            case _:
                sys.stdout.write(f"{command}: command not found\n")
        continue



if __name__ == "__main__":
    main()
