from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRFRegressor
from sklearn.base import BaseEstimator, RegressorMixin

class XGBRFRegressorWrapper(BaseEstimator, RegressorMixin):
    def __init__(self, **params):
        self.params = params
        self.model = XGBRFRegressor(**params)

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict(self, X):
        return self.model.predict(X)

    def __sklearn_tags__(self):
        return self.model.__sklearn_tags__() if hasattr(self.model, "__sklearn_tags__") else {}

def xgbmodel_build(params):
    column_transformation = ColumnTransformer(
        transformers=[
            ('One_hot_encoding', OneHotEncoder(drop='first', sparse_output=True), [0, 1]),
            ('Standard Scaler', StandardScaler(), [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        ]
    )
    
    xgb_pipeline = Pipeline(
        steps=[
            ('column transformation', column_transformation),
            ('XGBRFRegressor', XGBRFRegressorWrapper(**params))
        ]
    )
    
    return xgb_pipeline
