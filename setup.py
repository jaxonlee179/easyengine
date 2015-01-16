
from setuptools import setup, find_packages
import sys
import os
import glob

conf = []
templates = []

long_description = '''EasyEngine is the commandline tool to manage your
                      Websites based on WordPress and NGINX with easy to use
                      commands'''

for name in glob.glob('config/plugins.d/*.conf'):
    conf.insert(1, name)

for name in glob.glob('ee/cli/templates/*.mustache'):
    templates.insert(1, name)

if not os.path.exists('/var/log/ee/'):
    os.makedirs('/var/log/ee/')

if not os.path.exists('/var/lib/ee/'):
    os.makedirs('/var/lib/ee/')

setup(name='ee',
      version='3.0',
      description=long_description,
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='rtCamp Soultions Pvt. LTD',
      author_email='sys@rtcamp.com',
      url='http://rtcamp.com/easyengine',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests',
                                      'templates']),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=[
          # Required to build documentation
          # "Sphinx >= 1.0",
          # Required for testing
          # "nose",
          # "coverage",
          # Required to function
          'cement == 2.4',
          'pystache',
          'python-apt',
          'pynginxconfig',
          'pymysql3 == 0.4',
          'psutil',
          'sh',
          'sqlalchemy',
          ],
      data_files=[('/etc/ee', ['config/ee.conf']),
                  ('/etc/ee/plugins.d', conf),
                  ('/usr/lib/ee/templates', templates)],
      setup_requires=[],
      entry_points="""
          [console_scripts]
          ee = ee.cli.main:main
      """,
      namespace_packages=[],
      )
