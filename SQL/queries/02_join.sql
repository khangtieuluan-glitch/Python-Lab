-- 2026-09-29 A2 SQL 练习（② 段：第二张表 + 最简 JOIN）
-- 前提：categories 表已建并灌入数据（见 schema/01 + 下面 INSERT）。

-- 灌入类别维度数据（id 由 AUTO_INCREMENT 自动填，不必手写）
INSERT INTO categories (name, budget) VALUES
  ('餐饮', 800.00),
  ('购物', 500.00),
  ('交通', 200.00);

SELECT * FROM categories;

-- INNER JOIN：两边对上才算。expenses 每笔都能匹配类别 → 5 行
SELECT e.note, e.amount, c.name, c.budget
FROM expenses e
JOIN categories c ON e.category = c.name
ORDER BY e.amount DESC;

-- LEFT JOIN 实验：插一笔未归类支出，INNER 会丢行，LEFT 保留 NULL
-- START TRANSACTION;
-- INSERT INTO expenses (spend_date, amount, note) VALUES ('2026-09-29', 9.90, '打印');
-- 再跑上面的 JOIN 只剩 5 行；改成 LEFT JOIN 则 6 行，打印那行 budget 为 NULL
-- ROLLBACK;  -- 实验完撤销，保持数据干净
SELECT e.note, e.amount, c.name, c.budget
FROM expenses e
LEFT JOIN categories c ON e.category = c.name
ORDER BY e.amount DESC;
