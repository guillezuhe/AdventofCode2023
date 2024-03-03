# Open the input file
file = open("Day2/input", "r")
colors = ['red', 'green', 'blue']
max_number = [12, 13, 14]

sum = 0
for line in file:
    # Each line has the format:
    # Game index: i color, j color, k color; l color, m color, n color; o color, p color, q color
    
    valid_game = True
    # Get the game index
    game_index = int(line.split(":")[0].split(" ")[-1])
    print('Game index:', game_index)
    # Get the number of experiments
    experiments = line.split(":")[1].split(";")

    for k, experiment in enumerate(experiments):
        experiment = experiment.strip()
        # Get the colors and its number
        for n_color in experiment.split(","):
            color = n_color.strip().split(" ")
            # Get the corresponding index of the color comparing to the list of colors
            color_index = colors.index(color[1])
            # Get the number of the color
            number = int(color[0])

            if number > max_number[color_index]:
                print('Invalid game:', game_index, 'In experiment', k, 'the number', number, 'is greater than the maximum number of', colors[color_index], 'which is', max_number[color_index])
                valid_game = False
                break
    
    if valid_game:
        sum += game_index

print('The sum of the valid games is:', sum)
