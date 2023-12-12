import os
import argparse

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print("Directory not found.")


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path to the directory")
args = parser.parse_args()
change_directory(args.path)
