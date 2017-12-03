from data_util import *
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

data = pd.read_csv('./data/champion_data.csv')

le = LabelEncoder()
data = data.apply(LabelEncoder().fit_transform)

features = list(data)

features.remove('Rank')
features.remove('Position Change')
features.remove('Champion')

features.remove('Win Percent')

data_x = data[features]
data_y = data['Win Percent']

#5 = .495, 6 = .518, 7 = .5427, 1 = .59
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = .3, random_state = 0)

linear_mod = linear_model.LinearRegression()
linear_mod.fit(x_train, y_train)
preds = linear_mod.predict(x_test)

print(str(r2_score(y_test, preds))) #.42597

#alphas = [0.0, 0.01, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0] #.01 best w/ .43304
alphas = [.01]
for a in alphas:
	lasso_mod = linear_model.Lasso(alpha=a, normalize=True, fit_intercept=True)
	lasso_mod.fit(x_train, y_train)
	preds = lasso_mod.predict(x_test)
	print('R^2 (Lasso Model with alpha=' + str(a) + '): ' + str(r2_score(y_test, preds)))