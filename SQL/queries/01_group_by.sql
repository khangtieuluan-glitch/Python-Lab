-- 2026-09-29 A2 SQL 练习（① 段：UPDATE 安全网 + GROUP BY）
-- 前提：expenses 已加 category 列并改名为 category（见 schema/00）。

-- 先把 5 行数据按口径归类：餐饮=1,4 / 购物=2,5 / 交通=3
-- 先挂事务网，改完 SELECT 逐行核对再 COMMIT（漏写 WHERE 会全表改写）
START TRANSACTION;
UPDATE expenses SET category = '餐饮' WHERE id IN (1, 4);
UPDATE expenses SET category = '购物' WHERE id IN (2, 5);
UPDATE expenses SET category = '交通' WHERE id = 3;
SELECT * FROM expenses;          -- 铁律：逐行核对 5 行分类
COMMIT;

-- 按类别分组统计（SELECT 只能放分组列 + 聚合函数）
SELECT category, SUM(amount) AS 合计, COUNT(*) AS 笔数
FROM expenses
GROUP BY category
ORDER BY 合计 DESC;
