import sys
import os

paths = os.environ.get("PATH").split(":")
builtin_commands = ["exit", "echo", "type"]

def find_executable(command):
    for path in paths:
        if os.path.isfile(f"{path}/{command}"):
            return path
    return None


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
                sys.stdout.write(f"{args[0]} ")
                if args[0] in builtin_commands:
                    sys.stdout.write("is a shell builtin\n")
                elif path := find_executable(args[0]):
                    sys.stdout.write(f"is {path}/{args[0]}\n")
                else:
                    sys.stdout.write("not found\n")
            case _:
                if find_executable(command):
                    os.system(command *args)
                else:
                    sys.stdout.write(f"{command}: command not found\n")
        continue



if __name__ == "__main__":
    main()
