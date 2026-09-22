# Python-Lab

我的 Python 练习仓库。里面都是能直接跑起来的小工具，配合 AI Agent 转码路线 A 段使用。

## 环境

- Python 3.13.9（`D:\develop`）
- 虚拟环境在项目内 `venv\`，**不要移动项目文件夹**（移动后 venv 会失效）

```powershell
cd D:\Documents\ChatGPT\repositary\Python-Lab
venv\Scripts\activate
pip install -r requirements.txt
```

判断激活是真的：`where python` 第一行应该是 `...\Python-Lab\venv\Scripts\python.exe`。

## 目录结构

```
Python-Lab\
├─ expense_cli.py     记账命令行工具（本项目第一个完整脚本）
├─ records.json       账目数据（由 expense_cli.py 自动生成，跟着脚本走）
├─ practice\          单个知识点的验证脚本，一个文件对应一个知识点
│  ├─ t1.py           sys.argv 命令行传参
│  ├─ t2.py           文件读写 open / with
│  ├─ t3.py           JSON 读写
│  ├─ t4.py           异常处理 try / except
│  └─ t5.py           datetime 日期
├─ requirements.txt   依赖清单
└─ README.md
```

## expense_cli.py 怎么跑

```powershell
python expense_cli.py add 25.5 午饭
python expense_cli.py add 8 地铁
python expense_cli.py add 128 "买了本书，满减后价格"

python expense_cli.py list              # 列出全部，第一列是序号
python expense_cli.py list 2026-09      # 只看某个月
python expense_cli.py total             # 合计
python expense_cli.py total 2026-09     # 某个月合计
python expense_cli.py delete 2          # 删掉序号 2 的那笔
python expense_cli.py help              # 用法说明
```

要点：

- 金额是数字，备注可以有空格（要用引号包起来）
- 备注会把后面的词全部拼起来，所以 `add 20 早饭 加豆浆` 记成「早饭 加豆浆」
- 每笔自动带上今天日期，数据存在 `records.json`
- 删错、金额写错、`records.json` 被改坏，都不会崩，只会提示一句人话

## 常用命令备忘

| 命令 | 作用 |
| --- | --- |
| `git status` | 看有哪些改动 |
| `git add .` | 把改动放进暂存区 |
| `git commit -m "说明"` | 存成一个版本 |
| `git push` | 推到 GitHub |
| `where python` | 确认当前用的是哪个解释器 |
