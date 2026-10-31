# 等你来 · 建模文件

这里是便于 GitHub 网页下载的平铺交付。**打印用 3MF 可以直接下载后打开 Bambu Studio**；源码、STL、说明与网格预览按家族放在 ZIP 中。

## 直接打开的 9 个模型

| 文件 | 内容 | 版本/设备 |
| --- | --- | --- |
| [01-enclosure-v3-wide-two-parts.3mf](01-enclosure-v3-wide-two-parts.3mf) | **最新加宽外壳 + 匹配后盖** | V3，通用模型；按实际设备切片。 |
| [02-esp32-holder-with-fasteners.3mf](02-esp32-holder-with-fasteners.3mf) | ESP32 托座 + 2 螺丝 + 2 压片 | 板尺寸参考 52×28 mm；通用模型。 |
| [03-button-holder-with-fasteners.3mf](03-button-holder-with-fasteners.3mf) | 原尺寸按钮托座 + 2 螺丝 + 2 压片 | 原凹槽 30.6×20.6 mm；通用模型。 |
| [04-button-support-roomier-13-parts-P2S-0.4.3mf](04-button-support-roomier-13-parts-P2S-0.4.3mf) | **最新加大小底托 + 12 件承托柱组件** | P2S 0.4 mm Bambu 工程；凹槽 31.6×21.6 mm。 |
| [05-button-support-roomier-13-parts-generic.3mf](05-button-support-roomier-13-parts-generic.3mf) | 同上 13 件，已排在同一盘 | 通用模型，无设备参数。 |
| [06-adjustable-support-12-parts-generic.3mf](06-adjustable-support-12-parts-generic.3mf) | 仅 12 件可调承托柱组件 | 通用模型，不含按钮底托。 |
| [07-black-pupils-two.3mf](07-black-pupils-two.3mf) | 两只黑色眼珠 | Bambu 保存模型，打印时重选实际设备和耗材。 |
| [08-black-smile.3mf](08-black-smile.3mf) | 黑色笑嘴 | 通用模型。 |
| [09-enclosure-v2-reference-two-parts.3mf](09-enclosure-v2-reference-two-parts.3mf) | 旧 V2 外壳 + 后盖 | 版本参考；不能把 V2 后盖与 V3 主体混用。 |

全部尺寸单位为毫米，不含 G-code。绿色顶部按钮帽位于 `07-original-interface-and-pupils.zip` 中。眼珠、笑嘴、按钮帽继续使用原接口；V3 主体后口为 80×56 mm、匹配后盖为 90×64 mm。V3 顶棚/按钮导向结构需在切片预览核对支撑。

## 分类 ZIP

| 压缩包 | 包含内容 |
| --- | --- |
| [00-models-instructions-and-build-tools.zip](00-models-instructions-and-build-tools.zip) | 完整原始 README、模型清单、复建顺序、依赖、解压及辅助脚本。 |
| [01-enclosure-v3-wide-source-and-stl.zip](01-enclosure-v3-wide-source-and-stl.zip) | 最新 V3 主体/后盖 STL、源码、检查记录、真实网格预览。 |
| [02-board-holders-and-fasteners.zip](02-board-holders-and-fasteners.zip) | ESP32/按钮托座、自定义螺丝、压片的 STL、源码及说明。 |
| [03-adjustable-support-and-roomier-tray.zip](03-adjustable-support-and-roomier-tray.zip) | 轻量承托柱各型 STL、最新加大底托 STL、源码、装配说明及检查。 |
| [04-enclosure-v2-reference-source.zip](04-enclosure-v2-reference-source.zip) | V2 对照源码与说明，供复建历史四盘使用。 |
| [05-four-plate-rebuild-source.zip](05-four-plate-rebuild-source.zip) | 旧 V2 四盘工程的复建源码；超限旧合并 3MF 未重复上传。 |
| [06-black-smile-source-and-stl.zip](06-black-smile-source-and-stl.zip) | 笑嘴 STL、源码与实际网格装配预览。 |
| [07-original-interface-and-pupils.zip](07-original-interface-and-pupils.zip) | **绿色按钮帽 STL**、眼珠 STL/源码、原始几何生成器及检查工具。 |

ZIP 内的所有文件路径都从 `models/` 开始；**解压到同一个位置**，目录会合并。ZIP 不重复存放上面的 9 个 3MF。两件大 STL 使用无损 `.stl.gz`，可在还原后运行 `python3 models/extract_stl.py` 解压。

## 一次恢复完整目录

将本页全部文件下载到同一个文件夹，运行：

```bash
python3 restore_models.py
```

脚本会核对本页文件哈希，解压全部 ZIP 到同一位置，把 9 个 3MF 恢复到原相对路径，再逐件核对原始 **80 个文件**。之后打开 `models/README.md` 即可按原结构阅读和复建。已有文件内容不同会停止，不会直接覆盖。也可以用 `--output 路径` 指定还原位置。

无需复建时，直接下载上表所需 3MF 即可。需要手动整理时，[model-file-map.json](model-file-map.json) 给出每个公开 3MF 的原始位置；[models-manifest.json](models-manifest.json) 是完整原目录的逐件 SHA-256 清单，[web-manifest.json](web-manifest.json) 是本页平铺交付清单。

本包保留数字网格检查证据；真实板厚、焊点、接头、按钮触发/回弹、打印收缩、螺纹插合和支承稳定性仍需实物核对。托座螺丝是自定义螺纹，不是标准 M3/M6。当前外壳没有扬声器孔或扬声器安装座。
