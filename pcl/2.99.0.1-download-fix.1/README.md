# Plain Craft Launcher (PCL) CQin04 下载入口修复版

原作者：**龙腾猫跃** · [原项目](https://github.com/Meloong-Git/PCL) · [赞助原作者](https://afdian.com/a/LTCat)

这是第三方基于 PCL 独立修改的下载入口修复版，与官方无隶属关系。

| 项目 | 版本 |
| --- | --- |
| 原始程序 | PCL 正式版 **2.99.0.1**，内部构建号 **415** |
| 本次发布 | **2.99.0.1-download-fix.1** |
| 修复日期 | 2026-11-08（北京时间） |
| 程序内部文件版本 | **2.99.0.1**，保持原值 |
| 对比旧版 | PCL **2.12.1.0**，构建号 **379** |

## 下载与使用

[下载修复程序包 PCL-2.99.0.1-download-fix.1.zip](https://github.com/CQin04/minecraft-resources/releases/download/pcl-2.99.0.1-download-fix.1/PCL-2.99.0.1-download-fix.1.zip)

[查看发布页和校验文件](https://github.com/CQin04/minecraft-resources/releases/tag/pcl-2.99.0.1-download-fix.1)

1. 关闭 PCL，保留原启动器备份。
2. 解压程序包，将其中的 `Plain Craft Launcher (PCL) CQin04 Download Fix 2.99.0.1-fix.1.exe` 放进自己的 PCL 目录，再运行。
3. 打开“下载 → 原版游戏”，选择版本后点击“开始下载”。没有游戏版本时，也可以从首页“下载游戏”进入。
4. 如果需要回退，关闭修复版，再运行之前保留的原启动器。

程序包仅包含修复后的启动器、补丁源码、修改记录、许可和说明。原作者信息、赞助入口、正版购买提示及蓝色默认界面沿用原程序。

## 修了什么

- 恢复下载页左侧“原版游戏”和“社区资源”标题。
- 恢复实际 Minecraft 版本列表加载，替换“关闭下载”错误加载器。
- 没有游戏版本时，恢复首页“下载游戏”按钮。

本次只恢复上述三个入口路径。整合包安装中另外的下载限制不属于本补丁覆盖范围。

## 怎么修改的

对比本地旧版与新版的 .NET IL，并核对[官方源码快照](https://github.com/Meloong-Git/PCL/tree/93ede5d9e638c99fcec853a9ba1eecd91ceee7f5)。该快照中 `ModSecret.vb` 的 `RestrictMcDownload` 常量为 `True`，编译器已把调用位置的限制固化进 EXE，因此仅改常量的元数据不能恢复功能。

本补丁直接修正三个方法中现有的 IL 字节，保留全部资源、依赖、元数据标记和文件长度。三个编辑区域共 50 字节，其中实际变化 **43 字节**。

| 方法 | EXE 文件偏移（十进制） | 修改内容 |
| --- | ---: | --- |
| `PageDownloadInstall.LoaderInit` | 180590，长度 48 | 将创建“关闭下载”加载器的代码替换为 `ldsfld DlClientListLoader`，字段标记 `0x0400040F`；剩余位置填充 `nop`，保留原回调与后续调用。 |
| `PageDownloadLeft..ctor` | 404991，长度 1 | 将 `InitializeComponent()` 后的 `ldarg.0`（`02`）改为 `ret`（`2A`），与旧版一样保留默认原版游戏下载页。 |
| `PageLaunchLeft.RefreshButtonsUI` | 392649，长度 1 | 将没有游戏版本时的状态从 `1`（禁用）改为现有的 `2`（下载游戏），即 `17 → 18`。 |

首页无版本路径会直接进入下载状态；此处没有重新引入旧版对 `UiHiddenPageDownload` 设置的条件分支。已有游戏版本时的启动路径未改动。

完整的修改前后字节、方法 RVA、IL 偏移及校验值见 [patch-report.json](patch-report.json)。补丁源码见 [apply_patch.py](apply_patch.py)，仅依赖 Python 3 标准库。

### 自行复现

准备与下列原始 SHA256 **完全相同**的未修改 PCL 2.99.0.1，并将 `apply_patch.py` 与 `patch-report.json` 放在同一目录：

```text
python apply_patch.py "原始的 Plain Craft Launcher 2.exe" "PCL-2.99.0.1-download-fix.1.exe"
```

输出路径必须不存在。脚本会先检查原文件 SHA256、每个修改区域的原始字节，再确认输出 SHA256，全部匹配后才写入新文件。它不会覆盖输入文件或已有输出。不同版本、重复打补丁及其他修改过的程序会被拒绝。

## 校验与验证

原始 EXE SHA256：

```text
0db34e19d9eeb6d496d20fabe786ec16bbd36ba6b0ccdc8d29cb7e909c114397
```

修复后 EXE SHA256：

```text
eca243d2f483fb4fca8c1685758bb05d2c3a96b448ce2b89f0e5d3f3c042b1d4
```

EXE 大小：6,013,952 字节。

- 已实际启动，确认原版游戏入口、首页下载按钮正常。
- 已确认 Mojang 官方版本列表加载完成、正式版分类可展开。
- 已选择 26.3 进入安装页面，确认“开始下载”按钮可用。
- 用户随后反馈“验证过可以正常用”。
- 发布前重新运行补丁生成，结果与用户已验证的 EXE 逐字节一致。

自动复现与发布校验未执行完整游戏下载；以上用户使用反馈单独记录。Release 附带的 `SHA256SUMS` 同时列出压缩包和 EXE 的 SHA256。

## 来源与许可

PCL 原作者为龙腾猫跃，原项目及代码归原作者和相应贡献者所有。本目录保留上游 [LICENCE](LICENCE)，不将原程序改授为其他许可证。上游源码链接仅用于说明代码来源；发布的二进制是对本地 2.99.0.1 的三个方法进行修改，并非声称从该公开快照完整编译。

参考文件：

- [ModSecret.vb](https://github.com/Meloong-Git/PCL/blob/93ede5d9e638c99fcec853a9ba1eecd91ceee7f5/Plain%20Craft%20Launcher%202/Modules/ModSecret.vb)
- [PageDownloadInstall.xaml.vb](https://github.com/Meloong-Git/PCL/blob/93ede5d9e638c99fcec853a9ba1eecd91ceee7f5/Plain%20Craft%20Launcher%202/Pages/PageDownload/PageDownloadInstall.xaml.vb)
- [PageDownloadLeft.xaml.vb](https://github.com/Meloong-Git/PCL/blob/93ede5d9e638c99fcec853a9ba1eecd91ceee7f5/Plain%20Craft%20Launcher%202/Pages/PageDownload/PageDownloadLeft.xaml.vb)
- [PageLaunchLeft.xaml.vb](https://github.com/Meloong-Git/PCL/blob/93ede5d9e638c99fcec853a9ba1eecd91ceee7f5/Plain%20Craft%20Launcher%202/Pages/PageLaunch/PageLaunchLeft.xaml.vb)
