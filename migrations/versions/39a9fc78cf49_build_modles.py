"""build modles

Revision ID: 39a9fc78cf49
Revises: 5c9db378a810
Create Date: 2020-04-18 18:05:44.121260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39a9fc78cf49'
down_revision = '5c9db378a810'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visitors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ordinal', sa.Integer(), nullable=True),
    sa.Column('land_status', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('queues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('remark', sa.String(length=150), nullable=True),
    sa.Column('close_time', sa.DateTime(), nullable=True),
    sa.Column('quota', sa.Integer(), nullable=True),
    sa.Column('rotate_mode', sa.Integer(), nullable=True),
    sa.Column('interval', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('visitor_id', sa.Integer(), nullable=False),
    sa.Column('queue_id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['queue_id'], ['queues.id'], ),
    sa.ForeignKeyConstraint(['visitor_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('queues')
    op.drop_table('visitors')
    # ### end Alembic commands ###