"""change login on username

Revision ID: bb31acac5dd6
Revises: 7e7bf2c25118
Create Date: 2019-11-03 13:59:30.109257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb31acac5dd6'
down_revision = '7e7bf2c25118'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('privat_settings', sa.Column('name', sa.String(length=12), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('privat_settings', 'name')
    # ### end Alembic commands ###
