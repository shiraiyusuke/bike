for line in `cat ../data/honda__cb1300_super_four_jpg_link.lst`
do
 wget $line -P ../data/honda__cb1300_super_four/
 sleep 2
done
