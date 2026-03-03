from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organization_Members" ADD "invitation_code" VARCHAR(6);
        ALTER TABLE "Organization_Members" ALTER COLUMN "role" SET DEFAULT 'user';
        ALTER TABLE "Organization_Members" ALTER COLUMN "role" TYPE VARCHAR(5) USING "role"::VARCHAR(5);
        COMMENT ON COLUMN "Organization_Members"."role" IS 'ADMIN: admin
USER: user';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "Organization_Members" DROP COLUMN "invitation_code";
        ALTER TABLE "Organization_Members" ALTER COLUMN "role" TYPE VARCHAR(40) USING "role"::VARCHAR(40);
        ALTER TABLE "Organization_Members" ALTER COLUMN "role" DROP DEFAULT;
        COMMENT ON COLUMN "Organization_Members"."role" IS NULL;"""


MODELS_STATE = (
    "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"
    "qdXfqSe+7XfwGssfUE"
)
