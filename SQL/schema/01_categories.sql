-- 2026-09-29 A2 SQL 练习（schema 建表）
-- 类别维度表：被 expenses 通过 category 字段引用。
-- 先定口径（动手前先定义，避免以后摇摆）：
--   餐饮 = 吃进肚子里的（午饭、水果）
--   购物 = 买回来的实物（买书、耳机）
--   交通 = 出行开销（公交）
CREATE TABLE categories (
  id     INT           PRIMARY KEY AUTO_INCREMENT,
  name   VARCHAR(20)   NOT NULL,
  budget DECIMAL(10,2) DEFAULT 0
);
