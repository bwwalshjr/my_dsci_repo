import pandas as pd
from data_util import *
from sklearn import svm
from sklearn import tree
from sklearn import ensemble
from sklearn import neighbors
from sklearn import naive_bayes
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

data = pd.read_csv('./data/churn_data.csv')
validation_data = pd.read_csv('./data/churn_validation.csv')

features = list(data)
validation_features = list(validation_data)

features.remove('CustID')
features.remove('Churn')
validation_features.remove('CustID')
validation_features.remove('Churn')

data_x = data[features]
data_y = data['Churn']
validation_data_x = validation_data[validation_features]
validation_data_y = validation_data['Churn']

data_x = pd.get_dummies(data_x)
validation_data_x = pd.get_dummies(validation_data_x)

le = LabelEncoder()
data_y = le.fit_transform(data_y)
validation_data_y = le.fit_transform(validation_data_y)

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = .3, random_state = 4)

#Logistic Regression: Accuracy: .74, Precision .76
log_mod = linear_model.LogisticRegression()
log_mod.fit(x_train, y_train)
preds = log_mod.predict(x_test)
best_f1_log = f1_score(y_test, preds)
#print("Logistic Regression Model")
#print_multiclass_classif_error_report(y_test, preds)

#K Nearest Neighbors with k = 16: Accuracy: .67, Precision: .67
ks = [2,4,6,8,10,12,14,16,18,20]
best_f1_knn = 0
best_k = 0
for k in ks:
	knn_mod = neighbors.KNeighborsClassifier(n_neighbors = k)
	knn_mod.fit(x_train, y_train)
	preds = knn_mod.predict(x_test)
	this_f1 = f1_score(y_test, preds)
	if (this_f1 > best_f1_knn):
		best_f1_knn = this_f1
		best_k = k

#Random forest with n_est = 50 and depth = NA and criterion = gini: Accuracy: .87, Precision: .90
n_est = [5, 10, 50, 100]
depth = [3,6,None]
criteria = ['entropy', 'gini']
best_f1_rf = 0
best_n_rf = 0
best_depth = 0
best_criterion_rf = ''
for n in n_est:
	for dp in depth:
		for my_criterion in criteria:
			rf_mod = ensemble.RandomForestClassifier(criterion=my_criterion, n_estimators=n, max_depth = dp)
			rf_mod.fit(x_train, y_train)
			preds = rf_mod.predict(x_test)
			this_f1 = f1_score(y_test, preds)
			if (this_f1 > best_f1_rf):
				best_f1_rf = this_f1
				best_n_rf = n
				best_depth = dp
				best_criterion_rf = my_criterion
#			print("Random Forest with n_estimators: " + str(n) + " and depth: " + str(dp))
#			print_multiclass_classif_error_report(y_test, preds)

#Support Vector Machine classifier with c = 10: Accuracy: .59, Precision: .65
cs = [.2, .5, 1, 2, 5, 10]
best_f1_svm = 0
best_c = 0
for c in cs:
	svm_mod = svm.SVC(C=c)
	svm_mod.fit(x_train, y_train)
	preds = svm_mod.predict(x_test)
	this_f1 = f1_score(y_test, preds)
	if (this_f1 > best_f1_svm):
		best_f1_svm = this_f1
		best_c = c
#	print("SVM with c: " + str(c))
#	print_multiclass_classif_error_report(y_test, preds)

#Decision Tree with Gini criteria: Accuracy: .80, Precision: .83
criteria = ['gini', 'entropy']
best_f1_dtree = 0
best_criterion_dtree = ''
for my_criteria in criteria:
	dtree_mod = tree.DecisionTreeClassifier(criterion=my_criteria)
	dtree_mod.fit(x_train, y_train)
	preds = dtree_mod.predict(x_test)
#	print("Decision tree with criteria: " + str(my_criteria))
#	print_multiclass_classif_error_report(y_test, preds)

#Gaussian Naive Bayes model: Accuracy: .69, Precision: .72
naive_bayes_mod = naive_bayes.GaussianNB()
naive_bayes_mod.fit(x_train, y_train)
preds = naive_bayes_mod.predict(x_test)
best_f1_naive_bayes = f1_score(preds, y_test)
#print("Gaussian Naive Bayes Model")
#print_multiclass_classif_error_report(y_test, preds)

models = {}
models['log_mod'] = log_mod
models['knn'] = knn_mod
models['rf_mod'] = rf_mod
models['svm_mod'] = svm_mod
models['dtree_mod'] = dtree_mod
models['naive_bayes_mod'] = naive_bayes_mod

f1_scores = {}
f1_scores['log_mod'] = best_f1_log
f1_scores['knn'] = best_f1_knn
f1_scores['rf_mod'] = best_f1_rf
f1_scores['svm_mod'] = best_f1_svm
f1_scores['dtree_mod'] = best_f1_svm
f1_scores['naive_bayes_mod'] = best_f1_naive_bayes

best_k_fold_score = 0
best_k_fold_mod = ''
best_loo_score = 0
best_loo_mod = ''
best_ss_score = 0
best_ss_mod = ''

best_avg_score = 0
best_avg_mod = '' 

k_fold = KFold(n_splits = 5, random_state = 4)
loo = LeaveOneOut()
shuffle_split = ShuffleSplit(test_size = .2, train_size = .8, n_splits = 5)

for model_name, model_var in models.iteritems():
	k_fold_scores = cross_val_score(model_var, data_x, data_y, scoring = 'f1', cv = k_fold)
	k_fold_mean = k_fold_scores.mean()
	if k_fold_mean > best_k_fold_score:
		best_k_fold_score = k_fold_mean
		best_k_fold_mod = model_name
	#print('CV Scores (K-Fold) with ' + model_name + ': ' + str(k_fold_scores.mean()))

	loo_scores = cross_val_score(model_var, data_x, data_y, scoring = 'accuracy', cv = loo)
	loo_mean = loo_scores.mean()
	if loo_mean > best_loo_score:
		best_loo_score = loo_mean
		best_loo_mod = model_name
	#print('CV Scores (Leave One Out) with ' + model_name + ': ' + str(loo_scores.mean()))

	ss_scores = cross_val_score(model_var, data_x, data_y, scoring='f1', cv=shuffle_split)
	ss_mean = ss_scores.mean()
	if ss_mean > best_ss_score:
		best_ss_score = ss_mean
		best_ss_mod = model_name
	#print('CV Scores (Shuffle-Split) with ' + model_name + ': ' + str(ss_scores.mean()))
	
	total_mean = (k_fold_mean + loo_mean + ss_mean)/3
	if total_mean > best_avg_score:
		best_avg_score = total_mean
		best_avg_mod = model_name

#max_f1 = max(f1_scores, key=f1_scores.get)
#print("Best simple f1_score: " + str(max_f1) + " from the " + str(f1_scores[max_f1]) + " model")
#print("Best Cross validated f1 score: + " + str(best_avg_score) + " from the " + best_avg_mod + " model")

#for model_name, f1_value in f1_scores.iteritems():
#	print ("Model: " + model_name + ", F1 score: " + str(f1_value))

print("Best model: " + best_avg_mod)
optimal_model = models[best_avg_mod]

optimal_model.fit(data_x, data_y)
validation_preds = optimal_model.predict(validation_data_x)
#print_multiclass_classif_error_report(validation_preds, validation_data_y)
final_f1_score = f1_score(validation_preds, validation_data_y)
print('Final F1: ' + str(final_f1_score))


