from datetime import datetime

def lambda_handler(event, context):
    time = datetime.now()
    print(time)
