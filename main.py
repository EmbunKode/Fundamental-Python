import requests

print('Hello World!')
try:
    r = requests.get('https://goog le.com')
    print(r.status_code)
    # Jika status 200 maka berhasil dan tampilkan text dari url google.com
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    # text jika terjadi error
    print('Ada Error', e)