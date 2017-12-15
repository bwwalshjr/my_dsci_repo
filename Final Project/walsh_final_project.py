from data_util import *
#import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import f_regression  	#~5% drop in r2 score with feature selections tested
from sklearn.model_selection import train_test_split

data = pd.read_csv('./data/champion_data.csv')

le = LabelEncoder()
data = data.apply(LabelEncoder().fit_transform)
del data['Rank'] 
del data['Position Change']
del data['Champion']

#sm = pd.plotting.scatter_matrix(data, diagonal='kde')
#plt.show()

features = list(data)
features.remove('Win Percent')

data_x = data[features]
data_y = data['Win Percent']

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = .3, random_state = 1)

#selector_f = SelectKBest(f_regression, k=12)
#selector_f.fit(x_train, y_train)
#xt_train, xt_test = selector_f.transform(x_train), selector_f.transform(x_test) 

#linear_mod = linear_model.LinearRegression()
#linear_mod.fit(x_train, y_train)
#preds = linear_mod.predict(x_test)
#linear_r2 = r2_score(y_test, preds) 
#print("Linear R2: " + str(linear_r2))

param_grid = {'alpha':[0.1, 0.25, 0.5, 1.0, 2.5, 5.0], 'normalize':[True, False], 'fit_intercept':[True, False]}
optimized_lasso = GridSearchCV(linear_model.Lasso(), param_grid, cv=5, scoring='r2')
optimized_lasso.fit(x_train, y_train)
lasso_r2 = optimized_lasso.score(x_test, y_test) 
print("Lasso R2: " + str(lasso_r2))

#rfr_mod = RandomForestRegressor(n_estimators=100)
#rfr_mod.fit(x_train, y_train)
#preds = rfr_mod.predict(x_test)
#rfr_r2 = r2_score(preds, y_test)
#print("RFR R2: " + str(rfr_r2))


