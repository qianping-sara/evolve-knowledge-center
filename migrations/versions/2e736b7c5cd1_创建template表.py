"""创建template表

Revision ID: 2e736b7c5cd1
Revises: 
Create Date: 2024-07-14 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e736b7c5cd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### 创建template表 ###
    op.create_table('template',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('tags', sa.Text(), nullable=True),
        sa.Column('version', sa.String(), nullable=True),
        sa.Column('createdAt', sa.DateTime(), nullable=True),
        sa.Column('updatedAt', sa.DateTime(), nullable=True),
        sa.Column('createdBy', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_template_createdBy'), 'template', ['createdBy'], unique=False)
    op.create_index(op.f('ix_template_id'), 'template', ['id'], unique=False)
    op.create_index(op.f('ix_template_name'), 'template', ['name'], unique=False)
    # ### end 创建template表 ###


def downgrade() -> None:
    # ### 删除template表 ###
    op.drop_index(op.f('ix_template_name'), table_name='template')
    op.drop_index(op.f('ix_template_id'), table_name='template')
    op.drop_index(op.f('ix_template_createdBy'), table_name='template')
    op.drop_table('template')
    # ### end 删除template表 ### 