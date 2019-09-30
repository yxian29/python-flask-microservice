import connexion
from connexion.resolver import RestyResolver

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='spec/')
    app.add_api('openapi.yaml',
                arguments={'title': 'demo'},
                resolver=RestyResolver('api'))
    app.run(port=9090)