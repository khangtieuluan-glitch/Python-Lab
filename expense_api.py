"""expense_api.py - 把记账工具包成 HTTP 接口。

启动：.\venv\Scripts\python.exe -m uvicorn expense_api:app --reload
打开：http://127.0.0.1:8000/docs
"""

import datetime

from fastapi import FastAPI
from pydantic import BaseModel, Field

from expense_cli import load_records, save_records

app = FastAPI(title="记账 API")


class ExpenseIn(BaseModel):
    """新增一笔支出时的数据形状。

    Field(...) 里的 description 会显示在 /docs 上，
    也是将来 Agent 选工具、填参数时唯一能读到的说明 —— 必须写清楚。
    """
    amount: float = Field(gt=0, description="金额（元），必须大于 0")
    note: str = Field(min_length=1, description="备注，不能为空")


class Expense(ExpenseIn):
    """返回给调用方的样子（比输入多一个 date）。"""
    date: str


@app.get("/expenses")
def list_expenses():
    """查全部账目。"""
    return load_records()


@app.get("/summary")
def summary():
    """算总额和笔数。"""
    records = load_records()
    total = sum(float(r["amount"]) for r in records)
    return {"count": len(records), "total": round(total, 2)}


@app.post("/expenses")
def create_expense(item: ExpenseIn):
    """新增一笔。"""
    records = load_records()

    new_record = {
        "date": datetime.date.today().isoformat(),
        "amount": item.amount,
        "note": item.note,
    }

    records.append(new_record)
    save_records(records)

    return {"status": "created", "record": new_record}
