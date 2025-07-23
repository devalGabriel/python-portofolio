from datetime import datetime
import uuid

def generate_transaction_id():
    return f"TXN-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6]}"
