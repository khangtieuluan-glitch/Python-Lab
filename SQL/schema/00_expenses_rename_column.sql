-- 2026-09-29 A2 SQL 练习（schema 修复）
-- 建表时把 category 拼错成 catagory，这里改回正确拼写。
-- 注意：此语句已在本机执行过；若列已是 category，重跑会报 "Unknown column 'catagory'" 属正常，
--       说明修复已完成，可直接跳过。
ALTER TABLE expenses RENAME COLUMN catagory TO category;
