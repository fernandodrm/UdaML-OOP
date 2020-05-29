from nearest import nearest_square

nearest_5 = nearest_square(5)
print("Nearest <=5: returned {}, correct is 4".format(nearest_5))
assert(nearest_5==4)