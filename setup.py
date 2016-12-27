from distutils.core import setup
setup(
  name = 'pymvrd',
  packages = ['pymvrd'],
  version = '0.1',
  description = 'Motor Vehicle Registration Information Search Portal Library',
  author = 'Obi Uchenna David',
  author_email = 'daviduchenna@outlook.com',
  url = 'https://github.com/othreecodes/pymvrd', 
  download_url = 'https://github.com/othreecodes/pymvrd/tarball/0.1', 
  keywords = ['vehicle','plate number','registration'], 
  classifiers = [],
    install_requires=[
        'requests',
        'bs4',
    ],
)
