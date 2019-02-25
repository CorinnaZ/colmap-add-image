import sys
mergefrom='D:/BA_IENT/COLMAP_Workspace/MergeTest/1_2/1_2.txt'
mergeto='D:/BA_IENT/COLMAP_Workspace/MergeTest/KF9/KF9.txt'
newfile = 'D:/BA_IENT/COLMAP_Workspace/MergeTest/new_merged/output.txt'
idxlist_1 = []
imglist_1 = []
linelist_1 = []
idxlist_2 = []
imglist_2 = []
linelist_2 = []
mylist = []
with open (mergefrom) as f:
    file1 = f.readlines()
file1 = file1[3:]
with open(mergeto) as f:
    file2 = f.readlines()
file2 = file2[3:]
filewrite = open(newfile, 'a')
for line in file2:
    line1 = line[:line.find(" ")]
    imgids = [int(s)for s in line.split() if s.isdigit()]
    imgids = imgids[4:]
    idxlist_1.append(int(line1))
    imglist_1.append(imgids)
    linelist_1.append(line)
for line in file1:
    line1 = line[:line.find(" ")]
    imgids = [int(s)for s in line.split() if s.isdigit()]
    imgids = imgids[4:]
    idxlist_2.append(int(line1))
    imglist_2.append(imgids)
    linelist_2.append(line)
for line in linelist_2:
    ids = []
    point3dID = line[:line.find(" ")]
    for j, item in enumerate(idxlist_1):
        if int(point3dID) == int(item):
            ids = [int(s) for s in line.split() if s.isdigit()]
            ids = ids[4:]
            for k, number in enumerate(imglist_1[j]):
                if k%2 == 0:
                    if number not in ids:
                        ids.extend(imglist_1[j][k:k+2])
            search = " "+str(ids[0]) + " "
            filewrite.write(line[:line.find(search)])
            for thing in ids:
                filewrite.write(" "+str(thing))
            filewrite.write("\n")
            mylist.append(point3dID)
    if int(point3dID) not in idxlist_1:
        filewrite.write(line)
print(mylist)
for item in mylist:
    for line in linelist_1:
        if item == line[:line.find(" ")]:
            linelist_1.remove(line)
for line in linelist_1:
    filewrite.write(line)
