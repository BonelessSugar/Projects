def userInputs():
    print("Input Base Stats for Pokemon")
    print("HP Atk Def Sp.Atk Sp.Def Speed")
    print("EX: 90 92 75 92 85 60")
    baseStatsIn = input("").split()
    totalIVList = []
    nextPokemon = 'y'
    while nextPokemon == "y":
        levelIn = int(input("Input Level: "))
        numberNatureList = ['hardy', [1, 1], 'lonely', [1, 2], 'adamant', [1, 3], 'naughty', [1, 4], 'brave', [1, 5], 'bold', [2, 1], 'docile', [2, 2], 'impish', [2, 3], 'lax', [2, 4], 'relaxed', [2, 5], 'modest', [3, 1], 'mild', [3, 2], 'bashful', [3, 3], 'rash', [3, 4], 'quiet', [3, 5], 'calm', [4, 1], 'gentle', [4, 2], 'careful', [4, 3], 'quirky', [4, 4], 'sassy', [4, 5], 'timid', [5, 1], 'hasty', [5, 2], 'jolly', [5, 3], 'naive', [5, 4], 'serious', [5, 5]]
        natureIn = input("Input Nature: ")
        natureIn = natureIn.lower()
        while natureIn not in numberNatureList:
            natureIn = input("Invalid Nature, try again: ")
            natureIn = natureIn.lower()
        numberNature = numberNatureList[numberNatureList.index(natureIn)+1]
        statsIn = input("Input Given Stats for Pokemon: ").split()
        IVList = []
        IVList = IVHP(baseStatsIn, levelIn, statsIn, IVList)
        IVList = IVOtherStats(baseStatsIn, levelIn, numberNature, statsIn, IVList)
        IVTotal = 0
        for IV in range(0,len(IVList)):
            IVTotal = IVTotal + IVList[IV]
        IVList.append(IVTotal)
        nextPokemon = input("Next Pokemon? y/n: ")
        totalIVList.append(IVList)
    for elem in totalIVList:
        print(elem)
    print("[hp, atk, def, sp.a, sp.d, spd, total]")

def IVHP(baseStatsIn, levelIn, statsIn, IVList):
    hpStatLow = int(statsIn[0]) - int(levelIn) - 10 
    hpStatLow = hpStatLow * 100 / int(levelIn)
    hpStatLow = int(hpStatLow - (2 * int(baseStatsIn[0])))
    hpStatHigh = int(statsIn[0]) + 1 - int(levelIn) - 10 
    hpStatHigh = hpStatHigh * 100 / int(levelIn)
    hpStatHigh = int(hpStatHigh - (2 * int(baseStatsIn[0]))) - 1
    hpStatAvg = round((hpStatLow + hpStatHigh) / 2)
    IVList.append(hpStatAvg)
    return IVList

def IVOtherStats(baseStatsIn, levelIn, numberNature, statsIn, IVList):
    for statNum in range(1,6):
        if statNum == numberNature[0]:
            if statNum == numberNature[1]:
                IVList.append(otherStatAvg(statsIn, levelIn, baseStatsIn, statNum, 1))
            else:
                IVList.append(otherStatAvg(statsIn, levelIn, baseStatsIn, statNum, 1.1))
        elif statNum == numberNature[1]:
            if statNum == numberNature[0]:
                IVList.append(otherStatAvg(statsIn, levelIn, baseStatsIn, statNum, 1))
            else:
                IVList.append(otherStatAvg(statsIn, levelIn, baseStatsIn, statNum, 0.9))
        else:
            IVList.append(otherStatAvg(statsIn, levelIn, baseStatsIn, statNum, 1))
    return IVList

def otherStatAvg(statsIn, levelIn, baseStatsIn, statNum, natureIn):
    import math
    statNumLow = int(statsIn[statNum]) / natureIn
    statNumLow = math.ceil(statNumLow)
    statNumLow = statNumLow - 5
    statNumLow = statNumLow * 100
    statNumLow = statNumLow / int(levelIn)
    statNumLow = (statNumLow - (2 * int(baseStatsIn[statNum])))
    statNumLow = math.ceil(statNumLow)
    statNumHigh = (int(statsIn[statNum]) + 1) / natureIn
    statNumHigh = math.ceil(statNumHigh)
    statNumHigh = statNumHigh - 5
    statNumHigh = statNumHigh * 100
    statNumHigh = statNumHigh / int(levelIn)
    statNumHigh = (statNumHigh - (2 * int(baseStatsIn[statNum]))) - 1
    statNumHigh = math.ceil(statNumHigh)
    statNumAvg = round((statNumLow + statNumHigh) / 2)
    return statNumAvg

userInputs()

#further could be sorted by highest sum of IVs?
