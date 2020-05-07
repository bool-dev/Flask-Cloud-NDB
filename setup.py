"""Flask Cloud NDB: Adds Google Cloud NDB support to Flask"""

import re
from setuptools import setup


with open('flask_cloud_ndb/__init__.py', 'r') as f:
    version = re.search(
        r'__version__ = \"(.*?)\"', f.read(), re.MULTILINE).group(1)


setup(
    name='Flask-Cloud-NDB',
    version=version,
    url='https://github.com/bool-dev/flask-cloud-ndb',
    project_urls={
        'Documentation': 'https://github.com/bool-dev/flask-cloud-ndb',
        'Code': 'https://github.com/bool-dev/flask-cloud-ndb',
        'Issue tracker': 'https://github.com/bool-dev/flask-cloud-ndb/issues',
    },
    license='MIT',
    author='Rituraj Dowerah',
    author_email='bool.dev@gmail.com',
    maintainer='Rituraj Dowerah',
    maintainer_email='bool.dev@gmail.com',
    description=__doc__,
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    python_requires='>= 3.0, != 3.0.*, != 3.1.*, != 3.2.*, != 3.3.*',
    packages=['flask_cloud_ndb'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['Flask>=1.1.2', 'google-cloud-ndb>=1.2.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
