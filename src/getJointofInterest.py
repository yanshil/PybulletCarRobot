"""
Get index of joint of interest in loaded URDF
"""
import pybullet as p

## The joints'name you are interested in
# jointOfInterest = ['BackRight', 'FrontRight', 'BackLeft', 'FrontLeft']

# jointOfInterest = ['BR', 'FR', 'BL', 'FL']
# URDF_path = "../simple_cuboid_4074g/simple_cuboid_4074g.urdf"
## {'BR': 1, 'FR': 2, 'BL': 0, 'FL': 3}

jointOfInterest = ['right_rear_wheel_joint', 'right_front_wheel_joint', 'left_rear_wheel_joint', 'left_front_wheel_joint']
URDF_path = "../Pybullet_racecar/racecar_fix_steer.urdf"
# {'right_rear_wheel_joint': 3, 'right_front_wheel_joint': 7, 'left_rear_wheel_joint': 2, 'left_front_wheel_joint': 5}


##############################################
physicsClient = p.connect(p.DIRECT)#or p.DIRECT for non-graphical version
robotId = p.loadURDF(URDF_path,[0,0,0], p.getQuaternionFromEuler([0,0,0]), 
                   # useMaximalCoordinates=1, ## New feature in Pybullet
                   flags=p.URDF_USE_INERTIA_FROM_FILE)
JointIDs = []
JointNames = []
for j in range(p.getNumJoints(robotId)):
    info = p.getJointInfo(robotId, j)
    JointIDs.append(info[0])
    JointNames.append(info[1].decode("utf-8")) ## PyBullet output bytes as the joint names

jointInfo = {}
for jt in jointOfInterest:
    cid = JointNames.index(jt)
    jointInfo[jt] = JointIDs[cid]
print(jointInfo)

p.disconnect()

