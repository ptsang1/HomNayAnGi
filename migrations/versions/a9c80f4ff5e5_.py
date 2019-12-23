"""

Revision ID: a9c80f4ff5e5
Revises: 
Create Date: 2019-12-23 01:50:45.961578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9c80f4ff5e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FOOD_TYPES',
    sa.Column('typeID', sa.INTEGER(), nullable=False),
    sa.Column('typeName', sa.NVARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('typeID')
    )
    op.create_table('GENDERS',
    sa.Column('genderID', sa.BOOLEAN(), nullable=False),
    sa.Column('genderName', sa.VARCHAR(length=4), nullable=True),
    sa.PrimaryKeyConstraint('genderID')
    )
    op.create_table('ROLES',
    sa.Column('roleID', sa.INTEGER(), nullable=False),
    sa.Column('roleName', sa.VARCHAR(length=5), nullable=True),
    sa.PrimaryKeyConstraint('roleID')
    )
    op.create_table('USERS',
    sa.Column('userID', sa.VARCHAR(length=50), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=True),
    sa.Column('password', sa.VARCHAR(length=128), nullable=True),
    sa.Column('roleID', sa.INTEGER(), nullable=True),
    sa.Column('fullName', sa.NVARCHAR(length=50), nullable=True),
    sa.Column('genderID', sa.BOOLEAN(), nullable=True),
    sa.Column('birthDate', sa.DATE(), nullable=True),
    sa.Column('avatalink', sa.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['genderID'], ['GENDERS.genderID'], ),
    sa.ForeignKeyConstraint(['roleID'], ['ROLES.roleID'], ),
    sa.PrimaryKeyConstraint('userID')
    )
    op.create_table('RECIPE_POSTS',
    sa.Column('ownerID', sa.VARCHAR(length=50), nullable=False),
    sa.Column('postID', sa.INTEGER(), nullable=False),
    sa.Column('typeID', sa.INTEGER(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('ingredients', sa.TEXT(), nullable=True),
    sa.Column('image', sa.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['ownerID'], ['USERS.userID'], ),
    sa.PrimaryKeyConstraint('ownerID', 'postID')
    )
    op.create_table('COMMENTS_IN_POSTS',
    sa.Column('ownerPostID', sa.VARCHAR(length=50), nullable=False),
    sa.Column('postID', sa.INTEGER(), nullable=False),
    sa.Column('commentID', sa.INTEGER(), nullable=False),
    sa.Column('userID', sa.VARCHAR(length=50), nullable=True),
    sa.ForeignKeyConstraint(['ownerPostID'], ['RECIPE_POSTS.ownerID'], ),
    sa.ForeignKeyConstraint(['postID'], ['RECIPE_POSTS.postID'], ),
    sa.ForeignKeyConstraint(['userID'], ['USERS.userID'], ),
    sa.PrimaryKeyConstraint('ownerPostID', 'postID', 'commentID')
    )
    op.create_table('POSTS_SAVED_BY_USERS',
    sa.Column('userID', sa.VARCHAR(length=50), nullable=False),
    sa.Column('ownerID', sa.VARCHAR(length=50), nullable=False),
    sa.Column('postID', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['ownerID'], ['RECIPE_POSTS.ownerID'], ),
    sa.ForeignKeyConstraint(['postID'], ['RECIPE_POSTS.postID'], ),
    sa.ForeignKeyConstraint(['userID'], ['USERS.userID'], ),
    sa.PrimaryKeyConstraint('userID', 'ownerID', 'postID')
    )
    op.create_table('POSTS_TYPES',
    sa.Column('ownerID', sa.VARCHAR(length=50), nullable=False),
    sa.Column('postID', sa.INTEGER(), nullable=False),
    sa.Column('i', sa.INTEGER(), nullable=False),
    sa.Column('typeID', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['ownerID'], ['RECIPE_POSTS.ownerID'], ),
    sa.ForeignKeyConstraint(['postID'], ['RECIPE_POSTS.postID'], ),
    sa.ForeignKeyConstraint(['typeID'], ['FOOD_TYPES.typeID'], ),
    sa.PrimaryKeyConstraint('ownerID', 'postID', 'i')
    )
    op.drop_table('posts_saved_by_users')
    op.drop_table('recipe_posts')
    op.drop_table('posts_types')
    op.drop_table('users')
    op.drop_table('comments_in_posts')
    op.drop_table('genders')
    op.drop_table('roles')
    op.drop_table('food_types')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food_types',
    sa.Column('typeid', sa.INTEGER(), server_default=sa.text("nextval('food_types_typeid_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('typename', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('typeid', name='food_types_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('roles',
    sa.Column('roleid', sa.SMALLINT(), server_default=sa.text("nextval('roles_roleid_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('rolename', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('roleid', name='roles_pkey'),
    sa.UniqueConstraint('rolename', name='roles_rolename_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('genders',
    sa.Column('genderid', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('gendername', sa.VARCHAR(length=4), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('genderid', name='genders_pkey'),
    sa.UniqueConstraint('gendername', name='genders_gendername_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('comments_in_posts',
    sa.Column('ownerpostid', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('postid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('commentid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('userid', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ownerpostid', 'postid'], ['recipe_posts.ownerid', 'recipe_posts.postid'], name='comments_in_posts_ownerpostid_fkey'),
    sa.ForeignKeyConstraint(['userid'], ['users.userid'], name='comments_in_posts_userid_fkey'),
    sa.PrimaryKeyConstraint('ownerpostid', 'postid', 'commentid', name='comments_in_posts_pkey')
    )
    op.create_table('users',
    sa.Column('userid', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('roleid', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('fullname', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('genderid', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('birthday', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('avatarlink', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['genderid'], ['genders.genderid'], name='users_genderid_fkey'),
    sa.ForeignKeyConstraint(['roleid'], ['roles.roleid'], name='users_roleid_fkey'),
    sa.PrimaryKeyConstraint('userid', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('posts_types',
    sa.Column('ownerid', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('postid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('i', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('typeid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ownerid', 'postid'], ['recipe_posts.ownerid', 'recipe_posts.postid'], name='posts_types_ownerid_fkey'),
    sa.ForeignKeyConstraint(['typeid'], ['food_types.typeid'], name='posts_types_typeid_fkey'),
    sa.PrimaryKeyConstraint('ownerid', 'postid', 'i', name='posts_types_pkey')
    )
    op.create_table('recipe_posts',
    sa.Column('ownerid', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('postid', sa.INTEGER(), server_default=sa.text("nextval('recipe_posts_postid_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('foodname', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('ingredients', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['ownerid'], ['users.userid'], name='recipe_posts_ownerid_fkey'),
    sa.PrimaryKeyConstraint('ownerid', 'postid', name='recipe_posts_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('posts_saved_by_users',
    sa.Column('userid', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('ownerid', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('postid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['ownerid', 'postid'], ['recipe_posts.ownerid', 'recipe_posts.postid'], name='posts_saved_by_users_ownerid_fkey'),
    sa.ForeignKeyConstraint(['userid'], ['users.userid'], name='posts_saved_by_users_userid_fkey'),
    sa.PrimaryKeyConstraint('userid', 'ownerid', 'postid', name='posts_saved_by_users_pkey')
    )
    op.drop_table('POSTS_TYPES')
    op.drop_table('POSTS_SAVED_BY_USERS')
    op.drop_table('COMMENTS_IN_POSTS')
    op.drop_table('RECIPE_POSTS')
    op.drop_table('USERS')
    op.drop_table('ROLES')
    op.drop_table('GENDERS')
    op.drop_table('FOOD_TYPES')
    # ### end Alembic commands ###