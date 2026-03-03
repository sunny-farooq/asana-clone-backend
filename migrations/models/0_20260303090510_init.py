from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "Organizations" (
    "id" UUID NOT NULL PRIMARY KEY,
    "name" VARCHAR(40),
    "trial_status" VARCHAR(40) NOT NULL DEFAULT 'Inactive',
    "billing_date" DATE,
    "card_number" VARCHAR(12),
    "card_expiry" VARCHAR(12),
    "card_cvv" VARCHAR(3),
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "Accounts" (
    "id" UUID NOT NULL PRIMARY KEY,
    "email" VARCHAR(40) NOT NULL UNIQUE,
    "name" VARCHAR(40) NOT NULL,
    "password" VARCHAR(500) NOT NULL,
    "is_verified" BOOL NOT NULL DEFAULT False,
    "role" VARCHAR(5) NOT NULL DEFAULT 'user',
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "organization_id" UUID NOT NULL REFERENCES "Organizations" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "Accounts"."role" IS 'ADMIN: admin\nUSER: user';
CREATE TABLE IF NOT EXISTS "Notifications" (
    "id" UUID NOT NULL PRIMARY KEY,
    "text" VARCHAR(30) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "is_read" BOOL NOT NULL DEFAULT False,
    "recepient_id" UUID NOT NULL REFERENCES "Accounts" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Portfolios" (
    "id" UUID NOT NULL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL,
    "status" VARCHAR(10),
    "start_date" DATE,
    "end_date" DATE,
    "isOngoing" BOOL NOT NULL DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "organization_id" UUID NOT NULL REFERENCES "Organizations" ("id") ON DELETE CASCADE,
    "owner_id" UUID NOT NULL REFERENCES "Accounts" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Goals Table" (
    "id" UUID NOT NULL PRIMARY KEY,
    "title" VARCHAR(20) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "organization_id" UUID NOT NULL REFERENCES "Organizations" ("id") ON DELETE CASCADE,
    "owner_id" UUID NOT NULL REFERENCES "Accounts" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Organization_Members" (
    "id" UUID NOT NULL PRIMARY KEY,
    "role" VARCHAR(40) NOT NULL,
    "joined_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "account_id" UUID NOT NULL REFERENCES "Accounts" ("id") ON DELETE CASCADE,
    "organization_id" UUID REFERENCES "Organizations" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Projects" (
    "id" UUID NOT NULL PRIMARY KEY,
    "name" VARCHAR(40) NOT NULL,
    "status" VARCHAR(30) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "organization_id" UUID NOT NULL REFERENCES "Organizations" ("id") ON DELETE CASCADE,
    "portfolio_id" UUID REFERENCES "Portfolios" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Tasks" (
    "id" UUID NOT NULL PRIMARY KEY,
    "category" VARCHAR(20) NOT NULL,
    "assign_date" DATE,
    "due_date" DATE,
    "priority" VARCHAR(20),
    "status" VARCHAR(20),
    "parent_task_id" VARCHAR(100),
    "is_subtask" BOOL NOT NULL DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "assignee_id" UUID REFERENCES "Accounts" ("id") ON DELETE CASCADE,
    "project_id" UUID NOT NULL REFERENCES "Projects" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Comments" (
    "id" UUID NOT NULL PRIMARY KEY,
    "comment_text" VARCHAR(1000) NOT NULL,
    "has_attachment" BOOL NOT NULL DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "account_id" UUID NOT NULL REFERENCES "Accounts" ("id") ON DELETE CASCADE,
    "task_id" UUID NOT NULL REFERENCES "Tasks" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Task_Like" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "account_id" UUID NOT NULL REFERENCES "Accounts" ("id") ON DELETE CASCADE,
    "task_id" UUID NOT NULL REFERENCES "Tasks" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Goal_Tasks" (
    "id" UUID NOT NULL PRIMARY KEY,
    "goal_id" UUID NOT NULL REFERENCES "Goals Table" ("id") ON DELETE CASCADE,
    "task_id" UUID NOT NULL REFERENCES "Tasks" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Goal Projects" (
    "id" UUID NOT NULL PRIMARY KEY,
    "goal_id" UUID NOT NULL REFERENCES "Goals Table" ("id") ON DELETE CASCADE,
    "project_id" UUID NOT NULL REFERENCES "Projects" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "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"
)
