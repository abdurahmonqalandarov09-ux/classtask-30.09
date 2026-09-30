# with open("text.txt", "w") as file:
#     file.write("Salom, jahon")



# test 2
# with open("text.txt", "r") as file:
#     print(file.read())


# test 3

# with open("text.txt", "r") as file:
#     for i in file:
#         print(i.strip())


# test 4

# cnt = 0
# with open("text.txt", "r") as file:
#     for i in file:
#         cnt += 1
# print(cnt)


# test 5

# with open("text.txt", "a") as file:
#     file.write("orange")

# test 6

# with open("text.txt", "w") as file:
#     file.writelines(["Ali\n", "Vali\n", "Guli\n"])



# test 7

# with open("text.txt", "r") as file:
#     print(len(file.read().split()))


# test 8
# cnt = 0
# with open("text.txt", "r") as file:
#     for i in file.read().replace(" ", ""):
#         cnt += 1
# print(cnt)

# test 9

# sm = 0
# with open("text.txt", "r") as file:
#     for  i in file:
#         sm += int(i)

# print(sm)


# test 10
# with open("text.txt") as file:
#     s=file.readlines()
#     d=max(s)
#     d=d.rstrip()
#     print(d)


# test 11

# with open("text.txt", "r") as file:
#     d = file.read()

# with open("copy.txt", "w") as f:
#     b = f.write(d)


# test 12

# with open("text.txt", "r") as file:
#     for i, file in enumerate(file, start=1):
#         print(f"{i}: {file.strip()}")


# test 13

# with open("text.txt", "r") as file:
#     w = file.read().split()

# print(w.count("python"))


# test 14

# with open("text.txt", "r")as file:
#     l = [l.rstrip("\n") for l in file]

# print(max(l, key=len))


# test 15

# with open("text.txt", "r") as f:
#     f = f.read()

# with open("copy.txt", "w") as file:
#     file.write(f.upper())


# test 16

# with open("text.txt") as f:
#     lines = f.readlines()

# clean = [line for line in lines if line.strip()]

# with open("copy.txt", "w") as file:
#     file.writelines(clean)

# test 17

