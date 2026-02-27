from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organizations" ADD "owner_id" UUID;
        ALTER TABLE "Organizations" ADD CONSTRAINT "fk_Organiza_Accounts_9dd6f097" FOREIGN KEY ("owner_id") REFERENCES "Accounts" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organizations" DROP CONSTRAINT IF EXISTS "fk_Organiza_Accounts_9dd6f097";
        ALTER TABLE "Organizations" DROP COLUMN "owner_id";"""


MODELS_STATE = (
    "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"
    "xzf/0PMgBj9w=="
)
