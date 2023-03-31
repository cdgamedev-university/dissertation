import numpy as np

# detect anomalies in data
def detect_anomalies(d: list, t):
    # calculate mean
    m = np.mean(d)
    # calculate standard deviation
    s = np.std(d)
    # create threshold based on s
    st = s * t
    # store the anomalies
    a = []
    # for every value in data
    for i in d:
        # if point is in range
        if abs(i - m) > st:
            # add point to a
            a.append(i)
    # return all anomalies
    return a

def load_dataset(path):
    d = []
    f = open(path, 'r')
    for i in f:
        try:
            d.append(int(i) * -1)
        except ValueError:
            continue
    f.close()
    return d
    
# load a sample dataset
d = load_dataset('algorithms/data.txt')
# find anomalies
a = detect_anomalies(d, 1)
# display the anomalies
print(a)