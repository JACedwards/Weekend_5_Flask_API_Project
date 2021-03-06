"""empty message

Revision ID: 0521b62edd34
Revises: 313e15cde510
Create Date: 2022-05-27 09:35:13.517984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0521b62edd34'
down_revision = '313e15cde510'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('api_token', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'api_token')
    # ### end Alembic commands ###
