import pytest

def calculateGameIds():
    sumIds = 0
    games = getGamesFromFile()

    for i, game in enumerate(games):
        gameInfo = game.split(":")
        gameId = int(gameInfo[0].split(' ')[1])
        if (isPossibleGame(gameInfo[1])):
            sumIds += gameId

    return sumIds

def calculatePower():
    powerSum = 0
    games = getGamesFromFile()

    for i, game in enumerate(games):
        gameInfo = game.split(":")
        powerSum += getPowerFromGame(gameInfo[1])

    return powerSum


def getGamesFromFile():
    games = []

    file = open('input.txt', 'r')
    lines = file.readlines()
    
    for line in lines:
        games.append(line.strip())

    return games

def isPossibleGame(gameInfo):
    gameCubes = {'red': 0, 'green': 0, 'blue': 0}

    setOfCubes = gameInfo.split(";")

    for subSet in setOfCubes:
        separatedCubes = subSet.split(',')
        for cube in separatedCubes:
            value = int(cube.strip().split(" ")[0])
            if ("red" in cube):
                gameCubes['red'] = value
            elif ("green" in cube):
                gameCubes['green'] = value
            elif ("blue" in cube):
                gameCubes['blue'] = value

        if (gameCubes['red'] > 12 or gameCubes['green'] > 13 or gameCubes['blue'] > 14):
            return False

    return True

def getPowerFromGame(gameInfo):
    gameCubes = {'red': 0, 'green': 0, 'blue': 0}

    setOfCubes = gameInfo.split(";")

    for subSet in setOfCubes:
        separatedCubes = subSet.split(',')
        for cube in separatedCubes:
            value = int(cube.strip().split(" ")[0])
            if ("red" in cube):
                if (value > gameCubes['red']):
                    gameCubes['red'] = value
            elif ("green" in cube):
                if (value > gameCubes['green']):
                    gameCubes['green'] = value
            elif ("blue" in cube):
                if (value > gameCubes['blue']):
                    gameCubes['blue'] = value

    return gameCubes['red'] * gameCubes['green'] * gameCubes['blue']


@pytest.mark.parametrize("test_input,expected", [('3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', True), ('1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', True), ('8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', False), ('1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', False), ('6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', True)])
def testTrebuchet(test_input, expected):
    assert isPossibleGame(test_input) == expected


# MAIN
if __name__=='__main__':
    print('sumIds: ' + str(calculateGameIds()))
    print('power: ' + str(calculatePower()))