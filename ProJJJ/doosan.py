import ast  # library for a string converting
import math

# Turn OFF the grinding
set_digital_outputs(1, 4, 0)

# Set the initial motions parameters
set_tool("twGrindingMirka")
set_tcp("tcpGrindingMirka")
set_tool_shape("tshGrindingMirka")
set_accx(400)
set_accj(70)
set_velx(500)
set_velj(80)

# Initial trajectory variables
path = []
listPose = {0: []}
Global_force = []
global thrdForce

# There are globals variables which will be in the TP
# Global_flagAlign = 1
# Global_flagAverage = 1
# Global_valForce = 0
# Global_numRPM = 1
# Global_flagForce = 0
# Global_grindVel = 200
# Global_grindAcc = 300
# Global_path = []
# Global_xOffs = 610 # [mm]
# Global_yOffs = 450 # [mm]
# Global_numX = 1
# Global_numY = 1

# Additinal variables
numDiscrete = 5  # [mm]

# User cartensian
usrCart1 = set_user_cart_coord([-650, 677, 1392, 0, 0, 0], DR_BASE)


# ------------------------
# Procedures and functions
# ------------------------

# There is a correction points method by the Z-direction average and ZY-plane align
def points_correction():
    # Global veriables importing
    global Global_flagAlign
    global Global_flagAverage
    global path
    # Locals variables
    averZ = 0
    # Align correction
    if Global_flagAlign:
        for point in path:
            point[4] = 0.0
    # Average correction
    if Global_flagAverage:
        for point in path:
            averZ += point[2] / len(path)
        for point in path:
            point[2] = averZ
    # Add the exit pose
    offsPoint = subtract_pose(posx(path[-1]), posx(path[-2]))
    exitPoint = path[-1]
    exitPoint = posx([exitPoint[0] + offsPoint[0], exitPoint[1] + offsPoint[1], exitPoint[2] - 20] + exitPoint[3:])
    path.append(posx(exitPoint))
    return None


# There is a path recording method in the collaborative zone by freedriving
def path_recording():
    # Global veriables importing
    global path
    global listPose
    global thrdPathRec
    global numDiscrete
    global usrCart1
    global force
    # Locals variables
    solution = 0
    numPoint = 0
    # Main cicle of the path recording
    while True:
        numWaitTime = 0.4  # [s]
        listPose[numPoint], solution = get_current_posx(usrCart1)
        if numPoint != 0:
            # Get the posex with
            while abs(get_distance(listPose[numPoint], listPose[numPoint - 1])) < numDiscrete and thread_state(
                    thrdPathRec) != 3:
                wait(numWaitTime)
                listPose[numPoint], solution = get_current_posx(usrCart1)
                if get_digital_inputs(13, 14) == 0b01:
                    set_digital_output(9)
                    wait_digital_input(14, ON)
                    wait_digital_input(13, OFF)
                elif get_digital_inputs(13, 14) == 0b11:
                    set_digital_output(-9)
                    wait_digital_input(14, OFF)
                    wait_digital_input(13, OFF)
        path.append(listPose[numPoint])  # Add the poseX in the end of the path array
        Global_force.append([get_digital_input(14)])  # Add force state
        if thread_state(thrdPathRec) == 3:  # Check this thread OFF-state
            # Leave the method
            points_correction()
            break
        numPoint += 1
    return None


def file_writing():
    global path
    global startPose
    with open("trajectory.txt", "w") as trajectory_w:
        trajectory_w.write(str(path))
        trajectory_w.close()
    with open("start.txt", "w") as start_w:
        start_w.write(str(startPose))
        start_w.close()
    wait(0.5)
    return None


def file_reading():
    global path
    global startPose
    with open("trajectory.txt", "r") as trajectory_r:
        path_str = trajectory_r.read()
        trajectory_r.close
        pathBad = ast.literal_eval(path_str)
        path = []
        for pointBad in pathBad:
            path.append(posx(pointBad[0], pointBad[1], pointBad[2], pointBad[3], pointBad[4], pointBad[5]))
    with open("start.txt", "r") as start_r:
        startPose_str = start_r.read()
        start_r.close()
        startPose = ast.literal_eval(startPose_str)
    wait(0.5)
    return None


