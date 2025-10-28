# display_set.py - create and display a set

def create_set_from_input():
    """Create a set from user input. If the user enters nothing, return a default set.

    Items separated by whitespace are parsed. If an item can be parsed as int, it will
    be converted to int; otherwise it remains a string.
    """
    s = set()
    user = input("Enter items separated by spaces (or press Enter to use default set): ").strip()
    if not user:
        # default with duplicates to show that duplicates are removed in a set
        return {1, 2, 3, 2, 1}
    for item in user.split():
        try:
            val = int(item)
        except ValueError:
            val = item
        s.add(val)
    return s


def main():
    s = create_set_from_input()
    print("Set (duplicates removed):", s)


if __name__ == "__main__":
    main()
