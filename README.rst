Flask-Cloud-NDB
================

Flask-Cloud-NDB is an extension for `Flask`_ that adds support for
`Google Cloud NDB`_ to your application.


Installing
----------

Install and update using `pip`_:

.. code-block:: text

  $ pip install -U Flask-Cloud-NDB


A Simple Example
----------------

.. code-block:: python

    from flask import Flask
    from google.cloud import ndb
    from flask_cloud_ndb import CloudNDB

    app = Flask(__name__)
    cloud_ndb = CloudNDB(app)


    class Note(ndb.Model):
        title = ndb.StringProperty()
        content = ndb.StringProperty()
        created_at = ndb.DateTimeProperty()


    @app.route('/')
    def index():
        Note(
            title="Flask Cloud NDB with request",
            content="This is an extension, and here is an example"
            " of how to use within a request").put()

        notes = Note.query().fetch()

        return notes[0].title


    # we can also simply use the context wrapper:
    with cloud_ndb.context():
        Note(
            title="Flask Cloud NDB without request",
            content="This is an extension, and here is an example "
            "of how to use without request").put()
        notes = Note.query().fetch()
        print(notes[0].title)


    if __name__ == '__main__':
        app.run()


Configuration Options
---------------------

By default the extension will run by itself in the cloud, without any additional configurations, using the default app engine credentials.


TODOS
----------------

-   Add full configuration options description in readme
-   Add black formatting
-   Add more links to readme
-   Add more documentation to code
-   Add changes file
-   Complete manifest.in file
-   Complete setup.cfg file
-   Add tests!!
-   Add coverage
-   Build distribution for pypi


Links
-----

-   Code: https://github.com/bool-dev/flask-cloud-ndb
-   Issue tracker: https://github.com/bool-dev/flask-cloud-ndb/issues

.. _Flask: https://palletsprojects.com/p/flask/
.. _Google Cloud NDB: https://pypi.org/project/google-cloud-ndb/
.. _pip: https://pip.pypa.io/en/stable/quickstart/