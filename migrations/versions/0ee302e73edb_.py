"""renamed StrategyTheme.parent column

Revision ID: 0ee302e73edb
Revises: 2e37972246c1
Create Date: 2018-01-09 15:08:11.353525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ee302e73edb'
down_revision = '2e37972246c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('strategy_themes', sa.Column('tactic_id', sa.Integer(), nullable=False))
    op.drop_constraint(u'strategy_themes_parent_fkey', 'strategy_themes', type_='foreignkey')
    op.create_foreign_key(None, 'strategy_themes', 'strategy_tactics', ['tactic_id'], ['id'])
    op.drop_column('strategy_themes', 'parent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('strategy_themes', sa.Column('parent', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'strategy_themes', type_='foreignkey')
    op.create_foreign_key(u'strategy_themes_parent_fkey', 'strategy_themes', 'strategy_tactics', ['parent'], ['id'])
    op.drop_column('strategy_themes', 'tactic_id')
    # ### end Alembic commands ###