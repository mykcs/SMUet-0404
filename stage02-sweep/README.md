# SMUet-0404

## stage02-sweep

加入了sweep。

“但其实sweep没有什么用。他是帮选哪个超参数效果好，
你想要训练你就用下面的formal test 或者 pre train test”

[issue 2](https://github.com/mykcs/SMUet-0404/issues/2)
每一组sweeps的sweep-1和最后的Origin_UNet_noAtt_Max150_DiceCELoss有数据，中间的都没有。

### run 记录

### run-0404-2300 
webrun [wandb run](https://wandb.ai/team-mykcs/lightning_logs/runs/c5e1wmlb?nw=nwuserkagura0108)

sweep+formal test 跳着运行了，没有什么意义 [wandb sweep](https://wandb.ai/team-mykcs/test-sweeps01?nw=nwusermykcs)

### run-0405-0342
-gpu webrun

[wandb run](https://wandb.ai/team-mykcs/lightning_logs/runs/vl8chrw1) 

[sweep](https://wandb.ai/team-mykcs/test-sweeps02/) 

### run03

在kaggle web运行了，同时按了saverun。出现了下面的情况。

run03-webrun [wandb](https://wandb.ai/team-mykcs/lightning_logs/runs/8hny8gx9)
run03-webrun [sweep](https://wandb.ai/team-mykcs/test-sweeps03/sweeps/8gaeiub3) 

run03-saverun [wandb](https://wandb.ai/team-mykcs/lightning_logs/runs/pytbhywb)
run03-saverun [sweep](https://wandb.ai/team-mykcs/test-sweeps03/sweeps/ami2it79) 

### run04 -cpu-saverun
[kaggle notebook]( https://www.kaggle.com/code/yufang18/run04-cpu-saverun/output?scriptVersionId=170453763)
好像缺失

[wandb](https://wandb.ai/team-mykcs/lightning_logs/runs/98b6flex)

运行中，在kaggle notebook setting，改了名字。就结束了。

没有sweep

### run05 -webrun cpu nosweep

notebook delete

### run06
kaggle，没有在add-ons scrects加入wandb_key。运行作废。

run07-sweep里的[version2](https://www.kaggle.com/code/mykcs01/run07-sweep?scriptVersionId=170456679)

### run07 -saverun
没有存到github里，奇怪。

kaggle notebook [version3](https://www.kaggle.com/code/mykcs01/run07-sweep/notebook
)

output 在kaggle的output可以下载

[wandb](https://wandb.ai/team-mykcs/lightning_logs/runs/vxfxwipt) 

[sweep](https://wandb.ai/team-mykcs/test-sweeps07) 

issue：cell27 MisconfigurationException: No `test_step()` method defined to run `Trainer.test`.
（跳过了，没去解决。）

---

## 下一步

理解代码

---

### run08 webrun

[notebook](https://www.kaggle.com/code/mykcs01/run08-nosweep-lsft/notebook) 

[run](https://wandb.ai/team-mykcs/lightning_logs/runs/05wdum4l?nw=nwusermykcs)

sweep no 直接跳过了，没有运行

Lightning Style Formal Test [尝试](https://wandb.ai/team-mykcs/UNet_Baseline-08/runs/o359bita)

### run09 -saverun-sweep-lsft

[kaggle notebook](https://www.kaggle.com/code/yufang18/run09-saverun-sweep-lsft/notebook)

### run10 -webrun

[notebook](https://www.kaggle.com/code/mykcs01/run10-test-step-sweep-lsft/notebook?scriptVersionId=170546708) 

[run](https://wandb.ai/team-mykcs/lightning_logs/runs/1mql96qg) 

[sweep](https://wandb.ai/team-mykcs/test-sweeps10) 

formal [test](https://wandb.ai/team-mykcs/test-sweeps10/runs/ah96kd98/overview?nw=nwusermykcs
)

cell 31 路径没有改，运行失败

---

### run11 sweep

ref [lgy-notebook-ver6](https://www.kaggle.com/code/liaoguoying/smu-dataset?scriptVersionId=169703867)

没有运行第一部分的run

直接sweep（其实不是很理解）  [wandb sweep](https://wandb.ai/team-mykcs/test-sweeps11)

运行到cell `wandb_logger = WandbLogger(project="SMU_MOA-run11", name="ResUNetPP50_monaiDiceCELoss_Max150")`

这一段的运行顺序不是交代的很明白。通过查

突然界面全没了。只能刷新。cell output全没了。右侧的kaggle/working也全没了。

重新运行cell `trainer = Trainer(max_epochs=150` 。wandb界面还有，离谱。kaggle界面就是cell下面的output都没了，但是还在运行。
<img width="1544" alt="image" src="https://github.com/mykcs/SMUet-0404/assets/165669834/cc9d0ccc-cbe7-4eae-8bdc-264abd3be6ee">


