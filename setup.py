from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
      author='Alessandro Puzielli aka Alepuzio',
      author_email='alessandro.puzielli@alepuzio.net',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GPL 3 License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
      ],
      description='This script prints a file with the activities with their priority in the root directory',
      entry_points={
          'console_scripts': ['activities=funniest.command_line:main'],
      },
      include_package_data=True,
      install_requires=[
          'markdown',
      ],
      license='GPL 3',
	  long_description=readme(),
      name='calculate-priority-activities',
      packages=setuptools.find_packages(),
      script=['calculate-priority-activities'],
      url='http://github.com/alepuzio/calculate-priority-activities',
      version='0.1',      
      zip_safe=False)

