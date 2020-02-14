import redis


class RedisHandler(object):
    '''
    make sure your redis server is available!
    Attributes:
        db: Database
        password: Password
        host: Server
        port: Port
    '''

    def __init__(self, host="127.0.0.1", port=6379, db=None, password=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password

    def __connect(self):
        '''connect to redis server
        Raises:
            redis.exceptions.ConnectionError: Error 61 \
                connecting to {host}:{port}. Connection refused.
        '''
        return redis.Redis(host=self.host, port=self.port,
                           db=self.db, password=self.password)

    def set_(self, key, value):
        '''set method in redis'''
        conn = self.__connect()
        conn.set(key, value)
        conn.close()

    def get_(self, key):
        '''get method in redis'''
        conn = self.__connect()
        result = conn.get(key)
        conn.close()
        return result

    def del_(self, key):
        '''del method in redis'''
        conn = self.__connect()
        result = conn.delete(key)
        conn.close()
        return result

    def getrange(self, key, start, end=-1) -> list:
        '''
        getrange method in redis
        Args:
            key: key in redis set
            start: the start index of the set
            end: the end index of the set
        Returns:
            result: a list contains all the items in the set
        '''
        conn = self.__connect()
        range_ = str(conn.getrange(key, start, end), encoding='utf-8')
        print(range_)
        result = [item for item in range_ if item != ' ']
        return result


if __name__ == "__main__":
    rd_handler = RedisHandler()
    rd_handler.set_("name", "I am z bc")
    rd_handler.getrange("name", 0, 2)
    # print(rd_handler.del_("name"))
