# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Analytics(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    opt_out_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analytics'


class AuthAssignment(models.Model):
    item_name = models.OneToOneField('AuthItem', models.DO_NOTHING, db_column='item_name', primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    created_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_assignment'
        unique_together = (('item_name', 'user'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthItem(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    type = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    rule_name = models.ForeignKey('AuthRule', models.DO_NOTHING, db_column='rule_name', blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)
    group_code = models.ForeignKey('AuthItemGroup', models.DO_NOTHING, db_column='group_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_item'


class AuthItemChild(models.Model):
    parent = models.CharField(primary_key=True, max_length=64)
    child = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'auth_item_child'
        unique_together = (('parent', 'child'),)


class AuthItemGroup(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=255)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_item_group'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthRule(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    data = models.TextField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_rule'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ColdStorageAutoaccept(models.Model):
    storage = models.FloatField(blank=True, null=True)
    user_type = models.CharField(max_length=15, blank=True, null=True)
    autoaccept_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cold_storage_autoaccept'


class ColdStorageLimits(models.Model):
    storage = models.BigIntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=15, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    number_of_projects = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cold_storage_limits'


class ColdStorageRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.BigIntegerField(blank=True, null=True)
    storage = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    additional_resources = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    vm_type = models.IntegerField(blank=True, null=True)
    num_of_volumes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cold_storage_request'


class Configuration(models.Model):
    reviewer_num = models.IntegerField(blank=True, null=True)
    home_page = models.IntegerField(blank=True, null=True)
    privacy_page = models.IntegerField(blank=True, null=True)
    help_page = models.IntegerField(blank=True, null=True)
    schema_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuration'


class CronJob(models.Model):
    id_cron_job = models.AutoField(primary_key=True)
    controller = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    limit = models.IntegerField(blank=True, null=True)
    offset = models.IntegerField(blank=True, null=True)
    running = models.SmallIntegerField()
    success = models.SmallIntegerField()
    started_at = models.IntegerField(blank=True, null=True)
    ended_at = models.IntegerField(blank=True, null=True)
    last_execution_time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cron_job'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Email(models.Model):
    recipient_ids = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'


class EmailEvents(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_creation = models.BooleanField(blank=True, null=True)
    new_project = models.BooleanField(blank=True, null=True)
    project_decision = models.BooleanField(blank=True, null=True)
    new_ticket = models.BooleanField(blank=True, null=True)
    expires_30 = models.BooleanField(blank=True, null=True)
    expires_15 = models.BooleanField(blank=True, null=True)
    edit_project = models.BooleanField(blank=True, null=True)
    expires_1 = models.BooleanField(blank=True, null=True)
    expires_5 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_events'


class EmailEventsAdmin(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_creation = models.BooleanField(blank=True, null=True)
    new_ticket = models.BooleanField(blank=True, null=True)
    expires_1 = models.BooleanField(blank=True, null=True)
    expires_5 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_events_admin'


class EmailEventsModerator(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    new_project = models.BooleanField(blank=True, null=True)
    expires_30 = models.BooleanField(blank=True, null=True)
    expires_15 = models.BooleanField(blank=True, null=True)
    expires_1 = models.BooleanField(blank=True, null=True)
    expires_5 = models.BooleanField(blank=True, null=True)
    project_decision = models.BooleanField(blank=True, null=True)
    edit_project = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_events_moderator'


class EmailEventsUser(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    project_decision = models.BooleanField(blank=True, null=True)
    expires_1 = models.BooleanField(blank=True, null=True)
    expires_5 = models.BooleanField(blank=True, null=True)
    expires_30 = models.BooleanField(blank=True, null=True)
    expires_15 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_events_user'


class HotVolumes(models.Model):
    name = models.TextField(blank=True, null=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    volume_id = models.TextField(blank=True, null=True)
    mountpoint = models.TextField(blank=True, null=True)
    accepted_at = models.DateTimeField(blank=True, null=True)
    vm_type = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.TextField(blank=True, null=True)
    vm_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    mult_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hot_volumes'


class MachineComputeLimits(models.Model):
    user_type = models.CharField(max_length=15, blank=True, null=True)
    number_of_projects = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_compute_limits'


class MachineComputeRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    num_of_vms = models.SmallIntegerField(blank=True, null=True)
    num_of_cores = models.SmallIntegerField(blank=True, null=True)
    num_of_ips = models.SmallIntegerField(blank=True, null=True)
    ram = models.FloatField(blank=True, null=True)
    storage = models.FloatField(blank=True, null=True)
    request_id = models.BigIntegerField(blank=True, null=True)
    vm_flavour = models.TextField(blank=True, null=True)
    disk = models.IntegerField(blank=True, null=True)
    additional_resources = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_compute_request'


class Migration(models.Model):
    version = models.CharField(primary_key=True, max_length=180)
    apply_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migration'


# class Notification(models.Model):
#     #recipient_id = models.AutoField()
#     message = models.TextField(blank=True, null=True)
#     seen = models.BooleanField(blank=True, null=True)
#     type = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     read_at = models.DateTimeField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'notification'


class OndemandAutoaccept(models.Model):
    num_of_jobs = models.IntegerField(blank=True, null=True)
    cores = models.IntegerField(blank=True, null=True)
    ram = models.FloatField(blank=True, null=True)
    user_type = models.CharField(max_length=15, blank=True, null=True)
    autoaccept_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ondemand_autoaccept'


class OndemandLimits(models.Model):
    num_of_jobs = models.IntegerField(blank=True, null=True)
    cores = models.IntegerField(blank=True, null=True)
    ram = models.FloatField(blank=True, null=True)
    user_type = models.CharField(max_length=15, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    number_of_projects = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ondemand_limits'


class OndemandRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    maturity = models.TextField(blank=True, null=True)  # This field type is a guess.
    analysis_type = models.CharField(max_length=200, blank=True, null=True)
    containerized = models.BooleanField(blank=True, null=True)
    num_of_jobs = models.IntegerField(blank=True, null=True)
    ram = models.FloatField(blank=True, null=True)
    cores = models.IntegerField(blank=True, null=True)
    additional_resources = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ondemand_request'


class Openstack(models.Model):
    nova_url = models.TextField(blank=True, null=True)
    keystone_url = models.TextField(blank=True, null=True)
    cinder_url = models.TextField(blank=True, null=True)
    neutron_url = models.TextField(blank=True, null=True)
    glance_url = models.TextField(blank=True, null=True)
    tenant_id = models.TextField(blank=True, null=True)
    floating_net_id = models.TextField(blank=True, null=True)
    cred_id = models.TextField(blank=True, null=True)
    cred_secret = models.TextField(blank=True, null=True)
    internal_net_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openstack'


class OpenstackMachines(models.Model):
    nova_url = models.TextField(blank=True, null=True)
    keystone_url = models.TextField(blank=True, null=True)
    cinder_url = models.TextField(blank=True, null=True)
    neutron_url = models.TextField(blank=True, null=True)
    glance_url = models.TextField(blank=True, null=True)
    tenant_id = models.TextField(blank=True, null=True)
    floating_net_id = models.TextField(blank=True, null=True)
    cred_id = models.TextField(blank=True, null=True)
    cred_secret = models.TextField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    internal_net_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openstack_machines'


class Pages(models.Model):
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    latest_project_request_id = models.BigIntegerField(blank=True, null=True)
    pending_request_id = models.BigIntegerField(blank=True, null=True)
    project_type = models.SmallIntegerField(blank=True, null=True)
    favorite = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    user_num = models.IntegerField(blank=True, null=True)
    user_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    backup_services = models.BooleanField(blank=True, null=True)
    viewed = models.BooleanField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    submitted_by = models.IntegerField(blank=True, null=True)
    submission_date = models.DateTimeField(blank=True, null=True)
    assigned_to = models.BigIntegerField(blank=True, null=True)
    project_type = models.SmallIntegerField(blank=True, null=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    deletion_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    additional_resources = models.TextField(blank=True, null=True)
    louros = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_request'


class ServiceAutoaccept(models.Model):
    vms = models.IntegerField(blank=True, null=True)
    cores = models.IntegerField(blank=True, null=True)
    ips = models.IntegerField(blank=True, null=True)
    ram = models.FloatField(blank=True, null=True)
    storage = models.FloatField(blank=True, null=True)
    user_type = models.CharField(max_length=15, blank=True, null=True)
    autoaccept_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_autoaccept'


class ServiceLimits(models.Model):
    vms = models.IntegerField(blank=True, null=True)
    cores = models.IntegerField(blank=True, null=True)
    ips = models.IntegerField(blank=True, null=True)
    ram = models.FloatField(blank=True, null=True)
    storage = models.FloatField(blank=True, null=True)
    user_type = models.CharField(max_length=15, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    number_of_projects = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_limits'


# class ServiceRequest(models.Model):
#     #id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     version = models.CharField(max_length=50, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     url = models.TextField(blank=True, null=True)
#     num_of_vms = models.SmallIntegerField(blank=True, null=True)
#     num_of_cores = models.SmallIntegerField(blank=True, null=True)
#     num_of_ips = models.SmallIntegerField(blank=True, null=True)
#     ram = models.FloatField(blank=True, null=True)
#     storage = models.FloatField(blank=True, null=True)
#     request_id = models.BigAutoField()
#     trl = models.SmallIntegerField(blank=True, null=True)
#     vm_flavour = models.TextField(blank=True, null=True)
#     disk = models.IntegerField(blank=True, null=True)
#     additional_resources = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'service_request'


class Smtp(models.Model):
    encryption = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    port = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smtp'


class TicketBody(models.Model):
    id_head = models.ForeignKey('TicketHead', models.DO_NOTHING, db_column='id_head')
    name_user = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    client = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_body'


class TicketFile(models.Model):
    id_body = models.ForeignKey(TicketBody, models.DO_NOTHING, db_column='id_body')
    filename = models.CharField(db_column='fileName', max_length=255)  # Field name made lowercase.
    document_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_file'


class TicketHead(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    department = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    page = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_head'


class User(models.Model):
    username = models.CharField(max_length=255)
    auth_key = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=255)
    confirmation_token = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    superadmin = models.SmallIntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    registration_ip = models.CharField(max_length=15, blank=True, null=True)
    bind_to_ip = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    email_confirmed = models.SmallIntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserVisitLog(models.Model):
    token = models.CharField(max_length=255)
    ip = models.CharField(max_length=15)
    language = models.CharField(max_length=2)
    user_agent = models.CharField(max_length=255)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    visit_time = models.IntegerField()
    browser = models.CharField(max_length=30, blank=True, null=True)
    os = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_visit_log'


class Vm(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    ip_id = models.TextField(blank=True, null=True)
    vm_id = models.TextField(blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)
    image_id = models.TextField(blank=True, null=True)
    image_name = models.CharField(max_length=100, blank=True, null=True)
    request_id = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    keypair_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    volume_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    do_not_delete_disk = models.BooleanField(blank=True, null=True)
    windows_unique_id = models.TextField(blank=True, null=True)
    read_win_password = models.BooleanField(blank=True, null=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vm'


class VmMachines(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    ip_id = models.TextField(blank=True, null=True)
    vm_id = models.TextField(blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)
    image_id = models.TextField(blank=True, null=True)
    image_name = models.CharField(max_length=100, blank=True, null=True)
    request_id = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    keypair_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    volume_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    do_not_delete_disk = models.BooleanField(blank=True, null=True)
    windows_unique_id = models.TextField(blank=True, null=True)
    read_win_password = models.BooleanField(blank=True, null=True)
    project_id = models.BigIntegerField(blank=True, null=True)
    project_multiple_order = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vm_machines'

