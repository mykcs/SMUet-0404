# SMUet-0404

## stage05-macro

修改指标为macro

---

baseline：resnet50-Unet-DiceCE

## 数据集对比

baseline: dataset2

compare:

run-old_dataset 
[notebook-kaggle-ver1](https://www.kaggle.com/code/mykcs01/diceceloss?scriptVersionId=172743614)
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/1wfvee3h)

## loss 对比
baseline: resnet50-Unet-DiceCE

compare: 

Dice
[kaggle-notebook](https://www.kaggle.com/code/gemini2024/resnet50-unet-monai-dice?scriptVersionId=172892353) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/ovnlwkwj)

resnet50-Unet-DiceCEKL-kl2
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/tx6cw5nm)

DiceCELossWithKL

Focal
[kaggle-notebook](https://www.kaggle.com/code/mykcs01/focalloss) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/v6cewtc2)

smp-Dice
[kaggle-notebook](https://www.kaggle.com/code/gemini2024/resnet50-unet-smp-dice?scriptVersionId=172881878)
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/514ebpd6)

12.3 encoder 对比
baseline: resnet50-Unet-DiceCE
compare: 
mitb2-Unet
mitb5-Unet
mitb2-MAnet
mitb5-MAnet notebook-kaggle


### ver0418-stage04

0418，距离上次运行很久了，现在熟悉一下。

notebook [kaggle](https://www.kaggle.com/code/mykcs01/ver0418/notebook)

wandb [run](https://wandb.ai/team-mykcs/UNet_Compare/runs/tp3mutkp)

### run0418-macro-lambda_kl=2

修改了Metrics部分，micro改为macro

lambda_dice=0.85, lambda_ce=0.15, lambda_kl=2.0，但是看着效果好像不太好

[kaggle-notebook](https://www.kaggle.com/code/mykcs01/run0418-macro-lambda-kl-2/notebook) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/tx6cw5nm)

### run0418

目前当作baseline吧

[kaggle-notebook](https://www.kaggle.com/code/yufang18/run0418/notebook) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/cf3v4x1l)

### run-old_dataset

使用旧dataset

[kaggle-notebook](https://www.kaggle.com/code/mykcs01/run-old-dataset/notebook) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/1wfvee3h?nw=nwusermykcs)

### MViTUNet

encoder_name='mit_b2'，in_channels=3

kaggle-notebook
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/76hx468j)

### DiceCELoss

DiceCELoss

[kaggle-notebook](https://www.kaggle.com/code/mykcs01/diceceloss/notebook) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/3v7gn20j)

### MViTUNet-DiceCELoss

[kaggle-notebook](https://www.kaggle.com/code/yufang18/mvitunet-diceceloss)
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/355n4b8x)

### FocalLoss

[kaggle-notebook](https://www.kaggle.com/code/mykcs01/focalloss) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/v6cewtc2)

### MViTMAnet-DiceCELoss

‘# decoder_attention_type='scse',’
x = x.repeat(1,3,1,1)

[kaggle-notebook](https://www.kaggle.com/code/yufang18/mvitmanet-diceceloss/notebook)
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/1pxr47e2)

#### DiceLoss-icl_bk

参数，include_background=True，实际上默认也是True

[kaggle-notebook](https://www.kaggle.com/code/mykcs01/diceloss-icl-bk/notebook) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/4q9veicm)

### mitb5-MAnet-DiceCELoss

[kaggle-notebook](https://www.kaggle.com/code/yufang18/mitb5-manet-diceceloss/notebook)  
[wandb-run]()

