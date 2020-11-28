export KITTI_SEQ=00  # Select KITTI odometry sequence: 00-
export KITTI_BASE_DIR=$HOME/dataset-kitti/  # set to your local copy!

cd ~/mola/demos
mola-cli -c kitti_lidar_slam.yml -p
