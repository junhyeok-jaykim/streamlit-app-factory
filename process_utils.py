import os
from datetime import datetime
import psutil
# https://psutil.readthedocs.io/en/latest/#recipes


# ip, port checking
# proc.connections()[0].laddr.ip
# proc.connections()[0].laddr.port
# conn = proc.connections()
# local_ip = conn.laddr[0]
# localport = conn.laddr[1]
# remote_ip = conn.raddr[0] if conn.raddr else '-'
# remote_port = conn.raddr[1] if conn.raddr else '-'

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(['name']):
        print(p.info['name'])
        if p.info['name'] == name:
            ls.append(p)
    return ls


def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(["name", "exe", "cmdline"]):
        print(p.info)
        print(p.pid)
        try:
            print(p.cwd())
        except:
            continue
        if ((name == p.info['name'])
            or (p.info['exe'] and os.path.basename(p.info['exe']) == name)
            or (p.info['cmdline'] and p.info['cmdline'][0] == name)):
            ls.append(p)
    return ls

"""
demo_generator.py 앱에서 동작한 프로세스를 확인하기 위해서는
running + cmdline + cwd 
"""

# find_procs_by_name('python3.9')
find_procs_by_name('streamlit')

def find_demo_generator_deploy_procs():
    for p in psutil.psutil.process_iter(["cmdline"]):
        [x for x in p.info['cmdline'] if 'streamlit.log']
        
    # 시간 순서대로 정렬한다. 
    pass


# for proc in psutil.process_iter():
#     try:
#         if 'AppFactory' in proc.cwd() and proc.connections():
#             print(proc)
#             print('\t', proc.is_running())
#             for x in proc.connections():
#                 print(type(x), x)
#             print('\t', proc.cwd())
#     except:
#         continue

# process = psutil.Process(48629)
# print(process)

# process_info = process.as_dict()
# for k, v in process_info.items():
#     print(k , v, sep='\t')
# created_at = datetime.fromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')


# with process.oneshot():
#     process.name()
#     process.cpu_times()
#     process.cpu_percent()
#     process.create_time()
#     process.ppid()
#     process.gids()
#     process.uids()
#     process.status()
#     process.cwd()
#     process.is_running()
#     process.cmdline()
#     process.connections()
#     # process.kill()
