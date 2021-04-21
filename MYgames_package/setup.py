from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='MYgames',
      version='0.1',
      description='Simple games to play',
      author='Mandi Yang',
      author_email='yangmandi2008@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MandiYang/MYgames',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
      ],
      python_requires='>=3.5',
      license='MIT',
      packages=find_packages(),
      download_url = 'https://github.com/MandiYang/MYgames/releases/download/0.1/MYgames.zip'
)
