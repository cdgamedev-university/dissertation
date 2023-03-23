import numpy as np

# standard deviation around the mean algorithm
def sd_median_anomaly_detection(data, threshold):
    # get the gem costs
    costs = get_costs(data)
    
    # calculate the mean of the data
    average = np.median(costs)
    
    # calculate the anomaly threshold based on the costs
    anomaly_threshold = calculate_threshold(costs, threshold)
    
    # initialize a list to store the anomalies
    anomalies = []
    
    # iterate through the data and detect anomalies
    for i in range(len(data)):
        gem = data[i]
        deviance = abs(gem.cost - average)
        if deviance > anomaly_threshold:
            anomalies.append(gem)
    
    return anomalies