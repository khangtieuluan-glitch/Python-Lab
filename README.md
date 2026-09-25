# Python-Lab

Python 工程化练习仓库。记录从零开始练手的可运行脚本。
环境：Windows + Python 3.13.9

---

## 一、环境准备

```powershell
# 1. 创建虚拟环境（只需做一次）
python -m venv venv

# 2. 激活虚拟环境（每次开新的终端都要做）
venv\Scripts\activate

# 3. 安装依赖（只需做一次）
pip install -r requirements.txt
```

**怎么确认激活成功了**：

```powershell
where python
```

第一行必须是 `...\Python-Lab\venv\Scripts\python.exe`。
如果显示的是 `D:\develop\python.exe`，说明没激活成功，pip 会把包装到系统里。

> ⚠️ 虚拟环境建好之后**不要移动文件夹**，移动会导致 pip / activate 失效。
> 万一移了，删掉 `venv` 文件夹重建，再 `pip install -r requirements.txt`。

---

## 二、脚本说明

### 1. `expense_cli.py` —— 命令行记账工具

数据存在脚本旁边的 `records.json`。

```powershell
python expense_cli.py add 25.5 午饭    # 记一笔
python expense_cli.py list            # 列出全部，底部显示合计
python expense_cli.py total           # 只看总额和笔数
python expense_cli.py delete 1        # 删除第 1 条
python expense_cli.py help            # 查看用法
```

### 2. `api_demo.py` —— 调用公开 API 并保存为本地 JSON

调用 `https://jsonplaceholder.typicode.com/posts`，取前 10 条写进 `data/posts.json`。

```powershell
python api_demo.py
```

成功会打印：`前10条数据已保存到data/posts.json`

三个必须记住的点：

1. `timeout` 一定要给，否则网络挂住会卡死整个程序
2. `r.raise_for_status()` 把 4xx/5xx 变成异常，不然会拿到一堆错误 HTML 还以为成功了
3. 写文件必须带 `encoding="utf-8"`，Windows 默认是 GBK，中文会炸

---

## 三、目录说明

| 路径 | 说明 |
| --- | --- |
| `data/` | 脚本生成的数据，**已加入 .gitignore，不会上传** |
| `records.json` | 记账工具的数据文件（本地） |
| `venv/` | 虚拟环境，**已加入 .gitignore，不会上传** |
| `requirements.txt` | 依赖清单 |

---

## 四、常用 Git 命令

```powershell
git status                  # 看改了什么
git add 文件名              # 放进待提交区（不要用 git add .）
git commit -m "说明"        # 打包成一个版本
git push                    # 推到 GitHub
git log --oneline -5        # 看最近 5 次提交
```

提交说明前缀：`feat:` 新功能 ｜ `fix:` 修 bug ｜ `docs:` 只改文档 ｜ `refactor:` 重写代码
