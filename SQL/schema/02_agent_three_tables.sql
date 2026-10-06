-- 三张表：一个用户开多次对话，一次对话有多条消息
-- 建表顺序：users → conversations → messages（先父后子）

CREATE TABLE users (
  id         INT          PRIMARY KEY AUTO_INCREMENT,
  username   VARCHAR(50)  NOT NULL UNIQUE,
  email      VARCHAR(100) NOT NULL UNIQUE,
  created_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE conversations (
  id         INT          PRIMARY KEY AUTO_INCREMENT,
  user_id    INT          NOT NULL,
  title      VARCHAR(100) NOT NULL DEFAULT '新对话',
  started_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  -- 选 CASCADE：用户注销了，他的对话留着没意义
  CONSTRAINT fk_conv_user
    FOREIGN KEY (user_id) REFERENCES users (id)
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE messages (
  id          INT                               PRIMARY KEY AUTO_INCREMENT,
  conv_id     INT                               NOT NULL,
  role        ENUM('user','assistant','system') NOT NULL,
  content     TEXT                              NOT NULL,
  token_count INT                               NOT NULL DEFAULT 0,
  created_at  DATETIME                          NOT NULL DEFAULT CURRENT_TIMESTAMP,
  -- 选 CASCADE：对话删了，消息必须跟着删，否则堆一堆孤儿
  CONSTRAINT fk_msg_conv
    FOREIGN KEY (conv_id) REFERENCES conversations (id)
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;
