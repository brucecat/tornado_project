"""add user.creat_time

Revision ID: ca7bf6c95148
Revises: c3556ad792ea
Create Date: 2019-03-02 15:16:53.272289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca7bf6c95148'
down_revision = 'c3556ad792ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.create_unique_constraint(None, 'user', ['telephone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type='unique')
    op.drop_column('user', 'create_time')
    # ### end Alembic commands ###
