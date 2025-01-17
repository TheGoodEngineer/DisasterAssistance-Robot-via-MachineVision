# Credit to:
# https://hotblackrobotics.github.io/en/blog/2018/01/29/action-client-py/

#!/usr/bin/env python
# license removed for brevity

import rospy

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client(x_pos, y_pos, w_orient):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = x_pos
    goal.target_pose.pose.position.y = y_pos
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = w_orient

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')

        result = movebase_client(-3.5, 3.0, 1)
        if result:
            rospy.loginfo("Goal execution done!")


        # result = movebase_client(4.4, 3.4, 1)
        # if result:
        #     rospy.loginfo("Goal execution done!")

        # result = movebase_client(-3.5, 3.0, 1)
        # if result:
        #     rospy.loginfo("Goal execution done!")

        # result = movebase_client(-3.5, -3.5, 1)
        # if result:
        #     rospy.loginfo("Goal execution done!")


        # result = movebase_client(3.5, -3.0, 1)
        # if result:
        #     rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
