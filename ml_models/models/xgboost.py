from xgboost import XGBClassifier
import pickle


class XGBoost():
    """
    Class for the XGBoost classifier. 
    
    A wrapper for the xgboost implemenation.
    """
    
    def __init__(self, max_depth=30, n_estimators=200, learning_rate=0.1,
                 save_model=False, use_saved_model=False, model_path='./models/saved_models/xgboost.pickle'):
        self.model_path = model_path
        self.save_model = save_model
        
        if use_saved_model:
            with open(self.model_path, 'rb') as file:
                self.model = pickle.load(file)
        else:
            self.model = xgboost = XGBClassifier(max_depth=max_depth, n_estimators=n_estimators, learning_rate=learning_rate)  
    
    
    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        
        if self.save_model:
            with open(self.model_path, 'wb') as handle:
                pickle.dump(self.model, handle)
    
    
    def predict(self, X_test):
        return self.model.predict(X_test)