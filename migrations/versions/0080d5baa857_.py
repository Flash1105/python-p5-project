"""empty message

Revision ID: 0080d5baa857
Revises: 59ffcd25bce1
Create Date: 2023-09-28 06:38:01.304741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0080d5baa857'
down_revision = '59ffcd25bce1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.drop_index('ix_users_username')

    op.drop_table('users')
    op.drop_table('discussions')
    op.drop_table('observations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('observations',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('species', sa.VARCHAR(), nullable=False),
    sa.Column('location', sa.VARCHAR(), nullable=False),
    sa.Column('behavior', sa.VARCHAR(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('images', sa.VARCHAR(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('discussions',
    sa.Column('discussion_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('observation_id', sa.INTEGER(), nullable=False),
    sa.Column('message', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['observation_id'], ['observations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('discussion_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('role', sa.VARCHAR(length=12), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('ix_users_username', ['username'], unique=False)
        batch_op.create_index('ix_users_email', ['email'], unique=False)

    # ### end Alembic commands ###