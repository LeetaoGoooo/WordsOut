from abc import ABC
from http.cookiejar import CookieJar
import random
import time
from typing import List, Union

registry = {}

def register(cls):
    registry[cls.name] = cls()


class BaseExport(ABC):
    
    name = None  # use short name to describe which your class work for 

    def __init_subclass__(cls, **kwargs):
      if not getattr(cls, 'name'):
            raise TypeError(f"Can't instantiate abstract class {cls.__name__} without name attribute defined")
      
      super().__init_subclass__(**kwargs)
      register(cls)

    @classmethod
    def export(self, cookie_str:Union[str, CookieJar]):
        """export words from dict"""
        raise NotImplementedError
    

    def write_words_to_txt(self, words:List[str]):
        """write words to text"""
        with open("words.txt", "a+") as f:
            f.write("\n".join(words))
            f.write("\n")
        
    def take_a_break(self):
        sleep_time = random.randint(1, 3)
        print("Task a random sleep for {}s".format(sleep_time))
        time.sleep(sleep_time)
