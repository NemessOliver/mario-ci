# Mario: prints a right-aligned pyramid of hashes (like CS50 "Mario, less comfortable").
#
#   Height: 4
#      #
#     ##
#    ###
#   ####


def get_height():
    # >> keep asking until the user types a whole number from 1 to 8
    while True:
        try:
            height = int(input("Height: "))
        except ValueError:
            # >> "abc" or "2.5" can't become an int -> just ask again
            continue
        if 1 <= height <= 8:
            return height


def build_pyramid(height):
    # >> build the whole pyramid as ONE string instead of printing it,
    # >> so the tests can check the result without reading the screen
    rows = []
    for i in range(1, height + 1):
        spaces = " " * (height - i)  # >> one space less every row -> right-aligned
        hashes = "#" * i             # >> one hash more every row
        rows.append(spaces + hashes)
    return "\n".join(rows)           # >> glue the rows together with a new line in between


def main():
    height = get_height()
    print(build_pyramid(height))


if __name__ == "__main__":
    # >> only runs when you start the file yourself (python mario.py),
    # >> NOT when test_mario.py imports it -> the tests never wait for input
    main()
