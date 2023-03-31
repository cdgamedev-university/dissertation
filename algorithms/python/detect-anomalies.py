import numpy as np

# detect anomalies in data
def detect_anomalies(d, t):
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
    
# load a sample dataset
d = load_dataset('data.txt')
# find anomalies
a = detect_anomalies(d, 1)
# display the anomalies
print(a)