import connexion
import six

from server.models.inline_response200 import InlineResponse200  # noqa: E501
from server import util


def search():
    """Health Check

    Retrieve information regarding service health # noqa: E501


    :rtype: InlineResponse200
    """
    response = InlineResponse200('success')
    return response