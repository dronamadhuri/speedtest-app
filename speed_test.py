import speedtest

print("Checking Internet Speed...")

st = speedtest.Speedtest()

download_speed = st.download() / 1_000_000  # Convert to Mbps
upload_speed = st.upload() / 1_000_000      # Convert to Mbps
ping = st.results.ping

print("Download Speed:", round(download_speed, 2), "Mbps")
print("Upload Speed:", round(upload_speed, 2), "Mbps")
print("Ping:", round(ping, 2), "ms")