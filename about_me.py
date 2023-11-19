import valorant, requests, time, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = None
bio_set = False

while True:
    try:
        session = valorant.LocalClient().get_session()
        name = session.get('game_name')
        tag = session.get('game_tag')
        region = session.get('region')
        region = None

        if session.get('state') != 'connected':
            print('Not logged in')
            bio_set = False
            time.sleep(5)
            continue

            requests.patch(url='https://discord.com/api/v9/users/@me', 
                           headers={'authorization': '<token>'},
                           json={'bio': f'> valorant -\n> main: **<main>** (EU)\n> logged into: **{name}#{tag}** ({region})'})
            print('Bio set')
            print(session)
            bio_set = True
    except:
        print('Valorant not open')
        bio_set = False
    time.sleep(5)
