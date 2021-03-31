import collections, sys
import arg_reader

def generate(args):
    f = open(args["inputFilePath"], 'r')
    allLines = f.readlines()

    outputDict = {}
    outputLines = []


    for line in allLines:
        # print(line)
        outputDict[line] = line

    # print(outputDict)

    for key in outputDict:
        line = outputDict[key]
        outputLines.append(line)

    w = open(args["outputFilePath"], 'w')
    w.writelines(outputLines)


if __name__ == '__main__':
    try:
        argv = sys.argv[1:]
        args = arg_reader.getArgs(argv)
        generate(args)
    except Exception as e:
        print(e)
