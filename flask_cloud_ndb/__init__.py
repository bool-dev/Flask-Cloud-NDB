"""
Flask Cloud NDB
-------------

Adds Google Cloud NDB support to Flask
"""

import os

from google.auth._default import _load_credentials_from_file
from google.cloud import ndb


__version__ = "0.2.0"


def ndb_wsgi_middleware(wsgi_app, client=None):
    """
    Simple middleware to add the client into the app context
    """
    if client is None:
        client = ndb.Client()

    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware


class CloudNDB(object):

    """This class is used to control the CloudNDB integration to one
    or more Flask applications.
    """

    def __init__(self, app=None, client=None):

        self.client = client
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        # defaults for the configuration
        app.config.setdefault("NDB_PROJECT", None)
        app.config.setdefault("NDB_NAMESPACE", None)
        app.config.setdefault("NDB_GOOGLE_APPLICATION_CREDENTIALS", None)
        app.config.setdefault("NDB_LOCAL_EMULATOR", False)
        app.config.setdefault("NDB_DATASTORE_DATASET", "")
        app.config.setdefault("NDB_DATASTORE_EMULATOR_HOST", "")
        app.config.setdefault("NDB_DATASTORE_EMULATOR_HOST_PATH", "")
        app.config.setdefault("NDB_DATASTORE_HOST", "")
        app.config.setdefault(
            "NDB_DATASTORE_PROJECT_ID", app.config["NDB_PROJECT"])

        if not self.client:
            # setup the client
            project = app.config["NDB_PROJECT"]
            namespace = app.config["NDB_NAMESPACE"]
            credentials_file = app.config["NDB_GOOGLE_APPLICATION_CREDENTIALS"]
            if credentials_file:
                # call google auth helper to initialise credentials
                credentials, project_id = _load_credentials_from_file(
                    credentials_file)
            else:
                # default credentials, OR load from env, through underlying
                # lib
                credentials = None

            # if local emulator, set the environ as required by underlying
            # google cloud ndb and related libraries
            if app.config["NDB_LOCAL_EMULATOR"]:
                os.environ["DATASTORE_DATASET"] = app.config[
                    "NDB_DATASTORE_DATASET"]
                os.environ["DATASTORE_EMULATOR_HOST"] = app.config[
                    "NDB_DATASTORE_EMULATOR_HOST"]
                os.environ["DATASTORE_EMULATOR_HOST_PATH"] = app.config[
                    "NDB_DATASTORE_EMULATOR_HOST_PATH"]
                os.environ["DATASTORE_HOST"] = app.config[
                    "NDB_DATASTORE_HOST"]
                os.environ["DATASTORE_PROJECT_ID"] = app.config[
                    "NDB_DATASTORE_PROJECT_ID"]
                credentials = None

            self.client = ndb.Client(
                project=project, namespace=namespace, credentials=credentials)

        app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app, client=self.client)

    def context(self):
        """Simple wrapper around the context from google cloud ndb client
        """
        if not self.client:
            raise Exception('No client connection configured')

        return self.client.context()
