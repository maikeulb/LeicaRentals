"""Update Model

Revision ID: 7e7a1df67763
Revises: ff0423fa4453
Create Date: 2018-02-16 04:13:35.020822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e7a1df67763'
down_revision = 'ff0423fa4453'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lenses', sa.Column('number_available', sa.Integer(), nullable=True))
    op.add_column('lenses', sa.Column('number_in_stock', sa.Integer(), nullable=True))
    op.drop_column('lenses', 'stock')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lenses', sa.Column('stock', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('lenses', 'number_in_stock')
    op.drop_column('lenses', 'number_available')
    # ### end Alembic commands ###
