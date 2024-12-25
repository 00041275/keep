"""Add is_provisioned column for DeduplicationRule table

Revision ID: 4f8c4b185d5b
Revises: 0c5e002094a9
Create Date: 2024-12-23 18:49:00.882402

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4f8c4b185d5b"
down_revision = "0c5e002094a9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Add the new column with a server default
    with op.batch_alter_table("alertdeduplicationrule", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "is_provisioned",
                sa.Boolean(),
                nullable=False,
                server_default=sa.text("false"),
            )
        )

    # Update existing records to have the default value
    op.execute("UPDATE alertdeduplicationrule SET is_provisioned = false")

    # Remove the server default (optional, to match schema-only behavior)
    with op.batch_alter_table("alertdeduplicationrule", schema=None) as batch_op:
        batch_op.alter_column("is_provisioned", server_default=None)
    # ### end Alembic commands ###

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table("alertdeduplicationrule", schema=None) as batch_op:
        batch_op.drop_column("is_provisioned")

    # ### end Alembic commands ###
