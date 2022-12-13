from fastapi import FastAPI
from classes import ModeloAPI, EntradaModelo, SalidaModelo
from typing import List

app = FastAPI(title="API de ejemplo Diplomado :)",
              version="1.42.69")
"""Esto sería documentar el objeto API :D"""

@app.post("/predecir", response_model=List[SalidaModelo],
          tags=[":v Del API Diplo"])

async def predecir_probabilidad(entradas: List[EntradaModelo]):
    '''
    Endpoint de la API encargado de predecir la probabilidad de dejar la organización
    '''
    respuesta = list()
    for entrada in entradas:
        modelo = ModeloAPI(
            entrada.satisfaction_level,
            entrada.number_project,
            entrada.dept)
        respuesta.append(modelo.predecir()[0])
    return respuesta




