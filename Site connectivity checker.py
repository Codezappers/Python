import urllib.request as urllib

def main (url):
    print('Checking the site connectivity...')
    response = urllib.urlopen(url)
    print('Site is up and running')
    print('Status code: ', response.getcode())

print('Site connectivity checker')
print('Enter the site URL: ')
url = input()

main(url)

    