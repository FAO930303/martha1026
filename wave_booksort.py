import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

collection_ref = db.collection("精選圖書列表")
docs = collection_ref.order_by("anniversary",direction=firestore.Query.DESCENDING).limit(3).get()
for doc in docs:
    print("文件內容：{}".format(doc.to_dict()))