# PopUping before task starting
def task_initializing():
    global thrdPathRec
    global startPose
    global usrCart1
    global Global_flagSplMot
    if Global_flagSplMot:
        if tp_get_user_input("Record a new trajectory?", DR_VAR_BOOL):  # Record a new trajectory
            if tp_get_user_input("Turn ON the Mirka?", DR_VAR_BOOL):  # Switching the grinding machine
                set_digital_outputs(1, 4, Global_numRPM)  # Turn ON the grinding
            while get_digital_inputs(5, 6) == 0:  # Checking the ON-state of the collaborative zone
                tp_popup("Release the collaborative button!")  # You should release the button before recording
            tp_popup("Move the robot to START position.")  # Record start position
            wait_manual_guide()
            startPose, solStart = get_current_posx(usrCart1)
            tp_popup("Trajectory recording is going to start after pushing 'Resume program'.")
            thrdPathRec = thread_run(path_recording)  # Record the trajectory
            wait_manual_guide()
            thread_stop(thrdPathRec)
            set_digital_outputs(1, 4, 0)
            file_writing()
        else:
            file_reading()
    else:
        pass


def path_deviding():
    global path
    lenPart = 98
    PATH = []
    lenPath = len(path)
    if lenPath > 100:
        if lenPath % lenPart == 1:
            for part in range((lenPath - 3) // lenPart):
                PATH.append(path[part * lenPart: part * lenPart + lenPart - 1])
            PATH.append(path[-((lenPath - 3) % lenPart): -4])
            PATH.append(path[-3:])
        else:
            for part in range(lenPath // lenPart):
                PATH.append(path[part * lenPart: part * lenPart + lenPart - 1])
            PATH.append(path[-(lenPath % lenPart):])
        pass
    else:
        PATH.append(path)
    return PATH


def set_cartensian(x, y):
    global Global_Lenght
    global Global_Width
    global usrCart1
    global Global_thick
    if x == 0 and y == 0:
        cartensian = set_user_cart_coord([Global_zero1[0], Global_zero1[1], 1408 - Global_thick, 0, 0, 0], DR_BASE)
    elif x == 1 and y == 0:
        cartensian = set_user_cart_coord(
            [Global_zero2[0] - Global_Lenght, Global_zero2[1], 1408 - Global_thick, 0, 0, 0], DR_BASE)
    elif x == 1 and y == 1:
        cartensian = set_user_cart_coord(
            [Global_zero3[0] - Global_Lenght, Global_zero3[1] + Global_Width, 1408 - Global_thick, 0, 0, 0], DR_BASE)
    elif x == 0 and y == 1:
        cartensian = set_user_cart_coord(
            [Global_zero4[0], Global_zero4[1] + Global_Width, 1408 - Global_thick, 0, 0, 0], DR_BASE)
    else:
        tp_popup("Not correct cartensian!", DR_PM_ALARM)
    return cartensian


def force_releasing():
    global UsrCart
    global path
    curPos, curSol = get_current_posx(UsrCart)
    while abs(get_distance(curPos, path[-3])) > 25:
        wait(0.01)
        tp_log("The distance to the point is {0}".format(get_distance(curPos, path[-3])))
    task_compliance_ctrl([20000, 20000, 20000, 400, 400, 400])
    release_force()
    release_compliance_ctrl()
    return None


def gringindig_on():
    global Global_flagForce
    global Global_valForce
    # Turn ON the grinding machine
    set_digital_outputs(1, 4, Global_numRPM)
    # Turn ON force
    if Global_flagForce == 1:
        task_compliance_ctrl([20000, 20000, 1000, 400, 400, 400])
        set_desired_force(fd=[0, 0, Global_valForce, 0, 0, 0], dir=[0, 0, 1, 0, 0, 0], time=0)
    return None


def gringindig_off():
    global Global_flagForce
    global Global_valForce
    if Global_flagForce == 1:
        release_compliance_ctrl()
        release_force()
    # Turn OFF the grinding machine
    set_digital_outputs(1, 4, 0)
    return None


def linear_moving(cart):
    global Global_Lenght
    global Global_Width
    global Global_grindVel
    global Global_grindAcc
    global Global_flagForce
    global Global_valForce
    # -------
    offsOver = 10  # [mm]
    initPose = posx((80 - offsOver) / 2, -((130 - offsOver) / 2), 5, 137.39, 0, 134.61)
    trigWay = True
    ttlStep = math.ceil((Global_Lenght + 2 * offsOver) / 80)
    offStep = 80 - (ttlStep * 80 - Global_Lenght - 2 * offsOver) / (ttlStep - 1)
    offsWidth = Global_Width + 2 * offsOver - 130
    # -------
    movel(trans(initPose, [0, 0, -50, 0, 0, 0], DR_TOOL), ref=cart)
    movel(trans(initPose, [0, 0, -10, 0, 0, 0], DR_TOOL), ref=cart)
    gringindig_on()
    wait(0.5)
    begin_blend(5)
    # Motion
    for xStep in range(ttlStep):
        if trigWay:
            movel(trans(initPose, [xStep * offStep, 0, 0, 0, 0, 0], cart, cart), v=Global_grindVel, a=Global_grindAcc,
                  ref=cart)
            movel(trans(initPose, [xStep * offStep, -offsWidth, 0, 0, 0, 0], cart, cart), v=Global_grindVel,
                  a=Global_grindAcc, ref=cart)
            trigWay = False
        else:
            movel(trans(initPose, [xStep * offStep, -offsWidth, 0, 0, 0, 0], cart, cart), v=Global_grindVel,
                  a=Global_grindAcc, ref=cart)
            movel(trans(initPose, [xStep * offStep, 0, 0, 0, 0, 0], cart, cart), v=Global_grindVel, a=Global_grindAcc,
                  ref=cart)
            trigWay = True
    end_blend()
    endPose, endSol = get_current_posx(cart)
    gringindig_off()
    movel(trans(endPose, [0, 0, -50, 0, 0, 0], DR_TOOL), ref=cart)
    return None


def spline_moving(cart):
    global thrdForce
    # Move from random pose (under the wood panel)
    randPose, randSol = get_current_posx()
    if randPose[2] > 1380:
        movel(trans(randPose, [0, 0, -50, 0, 0, 0], DR_TOOL), r=10)
    # Move to the start position (upper then wood panel)
    movel(trans(startPose, [0, 0, -50, 0, 0, 0], DR_TOOL), r=10, ref=cart)
    # Grinding
    movel(trans(PATH[0][0], [0, 0, -5, 0, 0, 0], DR_TOOL), ref=cart)
    gringindig_on()
    # Exit by force releasing
    if x == 0 and y == 0:
        thrdForce = thread_run(force_releasing, loop=True)
    else:
        thread_resume(thrdForce)
    # Move by the recorded trajectory
    for part in PATH:
        movesx(part, v=Global_grindVel, a=Global_grindAcc, vel_opt=DR_MVS_VEL_CONST, ref=cart)
    gringindig_off()
    # Turn OFF force
    thread_pause(thrdForce)
    # Move to the approach potision
    movel(trans(path[-1], [0, 0, -30, 0, 0, 0], DR_TOOL), ref=cart)


# ------------
# Main process
# ------------

task_initializing()
while True:
    # Confirm from operator
    if Global_flagSplMot:
        tp_popup("Start the spline motion with {0} points?".format(len(path)), DR_PM_MESSAGE)
    else:
        tp_popup("Start the linear motion?".format(len(path)), DR_PM_MESSAGE)
    PATH = path_deviding()
    for x in range(Global_numX):
        for y in range(Global_numY):
            UsrCart = set_cartensian(x, y)
            if Global_flagSplMot:
                spline_moving(UsrCart)
            else:
                linear_moving(UsrCart)