from setuptools import setup, find_packages

PACKAGE = "RB-CustomReports"
VERSION = "0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""Custom Reports extension for Review Board""",
    author="Raja Venkataraman",
    packages=["rbcustomreports"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbcustomreports.extension:CustomReportsExtension' % PACKAGE,
    },
    package_data={
        'rbcustomreports': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/rbcustomreports/*.html',
            'templates/rbcustomreports/*.txt',
        ],
    }
)
