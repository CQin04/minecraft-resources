# 伊蕾娜·巫师袍 2.3

Minecraft Java 版 **Yes Steve Model（YSM）** 模型备份。游戏内名称为“伊蕾娜”；“2.3”沿用原文件夹标记，不是 Minecraft 或 YSM 模组版本号。

## 下载

[下载完整 ZIP](https://github.com/CQin04/minecraft-resources/releases/download/ysm-elaina-wizard-robe-2.3/YSM-Elaina-Wizard-Robe-2.3.zip) · [Release 页面](https://github.com/CQin04/minecraft-resources/releases/tag/ysm-elaina-wizard-robe-2.3) · [SHA256 校验值](SHA256SUMS)

## 安装教程

### 1. 找到当前实例的模型目录

先为当前 Minecraft 版本和模组加载器安装匹配的 YSM，并启动一次游戏。

在 YSM 模型选择界面使用“打开模型文件夹”，或从启动器打开**当前游戏实例文件夹**，找到：

```text
config/yes_steve_model/custom/
```

开启版本隔离时，使用对应版本的实例目录，不要直接认定是启动器最外层的 `.minecraft`。

### 2. 解压并复制模型

退出游戏，完整解压下载的 ZIP。将其中 **`Elaina23` 整个文件夹**复制到 `custom` 中。

放好后的结构应为：

```text
当前游戏实例/
└─ config/
   └─ yes_steve_model/
      └─ custom/
         └─ Elaina23/
            ├─ ysm.json
            ├─ main.json
            ├─ animations/
            ├─ avatar/
            ├─ models/
            └─ textures/
```

关键检查：能找到 `custom/Elaina23/ysm.json`。不要把 `animations`、`models`、`textures` 等目录拆开单独放入 `custom`。

### 3. 进入游戏选择模型

重新启动游戏并进入世界，在按键设置中找到 YSM 的模型选择按键，打开模型界面，选择“伊蕾娜”。

## 找不到模型时

- 确认 YSM 已正常加载，且与当前游戏版本和模组加载器匹配。
- 检查实际放入的是当前实例的 `config/yes_steve_model/custom/`。
- 检查 `Elaina23/ysm.json` 是否存在、模型文件是否完整。
- 多人服务器的模型管理受服务端设置和权限限制，需由服主确认，不能保证只装客户端就能使用。

## 作者与许可

原模型署名 **friskid(伊雷娜教代行教皇)**，声明许可为 **CC BY-NC-SA 4.0**。详见 [许可与署名](LICENSE.md) 和原包内的 `ysm.json`。

本次保留全部 14 个原文件，未启动 Minecraft 或实测模型兼容性。原包根目录与 `models/` 下的 `main.json` 虽然内容相同，也一并保留。

参考：[YSM 模型目录说明](https://ysm.cfpa.team/wiki/type/) · [模型结构说明](https://ysm.cfpa.team/wiki/struct/)
