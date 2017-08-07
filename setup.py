from setuptools import setup, find_packages
from codecs import open
from os import path, system
import sys
import subprocess
from setuptools.command.install import install
import pkgutil

__version__ = '0.0.6'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')


class XPDFInstall(install):
    def run(self):
        try:
            if path.isfile('/usr/local/bin/pdftotext'):
                print("Detected xpdf library.")
            else:
                print("Did not detect xpdf library. Now attempting to install...")
                if sys.platform.startswith('linux'):
                    bash_script = 'linux_install.sh'
                    bash_instructions = "sh -c cd /tmp/ && wget ftp://ftp.foolabs.com/pub/xpdf/xpdfbin-linux-3.04.tar.gz && tar -xvzf xpdfbin-linux-3.04.tar.gz && cp xpdfbin-linux-3.04/bin64/* /usr/local/bin && cp xpdfbin-linux-3.04/doc/sample-xpdfrc /usr/local/etc/xpdfrc"
                elif sys.platform.startswith('darwin'):
                    bash_script = 'mac_install.sh'
                    bash_instructions = "cd /tmp/ && wget ftp://ftp.foolabs.com/pub/xpdf/xpdfbin-mac-3.04.tar.gz && tar -xvzf xpdfbin-mac-3.04.tar.gz && cp xpdfbin-mac-3.04/bin64/* /usr/local/bin && cp xpdfbin-mac-3.04/doc/sample-xpdfrc /usr/local/etc/xpdfrc"

                # subprocess.call([bash_instructions])
                system(bash_instructions)
        except Exception as e:
            print(e)
            print("Error installing xpdf.  Please follow custom installation instructions at: https://github.com/ecatkins/xpdf_python.")
        else:
            install.run(self)

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='xpdf_python',
    version=__version__,
    description='Python wrapper for xpdf',
    long_description=long_description,
    url='https://github.com/ecatkins/xpdf_python',
    download_url='https://github.com/ecatkins/xpdf_python/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Edward Atkins',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='ecatkins@gmail.com',
    #run custom code
    package_data = {
        'install_xpdf':['install_xpdf/mac_install.sh','install_xpdf/linux_install.sh']
    },
    cmdclass={'install': XPDFInstall},
)


