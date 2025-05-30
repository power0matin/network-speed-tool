import speedtest

def run_speed_test():
    try:
        st = speedtest.Speedtest()
        
        # انتخاب بهترین سرور
        st.get_best_server()
        
        # بررسی اطلاعات سرور
        server_info = st.results.server
        # print("Server Info:", server_info)  # چاپ اطلاعات سرور برای اشکال زدایی
        
        # دریافت سرعت دانلود و آپلود
        download_speed = st.download() / 1e+6  # تبدیل به Mbps
        upload_speed = st.upload() / 1e+6  # تبدیل به Mbps
        ping = st.results.ping
        
        # دریافت ID نتیجه از ویژگی 'id' سرور
        result_id = st.results.server.get('id', 'No data available')
        
        # چاپ نتایج برای اشکال زدایی
        # print(f"Download Speed: {download_speed} Mbps")
        # print(f"Upload Speed: {upload_speed} Mbps")
        # print(f"Ping: {ping} ms")
        
        return {
            "result_id": result_id,
            "download": download_speed,
            "upload": upload_speed,
            "ping": ping,
            "server": {
                "name": server_info.get("name", "No data available"),
                "location": server_info.get("country", "No data available"),
                "ip": server_info.get("host", "No data available")
            }
        }
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # چاپ خطا برای اشکال زدایی
        return {"error": str(e)}

def print_test_results():
    result = run_speed_test()
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("\nInternet Speed Test Results:")
        print("----------------------------")
        print(f"Result ID: {result['result_id']}")
        print(f"Download Speed: {result['download']:.2f} Mbps")
        print(f"Upload Speed: {result['upload']:.2f} Mbps")
        print(f"Ping: {result['ping']:.2f} ms")
        print("\nServer Info:")
        print("-------------")
        print(f"Server: {result['server']['name']}")
        print(f"Location: {result['server']['location']}")
        print(f"Server IP: {result['server']['ip']}")
        print("----------------------------")
        print("Test completed successfully!")

if __name__ == "__main__":
    print_test_results()
