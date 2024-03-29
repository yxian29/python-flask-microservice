import logging

import connexion
from connexion.resolver import RestyResolver

from flask_testing import TestCase
from server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', resolver=RestyResolver('server.controllers'))
        return app.app
