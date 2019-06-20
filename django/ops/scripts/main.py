
import datetime

import pymysql



def connect():
    '''
    def __init__(self, host=None, user=None, password="",
                 database=None, port=0, unix_socket=None,
                 charset='', sql_mode=None,
                 read_default_file=None, conv=None, use_unicode=None,
                 client_flag=0, cursorclass=Cursor, init_command=None,
                 connect_timeout=10, ssl=None, read_default_group=None,
                 compress=None, named_pipe=None,
                 autocommit=False, db=None, passwd=None, local_infile=False,
                 max_allowed_packet=16 * 1024 * 1024, defer_connect=False,
                 auth_plugin_map=None, read_timeout=None, write_timeout=None,
                 bind_address=None, binary_prefix=False, program_name=None,
                 server_public_key=None):
    '''
    return pymysql.connect(
        host = 'localhost',
        user = '',
        password = '123456',
        database = 'ops',
        port = 3306
    )


def Select(sql:str):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except Exception as e:
        return e.args, False
    else:
        rows = cur.fetchall()
        return rows, True
    finally:
        cur.close()
        conn.close()

def Insert(sql:str):
    conn = connect()
    # conn.autocommit(True)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return "", True
    except Exception as e:
        conn.rollback()
        return e.args, False
    finally:
        cur.close()
        conn.close()

def Binsert(sql:str):
    pass

def Update(sql:str):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if cur.rowcount != 1:
            return "Update fail", False

        conn.commit()
        return "", True
    except Exception as e:
        conn.rollback()
        return e.args, False
    finally:
        cur.close()
        conn.close()

def Delete(sql:str):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if cur.rowcount != 1:
            return "Delete fail", False

        conn.commit()
        return "", True
    except Exception as e:
        conn.rollback()
        return e.args, False
    finally:
        cur.close()
        conn.close()

def close():
    pass


def main():
    # 查询
    '''
    sql = "select * from users;"
    result, ok = Select(sql)
    for i in result:
        print(i)
    '''

    # 新增
    '''
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(cur_time, type(cur_time))
    sql = "INSERT INTO users(username, age, sex, phone, address, create_time, update_time)  " \
          "VALUES('51reboot', 4, '男', '1321xxx', '北京', '{}', '{}');".format(cur_time, cur_time)
    print(sql)
    result, ok = Insert(sql)
    print(ok)
    print(result)
    '''

    # 修改
    '''
    sql = "UPDATE users SET age = 22 WHERE username = '51reboot'"
    result, ok = Update(sql)
    print(ok)
    print(result)
    '''

    # 删除
    sql = "DELETE from users WHERE username = '51reboot'"
    result, ok = Delete(sql)
    print(ok)
    print(result)



if __name__ == '__main__':
    main()