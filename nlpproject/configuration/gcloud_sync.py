'''

import os

class GCloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url,filepath,filename):

        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"                            #To upload files to gcloud
        # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"

    def sync_folder_from_gcloud(self,gcp_bucket_url,filename,destination):

        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        #command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"      #To download files from gcloud 

        os.system(command)



        
'''        
# Run this code when having a gooogle cloud account

'''
Running these file commands
from nlpproject.configuration.gcloud_sync import GcloudSync

obj = GcloudSync()

To download files
obj.sync_folder_from_gcloud("#Project from which copied","Filename_from _cloud","Name_of_local_filename")

'''