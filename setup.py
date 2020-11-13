from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='calculate-priority-activities',
      version='1.0.4',      
      description='This script prints a file with the activities with their priority in the root directory',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 5 - Production/Stable'
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
      ],
      url='calculate-priority-activities',
      author='Alessandro Puzielli aka Alepuzio',
      author_email='alessandro.puzielli@alepuzio.net',
      license='GPL 3',
      packages=['src'],
      install_requires=[
          'markdown',
      ],
      entry_points={
          'console_scripts': ['calculate-priority-activities=main'],
      },
      include_package_data=True,
      url='http://github.com/alepuzio/calculate-priority-activities',
      zip_safe=False)
