"""mark table splite

Revision ID: 322a94418769
Revises: 4b6037645b7b
Create Date: 2024-01-01 11:33:01.326580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '322a94418769'
down_revision = '4b6037645b7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mark')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mark',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('userId', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('endPoint', sa.FLOAT(), nullable=True),
    sa.Column('status', sa.VARCHAR(length=255), server_default=sa.text("'Active'"), nullable=False),
    sa.Column('createAt', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###