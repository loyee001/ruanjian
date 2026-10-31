# 等你来 · 软件

Android 原生桌面求助器应用。ESP32 蓝牙按钮发起求助，手机逐级提醒，并记录回应与完成。这里使用平铺文件上传；完整源码和目录结构保存在 ZIP 中。

## 安装包

| 文件 | 用途 |
| --- | --- |
| [蓝牙原版 APK](deng-ni-lai-0.2.1-bluetooth.apk) | `com.loyee.dengnilai`，`0.2.1-bluetooth`，versionCode 3 |
| [独立模拟版 APK](deng-ni-lai-0.2.1-simulation.apk) | `com.loyee.dengnilai.simulation`，`0.2.1-simulation`，versionCode 3；有“5 秒后按一次”和“5 秒后连续按 3 次” |

两个包均为此前已生成的调试安装包，按原字节保留，最低 Android 8（API 26），目标 Android 15（API 35）。原版与模拟版使用不同包名，可以并装。

## 源码归档

- [稳定版完整源码 ZIP](software-source-0.2.1.zip)：0.2.1 的 Java/资源、Manifest、测试、Gradle 配置、构建和验收脚本、说明、校验记录以及完整目录清单。解压后根目录为 `software/`。
- [未完成开发快照 ZIP](software-development-incomplete-20261031.zip)：2026-10-31 晚间的“拍拍小怪兽”新界面、密码与协议相关开发，含源码、资源、测试、脚本、说明和检查记录。解压后放入 `software/development/source-snapshot-20261031/`。

**开发快照未完成，缺少 `AgreementActivity.java`，不能完整编译。它没有包含在上面的 0.2.1 安装包中。** 两个 ZIP 均不嵌入 APK，也不包含签名私钥、SDK、缓存、调试日志或使用者记录。

## 恢复完整项目结构

把本目录的两个 ZIP 和两个 APK 下载到一个空文件夹，在该文件夹打开终端，依次运行：

```sh
unzip software-source-0.2.1.zip
unzip software-development-incomplete-20261031.zip
mkdir -p software/releases/0.2.1
cp deng-ni-lai-0.2.1-bluetooth.apk software/releases/0.2.1/
cp deng-ni-lai-0.2.1-simulation.apk software/releases/0.2.1/
```

得到的结构为：

```text
software/
  app/                         稳定版源码与资源
  tests/                       稳定版测试
  simulation/                  独立模拟构建补丁
  tools/                       可选验收脚本
  releases/0.2.1/               两个原始 APK
  development/source-snapshot-20261031/  未完成开发快照
  verification/                脱敏校验记录
  README.md
  manifest.json
  test.sh
  manual-build.sh
  build-simulation.sh
  build.gradle
  settings.gradle
  source-provenance.json
```

已实际按上述归档加 APK 重组，并对照原完整交付目录：**69 项清单文件，加清单本身，共 70 个文件全部恢复，逐文件 SHA-256 一致。** 没有遗漏测试、资源或文档。

## 构建与验证

需要自行安装 JDK 17、Android SDK Platform 35 和 Build Tools 35.0.0。进入恢复后的 `software/`，按照其中 README 设置工具路径，再运行 `bash test.sh`、`bash manual-build.sh`、`bash build-simulation.sh`。

稳定版的 10 个 `app/src/main/` 文件已与历史构建快照逐一核对哈希；49 条状态与 BLE 协议检查通过，原版和模拟版在导出副本中重新构建、签名检查通过。重新构建的 `classes.dex`、`resources.arsc` 和 `AndroidManifest.xml` 与两个已有 APK 逐项一致。开发快照的 229 条策略检查通过，完整编译未通过。

简洁结论见 [版本和构建校验](version-build-verification.json)，本目录文件大小和 SHA-256 见 [web-manifest.json](web-manifest.json)。完整项目恢复后另有 `software/manifest.json`，覆盖归档中的全部交付文件。

本次上传整理没有操作手机或重新进行蓝牙、跨应用弹窗实测。悬浮提醒受 Android 系统和其他应用限制，不能保证所有场景均可覆盖。自行构建会使用自己的调试密钥，通常不能直接覆盖已有签名的 APK；本仓库没有发布原开发者私钥。

配套固件与接线：[loyee001/yingjian](https://github.com/loyee001/yingjian)。
