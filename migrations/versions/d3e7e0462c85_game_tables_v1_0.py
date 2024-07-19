"""Game tables v1.0

Revision ID: d3e7e0462c85
Revises: fcfe606ece1d
Create Date: 2024-07-14 17:56:19.046237

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd3e7e0462c85'
down_revision = 'fcfe606ece1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('suits', sa.String(length=255), nullable=False),
    sa.Column('rank', sa.String(length=255), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lastplayed_move', sa.String(length=255), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('player_hand', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('computer_hand', postgresql.ARRAY(sa.String()), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    op.drop_table('card')
    # ### end Alembic commands ###
