import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jstock1/Project2/webots_ros2_homework1_python/install/webots_ros2_homework1_python'
