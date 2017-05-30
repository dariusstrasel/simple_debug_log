import datetime


class debug:

    priority_map = {
        1: {'filename': 'INFO.log', 'message_header': 'INFO'},
        2: {'filename': 'DEBUG.log', 'message_header': 'DEBUG'},
        3: {'filename': 'CRITICAL.log', 'message_header': 'CRITICAL'},
    }

    def __init__(self):
        pass

    @classmethod
    def __debug_print(self, text, priority):
        final_message = "%s: %s" % (datetime.datetime.now(), text)
        print(final_message)
        try:
            return self.__write_to_log(self.priority_map[priority]['filename'], final_message)
        except KeyError:
            return self.__write_to_log(self.priority_map[1]['filename'], final_message)

    @staticmethod
    def __write_to_log(filename, text):
        try:
            with open(filename, 'a') as file:
                file.write(str(text) + '\n')
        except IOError:
            print("%s: Could not access logfile. :(" % (datetime.datetime.now()))
            raise

    @classmethod
    def info(self, text):
        info_priority = 3
        return self.__debug_print("%s: %s" % (self.priority_map[info_priority]['message_header'], text), info_priority)

    def api(self, text):
        api_priority = 2
        return self.__debug_print("%s: %s" % (self.priority_map[api_priority]['message_header'], text), api_priority)

    @classmethod
    def critical(self, text):
        critical_priority = 1
        return self.__debug_print("%s: %s" % (self.priority_map[critical_priority]['message_header'], text), critical_priority)

if __name__ == "__main__":
    import random
    for integer in range(0, random.randint(1, 25)):
        debug.info("Test: %s" % integer)

    for integer in range(0, random.randint(1, 25)):
        debug.critical("Test: %s" % integer)
