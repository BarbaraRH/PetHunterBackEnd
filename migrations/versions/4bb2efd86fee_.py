"""empty message

Revision ID: 4bb2efd86fee
Revises: 9c46b65d9c91
Create Date: 2019-08-10 18:37:04.490365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bb2efd86fee'
down_revision = '9c46b65d9c91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('accounType', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('accountNum', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('bank', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('rut', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'rut')
    op.drop_column('user', 'bank')
    op.drop_column('user', 'accountNum')
    op.drop_column('user', 'accounType')
    # ### end Alembic commands ###
