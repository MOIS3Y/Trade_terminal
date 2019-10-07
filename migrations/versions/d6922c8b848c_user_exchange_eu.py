"""User Exchange EU

Revision ID: d6922c8b848c
Revises: 8ddde86e485a
Create Date: 2019-10-07 21:25:56.878793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6922c8b848c'
down_revision = '8ddde86e485a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_exchanges',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('exchange_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['exchange_id'], ['exchange.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_exchanges')
    # ### end Alembic commands ###
