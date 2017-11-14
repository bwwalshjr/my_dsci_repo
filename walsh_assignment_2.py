import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, explained_variance_score

data_a = pd.read_csv('c:/github/my_dsci_401/data/AmesHousingSetA.csv')
data_b = pd.read_csv('c:/github/my_dsci_401/data/AmesHousingSetB.csv')

del data_a['PID']
del data_b['PID']

data_ax = data_a[list(data_a)[:-1]]
data_bx = data_b[list(data_b)[:-1]]

data_ay = data_a['SalePrice']
data_by = data_b['SalePrice']

data_ax = pd.get_dummies(data_ax)
data_bx = pd.get_dummies(data_bx)

imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
data_ax = imp.fit_transform(data_ax)
data_bx = imp.fit_transform(data_bx)

ax_train, ax_test, ay_train, ay_test = train_test_split(data_ax, data_ay, test_size = .2, random_state = 4)
linear_mod = linear_model.LinearRegression()
linear_mod.fit(ax_train, ay_train)
linear_preds = linear_mod.predict(ax_test)
print('Base linear model error measures:')
print('R2S: ' + str(r2_score(ay_test, linear_preds)))
print('EVS: ' + str(explained_variance_score(ay_test, linear_preds)))

lasso_mod = linear_model.Lasso(alpha = 5, normalize=True, fit_intercept=True)
lasso_mod.fit(ax_train, ay_train)
lasso_preds = lasso_mod.predict(ax_test)
print('Lasso model error measures with alpha: ' + str(5))
print('R2S: ' + str(r2_score(ay_test, lasso_preds)))
print('EVS: ' + str(explained_variance_score(ay_test, lasso_preds)))
print('')

lasso_preds_real = lasso_mod.predict(data_bx)
print('Lasso model error measures with alpha 8 on real data')
print('R2S: ' + str(r2_score(data_by, lasso_preds_real)))
print('EVS: ' + str(explained_variance_score(data_by, lasso_preds_real)))
print('')

