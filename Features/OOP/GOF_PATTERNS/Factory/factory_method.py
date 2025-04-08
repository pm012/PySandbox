from abc import abstractmethod, ABC

class Creator(ABC):
    def create(self):
        pass

    def send_messages(self) -> str:
        product = self.create()
        return product.sending()
       
    
class SendingMessages(ABC):
    @abstractmethod
    def sending(self)-> str:
        pass

class CreatorPush(Creator):
    def create(self)->SendingMessages:
        return SendingPushMessages()

class CreatorSMS(Creator):
    def create(self) -> SendingMessages:
        return SendingSMSMessages()
    
class SendingPushMessages(SendingMessages):
   def sending(self) -> str:
       return "Sending Push message"

class SendingSMSMessages(SendingMessages):
    def sending(self) -> str:
        return "Sending SMS message"
    

def client_code(creator: Creator)->None:
    print("We know nothing about code")
    result = creator.send_messages()
    print(f"Result {result}")


if __name__ == "__main__":
    print("Push will be sent:")
    client_code(CreatorPush())
    print("/n")

    print("SMS will be sent:")
    client_code(CreatorSMS())
    print("/n")

    
     
