"""
# from org.transcrypt.stubs.browser import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Normalize z will be used to normalize the data set such that the values in the dataset will be optimised for the model


def normalize_z(dfin, columns_means=None, columns_stds=None):
    if columns_means == None:
        columns_means = dfin.mean(axis=0)

    if columns_stds == None:
        columns_stds = dfin.std(axis=0)

    dfout = (dfin - columns_means)/columns_stds

    return dfout, columns_means, columns_stds

# get features and targets will help to separate the predictor and response variables into the features and target of the model respectively


def get_features_targets(df, feature_names, target_names):
    df_feature = pd.DataFrame(df.loc[:, feature_names])
    df_target = pd.DataFrame(df.loc[:, target_names])

    return df_feature, df_target

# prepare feature ensures that the features has the correct number of x-variables for the coefficients of the model
# ensure that the DataFrame is also converted into a numpy array and properly shaped for the regression model


def prepare_feature(df_feature):
    row = df_feature.shape[0]
    if isinstance(df_feature, pd.DataFrame):
        df_feature = df_feature.to_numpy()
    zero = np.ones((row, 1))
    df_feature = df_feature.reshape(-1, df_feature.shape[1])

    df_feature = np.concatenate((zero, df_feature), axis=1)
    return df_feature

# prepare target ensures that the target DataFrame is also converted into a numpy array and properly shaped for the regression model


def prepare_target(df_target):
    if isinstance(df_target, pd.DataFrame):
        df_target = df_target.to_numpy()

    df_target = df_target.reshape(-1, df_target.shape[1])
    return df_target

# split data will help to split the data set into the test and training sets to help in the assessment and evaluation of the model


def split_data(df_feature, df_target, random_state=None, test_size=0.5):
    indexes = df_feature.index
    if random_state != None:
        np.random.seed(random_state)

    test_index = np.random.choice(indexes, int(
        test_size*len(indexes)), replace=False)

    train_index = list(set(indexes)-set(test_index))
    df_feature_train = df_feature.loc[train_index, :]
    df_feature_test = df_feature.loc[test_index, :]
    df_target_train = df_target.loc[train_index, :]
    df_target_test = df_target.loc[test_index, :]

    return df_feature_train, df_feature_test, df_target_train, df_target_test


# Read the CSV file
df = pd.read_csv('data/Dataset.csv')
df.columns
df.shape

# Extract the features and the targets
feature_names = ['HDI', 'Population']
target_names = ['FoodIns']
df_features, df_target = get_features_targets(df, feature_names, target_names)

# Split the data set into training and test
df_features_train, df_features_test, df_target_train, df_target_test = split_data(
    df_features, df_target, 100, 0.3)

# Normalize the features using z normalization
df_features_train_z, means, stds = normalize_z(df_features_train)

sns.set()
plt.scatter(df_features["HDI"], df_target)

sns.set()
plt.scatter(df_features["Population"], df_target)


def compute_cost_linreg(X, y, beta):
    J = 0
    y_hat = calc_linreg(X, beta)
    error = y_hat - y
    J = np.sum(error**2)
    m = X.shape[0]
    J = J/(2*m)
    return J


def gradient_descent_linreg(X, y, beta, alpha, num_iters):
    J_storage = np.zeros((num_iters, 1))
    m = X.shape[0]

    for n in range(num_iters):
        y_hat = calc_linreg(X, beta)
        deriv = np.matmul(X.T, (y_hat-y))
        beta = beta - alpha * (1/m) * deriv
        J_storage[n] = compute_cost_linreg(X, y, beta)
    return beta, J_storage


def calc_linreg(X, beta):
    return np.matmul(X, beta)


features = prepare_feature(df_features_train_z)
target = prepare_target(df_target_train)
iterations = 1500
alpha = 0.01
beta = np.zeros((3, 1))

beta, J_storage = gradient_descent_linreg(
    features, target, beta, alpha, iterations)
print(beta)


def predict_linreg(df_feature, beta):
    df_normalized, _, _ = normalize_z(df_feature, means, stds)

    df_prepared = prepare_feature(df_normalized)

    y_hat = calc_linreg(df_prepared, beta)

    return y_hat


pred = predict_linreg(df_features_test, beta)

plt.scatter(df_features_test["HDI"], df_target_test)
plt.scatter(df_features_test["HDI"], pred)

plt.scatter(df_features_test["Population"], df_target_test)
plt.scatter(df_features_test["Population"], pred)


def r2_score(y, ypred):
    ymean = np.mean(y)
    diff = y - ymean
    error = y - ypred

    sstot = np.sum(diff**2)
    ssres = np.sum(error**2)

    r2 = 1 - (ssres/sstot)
    return r2


def mean_squared_error(target, pred):
    n = target.shape[0]
    mse = np.sum((target - pred)**2)
    mse = mse/n

    return mse


# change target test set to a numpy array
target = prepare_target(df_target_test)

# Calculate r2 score by calling a function
r2 = r2_score(target, pred)

print(r2)

# Calculate the mse
mse = mean_squared_error(target, pred)

print(mse)
# backend.py

"""
