import os
import requests
from flask import Flask, Response

app = Flask(__name__)

M3U_URL = os.getenv("M3U_URL")


def modify_m3u_content(content):
    lines = content.splitlines()
    modified_lines = []
    for line in lines:
        if line.startswith("#EXTINF"):
            # Modify the line to ensure the channel number is set to 0 while preserving other metadata
            if "tvg-chno" in line:
                line = line.replace(line.split('tvg-chno="')[1].split('"')[0], "0")
            else:
                line = line.replace(line.split(":")[1].split(",")[0], "0")
        modified_lines.append(line)
    return "\n".join(modified_lines)


@app.route("/m3u")
def get_modified_m3u():
    response = requests.get(M3U_URL)
    if response.status_code == 200:
        modified_content = modify_m3u_content(response.text)
        return Response(modified_content, mimetype="application/x-mpegURL")
    else:
        return Response("Failed to fetch M3U file", status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5020)
