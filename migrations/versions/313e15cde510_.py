"""empty message

Revision ID: 313e15cde510
Revises: 40063bc42219
Create Date: 2022-05-26 20:00:32.256211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '313e15cde510'
down_revision = '40063bc42219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'animal', ['species'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'animal', type_='unique')
    # ### end Alembic commands ###
