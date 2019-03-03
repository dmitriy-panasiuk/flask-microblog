"""new fields in user model

Revision ID: 00a193765af8
Revises: 9f1ef0f5aa8d
Create Date: 2019-03-03 22:15:03.792154

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "00a193765af8"
down_revision = "9f1ef0f5aa8d"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("user", sa.Column("about_me", sa.String(length=140), nullable=True))
    op.add_column("user", sa.Column("last_seen", sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column("user", "last_seen")
    op.drop_column("user", "about_me")
