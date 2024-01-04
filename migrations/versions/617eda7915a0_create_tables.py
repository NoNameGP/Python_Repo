"""create tables

Revision ID: 617eda7915a0
Revises: f8b3fe280e9a
Create Date: 2024-01-03 23:52:17.907663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '617eda7915a0'
down_revision = 'f8b3fe280e9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('route', sa.Integer(), nullable=False),
    sa.Column('pointX', sa.Float(), nullable=True),
    sa.Column('pointY', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['route'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pass_point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('route', sa.Integer(), nullable=False),
    sa.Column('pointX', sa.Float(), nullable=True),
    sa.Column('pointY', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['route'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('mark', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endX', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('endY', sa.Float(), nullable=True))
        batch_op.drop_column('endPoint')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mark', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endPoint', sa.FLOAT(), nullable=True))
        batch_op.drop_column('endY')
        batch_op.drop_column('endX')

    op.drop_table('pass_point')
    op.drop_table('object')
    # ### end Alembic commands ###