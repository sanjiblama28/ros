import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
   config = os.path.join(
      get_package_share_directory('launch_tutorial'),
      'config',
      'turtlesim.yaml'
      )

   return LaunchDescription([
      Node(
         package='turtlesim',
         executable='turtlesim_node',
         name='sim',
         parameters=[config]
         turtlesim_world_2 = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
               get_package_share_directory('launch_tutorial'), 'launch'),
                '/turtlesim_world_2.launch.py'])
            )
         turtlesim_world_2_with_namespace = GroupAction(
         actions=[
             PushRosNamespace('turtlesim2'),
             turtlesim_world_2,
         
      )
   ])
