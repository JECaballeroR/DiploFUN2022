from pydantic import BaseModel as BM
from pydantic import Field
from typing import Literal
import joblib
import pandas as pd


class EntradaModelo(BM):
    '''
    Esta es la clase que define las entradas del modelo
    '''
    satisfaction_level: float = Field(ge=0, le=1)
    number_project: int = Field(ge=2, le=7)
    dept: Literal['sales', 'accounting', 'hr', 'technical', 'support', 'management',
       'IT', 'product_mng', 'marketing', 'RandD']
    class Config:
        schema_extra = {
            "example":{
                "satisfaction_level": 0.69,
                "number_project": 3 ,
                "dept": 'sales',

            }
        }

class SalidaModelo(BM):
    '''
    Clase que controla que la salida si tenga sentido
    '''
    left : float= Field(ge=0, le=1)
    class Config:
        schema_extra = {
            "example":{
                "left": 0.42
            }
        }

class ModeloAPI:
    def __init__(
            self,
            satisfaction_level,
            number_project,
            dept):

        self.satisfaction_level = satisfaction_level
        self.number_project = number_project
        self.dept = dept

    def _cargar_modelo(self):
        self.modelo = joblib.load("logisticaAPI.pkl")


    def _preprocesar_datos(self):
        satisfaction_level = self.satisfaction_level
        number_project = self.number_project
        dept = self.dept
        sales_vals = [
            "dept_RandD",
            "dept_accounting",
            "dept_hr",
            "dept_management",
            "dept_marketing",
            "dept_product_mng",
            "dept_sales",
            "dept_support",
            "dept_technical",
        ]
        dept_binarios = [int(f'dept_{dept}' == x) for x in sales_vals]
        X_val = pd.DataFrame(
            data=[
                [
                    satisfaction_level,
                    number_project,
                    *dept_binarios,
                ]
            ],
            # columnas del X_train
            columns=[
                "satisfaction_level",
                "number_project",
                "dept_RandD",
                "dept_accounting",
                "dept_hr",
                "dept_management",
                "dept_marketing",
                "dept_product_mng",
                "dept_sales",
                "dept_support",
                "dept_technical",
            ],
        )
        return X_val

    def predecir(self):
        self._cargar_modelo()
        x = self._preprocesar_datos()
        y_pred = pd.DataFrame(
            self.modelo.predict_proba(x)[:,1]
        ).rename(columns={0:'left'})
        return y_pred.to_dict(orient='records')