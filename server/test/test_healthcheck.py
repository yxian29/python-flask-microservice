# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from server.models.inline_response200 import InlineResponse200  # noqa: E501
from server.test import BaseTestCase


class TestHealthcheckController(BaseTestCase):
    """HealthcheckController integration test stubs"""

    def test_healthcheck_get(self):
        """Test case for healthcheck_get

        Health Check
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/healthcheck',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
