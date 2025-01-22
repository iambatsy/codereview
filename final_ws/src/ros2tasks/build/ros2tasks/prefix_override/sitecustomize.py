import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kiara/final_ws/src/ros2tasks/install/ros2tasks'
