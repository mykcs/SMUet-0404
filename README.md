# SMUet-0404

wandb kaggle pytorch_lightning

seg

# run 记录

### run01 -webrun

run https://wandb.ai/team-mykcs/lightning_logs/runs/c5e1wmlb?nw=nwusermykcs

sweep+formal test 跳着运行了，没有什么意义 地址在这里 https://wandb.ai/team-mykcs/test-sweeps01?nw=nwusermykcs

### run02 -gpu webrun

run https://wandb.ai/team-mykcs/lightning_logs/runs/vl8chrw1?nw=nwusermykcs

sweep https://wandb.ai/team-mykcs/test-sweeps02

### run03

在kaggle界面运行了，同时按了saverun。出现了下面的情况。

webrun wandb https://wandb.ai/team-mykcs/lightning_logs/runs/8hny8gx9

webrun sweep https://wandb.ai/team-mykcs/test-sweeps03/sweeps/8gaeiub3

saverun wandb https://wandb.ai/team-mykcs/lightning_logs/runs/pytbhywb

saverun sweep https://wandb.ai/team-mykcs/test-sweeps03/sweeps/ami2it79

### run04 -cpu-saverun
https://www.kaggle.com/code/yufang18/run04-cpu-saverun/output?scriptVersionId=170453763

wandb
https://wandb.ai/team-mykcs/lightning_logs/runs/98b6flex/workspace?nw=nwusermykcs

运行中，在kaggle notebook setting，改了名字。就结束了。

没有sweep


### run05 -webrun cpu nosweep
notebook delete


### run06
kaggle，没有在add-ons scrects加入wandb_key。运行作废。

run07-sweep里的version2
https://www.kaggle.com/code/mykcs01/run07-sweep?scriptVersionId=170456679


### run07 -saverun
没有存到github里，奇怪。

notebook https://www.kaggle.com/code/mykcs01/run07-sweep/notebook

output 在kaggle的output可以下载

run https://wandb.ai/team-mykcs/lightning_logs/runs/vxfxwipt

sweep https://wandb.ai/team-mykcs/test-sweeps07

issue：cell27 MisconfigurationException: No `test_step()` method defined to run `Trainer.test`.

不理解：在wandb project=test-sweeps07里，sweep2-9都failed。

---

# 下一步
理解代码

尝试解决issue

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

没有第一部分的run

直接sweep（不是很理解）  [wandb sweep](https://wandb.ai/team-mykcs/test-sweeps11)

运行到cell `wandb_logger = WandbLogger(project="SMU_MOA-run11", name="ResUNetPP50_monaiDiceCELoss_Max150")`

突然界面全没了。只能刷新。结果运行结果全没了。

重新运行cell `trainer = Trainer(max_epochs=150` 。wandb界面还有，离谱。


# update

发布了 [Aug Dataset for Fine-tune](https://www.kaggle.com/datasets/liaoguoying/aug-dataset-for-fine-tune)

---

# Ref
dataset https://www.kaggle.com/datasets/liaoguoying/rawniidataset/code

notebook tps://www.kaggle.com/code/liaoguoying/smu-dataset
