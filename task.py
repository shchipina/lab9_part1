# part (a)
try:
    with open("TF12_1.txt", "w") as file:
        file.write("Hello, it's me\n")
        file.write("Hello, world\n")
        file.write("Let it snow\n")
        file.write("Last Christmas I gave you my heart\n")
        file.write("But the very next day you gave it away\n")
        file.write("Tris year, to save me from tears\n")
except Exception as e:
    print(f"Bzzz..z error something happened TF12_1.txt cannot create: {e}")

# part (b)
try:
    with open("TF12_1.txt", "r") as read_file, open("TF12_2.txt", "w") as write_file:
        lines = read_file.readlines()
        for i, line in enumerate(lines, start=1):
            write_file.write(line[:i] + '\n')
except Exception as e:
    print(f"Error: {e}")

# part (c)
try:
    with open("TF12_2.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
except Exception as e:
    print(f"Bzzz..z error something happened TF12_2.txt cannot be read: {e}")
