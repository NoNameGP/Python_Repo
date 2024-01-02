"""add Route Table

Revision ID: f8b3fe280e9a
Revises: fdd5b0073edf
Create Date: 2024-01-02 11:29:35.360156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b3fe280e9a'
down_revision = 'fdd5b0073edf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('route',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('startX', sa.Float(), nullable=True),
    sa.Column('startY', sa.Float(), nullable=True),
    sa.Column('endX', sa.Float(), nullable=True),
    sa.Column('endY', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password')

    op.drop_table('route')
    # ### end Alembic commands ###