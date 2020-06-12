
"""
Corresponding info_dict is located in that model folder.
Just copy the info_dict to replace the following to indicate the motor ID.

options: 
    global_wheel_control: bool. If yes, one value for all wheel.
    GUI_friction: bool. If yes, you can also change friction value during simulation with GUI
    trajPlot: path. Save trajectory to a plot
    dat_savePath: path. Save (x, y, theta) to somewher
    log_mp4: path. Dump a video of the simulation.
"""

from CarRobot import CarRobot

if __name__ == "__main__":
    info_dict = {
        'jointId': {0: 'BackRight',
                    20: 'FrontRight',
                    40: 'BackLeft',
                    60: 'FrontLeft'},
        'init_motorStatus': {0: {'controlMode': 0, 'targetVelocity': -10, 'force': 5},
                                20: {'controlMode': 0, 'targetVelocity': 12, 'force': 5},
                                40: {'controlMode': 0, 'targetVelocity': 10, 'force': 5},
                                60: {'controlMode': 0, 'targetVelocity': 14, 'force': 5}},
        'init_physical_para': {0: {'lateralFriction': .7, 'angularDamping': 0, 'linearDamping': 0, 'rollingFriction': 0, 'spinningFriction': 0},
                                20: {'lateralFriction': .7, 'angularDamping': 0, 'linearDamping': 0, 'rollingFriction': 0, 'spinningFriction': 0},
                                40: {'lateralFriction': .7, 'angularDamping': 0, 'linearDamping': 0, 'rollingFriction': 0, 'spinningFriction': 0},
                                60: {'lateralFriction': .7, 'angularDamping': 0, 'linearDamping': 0, 'rollingFriction': 0, 'spinningFriction': 0}}}

    options = {'global_wheel_control': False, 
               'GUI_friction': False, 
                'trajPlot': "show.png",
                # 'dat_savePath': './output/test.txt',
                'log_mp4': 'test.mp4'
                }

############# Run #####################
    c = CarRobot("../mecanum_simple/mecanum_simple.urdf", info_dict, GUI=True,
                 options=options, timesteps = 3600, debug=False, start_pos=[0, 0, 0.0007], start_ori = [0, 0, 0, 1])
    c.run()
