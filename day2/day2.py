import os


colours = {"green":13,"red":12,"blue":14}
# =================================================================================
#  main
# =================================================================================
def main():
    filename = "input"

    with open(filename) as data:
        input_data = data.readlines()

    first_answer = 0
    second_answer = 0
    games_dictionary = {}
    for line in input_data:
        line = line.replace("\n","")
        line = line.split(":")
        game_id = line[0].replace("Game ","")
        game_id = int(game_id)
        games = line[1].split(";")
        game_possible = True
        highest = {"red":0,"green":0,"blue":0}
        for game in games:
            game_occurr = count_cubes(game)
            game_possible = part_one(game_occurr,game_possible)
            highest = part_two(game_occurr,highest)
        if game_possible: first_answer = first_answer+game_id
        second_answer = second_answer + highest["red"]*highest["green"]*highest["blue"]

    allgood(f"First answer is {first_answer}")
    allgood(f"Second answer is {second_answer}")

# =================================================================================
#  Get part one answer
# =================================================================================
def part_one(game_occurr,game_possible):
    for col in colours.keys():
        if game_occurr[col]>colours[col]: game_possible = False
    return game_possible

# =================================================================================
#  Get part two answer
# =================================================================================
def part_two(game_occurr,highest):
    for col in colours.keys():
        if game_occurr[col]>highest[col]: highest[col] = game_occurr[col]
    return highest

# =================================================================================
#  count cubes of each colour in game
# =================================================================================
def count_cubes(game):
    game_occurr = {"red":0,"blue":0,"green":0}
    cubes = game.split(",")
    for cube in cubes:
        for colour in game_occurr.keys():
            found = cube.find(colour)
            if found!=-1:
                num_cubes = [int(s) for s in cube.split() if s.isdigit()]
                game_occurr[colour] = num_cubes[0]

    return game_occurr

# ===========================================================
#  Colours to throw scary messages on screen
# ===========================================================
class bcolors:
    INFO = '\033[95m' #PURPLE
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def warn(message): print(bcolors.WARNING+"=== "+message+" ==="+bcolors.RESET)
def fail(message): print(bcolors.FAIL+"=== "+message+" ==="+bcolors.RESET)
def allgood(message): print(bcolors.OK+"=== "+message+" ==="+bcolors.RESET)
def info(message): print(bcolors.INFO+"=== "+message+" ==="+bcolors.RESET)

# ===========================================================
# __main__
# ===========================================================
if __name__ == '__main__':
  main()
