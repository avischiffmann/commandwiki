#!/usr/bin/python

import wikipedia
import argparse

def wiki(txt):
    txt='wiki "'+txt+'"'
    txt = wikipedia.page(txt)
    print(txt.summary)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("txt", help="What do you want to search?", type=str)

    args = parser.parse_args()

    wiki(args.txt)

if __name__ == "__main__":
    Main()
