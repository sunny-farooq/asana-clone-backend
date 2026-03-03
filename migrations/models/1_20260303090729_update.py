from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organizations" ADD "participant_id" UUID;
        ALTER TABLE "Organizations" ADD CONSTRAINT "fk_Organiza_Accounts_2109e768" FOREIGN KEY ("participant_id") REFERENCES "Accounts" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organizations" DROP CONSTRAINT IF EXISTS "fk_Organiza_Accounts_2109e768";
        ALTER TABLE "Organizations" DROP COLUMN "participant_id";"""


MODELS_STATE = (
    "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"
)
