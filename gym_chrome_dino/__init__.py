#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Elvis Yu-Jing Lin <elvisyjlin@gmail.com>
# Licensed under the MIT License - https://opensource.org/licenses/MIT

from gym.envs.registration import register

register(
    id='ChromeDino-v0', 
    entry_point='gym_chrome_dino.envs:ChromeDinoEnv', 
    kwargs={'render': True, 'accelerate': False, 'autoscale': False}
)

register(
    id='ChromeDinoNoBrowser-v0', 
    entry_point='gym_chrome_dino.envs:ChromeDinoEnv', 
    kwargs={'render': False, 'accelerate': False, 'autoscale': False}
)