"""empty message

Revision ID: 9c46b65d9c91
Revises: 558672dc68c2
Create Date: 2019-08-10 18:35:32.352089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c46b65d9c91'
down_revision = '558672dc68c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photo', sa.Column('data', sa.LargeBinary(), nullable=True))
    op.add_column('photo', sa.Column('name', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('photo', 'name')
    op.drop_column('photo', 'data')
    # ### end Alembic commands ###
