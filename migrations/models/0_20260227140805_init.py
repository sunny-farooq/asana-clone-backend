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
    "role" VARCHAR(10) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "organization_id" UUID NOT NULL REFERENCES "Organizations" ("id") ON DELETE CASCADE
);
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
    "organization_id" UUID NOT NULL REFERENCES "Organizations" ("id") ON DELETE CASCADE
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
