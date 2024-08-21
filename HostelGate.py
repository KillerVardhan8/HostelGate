import datetime

# Define the hostel entry and exit times
ENTRY_TIME = datetime.time(6, 0) # 6:00 AM
EXIT_TIME = datetime.time(22, 0) # 10:00 PM

# Define the warden's contact information
WARDEN_PHONE = "0123456789"
WARDEN_EMAIL = "warden@hostel.com"

# Define the function for requesting permission
def request_permission():
    # Get the current time
    now = datetime.datetime.now().time()

    # Check if the current time is within the allowed entry time
    if now >= ENTRY_TIME and now <= EXIT_TIME:
        # If so, grant permission and alert the entry time
        entry_time = datetime.datetime.combine(datetime.date.today(), now)
        print("\n\nPermission granted.")
        print("Please enter the hostel before\n", entry_time + datetime.timedelta(hours=1))
    else:
    # If not, deny permission and provide contact information for the warden
        print("Permission denied. Please contact the warden for assistance.")
        print("Phone:", WARDEN_PHONE)
        print("Email:", WARDEN_EMAIL)

# Test the function with some example times
while(1):
    ask=int(input("\nEnter 1 for Request Permission :"))
    if ask==1:
        request_permission()
    else:
        break

