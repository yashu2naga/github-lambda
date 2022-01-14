import boto3
import pandas as pd
# import module
from tabulate import tabulate
ses_client = boto3.client('ses',region_name='ap-south-1')

# if __name__ == '__main__':
def lambda_handler(event, context):
    my_list=[('Abyaya', 'Hotta', 123), ('Balakrishna', 'Kompala', 345),
             ('Sathyanarayana', 'Dathrika', 567), ('Praveen', 'Maroju', 631),
             ('Giridhar', 'Pochareddy', 151)]
    
    print(my_list)
    # create header
    head = ["Name", "LastName","Number"]
  
    # display table
    print(tabulate(my_list, headers=head, tablefmt="grid"))
    # table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]
    second_list=tabulate(my_list,headers=head, tablefmt='html')
    print((second_list))
    
    print("calling the SES Function")
    CHARSET = "UTF-8"
    HTML_EMAIL_CONTENT = """ """
    HTML_EMAIL_CONTENT=second_list
     
    
    response= ses_client.send_email(
        
        Destination={
           
            "ToAddresses": [
                "yasaswini.kalamkuntla@wisseninfotech.com",
            ],
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": CHARSET,
                    "Data": HTML_EMAIL_CONTENT,
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Amazing Email Tutorial",
            },
        },
        Source="yasaswini.kalamkuntla@wisseninfotech.com",
        
    )
    
