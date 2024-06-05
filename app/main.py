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

        # Take user input
        match user_input := input().split():
            case ["exit", "0"]:
                sys.exit(0)
            case ["echo", *text]:
                print(*text)
            case ["type", command]:
                sys.stdout.write(f"{command} ")
                if command in builtin_commands:
                    print("is a shell builtin")
                elif path := find_executable(command):
                    print(f"is {path}/{command}")
                else:
                    print("not found")
            case ["pwd"]:
                print(os.getcwd())
            case _:
                if find_executable(user_input[0]):
                    os.system(" ".join(user_input))
                else:
                    print(f"{user_input[0]}: command not found")
        continue


if __name__ == "__main__":
    main()
