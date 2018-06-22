from setuptools import setup, find_packages


setup(
    name="local_selenium_pool",
    version="1.0.0",
    description="Concurrent local selenium execution using multiprocessing_on_dill",
    long_description="""
A local selenium pool for increased testing performance without requiring multiple hosts. multiprocessing-on-dill is used to provide a configurable number of Chrome webdriver instances on which to simultaneously run selenium tests. Each instance reuses its applicationCacheEnabled = False webdriver for multiple tests, erasing all cookies between tests.
The sample test test_pool.py, has nine tests in it which can be executed using any number of processes reading from the same queue of tests. Each test searches the site's products for a different keyword. It then adds each item found to the cart, one at a time. Finally, it goes to the checkout page and compares the expected total to the basket total.
After the pool of webdrivers has no remaining tests to execute, it creates a JSON report in an XUnit style.
""",
    author_email="chris@testlabauto.com",
    author="Test Lab Automation",
    license="Apache License Version 2.0",
    url="https://github.com/testlabauto/local_selenium_pool",
    keywords=["Selenium", "Local", "Concurrent"],
    install_requires=['selenium', 'attr', 'setuptools', 'multiprocessing_on_dill'],
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)