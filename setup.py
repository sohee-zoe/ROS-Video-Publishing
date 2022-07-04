from setuptools import setup

package_name = 'vi_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sohee',
    maintainer_email='sohee.forest@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'video_publisher = vi_pub.video_pub:main',
        	'video_subscriber = vi_pub.video_sub:main',
        ],
    },
)
