# adventure_roll.py:

import random
import json

rolled_10 = False

def theme_roll(themes):

	global rolled_10
	roll = random.randint(1,10)
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

def get_plot_point(theme):
    
    file_path = f"json/{theme.lower()}_table.json"

    with open(file_path, 'r',  encoding='utf-8') as file:
        table_data = json.load(file)
    
    roll = random.randint(1, 100)
    print("d100 roll: ", roll)

    for plot_point in table_data[f"{theme.lower()}_plot_points"]:
        roll_range = plot_point['roll'].split('-')
        if len(roll_range) == 1:
            if roll == int(roll_range[0]):
                return plot_point['name'], plot_point['description']
        else:
            if int(roll_range[0]) <= roll <= int(roll_range[1]):
                return plot_point['name'], plot_point['description']

def get_meta_plot_point():

	file_path = "json/meta_table.json"
	
	with open(file_path, 'r',  encoding='utf-8') as file:
	    table_data = json.load(file)
	roll = random.randint(1, 100)
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

if __name__ == "__main__":
	print("---------------------- INPUT THEME PRIORITY ------------------------")
	print("1: Action")
	print("2: Tension")
	print("3: Mystery")
	print("4: Social")
	print("5: Personal")
	print("Separate with comma (,)")
	print("Example priority input:")
	print("Input: 2,4,5,3,1")
	print("Theme priority: Tensom, Social, Personal, Mystery, Action")
	
	#values_string = input()
	
	#values = values_string.split(',')

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

	# Debugging: print the list of themes to check if all are processed
	print(f"Themes: {themes}")  # This should print all 5 themes in one line

	while True:
		print("------------------------------------------------------------------")
		theme = theme_roll(themes)
		print("Theme: ",theme)
		plot_point = get_plot_point(theme)
		print("Name: ", plot_point[0])
		print("Description: ", plot_point[1])
		if plot_point[0] == "META":
			print("------------------- META PLOT POINT ---------------------")
			plot_point = get_meta_plot_point()
			print("Name: ", plot_point[0])
			print("Description: ", plot_point[1])
		print("------------------------------------------------------------------")
		input("Press Enter to roll a new plot point...")
	