import pytest

def calculateFinalValue(arrayLines):
    result = 0

    for line in arrayLines:
        result += calculateCalibrationValue(line)

    return result


def getArrayEntriesFromFile():
    entries = []

    file = open('input.txt', 'r')
    lines = file.readlines()
    
    for line in lines:
        entries.append(line.strip())

    return entries


def calculateCalibrationValue(lineValue):
    firstValue = getFirstDigit(lineValue)
    lastValue = getFirstDigit(lineValue[::-1])

    result = concat(firstValue, lastValue)

    return result


def getFirstDigit(lineValue):
    for i, c in enumerate(lineValue):
        if (c.isdigit()):
            return c
        
    return ''


def concat(a, b):
    return int(f"{a}{b}")


@pytest.mark.parametrize("test_input,expected", [('1abc2', 12), ('pqr3stu8vwx', 38), ('a1b2c3d4e5f', 15), ('treb7uchet', 77)])
def testTrebuchet(test_input, expected):
    assert calculateCalibrationValue(test_input) == expected

# MAIN
if __name__=='__main__':
    # calculateCalibrationValue('1abc2')
    print('finalValue: ' + str(calculateFinalValue(getArrayEntriesFromFile())))