from os.path import basename, join
from urllib.parse import urlsplit

from requests import get


def download_url(url, directory_path):

    file_path = join(directory_path, basename(urlsplit(url).path))

    print(f"{url} =(download)=> {file_path} ...")

    with open(file_path, "wb") as io:

        io.write(get(url, allow_redirects=True).content)

    return file_path