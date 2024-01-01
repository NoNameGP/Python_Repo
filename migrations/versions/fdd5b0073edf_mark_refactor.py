"""Mark refactor

Revision ID: fdd5b0073edf
Revises: 460d84a640d8
Create Date: 2024-01-01 14:01:11.742943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdd5b0073edf'
down_revision = '460d84a640d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mark', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mark', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###