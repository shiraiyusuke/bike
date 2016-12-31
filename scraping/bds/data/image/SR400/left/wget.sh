for line in `cat url_l.lst`
do
 wget ${line}
 sleep 1
done
