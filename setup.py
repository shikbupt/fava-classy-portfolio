from os import path
from setuptools import find_packages, setup

with open(path.join(path.dirname(__file__), 'readme.md')) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='fava_classy_portfolio',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Fava Extension for viewing your financial portfolio kept in a Beancount plaintext accounting ledger.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/shikbupt/fava_classy_portfolio.git',
    author='sk',
    author_email='shikbupt@gmail.com',
    license='GPL-3.0',
    keywords='fava beancount accounting investment',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beancount>=2.3.2',
        'fava>=1.19',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Financial :: Investment',
    ],
)
