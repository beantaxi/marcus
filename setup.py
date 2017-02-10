import setuptools


setuptools.setup(name='marcus1',
                 description='A nice little library and pet project.',
                 keywords='python kernel utility',
                 version='0.0.1',
                 url='https://github.com/beantaxi/marcus',
                 author='Chris Lalos',
                 author_email='chris.lalos@gmail.com',
#                 install_requires=[],
                 packages=setuptools.find_packages('src'),
                 package_dir={'': 'src'}
                )
                
