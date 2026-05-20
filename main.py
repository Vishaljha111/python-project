path = "c:\\Users\\User\\Documents\\file.txt"

if os.path.exists(path):
    print("That location exists!")
else:
    print("That location does not exist!")