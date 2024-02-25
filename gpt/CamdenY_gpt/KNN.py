def KNN(kVal):
    """
    Implement the k-Nearest Neighbors (KNN) algorithm for classification.

    Parameters:
    - kVal (int): The number of nearest neighbors to consider for classification.

    Reads data from 'MNIST_training.csv' as training data and 'MNIST_test.csv' as test data.
    Calculates the accuracy of the algorithm and prints the result.

    Returns:
    None
    """
    trainingData = []
    testData = []
    correctPredict = 0
    predictedLabels = []

    # Read training data from 'MNIST_training.csv'
    with open('MNIST_training.csv', 'r') as trainingFile:
        reader = csv.reader(trainingFile)
        next(reader)  # Skip header
        for line in reader:
            if line:
                trainingData.append(line)

    # Read test data from 'MNIST_test.csv'
    with open('MNIST_test.csv', 'r') as testFile:
        reader = csv.reader(testFile)
        next(reader)  # Skip header
        for line in reader:
            if line:
                testData.append(line)

    # Classify each point in the test data
    for i in testData:
        closestLabels = []

        # Calculate Euclidean distances between the test point and all training points
        pointDistance = np.array(euclDistance(i, trainingData))
        trData = np.array(trainingData)

        # Sort training points based on distances
        sortedData = pointDistance.argsort()
        closestPoints = trData[sortedData]

        # Select k nearest neighbors
        for k in itertools.islice(closestPoints, kVal):
            closestLabels.append(k[0])

        # Predict the label based on majority vote
        predictedLabel = max(set(closestLabels), key=closestLabels.count)
        predictedLabels.append(predictedLabel)

    # Evaluate the accuracy of the predictions
    for (i, j) in zip(testData, predictedLabels):
        if i[0] == j:
            correctPredict += 1

    # Print the accuracy percentage without changing the format
    percentCorrect = float(correctPredict / len(testData)) * 100
    print(" The percent correct with a k value of " + str(kVal) + " is " + str(percentCorrect) + "%")