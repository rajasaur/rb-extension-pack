from setuptools import setup, find_packages

PACKAGE="RB-RSSFeeds"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""RSS Feed extension for Review Board""",
    author="Dolanor Tharivae, Raja Venkataraman",
    packages=["rbrssfeeds"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbrssfeeds.extension:RSSExtension' % PACKAGE,
    },
    package_data={
        'rbrssfeeds': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/rbrssfeeds/*.html',
            'templates/rbrssfeeds/*.txt',
        ],
    }
)
