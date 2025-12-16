import sys


def main() -> None:
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print("використовуємо src/sys_tool.py")
        print("друкуємо 'командний рядок' лише при прямому запуску")
        return

    print("командний рядок")


if __name__ == "__main__":
    main()
