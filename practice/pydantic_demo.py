# 核心套路
from pydantic import BaseModel, Field
class Expense(BaseModel):          # ① 继承 BaseModel
    amount: float = Field(gt=0)    # ② 字段: 类型 = 约束
    category: str = "其他"          #    可以给默认值
    note: str | None = None        #    可以不传（None）

e = Expense(amount="25.5", note="午饭")   # ③ 塞数据进去，pydantic 自动校验+转换
print(e)                # amount=25.5 category='其他' note='午饭'
print(e.amount, type(e.amount))   # 25.5  <class 'float'>  ← 字符串被转成 float 了
print(e.model_dump())   # {'amount': 25.5, 'category': '其他', 'note': '午饭'}

# 不合规时它怎么报错
from pydantic import ValidationError

try:
    Expense(amount=-5)
except ValidationError as err:
    print(err)

# 自定义规则：Field + @field_validator
# Field 管数据本身的边界：
amount: float = Field(gt=0, le=1_000_000)   # 0 < amount ≤ 100万
category: str = Field(min_length=1, max_length=10)

# @field_validator 管"业务规则"（比如类别必须在白名单里）：
from pydantic import field_validator

CATEGORIES = ["餐饮", "交通", "购物", "其他"]

class Expense(BaseModel):
    amount: float = Field(gt=0)
    category: str = "其他"

    @field_validator("category")
    @classmethod
    def check_category(cls, v):
        v = v.strip()                      # 顺手去掉空格
        if v not in CATEGORIES:
            raise ValueError(f"类别必须是 {CATEGORIES} 之一")
        return v

