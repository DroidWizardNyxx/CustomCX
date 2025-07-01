import os
from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Inicializa a aplicação Flask
app = Flask(__name__)

# Obtém as credenciais das variáveis de ambiente (mais seguro!)
API_KEY = os.environ.get('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.environ.get('SEARCH_ENGINE_ID')

# Validação inicial para garantir que as credenciais foram configuradas no ambiente
if not API_KEY or not SEARCH_ENGINE_ID:
    raise RuntimeError("As variáveis de ambiente GOOGLE_API_KEY e SEARCH_ENGINE_ID devem ser definidas.")

# Cria o endpoint /search
@app.route('/search', methods=['GET'])
def search():
    # Pega o parâmetro 'q' da URL (ex: /search?q=python)
    query = request.args.get('q')

    if not query:
        return jsonify({"error": "O parâmetro de busca 'q' é obrigatório."}), 400

    try:
        # Constrói o serviço da API do Google Custom Search
        service = build("customsearch", "v1", developerKey=API_KEY)
        
        # Executa a busca
        result = service.cse().list(
            q=query,
            cx=SEARCH_ENGINE_ID,
            # Você pode adicionar mais parâmetros aqui, como num=10 para 10 resultados
            # https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
        ).execute()

        # Retorna os resultados em formato JSON
        return jsonify(result)

    except HttpError as e:
        # Trata erros da API do Google (ex: cota excedida)
        return jsonify({"error": f"Ocorreu um erro na API do Google: {e}"}), e.resp.status
    except Exception as e:
        # Trata outros erros inesperados
        return jsonify({"error": f"Ocorreu um erro interno: {str(e)}"}), 500

# Rota principal apenas para teste
@app.route('/')
def index():
    return "API de busca está no ar! Use o endpoint /search?q=sua_busca"

# O Gunicorn usará o objeto 'app', então não precisamos de __main__ para o deploy
# Mas é útil para testes locais:
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)