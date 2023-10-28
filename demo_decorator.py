from typing import Optional, Callable


def is_auth(function) -> Callable:
    """authorization decorator used for method

    Args:
        function (DemoAuth): method to be authorized

    Returns:
        Callable: _description_
    """
    def check_auth(obj: "DemoAuth") -> Optional[Callable]:
        username: str = obj.username
        passwd: str = obj.passwd

        func = function(obj)
        if obj.check_db(username=username, passwd=passwd):
            return func

        return None

    return check_auth


class DemoAuth:
    """class with secret method to be

    Returns:
        _type_: _description_
    """
    __username: str
    __passwd: str

    def __init__(self, username: str, passwd: str) -> None:
        self.__username = username
        self.__passwd = passwd

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, in_username: str) -> None:
        self.__username = in_username

    @property
    def passwd(self) -> str:
        return self.__passwd

    @passwd.setter
    def passwd(self, in_passwd: str) -> None:
        self.__passwd = in_passwd

    def check_db(self, username: str, passwd: str) -> bool:
        if username == "foo" and passwd == "qwerty":
            return True
        return False

    @is_auth
    def something_secret(self) -> str:
        return f"{self.username}:{self.passwd} has access to secret"


if __name__ == "__main__":
    d: DemoAuth = DemoAuth("foo", "qwerty")

    print(d.something_secret())
