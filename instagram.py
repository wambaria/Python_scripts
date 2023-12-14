import instaloader
import os
import logging

def download_instagram(username, folder_path, log_file_path):

    #create the directory for long file if it does not exist
    log_dir = os.path.dirname(log_file_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(filename=log_file_path, level=logging.INFO)
    logging.info("Instagram download started for user: %s", username)

    try:
        instagram_loader= instaloader.Instaloader()
        profile = instaloader.Profile.from_username(instagram_loader.context, username)

        # Create the download folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Download the profile's posts 
        instagram_loader.download_profile(profile.username, profile_pic_only=False)

        logging.info("Instagram download completed successfully.")
    except Exception as e:
        logging.error("Error during Instagram download: %s", str(e))

if __name__ == "__main__":
    username = "itsmureithi"
    folder_path = "c:\\Users\\LENOVO\\Desktop"
    log_file_path = "path/to/logfile.log"

    download_instagram(username, folder_path, log_file_path)
