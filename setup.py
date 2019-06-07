from distutils.core import setup
setup(
  name='ControlPyWeb',
  packages=['controlpyweb'],
  version='v0.0.3',
  license='MIT',
  description='A project to facilitate easy read/write to the ControlByWeb line of Automation/SCADA IO products.',
  author='Steve Jackson',
  author_email='washad@gmail.com',
  url='https://github.com/washad/ControlPyWeb',
  download_url='https://github.com/washad/ControlPyWeb/archive/v0.0.3.tar.gz',
  keywords=['Automation', 'ControlByWeb', 'SCADA'],
  install_requires=[
          'requests',
          'str2bool',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)