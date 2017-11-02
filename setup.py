#!/usr/bin/env python

from distutils.core import setup
from DistUtilsExtra.command import *

import re
import glob
from subprocess import Popen, PIPE


try:
    line = open("kazam/version.py").readline()
    VERSION = re.search(r"VERSION='(.*)'", line).group(1)
except:
    VERSION="1.0.0"

setup(name="kazam",
      version=VERSION,
      description="A screencasting program created with design in mind.",
      author="David Klasinc",
      author_email="bigwhale@lubica.net",
      long_description= ( open('README').read() + '\n'),
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        "Topic :: Multimedia :: Sound/Audio :: Capture/Recording",
        "Topic :: Multimedia :: Video :: Capture",
       ],
      keywords='kazam screenshot screencast audio sound recorder',
      url='https://launchpad.net/kazam',
      license='GPLv3',
      scripts=["bin/kazam"
               ],
      packages = ['kazam',
                  'kazam.pulseaudio',
                  'kazam.backend',
                  'kazam.frontend',
                 ],
      data_files=[
                  ('share/kazam/ui/', glob.glob("data/ui/*ui")),
                  ('share/kazam/icons/', glob.glob("data/icons/*svg")),
                  ('share/kazam/icons/dark/', glob.glob("data/icons/dark/*png")),
                  ('share/kazam/icons/light/', glob.glob("data/icons/light/*png")),
                  ('share/kazam/sounds/', glob.glob("data/sounds/*ogg")),
                  ],
      cmdclass = { "build" : build_extra.build_extra,
                   "build_i18n" :  build_i18n.build_i18n,
                   "build_help" : build_help.build_help,
                   "build_icons" : build_icons.build_icons}
      )

