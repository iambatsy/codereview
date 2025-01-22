from setuptools import find_packages, setup

package_name = 'my_robot_controller'

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
    description='Python client server tutorial',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	'test_node= my_robot_controller.my_first_node:main',
    	'talker=my_robot_controller.publisher_member_function:main',
    	'listener=my_robot_controller.subscriber_member_function:main'
        ],
    },
)
