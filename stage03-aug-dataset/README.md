# SMUet-0404

## stage03-aug-ddataset

lgy [kaggle notebook](https://www.kaggle.com/code/liaoguoying/delve-into-aug-a-new-dataset-for-fine-tune)

[self fork](https://www.kaggle.com/code/yufang18/fork-delve-into-aug-a-new-dataset-for-fine-tuning/output)

生成了新dataset [Aug Dataset for Fine-tune](https://www.kaggle.com/datasets/liaoguoying/aug-dataset-for-fine-tune)


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

---

### lossHign-04100102
github notebook

[kaggle notebook](https://www.kaggle.com/code/mykcs01/loss-04100102/notebook)

[wandb run](https://wandb.ai/team-mykcs/UNet_Compare/runs/k74z1q5q)

[poor model](https://wandb.ai/team-mykcs/UNet_Compare/artifacts/model/poor-model-04100102)

### loss-high-04100202

[github notebook](https://github.com/mykcs/SMUet-0404/blob/main/loss-high-04100202.ipynb)

[wandb run](https://wandb.ai/team-mykcs/UNet_Compare/runs/5sm6w8km)

### epo480-half-04100132

按理说，这个也用了tuner。 应该loss high的，但是正常训练。

[wandb run](https://wandb.ai/team-mykcs/UNet_Compare/runs/y10ndgqn)
可以看到后面有点过拟合了。

### epo120-04100227
github notebook

[kaggle notebook](https://www.kaggle.com/code/mykcs01/epo120-04100227/notebook)

[wandb run](https://wandb.ai/team-mykcs/UNet_Compare/runs/3huy70i6)

model 在另一个run上。[here](https://wandb.ai/team-mykcs/uncategorized/artifacts/model/model-epo120-04100227/v0)
把run移动走了，但是model还在原来的project里面，也无法移动。

重新建立了一个[run](https://wandb.ai/team-mykcs/UNet_Compare/runs/2zh292n0)，把model传上去。

### epo480-half-04100132


### epo120-AugDataset

### epo200-AugDataset-04100422
notebook [kaggle](https://www.kaggle.com/code/mykcs01/epo200-augdataset-04100422?scriptVersionId=171226718)

wandb [run](https://wandb.ai/team-mykcs/UNet_Compare/runs/z8norpkj/overview?nw=nwusermykcs)

model [kaggle](https://www.kaggle.com/code/mykcs01/epo200-augdataset-04100422/output?scriptVersionId=171226718)