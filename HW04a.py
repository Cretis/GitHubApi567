import json
import requests


def get_git_hub(a):
    rep = []
    result = []
    i = a
    url1 = f'https://api.github.com/users/' + i + '/repos'
    response = requests.get(url1)
    answer = response.json()
    for r in answer:
        rep.append(r['name'])
    for k in rep:
        url2 = f'https://api.github.com/repos/' + i + '/' + k + '/commits'
        res = requests.get(url2)
        asn = res.json()
        result.append(f'Repo:' + k + ' Number of commits: ' + str(len(asn)))
    return result


if __name__ == '__main__':
    for item in get_git_hub('Cretis'):
        print(item)
