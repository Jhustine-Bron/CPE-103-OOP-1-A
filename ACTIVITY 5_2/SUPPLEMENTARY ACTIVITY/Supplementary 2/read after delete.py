# READ after delete
with open("BRON.txt", "r") as f:
    print("Reading file after deletion (should be empty):")
    print(f.read())
