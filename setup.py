from setuptools import setup

setup(name='smc',
      version='0.1',
      description='Package for Seven Mile Coding',
      long_description='Really, the funniest around.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='Seven Mile Coding SevenMileCoding smc 7mc',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'jinja2',
      ],
      include_package_data=True,
      zip_safe=False)
