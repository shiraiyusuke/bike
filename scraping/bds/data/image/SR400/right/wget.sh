for line in `cat url_r.lst`
do
 wget ${line}
 sleep 1
done
