import sys
import traceback
from contextlib import suppress
from typing import Union

from config import logger, process_list_path, host
from tools.app import App
from tools.odines import Odines
from tools.process import kill_process_list
from tools.web import Web


def main():

    app = App('')

    app.find_element({"title": "Хост:", "class_name": "Edit", "control_type": "Edit",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).click(double=True)
    app.find_element({"title": "Хост:", "class_name": "Edit", "control_type": "Edit",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).type_keys(host)

    app.find_element({"title": "Имя пользователя:", "class_name": "Edit", "control_type": "Edit",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).click(double=True)
    app.find_element({"title": "Имя пользователя:", "class_name": "Edit", "control_type": "Edit",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).type_keys(host)

    app.find_element({"title": "Пароль:", "class_name": "Edit", "control_type": "Edit",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).click(double=True)
    app.find_element({"title": "Пароль:", "class_name": "Edit", "control_type": "Edit",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).type_keys(host)

    app.find_element({"title": "Порт:", "class_name": "Edit", "control_type": "Edit",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).click(double=True)
    app.find_element({"title": "Порт:", "class_name": "Edit", "control_type": "Edit",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).type_keys(host)

    app.find_element({"title": "Быстрое соединение", "class_name": "Button", "control_type": "Button",
                      "visible_only": True, "enabled_only": True, "found_index": 0}).click()

    if app.wait_element({"title": "magnum-uploads", "class_name": "", "control_type": "TreeItem",
                         "visible_only": True, "enabled_only": True, "found_index": 0}):
        app.find_element({"title": "reports", "class_name": "", "control_type": "Edit",
                          "visible_only": True, "enabled_only": True, "found_index": 0}).click(double=True)

        app.find_element({"title_re": "outsourcingshifts.*", "class_name": "", "control_type": "Edit",
                          "visible_only": True, "enabled_only": True, "found_index": 0}).click()
        app.find_element({"title_re": "outsourcingshifts.*", "class_name": "", "control_type": "Edit",
                          "visible_only": True, "enabled_only": True, "found_index": 0}).click(right=True)

        app.find_element({"title": "Скачать", "class_name": "", "control_type": "MenuItem",
                          "visible_only": True, "enabled_only": True, "found_index": 0}).click()


if __name__ == '__main__':
    # noinspection PyTypeChecker
    app: Union[Web, Odines] = None
    # ? не убирать данный try, он необходим для того чтобы Pyinstaller не выводил traceback в окошко
    try:
        logger.warning("START")

        main()

        logger.warning("END")
    except (Exception,):
        with suppress(Exception):
            app.quit()
        kill_process_list(process_list_path)
        traceback.print_exc()
        sys.exit(1)
