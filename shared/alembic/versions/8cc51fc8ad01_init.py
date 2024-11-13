"""init

Revision ID: 8cc51fc8ad01
Revises: 
Create Date: 2024-11-13 14:33:36.296740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cc51fc8ad01'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sernder', sa.Integer(), nullable=False),
    sa.Column('catcher', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('data_transaction', sa.Date(), nullable=False),
    sa.Column('time_transaction', sa.Time(), nullable=False),
    sa.Column('status', sa.Enum('ACCEPTED', 'REJECTED', 'FAILED', name='transactionstatus'), nullable=False),
    sa.ForeignKeyConstraint(['catcher'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sernder'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transactions_data_transaction'), 'transactions', ['data_transaction'], unique=False)
    op.create_index(op.f('ix_transactions_time_transaction'), 'transactions', ['time_transaction'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transactions_time_transaction'), table_name='transactions')
    op.drop_index(op.f('ix_transactions_data_transaction'), table_name='transactions')
    op.drop_table('transactions')
    op.drop_table('users')
    # ### end Alembic commands ###