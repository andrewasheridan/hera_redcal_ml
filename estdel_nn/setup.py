from __future__ import absolute_import, print_function

from setuptools import setup, find_packages

import os, glob, numpy, subprocess

# ???: Where are all these print statements printed?
print("Generating estdel_nn/__version__.py: ", end='')
__version__ = open('VERSION').read().strip()
print(__version__)
open('estdel_nn/__version__.py','w').write('__version__="%s"'%__version__)

#read the latest git status out to an installed file
try:
    gitbranch = os.popen('git symbolic-ref -q HEAD').read().strip()
    print("Generating estdel_nn/__branch__.py")
    gitlog = os.popen('git log -n1 --pretty="%h%n%s%n--%n%an%n%ae%n%ai"').read().strip()
    print("Generating estdel_nn/__gitlog__.py.")
    print(gitlog)
except:
    gitbranch = "unknown branch"
    gitlog = "git log not found"
open('estdel_nn/__branch__.py','w').write('__branch__ = \"%s\"'%gitbranch)
open('estdel_nn/__gitlog__.py','w').write('__gitlog__ = \"\"\"%s\"\"\"'%gitlog)


def get_description():
    lines = [L.strip() for L in open('README.md').readlines()]
    d_start = None
    for cnt, L in enumerate(lines):
        if L.startswith('## Description'): d_start = cnt + 1
        elif not d_start is None:
            if len(L) == 0: return ' '.join(lines[d_start:cnt])
    raise RuntimeError('Bad README')

setup(name = 'estdel_nn',
      version = __version__,
      description = 'Neural networks creation and training for estimating interferometer anteanna delays',
      long_description = get_description(),
      url = 'https://github.com/andrewasheridan/hera_redcal_ml/estdel_nn',
      author = 'Andrew Sheridan',
      author_email = 'sheridan@berkeley.edu',
      license = 'MIT',
      package_dir = {'estdel_nn' : 'estdel_nn'},
      packages = find_packages(),
      install_requires = [
          'numpy>=1.2',
          'tensorflow>=1.8.0',
          'hera_cal',
          'pyuvdata',
      ],
      zip_safe=False,
      #include_package_data=True,
      #test_suite="estdel_nn.tests",
      )

# ???: On setup there are many 'Adding xxx to easy-install.pth file'. Why?