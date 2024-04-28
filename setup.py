from setuptools import setup

package_name = 'base_detection'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lufa',
    maintainer_email='lufa@todo.todo',
    description='The base_detection package for ROS 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'base_detection = base_detection.base_detection:main',
        ],
    },
)