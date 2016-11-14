tableData = [['apple', 'orange', 'cherries', 'banana', 'hhhhhhh'],
             ['Alice', 'Bob', 'Carol', 'David', 'oooooooooooo'],
             ['dogs', 'cats', 'moose', 'goose', 'wwwwwww']]

def printTable(tabledata):
    colWidths = []
    for i in range(len(tabledata[0])):
        for j in range(len(tabledata)):
            colWidths.append(len(tabledata[j][i]))
    for k in range(len(colWidths)-1):
        if colWidths[0] >= colWidths[1]:
            del colWidths[1]
        else:
            del colWidths[0]
    for i in range(len(tabledata[0])):
        for j in range(len(tabledata)):
            print(tabledata[j][i].rjust(colWidths[0]), end=' ')
        print()

printTable(tableData)

