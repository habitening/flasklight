"""A simple Python 3 Flask application to dump the containing environment."""

import json
import logging
import os

import flask

# The root logger is created with level WARNING
# To see less severe messages we have to set the level
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

def echo(request):
    """Dump various dictionaries to the response."""
    parameters = {
        'Environment variables': dict(os.environ),
        'Headers': dict(request.headers),
        'Properties': {
            'path': request.path,
            'full_path': request.full_path,
            'script_root': request.script_root,
            'url': request.url,
            'base_url': request.base_url,
            'url_root': request.url_root,
            'method': request.method,
            'referrer': request.referrer,
            'remote_addr': request.remote_addr,
            'scheme': request.scheme
        },
        'Parameters': request.values.to_dict(False)
    }
    logging.info(json.dumps(parameters, separators=(',', ':'), sort_keys=True))
    return flask.jsonify(parameters)

def echo_view():
    """Call echo() with the Flask request."""
    return echo(flask.request)

app = flask.Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.add_url_rule('/', 'echo', echo_view)
