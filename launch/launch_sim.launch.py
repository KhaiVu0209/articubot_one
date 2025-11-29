import os #Lấy đường dẫn thư mục package, Xử lý đường dẫn file

from ament_index_python.packages import get_package_share_directory # Lấy đường dẫn đến thư mục của package

from launch import LaunchDescription #khung mô tả toàn bộ các hành động muốn chạy
from launch.actions import IncludeLaunchDescription #include một file launch khác

from launch.launch_description_sources import PythonLaunchDescriptionSource #cho phép include nhiều loại file launch

from launch_ros.actions import Node # Run Node

def generate_launch_description():
    package_name = "articubot_one" # Khai bao package

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])
    )

    # Spawner node from the gazebo_ros package . The entity 
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')
    
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
    ])





