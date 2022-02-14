
import uuid
from pathlib import Path
import configparser
from contextlib import contextmanager

from model import Session, AppMeta, History

session = Session()


def _get_app_meta_from_repo():
    meta_path_list = [str(x) for x in Path('.').glob('**/app_meta.ini')]
    meta_parser = configparser.ConfigParser()  # 클래스 객체 생성

    app_meta = []
    for meta_path in meta_path_list:
        app_dir = '/'.join(meta_path.split('/')[:-1])
        meta_parser.read(meta_path)
        default = meta_parser["DEFAULT"]
        desc = default.get('desc', None)
        if desc is None:
            continue
        made_by = default.get('made_by', None)
        if made_by is None:
            continue

        app_meta.append(AppMeta(
            id=str(uuid.uuid1()),
            path=app_dir,
            desc=desc
        ))
    return app_meta


def create_app_meta():
    if len(read_app_meta()) != 0:
        print('[Info] App Meta Database already created (this is one time method)\n')
        return
    print('[Info] Initially create App Meta Database\n')
    app_meta = _get_app_meta_from_repo()
    session.add_all(app_meta)
    session.commit()


def read_app_meta(id=None):
    if id is None:
        return AppMeta.find_all(session)
    return AppMeta.find_by_id(session, id)


def update_app_meta():
    """ 
    reset?
    update, insert라고 한다면
    history도 바뀌어야하는가?
    """
    pass


def delete_app_meta():
    pass


def create_history():
    pass


def read_history():
    return History.find_all(session)


def delete_history():
    pass


def update_history():
    pass


def read_app_meta_columns():
    return AppMeta.__table__.columns.keys()


def read_history_columns():
    return History.__table__.columns.keys()


def test():
    create_app_meta()
    print(read_app_meta())
    print(read_app_meta(id='6a51b13e-6fce-11ec-99ec-acde48001122'))


if __name__ == '__main__':
    test()
