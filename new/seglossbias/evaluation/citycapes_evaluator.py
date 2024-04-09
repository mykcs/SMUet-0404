import numpy as np
import logging
from terminaltables import AsciiTable
import wandb

from .evaluator import DatasetEvaluator
from .metric import intersect_and_union

logger = logging.getLogger(__name__)


class CityscapesEvaluator(DatasetEvaluator):
    """Evaluate semantic segmenation performance on Cityscapes by IoU"""
    classes = [
        'road', 'sidewalk', 'building', 'wall', 'fence', 'pole',
        'traffic light', 'traffic sign', 'vegetation', 'terrain', 'sky',
        'person', 'rider', 'car', 'truck', 'bus', 'train', 'motorcycle',
        'bicycle',
    ]

    def __init__(self, ignore_index: int = 255):
        self.ignore_index = ignore_index
        self.num_classes = len(self.classes)
        self.reset()

    def num_samples(self):
        return self.nsamples

    def reset(self):
        self.total_area_intersect = np.zeros((self.num_classes, ), dtype=np.float)
        self.total_area_union = np.zeros((self.num_classes, ), dtype=np.float)
        self.total_area_pred_label = np.zeros((self.num_classes, ), dtype=np.float)
        self.total_area_label = np.zeros((self.num_classes, ), dtype=np.float)
        self.nsamples = 0

    def main_metric(self):
        return "miou"

    def update(self, pred: np.array, target: np.array):
        pred_labels = np.argmax(pred, axis=1)
        total_area_intersect = np.zeros((self.num_classes, ), dtype=np.float)
        total_area_union = np.zeros((self.num_classes, ), dtype=np.float)
        total_area_pred_label = np.zeros((self.num_classes, ), dtype=np.float)
        total_area_label = np.zeros((self.num_classes, ), dtype=np.float)
        for i in range(pred_labels.shape[0]):
            area_intersect, area_union, area_pred_label, area_label = (
                intersect_and_union(pred_labels[i],
                                    target[i],
                                    self.num_classes,
                                    self.ignore_index)
            )
            total_area_intersect  += area_intersect
            total_area_union += area_union
            total_area_pred_label += area_pred_label
            total_area_label += area_label

        self.total_area_intersect += total_area_intersect
        self.total_area_union += total_area_union
        self.total_area_pred_label += total_area_pred_label
        self.total_area_label += total_area_label
        self.nsamples += pred_labels.shape[0]

        iou = total_area_intersect.sum() / (np.spacing(1) + total_area_union.sum())

        self.curr = {"iou": iou}

        return iou

    def curr_score(self):
        return self.curr

    def mean_score(self, all_metric=False):
        class_acc = self.total_area_intersect / (np.spacing(1) + self.total_area_label)
        class_iou = self.total_area_intersect / (np.spacing(1) + self.total_area_union)

        class_table_data = [["id"] + ["Class"] + ["IoU"] + ["acc"]]
        for i in range(class_acc.shape[0]):
            class_table_data.append(
                [i] + [self.classes[i]]
                + ["{:.4f}".format(class_iou[i])]
                + ["{:.4f}".format(class_acc[i])]
            )
        miou = np.mean(class_iou)
        macc = np.mean(class_acc)
        class_table_data.append(
            [None] + ["mean"]
            + ["{:.4f}".format(miou)]
            + ["{:.4f}".format(macc)]
        )

        metric = {"miou": miou, "macc": macc}

        if not all_metric:
            return miou
        else:
            return metric, class_table_data

    def wandb_score_table(self):
        _, table_data = self.mean_score(all_metric=True)
        return wandb.Table(
            columns=table_data[0],
            data=table_data[1:]
        )

    def class_score(self):
        class_acc = self.total_area_intersect / (np.spacing(1) + self.total_area_label)
        class_iou = self.total_area_intersect / (np.spacing(1) + self.total_area_union)
        class_table_data = [["id"] + ["Class"] + ["IoU"] + ["acc"]]
        for i in range(class_acc.shape[0]):
            class_table_data.append(
                [i] + [self.classes[i]]
                + ["{:.4f}".format(class_iou[i])]
                + ["{:.4f}".format(class_acc[i])]
            )
        class_table_data.append(
            [""] + ["mean"]
            + ["{:.4f}".format(np.mean(class_iou))]
            + ["{:.4f}".format(np.mean(class_acc))]
        )
        table = AsciiTable(class_table_data)
        logger.info("\n" + table.table)
        return class_iou
