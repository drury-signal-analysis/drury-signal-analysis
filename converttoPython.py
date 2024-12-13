from scipy.io import loadmat
import csv

orientations = [
    'pronation',
    'rest',
    'supination',
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
    'Wrist_Flexion',
]

data = []
gesture_outputs = []

for subject in range(19):
    for orientation in orientations:
        for gesture in gestures:
            for iteration in range(5):
                path = f'FORS-EMG/Subject{subject + 1}/{orientation}/{gesture}-{iteration + 1}.mat'
                data.append(loadmat(path)['value'])
                gesture_outputs.append([gesture])

with open('fors_emg.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow([i + 1 for i in range(8)] + ['gesture'])

    for row, gesture in zip(data, gesture_outputs):
        writer.writerow(row.tolist() + gesture)
