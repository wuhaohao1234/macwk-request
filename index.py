import requests

url = 'https://tpi.macwk.com/api/items/soft?meta=total_count%2Cfilter_count&sort=-modified_on&offset=0&limit=100&filter%5Bperfect%5D%5Beq%5D=1&fields=icon.filename_disk.%2A%2Cmodified_on%2Cslug%2Cos_version%2Cversion%2Ctitle%2Ctitle_des%2Cdescription%2Csize%2Ciscrack%2Clanguage%2Cgallery.gallery_id.filename_disk.%2A&status=published'

res = requests.get(url)

f = open('./text.json', 'w')

f.write(res.text)

f.close()