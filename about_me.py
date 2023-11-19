import valorant, requests, time, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = None
bio_set = False

while True:
    try:
        session = valorant.LocalClient().get_session()
        name = session.get('game_name')
        tag = session.get('game_tag')
        region = None

        if session.get('state') != 'connected':
            print('Not logged in')
            bio_set = False
            time.sleep(5)
            continue
        if bio_set == False:
            if name == 'ollie':
                region = 'NA'
            else:
                region = 'EU'

            requests.patch(url='https://discord.com/api/v9/users/@me', 
                           headers={'authorization': 'OTAxNjk4OTQ0NjI5ODkxMDcz.G15dnT.0uLX29OoNFIYPS9karnQMyrxiCiGMB6mj_B068'},
                           json={'bio': f'https://myanimelist.net/animelist/SpaceTjabo\n\nvalorant -\nmain: **tjabo#meow** (EU)\nlogged into: **{name}#{tag}** ({region})'})
            print('Bio set')
            print(session)
            bio_set = True
    except:
        print('Valorant not open')
        bio_set = False
    time.sleep(5)