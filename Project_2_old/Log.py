# Project 2 for OMS6250
#
# Log function for the Spanning Tree Project.
#
# Copyright 2016 Michael Brown
#           Based on prior work by Sean Donovan, 2015


def log_spanning_tree(filename, switches):
    #TODO: Implement a logging function that outputs the spanning tree to a text file ('filename'.txt).
    #      Output the links included in the spanning tree in increasing order, first by source switch ID, then 
    #      destination switch ID.  This means each link should be printed twice, since links are bidirectional.
    #      Output all links for each source switch ID on the same line.  Use a new line for each source switch ID.
    #      Links must be printed as "(source switch id) - (destination switch id)", with links on same line separated by a commma ','.
    #      For example, given a spanning tree (1 ----- 2 ----- 3), a correct output file would have the following text:
    #      1 - 2
    #      2 - 1, 2 - 3
    #      3 - 2
    #
    #      An example of this valid output file is included (output.txt) with the project skeleton.
    outputFile = filename
    printList = []
    for i in range(1,len(switches)+1):
        ##clean up list
        for key, value in switches[i].connections.iteritems():
            if (value==1):
                if key not in printList:
                    printList.append(key)
    #sort list
    newList = []
    for item in printList:
        newItem = item.replace("$", ".")
        newList.append(newItem)
    sortedPrintList = sorted(newList, key=float)
    #put back into dollar sign format so as not to have float issues
    yetAnother = []
    for item in sortedPrintList:
        dollarItem = item.replace(".", "$")
        yetAnother.append(dollarItem)
    #write to log file
    with open(outputFile, "w") as text_file:
        for x in range(0, len(yetAnother)):
            #when they match, do the following. We need this line
            #if the current int(yetAnother[x].split("$")[0]) is equal to next int(yetAnother[x].split("$")[0]), append comma
            try:
                if int(yetAnother[x].split("$")[0]) == int(yetAnother[x+1].split("$")[0]):
                    #check if next int(yetAnother[x].split("$")[0]) is greater than mine, I need to append a new line, otherwise I will
                    #continue appending ,
                    if int(yetAnother[x].split("$")[0]) < int(yetAnother[x+1].split("$")[0]):
                        suffix = yetAnother[x].split("$")[1]
                        if suffix.startswith("0"):
                            newSuffix = suffix[1:]
                            text_file.write(yetAnother[x].split("$")[0]+" - "+newSuffix+"\n")
                        else:
                            text_file.write(yetAnother[x].split("$")[0]+" - "+suffix+"\n")
                    else:
                        suffix = yetAnother[x].split("$")[1]
                        if suffix.startswith("0"):
                            newSuffix = suffix[1:]
                            text_file.write(yetAnother[x].split("$")[0]+" - "+newSuffix+", ")
                        else:
                            text_file.write(yetAnother[x].split("$")[0]+" - "+suffix+", ")
                elif int(yetAnother[x].split("$")[0]) > int(yetAnother[x-1].split("$")[0]):
                    if int(yetAnother[x].split("$")[0]) < int(yetAnother[x+1].split("$")[0]):
                        suffix = yetAnother[x].split("$")[1]
                        if suffix.startswith("0"):
                            newSuffix = suffix[1:]
                            text_file.write(yetAnother[x].split("$")[0]+" - "+newSuffix+"\n")
                        else:
                            text_file.write(yetAnother[x].split("$")[0]+" - "+suffix+"\n")
                    else:
                        suffix = yetAnother[x].split("$")[1]
                        if suffix.startswith("0"):
                            newSuffix = suffix[1:]
                            text_file.write(yetAnother[x].split("$")[0]+" - "+newSuffix+", ")
                        else:
                            text_file.write(int(yetAnother[x].split("$")[0])+" - "+suffix+", ")
                elif int(yetAnother[x].split("$")[0]) == int(yetAnother[x-1].split("$")[0]):
                    if int(yetAnother[x].split("$")[0]) < int(yetAnother[x+1].split("$")[0]):
                        suffix = yetAnother[x].split("$")[1]
                        if suffix.startswith("0"):
                            newSuffix = suffix[1:]
                            text_file.write(yetAnother[x].split("$")[0]+" - "+newSuffix+"\n")
                        else:
                            text_file.write(yetAnother[x].split("$")[0]+" - "+suffix+"\n")
                    else:
                        suffix = yetAnother[x].split("$")[1]
                        if suffix.startswith("0"):
                            newSuffix = suffix[1:]
                            text_file.write(int(yetAnother[x].split("$")[0])+" - "+newSuffix+", ")
                        else:
                            text_file.write(yetAnother[x].split("$")[0]+" - "+suffix+", ")
            except IndexError:
                if x !=0:
                    if int(yetAnother[x].split("$")[0]) > int(yetAnother[x-1].split("$")[0]):
                        suffix = yetAnother[x].split("$")[1]
                        if suffix.startswith("0"):
                            if int(yetAnother[x].split("$")[0]) > int(yetAnother[x-1].split("$")[0]):
                                newSuffix = suffix[1:]
                                text_file.write(yetAnother[x].split("$")[0]+" - "+newSuffix)
                            elif int(yetAnother[x].split("$")[0]) < int(yetAnother[x+1].split("$")[0]):
                                newSuffix = suffix[1:]
                                text_file.write(yetAnother[x].split("$")[0]+" - "+newSuffix+"\n")
                            else:
                                newSuffix = suffix[1:]
                                text_file.write(yetAnother[x].split("$")[0]+" - "+newSuffix+", ")
                        else:
                            text_file.write(yetAnother[x].split("$")[0]+" - "+suffix)