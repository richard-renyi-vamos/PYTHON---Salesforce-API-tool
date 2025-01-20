from simple_salesforce import Salesforce
import json

# Replace these with your Salesforce login credentials
sf = Salesforce(username='your_username',
                password='your_password',
                security_token='your_security_token')

# Example: Querying Accounts data from Salesforce
try:
    accounts = sf.query_all("SELECT Id, Name, Industry FROM Account LIMIT 5")
    # Displaying the results
    for account in accounts['records']:
        print(f"Account ID: {account['Id']}, Name: {account['Name']}, Industry: {account.get('Industry', 'N/A')}")
except Exception as e:
    print(f"Error occurred: {str(e)}")

# Example: Querying Contacts data from Salesforce
try:
    contacts = sf.query_all("SELECT Id, FirstName, LastName, Email FROM Contact LIMIT 5")
    # Displaying the results
    for contact in contacts['records']:
        print(f"Contact ID: {contact['Id']}, Name: {contact['FirstName']} {contact['LastName']}, Email: {contact.get('Email', 'N/A')}")
except Exception as e:
    print(f"Error occurred: {str(e)}")
