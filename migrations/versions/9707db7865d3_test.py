"""test

Revision ID: 9707db7865d3
Revises: 2df51e19ff6a
Create Date: 2024-01-05 14:57:50.068414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9707db7865d3'
down_revision = '2df51e19ff6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mark', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pointX', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('pointY', sa.Float(), nullable=True))

    with op.batch_alter_table('object', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pointX', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('pointY', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('object', schema=None) as batch_op:
        batch_op.drop_column('pointY')
        batch_op.drop_column('pointX')

    with op.batch_alter_table('mark', schema=None) as batch_op:
        batch_op.drop_column('pointY')
        batch_op.drop_column('pointX')

    # ### end Alembic commands ###