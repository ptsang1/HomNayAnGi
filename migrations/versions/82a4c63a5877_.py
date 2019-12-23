"""

Revision ID: 82a4c63a5877
Revises: d61fb34d3146
Create Date: 2019-12-23 17:21:51.192632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82a4c63a5877'
down_revision = 'd61fb34d3146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_in_posts_ownerpostid_fkey', 'comments_in_posts', type_='foreignkey')
    op.create_foreign_key(None, 'comments_in_posts', 'recipe_posts', ['postid'], ['postid'])
    op.create_foreign_key(None, 'comments_in_posts', 'recipe_posts', ['ownerpostid'], ['ownerid'])
    op.alter_column('genders', 'gendername',
               existing_type=sa.VARCHAR(length=4),
               nullable=True)
    op.drop_constraint('genders_gendername_key', 'genders', type_='unique')
    op.drop_constraint('posts_saved_by_users_ownerid_fkey', 'posts_saved_by_users', type_='foreignkey')
    op.create_foreign_key(None, 'posts_saved_by_users', 'recipe_posts', ['ownerid'], ['ownerid'])
    op.create_foreign_key(None, 'posts_saved_by_users', 'recipe_posts', ['postid'], ['postid'])
    op.drop_constraint('posts_types_ownerid_fkey', 'posts_types', type_='foreignkey')
    op.create_foreign_key(None, 'posts_types', 'recipe_posts', ['ownerid'], ['ownerid'])
    op.create_foreign_key(None, 'posts_types', 'recipe_posts', ['postid'], ['postid'])
    op.add_column('recipe_posts', sa.Column('typeid', sa.INTEGER(), nullable=True))
    op.alter_column('recipe_posts', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('recipe_posts', 'image',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('recipe_posts', 'ingredients',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_column('recipe_posts', 'foodname')
    op.alter_column('roles', 'rolename',
               existing_type=sa.VARCHAR(length=5),
               nullable=True)
    op.drop_constraint('roles_rolename_key', 'roles', type_='unique')
    op.alter_column('users', 'birthday',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('users', 'fullname',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('users', 'genderid',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('users', 'genderid',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('users', 'fullname',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'birthday',
               existing_type=sa.DATE(),
               nullable=False)
    op.create_unique_constraint('roles_rolename_key', 'roles', ['rolename'])
    op.alter_column('roles', 'rolename',
               existing_type=sa.VARCHAR(length=5),
               nullable=False)
    op.add_column('recipe_posts', sa.Column('foodname', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.alter_column('recipe_posts', 'ingredients',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('recipe_posts', 'image',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('recipe_posts', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_column('recipe_posts', 'typeid')
    op.drop_constraint(None, 'posts_types', type_='foreignkey')
    op.drop_constraint(None, 'posts_types', type_='foreignkey')
    op.create_foreign_key('posts_types_ownerid_fkey', 'posts_types', 'recipe_posts', ['ownerid', 'postid'], ['ownerid', 'postid'])
    op.drop_constraint(None, 'posts_saved_by_users', type_='foreignkey')
    op.drop_constraint(None, 'posts_saved_by_users', type_='foreignkey')
    op.create_foreign_key('posts_saved_by_users_ownerid_fkey', 'posts_saved_by_users', 'recipe_posts', ['ownerid', 'postid'], ['ownerid', 'postid'])
    op.create_unique_constraint('genders_gendername_key', 'genders', ['gendername'])
    op.alter_column('genders', 'gendername',
               existing_type=sa.VARCHAR(length=4),
               nullable=False)
    op.drop_constraint(None, 'comments_in_posts', type_='foreignkey')
    op.drop_constraint(None, 'comments_in_posts', type_='foreignkey')
    op.create_foreign_key('comments_in_posts_ownerpostid_fkey', 'comments_in_posts', 'recipe_posts', ['ownerpostid', 'postid'], ['ownerid', 'postid'])
    # ### end Alembic commands ###