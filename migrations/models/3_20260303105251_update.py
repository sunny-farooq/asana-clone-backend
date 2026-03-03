from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organization_Members" ADD "invited_at" TIMESTAMPTZ;
        ALTER TABLE "Organization_Members" ALTER COLUMN "account_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organization_Members" DROP COLUMN "invited_at";
        ALTER TABLE "Organization_Members" ALTER COLUMN "account_id" SET NOT NULL;"""


MODELS_STATE = (
    "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"
)
