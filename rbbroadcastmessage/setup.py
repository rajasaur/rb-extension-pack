from setuptools import setup


PACKAGE = "RB-BroadcastMessage"
VERSION = "0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="Broadcast Message for ReviewBoard",
    author="Raja Venkataraman",
    packages=["rbbroadcastmessage"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbbroadcastmessage.extension:BroadcastMessageExtension' % (
        PACKAGE),
    },
    package_data={
        'rbbroadcastmessage': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templatetags/*.py',
            'templates/rbbroadcastmessage/*.txt',
            'templates/rbbroadcastmessage/*.html',
        ],
    }
)
