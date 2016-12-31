for line in `cat url_u.lst`
do
 wget ${line}
 sleep 1
done
