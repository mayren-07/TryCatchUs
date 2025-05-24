from difflib import SequenceMatcher
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('GOOGLE_FACT_CHECK_API_KEY')

def similaridade(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def verificar_afirmacao(afirmacao):
    url = 'https://factchecktools.googleapis.com/v1alpha1/claims:search'

    params = {
        'query': afirmacao,
        'languageCode': 'pt-BR',
        'key': API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        claims = data.get('claims', [])

        encontrou_relacionado = False

        for claim in claims:
            texto_claim = claim.get('text', '')
            print(texto_claim)
            score = similaridade(afirmacao, texto_claim)
            print(f"Similaridade: {score:.2f}")

            if score >= 0.6:
                encontrou_relacionado = True
                break

        if encontrou_relacionado:
            print("\033[31m🔴 FALSO\033[0m")
            return "Falso"
        else:
            print("\033[33m🟡 Essa afirmação passará por uma curadoria humana para verificação.\033[0m")
            return "Curadoria"
    else:
        print("Erro na API:", response.status_code, response.text)

if __name__ == "__main__":
    while True:
        prompt_color = "\033[32m>\033[0m "
        afirmacao = input(f"\nDigite a afirmação que deseja verificar (ou 'sair' para encerrar):\n{prompt_color}")

        if afirmacao.lower() == 'sair':
            print("Encerrando o verificador. Até mais!")
            break

        verificar_afirmacao(afirmacao)
