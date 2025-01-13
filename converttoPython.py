import numpy as np
from scipy.io import loadmat

subject_count = 19
iterations = 5
sensor_count = 8
sensor_data_length = 8000

orientations = [
    'Pronation',
    'Rest',
    'Supination'
]

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
    'Wrist_Flexion'
]

row_count = subject_count * len(orientations) * len(gestures) * iterations

inputs = np.zeros((row_count, sensor_count, sensor_data_length), dtype=np.float64)
outputs = np.zeros(row_count, dtype=np.uint8)

#Reads fpr each subject, each forearm orientation, in each gesture from each individual file
for subject in range(subject_count):
    for orientation_index, orientation in enumerate(orientations):
        for gesture_index, gesture in enumerate(gestures):
            for iteration in range(iterations):
                path = f'./FORS-EMG/Subject{subject + 1}/{orientation}/{gesture}-{iteration + 1}.mat'

                index = np.ravel_multi_index(
                    (subject, orientation_index, gesture_index, iteration),
                    (subject_count, len(orientations), len(gestures), iterations)
                )

                inputs[index] = loadmat(path)['value']
                outputs[index] = gesture_index

print(inputs)
print(outputs)
