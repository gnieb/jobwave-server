"""add done boolean column

Revision ID: 4408d09f31ea
Revises: f11f097adc64
Create Date: 2023-08-23 22:51:39.120387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4408d09f31ea'
down_revision = 'f11f097adc64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###
