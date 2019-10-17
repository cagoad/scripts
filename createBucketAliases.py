filename = "/Users/cagoad/dev/scripts/bucketMapping.csv"
dict = {}
with open(filename) as f:
    for line in f:
        (key, val) = line.rstrip("\n").split(",")
        dict[key] = val
        
for key, value in dict.iteritems():
    print("alias " + key +"='gull {}'").format(value)