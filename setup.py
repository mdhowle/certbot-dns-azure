from setuptools import find_packages
from setuptools import setup

version = '2.1.0'

# azure-mgmt-dns is still the old style SDK, so will change dramatically
# when they refactor, most notably the credential parts
install_requires = [
    'azure-identity>=1.11.0',
    'azure-mgmt-dns>=8.0.0',
    'setuptools>=41.6.0',
    'certbot>=2.0,<3.0'
]

with open("README.md") as f:
    long_description = f.read()

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='certbot-dns-azure',
    version=version,
    description="Azure DNS Authenticator plugin for Certbot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/binkhq/certbot-dns-azure',
    author="Terry Cain",
    author_email='opensource@bink.com',
    license='Apache License 2.0',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-azure = certbot_dns_azure._internal.dns_azure:Authenticator',
        ],
    },
)
