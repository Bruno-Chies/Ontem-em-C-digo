from google import genai
# Certifique-se de que a chave está inteira e dentro das aspas duplas
client = genai.Client(api_key="")
resposta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Olá!",)