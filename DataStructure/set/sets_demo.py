x = { "a", "b", "c", True }
y = { "a", "b", "i",1 }

# intersection : show samething of sets
z = x.intersection(y)
# print(z)

# symaticdif : it will show only not same thing ;
# note : true and 1 or 0 and false is same thing ;
z = x.symmetric_difference(y)
print(z)