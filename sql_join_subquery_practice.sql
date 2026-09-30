-- ============================================================
-- 文件：sql_join_subquery_practice.sql
-- 内容：SQL 多表查询练习 —— INNER/LEFT JOIN、子查询(IN/标量)、
--       反连接(LEFT JOIN + IS NULL)、JOIN+子查询组合、GROUP BY 分组聚合
-- 库：python_lab（MySQL 8.4，服务名 MySQL84）
-- 说明：示例表 categories + expenses_demo，不碰你现有 expenses 数据。
--       整段粘贴到 MySQL 命令行，或 mysql 客户端 `source` 执行。
-- ============================================================

USE python_lab;

-- 建表示例（先删后建，保证可重复跑）
DROP TABLE IF EXISTS expenses_demo;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE expenses_demo (
    id INT PRIMARY KEY,
    item VARCHAR(30),
    amount DECIMAL(10,2),
    category_id INT
);

INSERT INTO categories VALUES
    (1, '餐饮'), (2, '交通'), (3, '购物');

INSERT INTO expenses_demo VALUES
    (1, '午餐',   25.00, 1),
    (2, '地铁',    6.00, 2),
    (3, '衬衫',  199.00, 3),
    (4, '晚餐',   40.00, 1),
    (5, '不明消费', 12.00, NULL);   -- 这条没归类

-- ---------- 第一组：JOIN 基础 ----------
-- 练1 INNER JOIN：两边都对得上的才留，不明消费(category_id=NULL)被丢
SELECT e.item, e.amount, c.name
FROM expenses_demo e
INNER JOIN categories c ON e.category_id = c.id;

-- 练2 LEFT JOIN：左表(expenses_demo)全留，右表缺的填 NULL
SELECT e.item, e.amount, c.name
FROM expenses_demo e
LEFT JOIN categories c ON e.category_id = c.id;

-- ---------- 第二组：子查询 ----------
-- 练3 IN(SELECT)：先查餐饮/交通的 id 清单，再筛
SELECT item, amount
FROM expenses_demo
WHERE category_id IN (SELECT id FROM categories WHERE name IN ('餐饮','交通'));

-- 练4 标量子查询：先算平均(=56.4)，再比。只有衬衫199>56.4（晚餐40不达标）
SELECT item, amount
FROM expenses_demo
WHERE amount > (SELECT AVG(amount) FROM expenses_demo);

-- ---------- 第三组：反连接 + 组合 + 分组（23:20 后新增）----------
-- 练5 反连接 A1：哪些支出没归类（右表主键为 NULL）
SELECT e.id, e.item, e.amount
FROM expenses_demo e
LEFT JOIN categories c ON e.category_id = c.id
WHERE c.id IS NULL;          -- 必须 IS NULL，= NULL 查不到

-- 练6 反连接 A2：哪些分类没被任何支出使用（左右表调个位置）
SELECT c.name
FROM categories c
LEFT JOIN expenses_demo e ON c.id = e.category_id
WHERE e.id IS NULL;

-- 练7 JOIN + 子查询组合：高于平均的支出，连分类名一起显示
SELECT e.item, e.amount, c.name AS category
FROM expenses_demo e
INNER JOIN categories c ON e.category_id = c.id
WHERE e.amount > (SELECT AVG(amount) FROM expenses_demo);

-- 练8 分组聚合：每个分类的笔数 + 总额，按总额降序
SELECT c.name AS category, COUNT(*) AS 笔数, SUM(e.amount) AS 总额
FROM expenses_demo e
INNER JOIN categories c ON e.category_id = c.id
GROUP BY c.name
ORDER BY 总额 DESC;
