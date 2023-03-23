import numpy as np

# 2T algorithm
def twostage_sd(data, threshold, anomalies=None):
    # get the gem costs
    costs = get_costs(data)
    
    # calculate the anomaly threshold based on the costs
    anomaly_threshold = calculate_threshold(costs, threshold)
    
    # calculate the mean of the data
    average = np.mean(costs)
    
    # if the anomalies array doesn't exist, create it
    if (anomalies == None):
        anomalies = []
    
    # set a default value for anomalies found
    anomaly_found = False
    # iterate through the data and detect anomalies
    for i in range(len(data)):
        # if i is greater than the data length, break from the for loop
        if (len(data) <= i):
            break
        # get the gem
        gem = data[i]
        # calculate the deviance
        deviance = abs(gem.cost - average)
        # if the deviance is above the threshold
        if deviance > anomaly_threshold:
            # log that an anomaly was found
            anomaly_found = True
            # add the gem to the anomalies
            anomalies.append(gem)
            # remove the gem from the dataset
            data.remove(gem)
    
    # if an anomaly has been found, recursively call the function
    if anomaly_found:
        return twostage_sd(data, threshold, anomalies)
    
    # return the array of anomalies
    return anomalies