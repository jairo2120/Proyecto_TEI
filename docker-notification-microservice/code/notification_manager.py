from email_adapter import email_adapter
from sms_adapter import sms_adapter
class Notification_manager(): 
    def __init__(self,email,phone,message):
        self.email = email
        self.phone = phone
        self.message = message
        
    def email_ad(self):
        print(self.email,self.message)
        email_adapter(self.email,self.message)
        
    def sms_ad(self): 
        print(self.phone,self.message)
        sms_adapter(self.phone,self.message)
        
    
    
    
        