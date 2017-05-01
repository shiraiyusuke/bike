import cv2

dat_file = '/usr/local/wk/git_local/bike/analysis/front_fork/data/cascade/right/datfile/positive_reverse_right.dat'

with open(dat_file, 'r') as inf:
    for line in inf:
        line = line.rstrip()
        values = line.split(' ')
        image_path = values[0]
        x = int(values[1])
        y = int(values[2])
        w = int(values[3])
        h = int(values[4])
        image = cv2.imread(image_path, 1)
        clop_image = image[y:y+h, x:x+w]
        cv2.namedWindow('window')
        cv2.imshow('window', clop_image)
        cv2.waitKey(0)
