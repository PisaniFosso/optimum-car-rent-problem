#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Autor: Pisani Fosso                                                               +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Description:   A carriage company is renting cars and there is a particular car   +
#                for which the interest is the highest so the company decides to    +
#                book the requests one year in advance. We represent a request      +
#                with a tuple (x, y) where x is the first day of the renting and y  +
#                is the last. Your goal is to come up with an optimum strategy      +
#                where you serve the most number of requests.                       +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#import Librairies for copie and regular expressions
import re
import copy

# file direction first Line must be the nomber of booking request
# second Line the start days of renting
# thirt Line the last day of renting
path = '/Users/Fosso Print/Desktop/projets/PYTHON/car rent/Inputs.txt'

# Open the file and take the inputs
myFile = open(path, 'r')
numberOfQuery = int(myFile.readline())
startDateline = re.findall(r"\w+",(myFile.readline()))
endDateline = re.findall(r"\w+",(myFile.readline()))
startDates = []

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Name of the function: getRequest                                                  +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Description:  Put the lignes that we previously took from the file in a tuple     +
#               (x, y) where x is the start date and y the end date of renting      +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getRequest():
    for i in range (numberOfQuery):
        startDates.append((startDateline[i], endDateline[i]))
    return (startDates)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Name of the function: TheBestDeal                                                 +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Description:  find the optimum nomber of customer that we can satisfier           +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def TheBestDeal():

    test = 0
    tupleInput = getRequest()
    done = False
    Listfinal = []
    while not done:
        LisfinalNext = []
        Higher = 0
        if test == 0:
            for i in range (365):
                for start in tupleInput:
                    if i == int(start[0]) and i > int(Higher) :
                        Higher = start[1]
                        Listfinal.append(start)
                        break
        else:
            for i in range (365):
                for start in tupleInput:
                    if i == int(start[0]) and i > int(Higher) and int(start[0]) < int(start[1]):
                        Higher = start[1]
                        LisfinalNext.append(start)
                        break

        if len(Listfinal) < len (LisfinalNext):
            Listfinal = copy.copy(LisfinalNext)

        listtp = list(tupleInput)
        del(listtp[0])
        tupleInput = tuple(listtp)

        test += 1
        if test > numberOfQuery-1:
            done = True

    return tuple(Listfinal)


print(TheBestDeal())
