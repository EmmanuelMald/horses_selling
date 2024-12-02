from transformers import pipeline

# Texto de entrada
texto = "Caballo de la raza x, color café, ojos azules, pero creo que tiene una mancha morada en el lomo."

# Crear un pipeline de question-answering
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Definir preguntas para extraer información relevante
preguntas = [
    {"question": "¿Qué especie es?", "context": texto},
    {"question": "¿Cuál es la raza?", "context": texto},
    {"question": "¿De qué color es?", "context": texto},
    {"question": "¿De qué color son los ojos?", "context": texto},
    {"question": "¿Hay algún detalle adicional?", "context": texto},
]

# Extraer respuestas
respuestas = [qa_pipeline(p)["answer"] for p in preguntas]

# Estructurar datos en un diccionario
datos = {
    "Especie": [respuestas[0]],
    "Raza": [respuestas[1]],
    "Color": [respuestas[2]],
    "Ojos": [respuestas[3]],
    "Detalle extra": [respuestas[4]],
}

# Mostrar los datos estructurados
import pandas as pd
df = pd.DataFrame(datos)
print(df)
print(datos)
# Guardar como archivo Excel
df.to_excel("caballo_detalles.xlsx", index=False)
