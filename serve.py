from waitress import serve
from juros import app  # Assumindo que 'juros' é o nome do módulo e 'app' é a instância da aplicação

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
