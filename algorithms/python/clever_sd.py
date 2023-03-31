# CleverSD algorithm
def clever_sd(data, threshold, anomalies=None):
    # get the gem costs
    costs = get_costs(data)
    # calculate the anomaly threshold based on the costs
    anomaly_threshold = calculate_threshold(costs, threshold)
    # calculate the mean of the data
    average = np.mean(costs)
    # set a base index of the largest value
    largest_index = -1
    # set a base deviance of the largest value
    largest_deviance = -1
    # run through the data
    for i in range(len(data)):
        # get the gem
        gem = data[i]
        # calculate the deviance
        deviance = abs(gem.cost - average)
        # if the deviance is above the threshold AND above the largest deviance
        if deviance > anomaly_threshold and deviance > largest_deviance:
            # set the largest index
            largest_index = i
            # set the largest deviance
            largest_deviance = deviance
    # if the anomalies array doesn't exist, create it
    if (anomalies == None):
        anomalies = []
    # if the largest index is -1, return all the anomalies
    if (largest_index == -1):
        return anomalies
    # get the gem
    gem = data[largest_index]
    # add the gem to the anomalies
    anomalies.append(gem)
    # remove the gem from the dataset
    data.remove(gem)
    # recursively call the function
    return clever_sd(data, threshold, anomalies)