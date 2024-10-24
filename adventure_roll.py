# adventure_roll.py:

import argparse
import random
from pathlib import Path
import os
import json

rolled_10 = False

THEMES = [
    "Action",
    "Mystery",
    "Personal",
    "Social",
    "Tension"
]

cur_dir = Path(os.path.dirname(os.path.abspath(__file__)))


def theme_roll(themes, verbose):
    global rolled_10
    roll = random.randint(1, 10)
    if verbose:
        print("Theme roll d10: ", roll)
    if 1 <= roll <= 4:
        return themes[0]
    if 5 <= roll <= 7:
        return themes[1]
    if 8 <= roll <= 9:
        return themes[2]
    if roll == 10:
        if not rolled_10:
            rolled_10 = True
            return themes[3]
        else:
            rolled_10 = False
            return themes[4]


def values_to_themes(values):
    themes = []
    for value in values:
        if value == '1':
            themes.append("Action")
        if value == '2':
            themes.append("Tension")
        if value == '3':
            themes.append("Mystery")
        if value == '4':
            themes.append("Social")
        if value == '5':
            themes.append("Personal")
    return themes


def get_plot_point(theme, verbose):
    file_path = cur_dir / f"json/{theme.lower()}_table.json"

    with open(file_path, 'r', encoding='utf-8') as file:
        table_data = json.load(file)

    roll = random.randint(1, 100)
    if verbose:
        print("d100 roll: ", roll)

    for plot_point in table_data[f"{theme.lower()}_plot_points"]:
        roll_range = plot_point['roll'].split('-')
        if len(roll_range) == 1:
            if roll == int(roll_range[0]):
                return plot_point['name'], plot_point['description']
        else:
            if int(roll_range[0]) <= roll <= int(roll_range[1]):
                return plot_point['name'], plot_point['description']


def get_meta_plot_point(verbose):
    file_path = cur_dir / "json/meta_table.json"

    with open(file_path, 'r', encoding='utf-8') as file:
        table_data = json.load(file)
    roll = random.randint(1, 100)
    if verbose:
        print("d100 roll: ", roll)

    for plot_point in table_data["meta_plot_points"]:
        roll_range = plot_point['roll'].split('-')
        if len(roll_range) == 1:
            if roll == int(roll_range[0]):
                return plot_point['name'], plot_point['description']
        else:
            if int(roll_range[0]) <= roll <= int(roll_range[1]):
                return plot_point['name'], plot_point['description']


# if name = meta!!!!!

def read_input_themes():
    print("---------------------- INPUT THEME PRIORITY ------------------------")
    print("1: Action")
    print("2: Tension")
    print("3: Mystery")
    print("4: Social")
    print("5: Personal")
    print("Separate with comma (,)")
    print("Example priority input:")
    print("Input: 2,4,5,3,1")
    print("Theme priority: Tension, Social, Personal, Mystery, Action")
    # values_string = input()
    # values = values_string.split(',')
    # Input values
    values_string = input().strip()  # Strip leading/trailing whitespace
    # Debugging: print the input to ensure it's correct
    print(f"Raw input: '{values_string}'")
    # Split the input into a list and clean each item
    values = [value.strip() for value in values_string.split(',') if value.strip()]
    # Debugging: print the list to ensure it's what you expect
    print(f"Processed values: {values}")
    if len(values) != 5:
        print("Please input 5 themes.")
        exit()
    values = [str(value) for value in values]  # Convert each value to a string
    themes = values_to_themes(values)
    return themes


def roll_plot_points(themes, nr_points, markdown, verbose):
    if markdown:
        print("```")

    for i in range(nr_points):
        if not markdown:
            print("------------------------------------------------------------------")
        theme = theme_roll(themes, verbose)
        print("Theme: ", theme)
        plot_point = get_plot_point(theme, verbose)

        if plot_point[0] != "META":
            print("Name: ", plot_point[0])
            print("Description: ", plot_point[1])

        elif plot_point[0] == "META":
            if not markdown:
                print("------------------- META PLOT POINT ---------------------")
            
            plot_point = get_meta_plot_point(verbose)
            print("Name: ", plot_point[0])
            print("Description: ", plot_point[1])

    if markdown:
        print("```")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--themes",
        help="comma-separated list of themes (ex.: 'Tension, Social, Personal, Mystery, Action')",
        type=str,
        required=False,
    )
    parser.add_argument(
        "--random",
        help="whether to allocate random theme priority",
        action='store_true',
        required=False
    )
    parser.add_argument(
        "--verbose",
        help="whether to print dice rolls",
        action='store_true',
        required=False,
        default=False
    )
    parser.add_argument(
        "--points",
        help="nr. of plot points to generate",
        type=int,
        required=False,
        default=5
    )
    parser.add_argument(
        "--markdown",
        help="whether to output markdown-friendly string",
        action='store_true',
        required=False,
        default=False
    )
    args = parser.parse_args()

    if args.random:
        random.shuffle(THEMES)
        themes = THEMES

    elif args.themes:
        themes = [word.strip() for word in args.themes.split(",")]
        assert len(themes)==5, "Need to input 5 themes"
        assert set(themes) == set(THEMES), f"Need to provide all the themes in {THEMES}"

    else:
        themes = read_input_themes()

    if args.verbose:
        # Debugging: print the list of themes to check if all are processed
        print(f"Themes: {themes}")  # This should print all 5 themes in one line

    if args.points:
        roll_plot_points(themes, args.points, args.markdown, args.verbose)

    else:
        while True:
            try:
                num_plot_points = int(
                    input("Enter the number of plot points to generate: ")
                )
            except ValueError:
                print("Please enter a valid number.")
                continue

            roll_plot_points(themes, num_plot_points, args.markdown, args.verbose)
