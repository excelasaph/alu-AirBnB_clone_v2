import fabric.api as fab
from datetime import datetime


def do_pack():
    date_obj = datetime.now()
    date_str = date_obj.isoformat()
    char_rem = "-:.T"
    count = 0;
    try:
    	while char_rem[count] in date_str:
            date_str = date_str.split(char_rem[count])
            date_str = "".join(date_str)
            count += 1
    except IndexError:
        pass
    else:
    	print(date_str)
    fab.local("tar -czvf web_static_{0}.tar.gz web_static".format(date_str))
