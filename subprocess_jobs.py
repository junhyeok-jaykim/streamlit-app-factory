import os
import sys
import socket
import signal
import subprocess
import streamlit as st

def kill_child_process(pid):
    print(f'Shutting Process {pid}')
    os.killpg(os.getpgid(pid), signal.SIGTERM)
    # os.kill(pid, signal.SIGTERM)


def deploy_app(app_path: str):
    """ Deploy Form > Deploy 또는 Historical Run > Rerun 버튼을 클릭하는 경우
    기존 정보를 가져와서 앱을 실행하는 작업을 제출한다.
    (Port는 사용하지 않는 것으로 자동으로 선택하도록 한다)
    제출된 작업은 성공 시, Running Apps의 가장 상단에 보여진다. 
    """
    app_path = 'table_demo'
    # cmd = "cd sample_table; nohup sh run.sh &"
    cmd = "cd sample_table; nohup ./run.sh &> .log/streamlit.log &"
    # cmd = "cd sample_table; nohup streamlit run streamlit_app.py &> streamlit.log"
    # cmd = "python temp.py"
    # cmd = "nohup ./run.sh demo_generator.py"
    # sub_process = subprocess.run(
    #     cmd, 
    #     shell=True,  # if use plain shell command
    #     # stdout=subprocess.PIPE)
    #     capture_output=True  # stdout and stderr will be captured.
    # )
    # stdout, stderr 
    # print(f"[stderr] {sub_process.stderr.decode('utf-8')}")
    # print(f"[stdout] {sub_process.stdout.decode('utf-8')}")
    # print(output.returncode)

    # https://seokdev.site/286
    sub_process = subprocess.Popen(
        cmd, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        # start_new_session=True, # This will allow the parent process to exit while the child process continues to run.
        preexec_fn=os.setsid,
        # preexec_fn=os.setpgrp,
        shell=True)

    print(sub_process.pid)
    # print(os.getpgid(sub_process.pid))

    # NOTE: `streamlit run {script.py}`` 의 경우
    # 앱을 deploy한 후에 발생하는 에러들은 html로 화면에 표시한다.
    # 따라서 해당 앱의 화면에서 앱을 업데이트할 때마다 확인을 하던가
    # 혹은 {app_directory}/.log/streamlit.{datetime}.log 를
    # 조회하여 확인하도록 한다.
    # access stdout, stderr by using PIPE
    # print(sub_process.stdout.readlines())
    # print(sub_process.stderr.readlines())

    # TODO: color 추가
    # st.write('deploy app')


    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # line = ''
    # for raw_line in iter(sub_process.stdout.readline, b''):
    #     line = raw_line.decode("utf-8")
    #     print(line)
    #     if sock.connect_ex(('localhost', 8507)) == 0:  # 서버에서 반응이 오면, 로그 닫기
    #         ZK_STATUS = True
    #         sock.close()
    #         break

    # if output.returncode != 0:
    #     st.error('작업 제출에 실패했습니다 😱')
    #     st.write(output.stderr.decode('utf-8'))
    # else:
    #     st.balloons()
    #     st.write(output.stdout.decode('utf-8'))
        
    return sub_process.returncode


if __name__ == '__main__':
    deploy_app('afadsf')
