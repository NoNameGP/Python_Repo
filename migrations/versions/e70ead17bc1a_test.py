"""test

Revision ID: e70ead17bc1a
Revises: 9707db7865d3
Create Date: 2024-01-05 15:00:44.277627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e70ead17bc1a'
down_revision = '9707db7865d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mark', schema=None) as batch_op:
        batch_op.add_column(sa.Column('X', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('Y', sa.Float(), nullable=True))
        batch_op.drop_column('pointX')
        batch_op.drop_column('pointY')

    with op.batch_alter_table('object', schema=None) as batch_op:
        batch_op.add_column(sa.Column('X', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('Y', sa.Float(), nullable=True))
        batch_op.drop_column('pointX')
        batch_op.drop_column('pointY')

    with op.batch_alter_table('pass_point', schema=None) as batch_op:
        batch_op.add_column(sa.Column('X', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('Y', sa.Float(), nullable=True))

    with op.batch_alter_table('route', schema=None) as batch_op:
        batch_op.add_column(sa.Column('startX', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('startY', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('endX', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('endY', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('route', schema=None) as batch_op:
        batch_op.drop_column('endY')
        batch_op.drop_column('endX')
        batch_op.drop_column('startY')
        batch_op.drop_column('startX')

    with op.batch_alter_table('pass_point', schema=None) as batch_op:
        batch_op.drop_column('Y')
        batch_op.drop_column('X')

    with op.batch_alter_table('object', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pointY', sa.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('pointX', sa.FLOAT(), nullable=True))
        batch_op.drop_column('Y')
        batch_op.drop_column('X')

    with op.batch_alter_table('mark', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pointY', sa.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('pointX', sa.FLOAT(), nullable=True))
        batch_op.drop_column('Y')
        batch_op.drop_column('X')

    # ### end Alembic commands ###
