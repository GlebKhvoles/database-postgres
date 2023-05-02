db_info = {'host': 'dpg-ch7adag2qv26p1btlsig-a.oregon-postgres.render.com',
           'database': 'render_6bjb',
           'psw': 'jGuMtISwrcjpyNbCwFS5F2h2i3zsJJpr',
           'user': 'khvol',
           'port': '5432'}


class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
    #SQLALCHEMY_DATABASE_URI = f"postgres://khvol:jGuMtISwrcjpyNbCwFS5F2h2i3zsJJpr@dpg-ch7adag2qv26p1btlsig-a.oregon-postgres.render.com/render_6bjb"
