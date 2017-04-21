LABEL_NUM=$1

echo "create db"
bash ./src/mk_db.sh all
echo "set model"
sed -e s!@label_num@!${LABEL_NUM}!g ./model/train_temp.prototxt > ./model/train.prototxt
sed -e s!@label_num@!${LABEL_NUM}!g ./model/deploy_temp.prototxt > ./model/deploy.prototxt
