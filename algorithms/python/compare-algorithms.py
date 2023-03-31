# create a dictionary for anomalies
a = {}
    
# function to calculate results
def count_result(p):
    try:
        # if point already exists in anomalies increment it
        a[p] = a[p] + 1
    except:
        # create point in anomalies
        a[p] = 1

# function to check all results in the data
def check_results(d):
    # for all indexes in the data
    for i in d:
        # count the result of the index
        count_result(i)

# load the dataset
d = load_dataset('data.txt')

# check the results of the data
check_results(d)

# print the anomalies
print(a)