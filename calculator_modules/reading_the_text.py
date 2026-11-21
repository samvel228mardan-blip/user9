with open("text.txt", "w", encoding="utf-8") as file:
    file.write("\ntest")

with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

