"""empty message

Revision ID: f4a40f591d54
Revises: 90e5b517550a
Create Date: 2019-08-17 23:51:23.991712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4a40f591d54'
down_revision = '90e5b517550a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('adverts', sa.Column('city', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('adverts', 'city')
    # ### end Alembic commands ###
