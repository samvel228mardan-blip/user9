with open("text.txt", "a", encoding="uft-8") as file:
    file.write("\ntest")

with open("text.txt", "r", encoding="uft-8") as file:
    content = file.read()
    print(content)

