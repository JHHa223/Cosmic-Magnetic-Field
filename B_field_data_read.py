# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:32:25 2024

@author: J.-H. Ha
"""
import numpy as np

data = np.load('Bfield_unperturbed_data.npz')
t = data['time']
mag_unpert = data['magnetic_field']


