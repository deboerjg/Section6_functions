numbers = (0,1,2,3,4,5)

# print(numbers, sep=";")
# print(*numbers, sep=";") # * unpacks items
# # Equivialent to print(0,1,2,3,4,5)


def test_star(*values):
    print(values)
    for x in values:
        print(x)


test_star(1,2,3,4,5) # *args packs multiple variabls into tuple
print()
test_star()
test_star(1)