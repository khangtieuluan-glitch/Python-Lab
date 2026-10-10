# Python-Lab

Python 工程化练习仓库 —— 把 Python 基础变成「能干活」的东西。
环境：Windows + Python 3.13.9 ｜ 仓库：https://github.com/khangtieuluan-glitch/Python-Lab

**这个仓库证明了什么**：一个完整的工程闭环 —— 调 API + 读写文件 + 异常处理 + 双通道日志 + pytest 用例 + MySQL 建表查表 + 算法练习。
即「能写脚本」→「能交付一个有人用、坏了能查、改动有测试兜底的小系统」。

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

## 二、怎么跑测试（本仓库的验收方式）

在**仓库根目录**跑，**必须带 `-m`**：

```powershell
.\venv\Scripts\python.exe -m pytest -q
```

当前 17 个用例：`test_linked_list.py`(9) + `test_api_demo.py`(8)，期望输出 `17 passed`。

> 为什么必须用 `-m pytest` 而不是直接敲 `pytest`：直接敲时 pytest 不进 `sys.path` 的当前目录，
> `from linked_list import ...` 会报 `ModuleNotFoundError`。`python -m pytest` 会把当前目录加进去。

算法题**不进 pytest**（太重），每个文件自带 `assert` 自测，单独跑：

```powershell
.\venv\Scripts\python.exe leetcode/0001_two_sum.py
```

打印 `PASS  0001_two_sum` 就算过。

---

## 三、脚本

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

### 3. `csv_demo.py` —— CSV 读写

用标准库 `csv` 模块读写表格数据，不依赖 pandas。演示 `csv.DictReader` / `csv.DictWriter` 的用法。

### 4. `linked_list.py` —— 手写单链表

`Node` + `LinkedList`，含基础操作（`prepend` / `append` / `delete`）与进阶题（反转、找中点、判环）。
不看资料能默写出 `reverse` 的三指针，是刷栈/队列题的底子。

### 5. `hello_fastapi.py` —— FastAPI 起步（B 段）

```powershell
.\venv\Scripts\python.exe -m uvicorn hello_fastapi:app --reload
```

浏览器打开 http://127.0.0.1:8000/docs —— **一行文档都没写，Swagger UI 自动长出来了**。
`--reload` 表示改完代码保存即自动重启。

---

## 四、SQL

建表与查询脚本在 `SQL/`，跑在本地 MySQL 8.4（`python_lab` 库）。

```powershell
# 在 Git Bash / cmd 里（PowerShell 5.1 不认 `<`，会报 "The '<' operator is reserved for future use"）
"C:\Program Files\MySQL\MySQL Server 8.4\bin\mysql.exe" -u root -p --default-character-set=utf8mb4 python_lab < SQL/schema/02_agent_three_tables.sql
```

PowerShell 里改用管道喂：

```powershell
Get-Content SQL/schema/02_agent_three_tables.sql -Raw -Encoding UTF8 | & "C:\Program Files\MySQL\MySQL Server 8.4\bin\mysql.exe" -u root -p --default-character-set=utf8mb4 python_lab
```

| 文件 | 内容 |
| --- | --- |
| `SQL/schema/00_expenses_rename_column.sql` | 改列名（`ALTER TABLE`） |
| `SQL/schema/01_categories.sql` | 分类表 |
| `SQL/schema/02_agent_three_tables.sql` | **三张外键表**：`users` → `conversations` → `messages`，两个 `ON DELETE CASCADE` |
| `SQL/queries/01_group_by.sql` | 分组聚合 |
| `SQL/queries/02_join.sql` | 多表连接 + 子查询 |
| `SQL/queries/03_distinct_having.sql` | 去重 + `HAVING` 过滤分组 |

> 建表顺序有讲究：**先父后子**（`users` → `conversations` → `messages`），否则外键找不到被引用的表。

---

## 五、目录说明

| 路径 | 说明 | 是否进 Git |
| --- | --- | --- |
| `expense_cli.py` | 命令行记账工具 | ✅ |
| `api_demo.py` | 调 API 存 JSON | ✅ |
| `csv_demo.py` | CSV 读写 | ✅ |
| `linked_list.py` | 手写单链表 | ✅ |
| `hello_fastapi.py` | FastAPI 起步 | ✅ |
| `test_api_demo.py` / `test_linked_list.py` | pytest 用例（17 个） | ✅ |
| `SQL/` | 建表 + 查询脚本 | ✅ |
| `leetcode/` | 算法练习，每题自带 `assert` 自测 | ✅ |
| `practice/pydantic_demo.py` | pydantic 数据校验练习 | ✅ |
| `practice/_archive/` | 入门期小练习（`t1~t5`，保留备查） | ✅ |
| `requirements.txt` | 依赖清单 | ✅ |
| `data/` | 脚本生成的数据 | ❌ 已 gitignore |
| `venv/` | 虚拟环境 | ❌ 已 gitignore |
| `records.json` | 记账数据（本地） | ❌ |

---

## 六、依赖

见 `requirements.txt`（由 `pip freeze` 导出）。核心几个：

```
requests        # HTTP 请求
pydantic        # 数据校验（把 dict 变成有类型保证的对象）
pytest          # 测试
fastapi         # Web 框架
uvicorn         # ASGI 服务器（跑 fastapi）
```

---

## 七、Git 常用命令

```powershell
git status                  # 看改了什么
git add 文件名              # 放进待提交区
git commit -m "说明"        # 打包成一个版本
git push                    # 推到 GitHub
git log --oneline -5        # 看最近 5 次提交
```

提交说明前缀：`feat:` 新功能 ｜ `fix:` 修 bug ｜ `docs:` 只改文档 ｜ `test:` 加测试 ｜ `refactor:` 重写代码

---

## 八、进度

- [x] venv + requirements.txt
- [x] `expense_cli.py`（文件 IO + JSON + 异常 + 命令行参数）
- [x] `api_demo.py`（requests 调 API + 存 JSON）
- [x] `csv_demo.py`（CSV 读写）
- [x] `linked_list.py`（单链表 + 反转/中点/判环）
- [x] **logging 双通道**（控制台 + 文件，`api_demo.py` 内）
- [x] **pytest 17 个用例全绿**（`test_linked_list.py` + `test_api_demo.py`）
- [x] **pydantic 数据校验**（`practice/pydantic_demo.py`）
- [x] **MySQL 三张外键表**（`SQL/schema/02_agent_three_tables.sql`）
- [x] `hello_fastapi.py`（FastAPI 起步 + 自动文档）
- [ ] 算法：`0001_two_sum` ✅ / `0020_valid_parentheses` ✅ / 继续扩充中
- [ ] pandas 入门（工具，按需补）

**下一步（B 段）**：SQL 进阶 → FastAPI 路由 / 路径参数 / Pydantic 请求体 → `ledger-api`（20 个 pytest 用例）
