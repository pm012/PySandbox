from abc import ABC, abstractmethod
from time import sleep, time
class Request(ABC):
    @abstractmethod
    def request()->None:
        pass
    
    
class RealRequest:
    def request(self)->None:
        print("RealRequest: Handling request")
        sleep(0.5)
        
class TimeLoggingDecorator:
    def __init__(self, wrapped_request: Request):
        self._wrapped_request = wrapped_request
        
    def request(self)->None:
        start = time()
        self._wrapped_request.request()
        print(f"Decorator: Loggin execution time: {time()-start}")
        
def client_code(decorated_request):
    decorated_request.request()
        
if __name__ == "__main__":
    decorated_request = TimeLoggingDecorator(RealRequest())
    client_code(decorated_request)
    