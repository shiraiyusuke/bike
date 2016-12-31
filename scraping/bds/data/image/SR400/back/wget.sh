for line in `cat url_b.lst`
do
 wget ${line}
 sleep 1
done
