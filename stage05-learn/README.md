# SMUet-0404

## stage05-learn

修改代码，熟悉code

---

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


### MViTUNet

encoder_name='mit_b2'，in_channels=3

kaggle-notebook
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/76hx468j)

### DiceCELoss

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

### smp-DiceLoss
[kaggle-notebook](https://www.kaggle.com/code/gemini2024/smp-diceloss/notebook) 
[wandb-run](https://wandb.ai/team-mykcs/UNet_Compare/runs/514ebpd6)
