# Python-Lab

Python 工程化练习仓库。用来把 Python 基础变成「能干活」的脚本。
环境：Windows + Python 3.13.9

---

## 一、环境准备

```powershell
# 1. 创建虚拟环境（只需做一次）
python -m venv venv

# 2. 激活虚拟环境（每次新开终端都要做）
venv\Scripts\activate

# 3. 安装依赖（只需做一次）
pip install -r requirements.txt
```

**怎么确认激活成功**：

```powershell
where python
```

第一行必须是 `...\Python-Lab\venv\Scripts\python.exe`。
如果显示 `D:\develop\python.exe`，说明没激活，此时 `pip install` 会把包装到系统里。

> ⚠️ 虚拟环境建好后**不要移动文件夹**。移动会导致 pip / activate 失效，只能删掉 `venv` 重建。

---

## 二、脚本

### 1. `expense_cli.py` —— 命令行记账工具

数据存在脚本旁边的 `records.json`。

```powershell
python expense_cli.py add 25.5 午饭    # 记一笔
python expense_cli.py list            # 列出全部，底部显示合计
python expense_cli.py total           # 只看总额和笔数
python expense_cli.py delete 1        # 删除第 1 条
python expense_cli.py help            # 查看用法
```

异常输入（金额不是数字、序号超范围）会给出友好提示，不会崩溃。

### 2. `api_demo.py` —— 调用公开 API 并保存为本地 JSON

调用 `https://jsonplaceholder.typicode.com/posts`，取前 10 条写进 `data/posts.json`。

```powershell
python api_demo.py
```

成功会打印：`前10条数据已保存到data/posts.json`

三个必须记住的点：

1. `timeout` 一定要给，否则网络挂住会卡死整个程序
2. `r.raise_for_status()` 把 4xx/5xx 变成异常，否则会拿到一堆错误 HTML 还以为成功了
3. 写文件必须带 `encoding="utf-8"`，Windows 默认 GBK，中文会炸

---

## 三、目录说明

| 路径 | 说明 | 是否进 Git |
| --- | --- | --- |
| `expense_cli.py` | 命令行记账工具 | ✅ |
| `api_demo.py` | 调 API 存 JSON | ✅ |
| `requirements.txt` | 依赖清单 | ✅ |
| `data/` | 脚本生成的数据 | ❌ 已 gitignore |
| `venv/` | 虚拟环境 | ❌ 已 gitignore |
| `records.json` | 记账数据（本地） | ❌ |
| `practice/expense_cli.py` | 空文件，待删除 | — |

---

## 四、依赖

```
requests==2.34.2
```

---

## 五、Git 常用命令

```powershell
git status                  # 看改了什么
git add 文件名              # 放进待提交区（不要用 git add .）
git commit -m "说明"        # 打包成一个版本
git push                    # 推到 GitHub
git log --oneline -5        # 看最近 5 次提交
```

提交说明前缀：`feat:` 新功能 ｜ `fix:` 修 bug ｜ `docs:` 只改文档 ｜ `refactor:` 重写代码

---

## 六、进度

- [x] venv + requirements.txt
- [x] `expense_cli.py`（文件 IO + JSON + 异常 + 命令行参数）
- [x] `api_demo.py`（requests 调 API + 存 JSON）
- [ ] `logging` 版脚本
- [ ] `pytest` 用例（M1 要求）
- [ ] `pydantic` / pandas 入门

> MySQL 与 SQL 练习文件放在 `D:\学习进度\<日期>\sql\`，不进本仓库。
