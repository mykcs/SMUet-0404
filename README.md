# SMUet-0404

wandb kaggle pytorch_lightning

seg

## stage01-firsttry

熟悉项目

## stage02-sweep



## stage03-aug-ddataset


---

### run08 webrun

notebook https://www.kaggle.com/code/mykcs01/run08-nosweep-lsft/notebook

run https://wandb.ai/team-mykcs/lightning_logs/runs/05wdum4l?nw=nwusermykcs

sweep no 直接跳过了，没有运行

Lightning Style Formal Test 尝试 https://wandb.ai/team-mykcs/UNet_Baseline-08

### run09 -saverun-sweep-lsft

[kaggle notebook](https://www.kaggle.com/code/yufang18/run09-saverun-sweep-lsft/notebook)

### run10 -webrun

[notebook](https://www.kaggle.com/code/mykcs01/run10-test-step-sweep-lsft/notebook?scriptVersionId=170546708) 

run https://wandb.ai/team-mykcs/lightning_logs/runs/1mql96qg

sweep https://wandb.ai/team-mykcs/test-sweeps10

formal test https://wandb.ai/team-mykcs/test-sweeps10/runs/ah96kd98/overview?nw=nwusermykcs

cell 31 路径没有改，运行失败

---

# sweep

### run11 sweep

ref [lgy-notebook-ver6](https://www.kaggle.com/code/liaoguoying/smu-dataset?scriptVersionId=169703867)

没有运行第一部分的run

直接sweep（其实不是很理解）  [wandb sweep](https://wandb.ai/team-mykcs/test-sweeps11)

运行到cell `wandb_logger = WandbLogger(project="SMU_MOA-run11", name="ResUNetPP50_monaiDiceCELoss_Max150")`

这一段的运行顺序不是交代的很明白。通过查

突然界面全没了。只能刷新。cell output全没了。右侧的kaggle/working也全没了。

重新运行cell `trainer = Trainer(max_epochs=150` 。wandb界面还有，离谱。kaggle界面就是cell下面的output都没了，但是还在运行。
<img width="1544" alt="image" src="https://github.com/mykcs/SMUet-0404/assets/165669834/cc9d0ccc-cbe7-4eae-8bdc-264abd3be6ee">


# update

发布了 [Aug Dataset for Fine-tune](https://www.kaggle.com/datasets/liaoguoying/aug-dataset-for-fine-tune)

---

### train_froma_poormodel-04082323

[kaggle notebook](https://www.kaggle.com/yufang18/train-froma-poormodel-04082323)

没有 run-overfit

model 之前不知道哪个，好像有点弱的model

[wandb](https://wandb.ai/team-mykcs/UNet_Compare/runs/ewgcpqsb)

### run-04090529

[kaggle notebook](https://www.kaggle.com/code/yufang18/notebookc5abae8998/notebook)

run-overfit [wandb](https://wandb.ai/team-mykcs/lightning_logs/runs/83t1nw8o)

run ResUNet_ep120_DiceCELosswithKL crashed  [wandb](https://wandb.ai/team-mykcs/UNet_Compare/runs/odxjpwe3/overview?nw=nwusermykcs)

NameError: name 'model_ckpt' is not defined

# Ref
dataset https://www.kaggle.com/datasets/liaoguoying/rawniidataset/code

notebook tps://www.kaggle.com/code/liaoguoying/smu-dataset
