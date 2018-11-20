import sys

filename_new = sys.argv[1] # image data should be added to this file
filename_comp = sys.argv[2] # in this file there is all image data 
imagelist = sys.argv[3]
imglist = []
index = []
list_2 = []
file_1 = open(imagelist, 'r')
file_2 = open(filename_new, 'r')
file_3 = open(filename_comp, 'r')
for line in file_1:
    imglist.append("img"+line[:3]+".jpg")
for line in file_2:
    if line.find("img") is not -1:
        list_2.append(line[line.find("img"):line.find(".jpg")+4])
tmp = [x for x in imglist if x in list_2]
for i in range(len(tmp)):
    index.append(imglist.index(tmp[i]))
for i in range(len(index)):
    del imglist[index[i]]
file_1.close()
file_2.close()
file_2 = open(filename_new, 'a') # file.write("Text")
text = file_3.readlines() # list with all lines
for i in range(len(imglist)):
    for j in range(len(text)):
        if imglist[i] in text[j]:
            file_2.write(text[j])
            file_2.write(text[j+1])
