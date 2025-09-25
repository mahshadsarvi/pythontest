import sys


def main():

    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        if file_path.endswith(".py"):
            try:
                with open(file_path) as pyfile:
                    lines = pyfile.readlines()
            except FileNotFoundError:
                sys.exit("File does not exist")

            output = count_lines_of_code(lines)

            print(output)

        else:
            sys.exit("Not a Python file")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def count_lines_of_code(lines):
    line_count = 0
    in_multiline_comment = False

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue  # Ignore empty lines

        if stripped_line.startswith('"""') or stripped_line.startswith("'''"):
            # Handle multiline comments
            if in_multiline_comment:
                in_multiline_comment = False
            else:
                in_multiline_comment = True
            continue

        if in_multiline_comment:
            continue  # Ignore lines inside multiline comments

        if stripped_line.startswith('#'):
            continue  # Ignore single-line comments

        line_count += 1

    return line_count

if __name__ == "__main__":
    main()
