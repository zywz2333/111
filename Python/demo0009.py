f = open("./名字.txt", encoding='utf-8')

for user in f:
    if user.startswith("吴") and user.endswith("彬"):
        print(user)