# 哔哩哔哩私信聊天记录获取工具

## 简介

此工具允许你从哔哩哔哩私信中下载聊天记录，保存为 **.json** 形式，并从聊天消息中提取图片链接。

## 使用方法

### 前提条件

- 已安装 Python 3.x
- 必需的 Python 包：`requests`, `pickle`, `winreg`, `json`, `time`
- Windows 操作系统

---

### 获取 `SESSDATA` 和 `bili_jct`

1. **登录哔哩哔哩网站**：
   - 使用你的浏览器登录到哔哩哔哩的账号。
   - 确保你已经登录并能够访问私信页面。

2. **打开开发者工具**：
   - 在浏览器中按下 F12 键（或右键点击页面并选择“检查”），打开开发者工具。

3. **选择“网络”选项卡**：
   - 在开发者工具中，选择“网络”选项卡。

4. **刷新页面**：
   - 刷新哔哩哔哩页面，以便开发者工具捕获网络请求。

5. **查找请求中的 Cookie**：
   - 在网络请求列表中，找到包含私信请求的条目（通常以 `api.vc.bilibili.com` 开头）。
   - 点击该请求条目，在右侧的“标头”选项卡下找到“请求标头”部分。
   - 在请求标头中，可以找到名为 `Cookie` 的字段。

6. **复制 SESSDATA 和 bili_jct**：
   - 在 Cookie 字段中，复制包含 `SESSDATA` 和 `bili_jct` 的值。这些值通常以分号分隔，类似于 `SESSDATA=xxxxxxxx; bili_jct=xxxxxxxx`。

---

### 使用步骤

1. **克隆仓库:**

   ```bash
   git clone https://github.com/happycola233/Bilibili-Chat-History-Downloader.git
   cd Bilibili-Chat-History-Downloader
   ```
2. **运行程序:**

   - 打开终端或命令提示符，并导航到仓库目录。
   - 运行 Python 脚本:
     ```bash
     python src/B站聊天记录爬取.py
     ```
3. **选择操作:**

   - 输入 `1` 爬取聊天记录。
   - 输入 `2` 提取聊天消息中的图片链接。
4. **提供必要信息:**

   - 对于选项 `1`: 输入 SESSDATA、bili_jct 和 UID。
   - 对于选项 `2`: 选择一个聊天记录文件 (`*.txt` 文件)。
5. **输出结果:**

   - 文件将保存在你的桌面上：
     - `UID{uid}_变量全信息.txt`: 原始聊天记录数据（JSON）。
     - `UID{uid}_美化.txt`: 格式化的聊天记录数据（美化版 JSON）。
     - `消息图片链接提取.txt`: 从聊天消息中提取的图片链接（选项 2）。


## 注意事项

- 确保你有足够的权限和凭据（SESSDATA、bili_jct、UID）来访问哔哩哔哩的私信 API。
- 此工具仅供个人使用，请谨慎使用。