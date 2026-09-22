"""expense_cli.py —— 命令行记账小工具（A1 阶段练手项目）

用法：
    python expense_cli.py add 25.5 午饭      记一笔（金额 + 备注）
    python expense_cli.py list               列出全部账目
    python expense_cli.py list 2026-09       只看某个月
    python expense_cli.py total              合计全部
    python expense_cli.py total 2026-09      某个月合计
    python expense_cli.py delete 2           删掉序号为 2 的那笔
    python expense_cli.py help               看这份说明

数据存在脚本同目录的 records.json 里。
用到的 5 个知识点：sys.argv / open-with / json / try-except / datetime
"""

import datetime
import json
import sys
from pathlib import Path

# Path(__file__) = 这个脚本自己的路径，.parent = 它所在的文件夹。
# 好处：不管你在哪个目录敲命令，records.json 都固定放在脚本旁边，不会乱跑。
DATA_FILE = Path(__file__).parent / "records.json"


# ------------------------------------------------------------------ 读 / 写

def load_records():
    """读出全部账目，返回一个列表。文件不存在、内容坏掉时都返回空列表。"""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, encoding="utf-8") as f:  # 默认 r = 读
            data = json.load(f)                       # 文件里的 JSON → Python 对象
    except json.JSONDecodeError:
        print(f"[错误] {DATA_FILE.name} 不是合法的 JSON，本次按空账本继续。")
        return []
    except OSError as exc:
        print(f"[错误] 读不了 {DATA_FILE.name}：{exc}")
        return []

    if not isinstance(data, list):
        print(f"[错误] {DATA_FILE.name} 顶层应该是一个列表，实际是 {type(data).__name__}。")
        return []
    return data


def save_records(records):
    """把列表写回文件（w = 覆盖写）。"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        # ensure_ascii=False 让中文按原样存；indent=2 让文件人能看懂
        json.dump(records, f, ensure_ascii=False, indent=2)


# ------------------------------------------------------------------ 小工具

def to_amount(text):
    """把命令行传来的字符串转成金额；转不了就返回 None。"""
    try:
        amount = float(text)
    except ValueError:
        print(f"[错误] 金额必须是数字，你输入的是：{text}")
        return None

    if amount <= 0:
        print(f"[错误] 金额必须大于 0，你输入的是：{text}")
        return None
    return amount


def today():
    """今天的日期，形如 '2026-09-22'（字符串）。"""
    return datetime.date.today().isoformat()


def indexed(records, month=None):
    """把列表变成 [(全局序号, 记录), ...]，序号从 1 开始。

    delete 用的就是这个全局序号；即使按月份筛选，序号也不变，避免删错。
    """
    pairs = list(enumerate(records, start=1))
    if month is None:
        return pairs
    return [(i, r) for i, r in pairs if str(r.get("date", "")).startswith(month)]


def format_row(index, record):
    """把一笔账排成一行；金额坏掉也不会让程序崩。"""
    date = record.get("date", "?")
    note = record.get("note", "")
    try:
        amount = f"{float(record.get('amount')):>10.2f}"
    except (TypeError, ValueError):
        amount = f"{record.get('amount')!r:>10}"
    return f"{index:>3}   {date:<10} {amount}  {note}"


def sum_amount(records):
    """求合计；顺手跳过金额坏掉的记录，不崩。"""
    total = 0.0
    for record in records:
        try:
            total += float(record.get("amount", 0))
        except (TypeError, ValueError):
            print(f"[提示] 跳过金额异常的一笔：{record}")
    return total


# --------------------------------------------------------------- 四个子命令

def cmd_add(args):
    """add <金额> <备注>"""
    if len(args) < 2:
        print("用法：python expense_cli.py add <金额> <备注>")
        return 1

    amount = to_amount(args[0])
    if amount is None:
        return 1

    note = " ".join(args[1:])  # 备注里带空格也完整保留
    records = load_records()
    records.append({"date": today(), "amount": amount, "note": note})
    save_records(records)

    print(f"[OK] 已记账：{today()}  {amount:.2f}  {note}（共 {len(records)} 笔）")
    return 0


def cmd_list(args):
    """list [年月]"""
    month = args[0] if args else None
    pairs = indexed(load_records(), month)

    if not pairs:
        print("（没有账目）" if month is None else f"（{month} 没有账目）")
        return 0

    print(f"{'序号':>3}   {'日期':<10} {'金额':>10}  备注")
    print("-" * 46)
    for index, record in pairs:
        print(format_row(index, record))
    print("-" * 46)
    print(f"共 {len(pairs)} 笔，合计 {sum_amount([r for _, r in pairs]):.2f}")
    return 0


def cmd_total(args):
    """total [年月]"""
    month = args[0] if args else None
    records = [record for _, record in indexed(load_records(), month)]

    if not records:
        print("（没有账目）" if month is None else f"（{month} 没有账目）")
        return 0

    print(f"{month or '全部'} 合计：{sum_amount(records):.2f}（{len(records)} 笔）")
    return 0


def cmd_delete(args):
    """delete <序号>"""
    if len(args) != 1:
        print("用法：python expense_cli.py delete <序号>（序号看 list 的第一列）")
        return 1

    try:
        index = int(args[0])
    except ValueError:
        print(f"[错误] 序号必须是整数，你输入的是：{args[0]}")
        return 1

    records = load_records()
    if not 1 <= index <= len(records):
        print(f"[错误] 序号超范围：当前共 {len(records)} 笔，你输入的是 {index}")
        return 1

    removed = records.pop(index - 1)  # 序号从 1 开始，列表下标从 0 开始
    save_records(records)
    print(
        f"[OK] 已删除第 {index} 笔：{removed.get('date', '?')}  "
        f"{removed.get('amount', '?')}  {removed.get('note', '')}（剩 {len(records)} 笔）"
    )
    return 0


# -------------------------------------------------------------------- 入口

COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "total": cmd_total,
    "delete": cmd_delete,
}


def main(argv):
    """argv 就是 sys.argv，形如 ['expense_cli.py', 'add', '25', '午饭']。"""
    if len(argv) < 2 or argv[1] in ("help", "-h", "--help"):
        print(__doc__)
        return 0

    command = argv[1]
    handler = COMMANDS.get(command)
    if handler is None:
        print(f"[错误] 不认识这个命令：{command}\n")
        print(__doc__)
        return 1

    return handler(argv[2:])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
