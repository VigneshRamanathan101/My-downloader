from tqdm import tqdm 
import requests

chunk_s=1024*1024


url=input("Enter URL: " ).strip()
r=requests.get(url,stream=True)
print('-'*100)


total_length=int(r.headers.get('content-length'))
print(url.split('/'))

file_name=input("Enter file name: ")+'.'+input("Enter file extension without '.' :")
print('file_name:',file_name)
print('-'*100)
print()


with open(file_name,'wb') as f:
    for chunk in tqdm(iterable=r.iter_content(chunk_size=chunk_s),total=total_length/chunk_s,unit='MB'):
        f.write(chunk)

print("Download Sucessful")
print('-'*100)
