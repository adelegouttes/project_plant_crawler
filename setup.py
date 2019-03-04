from setuptools import setup

REQUIREMENTS = [
      'requests==2.21.0',
      'beautifulsoup4==4.7.1',
      'flask==1.0.2',
      'sqlalchemy==1.2.18',
      'pytest==4.3.0',
]

setup(name='project_plant_crawler',
      version='0.1',
      description='Organise your vegetable garden',
      url='https://github.com/adelegouttes/project_plant_crawler',
      author='Adele Gouttes',
      install_requires=REQUIREMENTS,
      )