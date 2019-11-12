import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='./hotel-09dc42379e26.json'
import json
from google.cloud import storage as gcs

def load_db(dbname):
    bucket_name = "raspberrydata"
    fname = dbname
    #project_name = "rare-ethos-255804"
    project_name = "hotel"

    client = gcs.Client(project_name)
    bucket = client.get_bucket(bucket_name)
    blob = gcs.Blob(fname, bucket)
    content = blob.download_as_string()
    dat2=content.decode("utf-8")
    with open(dbname,"wt") as fp:
        fp.write(dat2)
    #dat3=json.loads(dat2)

def save_db(dbname):
    print("-- in gcs_lib --")
    bucket_name = "raspberrydata"
    fname = dbname
    #project_name = "rare-ethos-255804"
    project_name = "hotel"

    print(dbname)
    
    client = gcs.Client(project_name)
    bucket = client.get_bucket(bucket_name)
    blob = gcs.Blob(fname, bucket)
    blob = bucket.blob(fname)
    blob.upload_from_filename(filename="./"+dbname)

def lsdb():
    project_name = "hotel"
    client = gcs.Client(project_name)

    bucket = client.get_bucket('raspberrydata')
    blobs = bucket.list_blobs(prefix="", delimiter="/")
#    blobs = bucket.list_blobs(delimiter="/")

    dirs = []
    for page in blobs.pages:
        dirs.extend(page.prefixes)
    print(dirs)



if __name__ == "__main__":
    lsdb()
