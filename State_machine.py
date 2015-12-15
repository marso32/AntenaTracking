__author__ = 'AlexisPotvin'

#this state machine will have 9 state with 2 variable and 3 state for each variable
#pan up = right pan down = left



import servo

DONTMOVE = 0
PANNTILTU = 1
PANNTILTD = 2
PANUTILTU = 3
PANUTILTD = 4
PANUTILTN = 5
PANDTILTU = 6
PANDTILTD = 7
PANDTILTN = 8


#state = 0 #state of mouvement


def dontmove ():
    servo.servo('hold', 'hold')


def panntiltu ():
    servo.servo('hold', 'up')


def panntiltd ():
    servo.servo('hold', 'down')


def panutiltd ():
    servo.servo('up', 'down')


def panutiltu ():
    servo.servo('up', 'up')


def panutiltn ():
    servo.servo('up', 'hold')


def pandtiltu ():
    servo.servo('down', 'up')


def pandtiltd ():
    servo.servo('down', 'down')


def pandtiltn ():
    servo.servo('down', 'hold')




def state_machine_action (state):

    if state == DONTMOVE:
        dontmove()
    elif state == PANNTILTD:
        panntiltd()
    elif state == PANNTILTU:
        panntiltu()
    elif state == PANUTILTD:
        panutiltd()
    elif state == PANUTILTU:
        panutiltu()
    elif state == PANUTILTN:
        panutiltn()
    elif state == PANDTILTD:
        pandtiltd()
    elif state == PANDTILTN:
        pandtiltn()
    elif state == PANDTILTU:
        pandtiltu()
    else:
        print"fatal error no good state in (state machine action)"

    return state


def state_machine_event_to_action (state,antena_pan_angle,antena_tilt_angle,uav_pan_angle,uav_tilt_angle,angle_tolerence):

    if state == DONTMOVE:
        if antena_pan_angle + angle_tolerence > uav_pan_angle:
            state = PANDTILTN
        elif antena_pan_angle < uav_pan_angle + angle_tolerence:
            state = PANUTILTN
        elif antena_tilt_angle + angle_tolerence > uav_tilt_angle:
            state = PANNTILTD
        elif antena_tilt_angle < uav_tilt_angle + angle_tolerence:
            state = PANNTILTU
        else :
            state = DONTMOVE


    elif state == PANNTILTD:
        if antena_pan_angle + angle_tolerence > uav_pan_angle:
            state = PANDTILTD
        elif antena_pan_angle < uav_pan_angle + angle_tolerence:
            state = PANUTILTD
        elif antena_tilt_angle + angle_tolerence > uav_tilt_angle:
            state = PANNTILTD
        elif antena_tilt_angle < uav_tilt_angle + angle_tolerence:
            state = PANNTILTU
        else :
            state = DONTMOVE

    elif state == PANNTILTU:

        if antena_pan_angle + angle_tolerence > uav_pan_angle:
            state = PANDTILTU
        elif antena_pan_angle < uav_pan_angle + angle_tolerence:
            state = PANUTILTU
        elif antena_tilt_angle + angle_tolerence > uav_tilt_angle:
            state = PANNTILTD
        elif antena_tilt_angle < uav_tilt_angle + angle_tolerence:
            state = PANNTILTU
        else :
            state = DONTMOVE

    elif state == PANUTILTD:
        if antena_pan_angle + angle_tolerence > uav_pan_angle:
            state = PANDTILTD
        elif antena_pan_angle < uav_pan_angle + angle_tolerence:
            state = PANUTILTD
        elif antena_tilt_angle + angle_tolerence > uav_tilt_angle:
            state = PANUTILTD
        elif antena_tilt_angle < uav_tilt_angle + angle_tolerence:
            state = PANUTILTU
        else :
            state = DONTMOVE


    elif state == PANUTILTU:

    elif state == PANUTILTN:

    elif state == PANDTILTD:

    elif state == PANDTILTN:

    elif state == PANDTILTU:

    else:
        state = DONTMOVE


    return state
