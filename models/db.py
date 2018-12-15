from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload = True)

db = DAL("sqlite://storage.sqlite")

db.define_table("Add_NOTES", Field('db_title'), Field('db_notes'),Field('db_file'))

db.define_table("noteWriter", 
                Field('db_firstname'),
                Field('db_middlename'),
                Field('db_lastname'),
                Field('db_email'),
                Field('db_password'),
                Field('db_repassword'))