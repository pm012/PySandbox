class UserSystem:
    def get_users(self) -> list:
        users = [
            {
                "name": "Allen Raymond",
                "email": "nulla.ante@vestibul.co.uk",
                "gender": "male",
            },
            {
                "name": "Chaim Lewis",
                "email": "dui.in@egetlacus.ca",
                "gender": "male",
            },
            {
                "name": "Kennedy Lane",
                "email": "mattis.Cras@nonenimMauris.net",
                "gender": "female",
            },
            {
                "name": "Wilie Pope",
                "email": "st@utquamvel.net",
                "gender": "female",
            },
            
        ]
        return users
    
    def separate_users(self, users):
        male = []
        female = []
        
        for user in users:
            if user.get("gender", None) == "male":
                male.append(user)
            else:
                female.append(user)
                
        return male, female
    
class EmailSystem:
    def get_text_email(self, gender) -> str:
        text = "Default text"
        if gender == 'male':
            text = "Male text email"
        if gender == 'female':
            text = "Female text email"
            
        return text
    
    def send_emails(self, users, text) -> str:
        for user in users:
            print(f"Send {user.get('name')} email: {text}")
        return "Done"
    
class FacadeNewsletter:
    def __init__(self, users_system, email_system):
        self._users_system = users_system
        self._email_system = email_system
        
    def sending(self) -> str:
        users = self._users_system.get_users()
        male, female = self._users_system.separate_users(users)
        text_for_male = self._email_system.get_text_email("male")
        text_for_female = self._email_system.get_text_email("female")
        self._email_system.send_emails(male, text_for_male)
        self._email_system.send_emails(female, text_for_female)
        
        
    
def client_cde(newsletter) -> None:
    print(newsletter.sending(), end='')
    
if __name__ == "__main__":
    facade = FacadeNewsletter(UserSystem(), EmailSystem())
    client_cde(facade)
        