from scipy.io import loadmat

import numpy as np 
=======
>>>>>>> bfed3a93a5b390cc35311faf1fe6088957e1d798

gestures = [
    'Hand_Close',
    'Index',
    'Index_Little',
    'Peace',
    'Radial_Deviation',
    'Right_Angle',
    'Thumb_Little',
    'Thumb_UP',
    'Ulner_Deviation',
    'Wrist_Extension',
    'Wrist_Flexion',
]

orientations = [
    'pronation',
    'rest',
    'supination',
]

for i in range(19):
    for orientation in orientations:
        for gesture in gestures:
            for j in range(5):
                path = f'FORS-EMG/Subject{i + 1}/{orientation}/{gesture}-{j + 1}.mat'
                data = loadmat(path)

                print(data['__header__'], data['__version__'], data['__globals__'], data['value'])
