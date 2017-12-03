execfile('imports.py')

def test_alphas(data_x, data_y, test_split=.2, norm = True, fit = True):
    x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = test_split)
    
    alphas = [.001, .01, .1, .25, .5, 1, 5, 10, 50, 100]
    best_alpha = -1
    best_r2 = 0

    for a in alphas:
        lasso_mod = linear_model.Lasso(alpha = a, normalize = norm, fit_intercept = fit)
        lasso_mod.fit(x_train, y_train)
        preds = lasso_mod.predict(x_test)
        r2 = r2_score(y_test, preds)
        if r2 > best_r2:
            best_alpha = a
            best_r2 = r2
    
    values = {"alpha":best_alpha, "r2":best_r2}
    return values
