for line in `cat url_t.lst`
do
 wget ${line}
 sleep 1
done
