opencv_traincascade -data ../model -vec positive.vec -bg negative_right.dat -numPos 2000 -numNeg 2500 -featureType HOG -maxFalseAlarmRate 0.1 -w 76 -h 116 -minHitRate 0.97 -numStages 3
