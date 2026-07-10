# format() method
# default(implicit) order
default_order = "{} {} and {}".format('Today','is','Sunday')
print(default_order)

# order using positional argument
positional_order = "{1} {0} and {2}".format('is','Today','Sunday')
print(positional_order)

# order using keyword argument
keyword_order = "{t} {i} and {s}".format(i='is',t='Today',s='Sunday')
print(keyword_order)