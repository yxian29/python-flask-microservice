import connexion
from connexion.resolver import RestyResolver

from server import encoder

app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Python Flask Micro-service Demo'},
            resolver=RestyResolver('server.controllers'))