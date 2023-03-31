# standard deviation around the median algorithm
def median_anomaly_detection(data, threshold):
    # get the gem costs
    costs = get_costs(data)
    # calculate the median and standard deviation of the data
    average = np.median(costs)
    # calculate the anomaly threshold based on the costs
    anomaly_threshold = calculate_threshold(costs, threshold)
    # initialize a list to store the anomalies
    anomalies = []
    # iterate through the data and add out of range data to anomalies
    for i in range(len(data)):
        gem = data[i]
        deviance = abs(gem.cost - average)
        if deviance > anomaly_threshold:
            anomalies.append(gem)
    # return the anomlies found
    return anomalies