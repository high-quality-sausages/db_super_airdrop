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


if __name__ == "__main__":
    rd_handler = RedisHandler()
    rd_handler.set_("name", "bc")
    print(rd_handler.del_("name"))
