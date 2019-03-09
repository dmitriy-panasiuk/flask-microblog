"""followers

Revision ID: e0620dc18786
Revises: 00a193765af8
Create Date: 2019-03-09 16:42:32.939429

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e0620dc18786"
down_revision = "00a193765af8"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "followers",
        sa.Column("follower_id", sa.Integer(), nullable=True),
        sa.Column("followed_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["followed_id"], ["user.id"]),
        sa.ForeignKeyConstraint(["follower_id"], ["user.id"]),
    )


def downgrade():
    op.drop_table("followers")
