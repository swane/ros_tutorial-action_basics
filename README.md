# ros_tutorial-action_basics
Basic files to test Actions in ROS
Action Tutorial
Acquire the Action package from Git Hub:
Move to directory ~/catkin_ws
Now download the action programs from Git:
https://github.com/swane/ros_tutorial-action_basics
This will create a directory called ros_tutorial-action_basics.
Now we will create a package:
catkin_create_pkg action_test rospy sensor_msgs
Now use File Manager to move the contects of ros_tutorial-action_basics into action_test, overwriting any other files there.
Make the packages:
catkin_make
Ensure roscore is running.
Move to directory action_test/src
Run the server:
./simple_action_server.py
In another terminal, same directory, run the client:
./simple_action_client.py

Close the programs, and repeat with fancy_action…
