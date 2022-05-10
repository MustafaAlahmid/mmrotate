
# the new config inherits the base configs to highlight the necessary modification
_base_ = 'D:/mmlab/mmrotate-main/configs/rotated_retinanet/rotated_retinanet_hbb_r50_fpn_1x_dota_oc.py'

# 1. dataset settings
dataset_type = 'DOTADataset'
CLASSES = ('CDIC_retro', 'CDIE_front')

data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=CLASSES,
        ann_file='D:/mmlab/mmrotate-main/data/split_ms_dota/trainval/annfiles',
        img_prefix='D:/mmlab/mmrotate-main/data/split_ms_dota/trainval/images'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=CLASSES,
        ann_file='D:/mmlab/mmrotate-main/data/split_ms_dota/trainval/annfiles',
        img_prefix='D:/mmlab/mmrotate-main/data/split_ms_dota/trainval/images'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=CLASSES,
        ann_file='D:/mmlab/mmrotate-main/data/split_ms_dota/test/annfiles',
        img_prefix='D:/mmlab/mmrotate-main/data/split_ms_dota/test/images'))

# 2. model settings
model = dict(
    bbox_head=dict(
        type='RotatedRetinaHead',
        # explicitly over-write all the `num_classes` field from default 15 to 5.
        num_classes=2))
