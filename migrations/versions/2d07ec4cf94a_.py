"""empty message

Revision ID: 2d07ec4cf94a
Revises: 097e186b97bf
Create Date: 2019-08-03 14:33:29.329523

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d07ec4cf94a'
down_revision = '097e186b97bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'firstname',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user', 'lastname',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user', 'lastname',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user', 'firstname',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###