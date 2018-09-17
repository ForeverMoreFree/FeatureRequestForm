"""Table create

Revision ID: 3cec07bedc6b
Revises: 
Create Date: 2018-09-17 11:50:11.903248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cec07bedc6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('client', sa.Text(), nullable=True),
    sa.Column('client_priority', sa.Integer(), nullable=True),
    sa.Column('target_date', sa.Text(), nullable=True),
    sa.Column('product_area', sa.Text(), nullable=True),
    sa.Column('edit_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('features')
    # ### end Alembic commands ###
