import random
import string
import re
import os

from Users import get_user
from models import db

def generate_password(length,complexity):

    char_set_list = [string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation]
    char_set=""
    for i in range(0,complexity):
        char_set += char_set_list[i]
    pwd = ''.join(random.choices(char_set,k=length))
    return pwd


def check_password_level(passwd):

    if re.match(r'[a-z]*', passwd):
        if len(passwd) >= 8:
            complexity = 2
        else:
            complexity = 1
    elif re.match(r'(?=.*[0-9])([a-z0-9]+)',passwd):
        if len(passwd) >= 8:
            complexity = 3
        else:
            complexity = 2
    elif re.match(r'(?=.*[0-9])(?=.*[A-Z])([a-zA-Z0-9]+)',passwd):
        complexity = 3
    elif re.match(r'(?=.*[0-9])(?=.*[A-Z])(?=.*[!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~])([a-zA-Z0-9!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]+)',passwd):
        complexity = 4

def create_user(dbfile):
    conn = db.connect_db(dbfile)
    db.create_user_table(conn)
    sql = "insert into users (name,email,passwd) values ('{}','{}','{}');"
    detail = get_user()
    pwd = generate_password(random.randint(6,12),random.randint(1,4))
    sql = sql.format(detail.get('fullname'),detail.get('email'),pwd)
    db.execute_insert_sql(sql,conn)
    conn.close()



if __name__ == '__main__':
    usercount = int(input("Enter no. of users to create :"))
    cur_dir= os.getcwd()
    db_file = os.path.join(cur_dir,'users.db')
    for i in range(0,usercount):
        create_user(db_file)
    con = db.connect_db(db_file)
    print(db.execute_sql('select * from users',con))
    con.close()