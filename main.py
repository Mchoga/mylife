import speedtest


def test_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10 ** 6
    upload_speed = st.upload() / 10 ** 6
    ping = st.results.ping

    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")


if __name__ == '__main__':
    test_speed()
