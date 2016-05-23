#!/usr/bin/env python

import rospy

import actionlib
from action_test.msg import TimerAction,TimerGoal,TimerResult

rospy.init_node('timer_action_client')
client=actionlib.SimpleActionClient('timer',TimerAction)
client.wait_for_server()
goal=TimerGoal()
goal.time_to_wait=rospy.Duration.from_sec(5.0)
client.send_goal(goal)
client.wait_for_result()
print('Time elpsed:%f'%(client.get_result().time_elapsed.to_sec()))

