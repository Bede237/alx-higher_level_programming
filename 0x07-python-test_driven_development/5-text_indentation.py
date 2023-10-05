#!/usr/bin/python3
def text_indentation(text):
    """THis function prints a new line after ., ?, :"""

    n = len(text)
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(n):
        if text[i] == '.' and text[i + 1] == ' ':
            print()
            continue
        elif text[i] == '?' and text[i + 1] == ' ':
            print()
            continue
        elif text[i] == ':' and text[i + 1] == ' ':
            print()
            continue
        elif text[i] == ' ':
            if text[i + 1] == '.':
                print()
            elif text[i + 1] == '?':
                print()
            elif text[i + 1] == ':':
                print()
            else:
                print(text[i])
        else:
            print("{}".format(text[i]), end='')
