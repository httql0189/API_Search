# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiCourse(models.Model):
    course_url = models.CharField(max_length=100)
    course_tag = models.CharField(primary_key=True, max_length=100)
    course_title = models.CharField(max_length=100, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    rating_count = models.CharField(max_length=20, blank=True, null=True)
    review_count = models.CharField(max_length=20, blank=True, null=True)
    offer_by = models.CharField(max_length=50, blank=True, null=True)
    enrolled = models.CharField(max_length=10, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    skill_gain = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=15, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    course_image = models.CharField(max_length=4096, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_course'


class ApiReview(models.Model):
    star = models.IntegerField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)
    reviewer = models.CharField(max_length=50, blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    review_vote = models.IntegerField(blank=True, null=True)
    review_link = models.CharField(max_length=200, blank=True, null=True)
    course_tag = models.ForeignKey(ApiCourse, models.DO_NOTHING, db_column='course_tag', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_review'


class ApiUser(models.Model):
    userid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=4096, blank=True, null=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50, blank=True, null=True)
    role = models.IntegerField()
    isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
    provider = models.CharField(max_length=20)
    type1 = models.CharField(max_length=50, blank=True, null=True)
    type2 = models.CharField(max_length=50, blank=True, null=True)
    type3 = models.CharField(max_length=50, blank=True, null=True)
    time_onscreen_page = models.TimeField(blank=True, null=True)
    most_action_each_page = models.IntegerField(blank=True, null=True)
    most_url_click = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'
