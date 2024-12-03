from transformers import T5Tokenizer, T5ForConditionalGeneration

# Cargar el modelo y tokenizer
model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Texto de entrada con ejemplos
texto_completo = """
Ejemplo:
4 años, 1.22, Guanajuato, Positivo en piro, 25k
Respuestas de ejemplo:
¿Que edad tiene?: 4 años,
¿Altura del caballo (ejemplo 1.5)?: 1.22
¿Precio en k euros (miles de euros)?: 25k
¿Conoces alguna información general?: Positivo en piro
¿Conoces la ciudad?: Guanajuato

Ahora responde para el siguiente texto:
"11 años, Nivel san Jorge 1.62 Libre de piro,70k"
¿Cual es la edad?
¿Altura del caballo en metros (ejemplo 1,5)?
¿Precio en k euros (miles de euros)?
¿Conoces alguna información general?
¿Conoces la ciudad?
"""

# Tokenizar el texto de entrada
inputs = tokenizer(texto_completo, return_tensors="pt", max_length=512, truncation=True)

# Generar la respuesta
outputs = model.generate(inputs["input_ids"], max_length=512, num_beams=5, early_stopping=True)

# Decodificar la salida
respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Respuesta generada:", respuesta)
