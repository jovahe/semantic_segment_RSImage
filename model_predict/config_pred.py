from collections import namedtuple


Config_Pred = namedtuple("Config_pred", [
  "img_input",
  "img_w",
  "img_h",
  "im_bands",
  "im_type",
  "target_name",
  "model_path",
  "activation",
  "mask_classes",
  "strategy",
  "window_size",
  "subdivisions",
  "slices",
  "block_size",
  "nodata",
  "mask_dir",
  "suffix"
])


