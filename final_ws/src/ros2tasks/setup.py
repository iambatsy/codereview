from setuptools import find_packages, setup

package_name = 'ros2tasks'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kiara',
    maintainer_email='kiarathapar37@gmail.com',
    description='vision detector',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_publisher_node= ros2tasks.image_publisher_node:main',
            'vision_detector_node=ros2tasks.vision_detector_node:main'
        ],
    },
)
