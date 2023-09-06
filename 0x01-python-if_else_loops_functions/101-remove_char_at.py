#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    news = str
    news = news[:n] + news[(n + 1):]
    return (news)
