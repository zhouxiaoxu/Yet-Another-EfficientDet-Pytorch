python script01_SplitDataset2List.py
python script02_voc2coco.py list_train.txt  Train2007  "annotations/instances_Train2007.json"
python script02_voc2coco.py list_val.txt  Val2007  "annotations/instances_Val2007.json"
python script02_voc2coco.py list_test.txt  Test2007  "annotations/instances_Test2007.json"

python train.py -c 2 --batch_size 8 --lr 1e-5 --num_epochs 10 --load_weights weights/efficientdet-d2.pth  --data_path  /root/dataset
