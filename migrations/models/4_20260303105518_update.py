from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organization_Members" ADD "email" VARCHAR(40) UNIQUE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "uid_Organizatio_email_cc168f";
        ALTER TABLE "Organization_Members" DROP COLUMN "email";"""


MODELS_STATE = (
    "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"
)
