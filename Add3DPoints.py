import sys

filename_new = sys.argv[1] # points should be added to this file
filename_old = sys.argv[2] # point data comes from this file
idlist = sys.argv[3] # txt file with image ids that shall be added
idxlist = []
addedpoints = []
file1 = open(idlist, 'r')
file2 = open(filename_new, 'r')
file3 = open(filename_old, 'r')
for line in file1: # generating list with indexes that shall be added
    line = line.strip()
    idxlist.append(int(line))
for i in range(len(idxlist)):
    file3.close()
    file3 = open(filename_old, 'r')
    for line in file3:
        # check whether the line already exists from another point
        number = line[:line.find(" ")]
        already_there = False
        for line_comparison in file2:
            number2 = line_comparison[:line_comparison.find(" ")]
            if number2 == number:
                already_there = True
        if already_there is False:
            id_list = []
            partline = line[16:] # in here are only image ids and 2d points
            #extract possible image ids
            numbers = [int(s) for s in partline.split() if s.isdigit()]
            for j in range(len(numbers)):
                if j%2 == 0:            
                    id_list.append(numbers[j])
            # match image id
            for k in range(len(id_list)):
                if idxlist[i] == id_list[k]:
                    addedpoints.append(line[:line.find(" ")])
            addedpoints = list(set(addedpoints)) # removes double entries
            print(addedpoints)
#add line
file3.close()
file2.close()
file2 = open(filename_new, 'a')
file3 = open(filename_old, 'r')
#file2.write("\n")
for line in file3:
    for i in range(len(addedpoints)):
        number = line[:line.find(" ")]
        if number == addedpoints[i]:
            file2.write(line)
file1.close()
file2.close()
file3.close()