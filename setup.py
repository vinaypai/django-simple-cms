import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-simple-cms',
    version='0.1.3',
    author='Vinay Pai',
    author_email='vinay@vinaypai.com',
    description='A simple  CMS for django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vinaypai/django-simple-cms/',
    packages=['cms'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System',
    ],
    install_requires=[
        'django >= 1.11',
        'django-mptt >= 0.9',
        'pillow >= 2.1',
    ]
)
