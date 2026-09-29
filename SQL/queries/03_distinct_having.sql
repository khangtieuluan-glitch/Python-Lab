-- 2026-09-29 A2 SQL 练习（③ 段：DISTINCT / HAVING）
-- 前提：expenses 已归类（见 queries/01）。

-- 1) DISTINCT：列出出现过的所有类别（去重，压的是整行组合）
SELECT DISTINCT category FROM expenses;

-- 2) HAVING：组级过滤，分组之后才生效。只显示笔数 >= 2 的组
SELECT category, COUNT(*) AS 笔数
FROM expenses
GROUP BY category
HAVING 笔数 >= 2;

-- 3) HAVING + BETWEEN：只显示合计在 50~250 之间的组
SELECT category, SUM(amount) AS 合计
FROM expenses
GROUP BY category
HAVING 合计 BETWEEN 50 AND 250;
