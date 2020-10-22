from sklearn.datasets import load_iris

iris_data = load_iris()
keys = iris_data.keys()
print('IRIS''s Keys', keys)
#Result
IRISs Keys dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])