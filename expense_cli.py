"""expense_cli.py 完整参考答案。

运行位置：把本文件放进 Python-Lab 仓库根目录，改名为 expense_cli.py。

用法：
    python expense_cli.py add 25.5 午饭
    python expense_cli.py list
    python expense_cli.py total
    python expense_cli.py delete 1
    python expense_cli.py help
"""

import datetime
import json
import os
import sys


# __file__ 是当前脚本的路径。
# 这样无论从哪个目录运行，records.json 都会固定放在脚本旁边。
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "records.json")


def get_arg(index, name):
    """读取 sys.argv 中指定位置的参数；参数不存在时给出友好提示。"""
    try:
        return sys.argv[index]
    except IndexError:
        print(f"[错误] 缺少参数：{name}")
        return None


def load_records():
    """读取全部账目。

    文件不存在时返回空列表；JSON 内容损坏或文件无法读取时也返回空列表，
    避免整个程序直接崩溃。
    """
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            records = json.load(f)
    except json.JSONDecodeError:
        print("[错误] records.json 不是合法的 JSON，本次按空账本继续。")
        return []
    except OSError as exc:
        print(f"[错误] 无法读取 records.json：{exc}")
        return []

    if not isinstance(records, list):
        print("[错误] records.json 顶层必须是列表，本次按空账本继续。")
        return []

    return records


def save_records(records):
    """把账目列表以 JSON 格式写回文件。"""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def add():
    """添加一笔账目。"""
    amount_text = get_arg(2, "金额")
    if amount_text is None:
        return

    if len(sys.argv) < 4:
        print("[错误] 缺少参数：备注")
        return

    try:
        amount = float(amount_text)
    except ValueError:
        print(f"[错误] 金额必须是数字，你输入的是：{amount_text}")
        return

    if amount <= 0:
        print(f"[错误] 金额必须大于 0，你输入的是：{amount_text}")
        return

    # 备注可能有空格，所以把第 3 个及后面的参数全部拼起来。
    note = " ".join(sys.argv[3:])
    today = datetime.date.today().isoformat()

    records = load_records()
    records.append({
        "date": today,
        "amount": amount,
        "note": note,
    })
    save_records(records)

    print(f"[完成] 已记账：{today}  {amount:.2f}  {note}")


def list_all():
    """列出全部账目。"""
    records = load_records()

    if not records:
        print("（没有账目）")
        return

    print(" 序号  日期           金额  备注")
    print("-" * 45)

    total_amount = 0.0
    for index, record in enumerate(records, start=1):
        amount = float(record["amount"])
        total_amount += amount
        print(
            f"{index:>4}  {record['date']}  "
            f"{amount:>8.2f}  {record['note']}"
        )

    print("-" * 45)
    print(f"共 {len(records)} 笔，合计 {total_amount:.2f}")


def show_total():
    """合计全部账目。"""
    records = load_records()

    if not records:
        print("（没有账目）")
        return

    total_amount = 0.0
    for record in records:
        total_amount += float(record["amount"])

    print(f"合计：{total_amount:.2f}（{len(records)} 笔）")


def delete():
    """按列表中的序号删除一笔账目。"""
    number_text = get_arg(2, "序号")

    try:
        number = int(number_text)
    except (TypeError, ValueError):
        print(f"[错误] 序号必须是整数，你输入的是：{number_text}")
        return

    records = load_records()

    if number < 1 or number > len(records):
        print(f"[错误] 序号超范围：当前共 {len(records)} 笔，你输入的是 {number}")
        return

    removed = records.pop(number - 1)
    save_records(records)

    print(
        f"[完成] 已删除第 {number} 笔："
        f"{removed['date']}  {float(removed['amount']):.2f}  {removed['note']}"
    )


def show_help():
    """显示用法说明。"""
    print(
        """expense_cli.py - 命令行记账工具

用法：
    python expense_cli.py add <金额> <备注>   添加一笔
    python expense_cli.py list                 列出全部
    python expense_cli.py total                合计全部
    python expense_cli.py delete <序号>        删除一笔
    python expense_cli.py help                 显示帮助

数据保存在脚本旁边的 records.json 中。"""
    )


def main():
    """根据第一个命令行参数选择要执行的命令。"""
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "add":
        add()
    elif command == "list":
        list_all()
    elif command == "total":
        show_total()
    elif command == "delete":
        delete()
    elif command == "help":
        show_help()
    else:
        print(f"[错误] 不认识这个命令：{command}")
        print()
        show_help()


if __name__ == "__main__":
    main()
