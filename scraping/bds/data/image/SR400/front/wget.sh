for line in `cat url_f.lst`
do
 wget ${line}
 sleep 1
done
