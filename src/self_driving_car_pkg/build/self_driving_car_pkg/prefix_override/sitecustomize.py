import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/leelang/auto_ws/src/self_driving_car_pkg/install/self_driving_car_pkg'
