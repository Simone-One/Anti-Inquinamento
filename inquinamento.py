import ollama

client = ollama.Client()
model = "gemma3:4b"

def consiglio(rifiuto):
    system_prompt = """- Sei una persona esperta nella raccolta differenziata. 
- Rispondi sempre in meno di 20 parole (un semplice messaggio).
- Stai parlando a un adolescente, quindi utilizza un linguaggio da coetaneo.
- Rispondi in formato Markdown."""
    user_prompt = f"""Dove dovrei buttare questo rifiuto?: {rifiuto}"""
    messages = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': user_prompt}
    ]
    risposta = client.chat(model=model, messages=messages, options={'temperature': 0.7})['message']['content']
    return risposta