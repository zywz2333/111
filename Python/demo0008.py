f = open("test.txt", "w")
f.writelines("xiaokunkun")
f.writelines("xiaolili")
f.close()

with open("test.txt", "w") as f:
    f.writelines("xiaokunkunaaaa")
    f.writelines("xiaoliliaaaa")