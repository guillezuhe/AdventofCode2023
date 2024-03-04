# Open the input file
file = open("Day2/input", "r")
colors = ['red', 'green', 'blue']

sum = 0
for line in file:
    # Each line has the format:
    # Game index: i color, j color, k color; l color, m color, n color; o color, p color, q color
    
    # Get the game index
    game_index = int(line.split(":")[0].split(" ")[-1])
    print('Game index:', game_index)
    # Get the number of experiments
    experiments = line.split(":")[1].split(";")

    max_red, max_green, max_blue = 0, 0, 0

    for k, experiment in enumerate(experiments):
        experiment = experiment.strip()
        # Get the colors and its number
        for n_color in experiment.split(","):
            color = n_color.strip().split(" ")
            # Get the corresponding index of the color comparing to the list of colors
            color_index = colors.index(color[1])
            # Get the number of the color
            number = int(color[0])

            # Get the maximum number of each color
            if color[1] == 'red':
                max_red = max(max_red, number)
            elif color[1] == 'green':
                max_green = max(max_green, number)
            elif color[1] == 'blue':
                max_blue = max(max_blue, number)
    
    # Get the power of each game as the product of maxima
    power = max_red * max_green * max_blue
    print('The power of the game is:', power)
    sum += power


print('The sum of the valid games is:', sum)
