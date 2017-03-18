while True:
    import random 
    print ('Shell Shock - Cold War')
    print ('Copyright Tuvnes Studios 2017')
    country = input ('Do you want: United States or Soviet Union')
    if country == 'United States':
        print ('1952')
        print ('Military Adviser: Sir our scientists have discovered a new bomb they call it the Hydgreon bomb.')
        print ('Will You Fund the Plan?')
        HBomb=input ('Yes or No')
        if HBomb == 'Yes':
            print ('Military Advisor: Very Well.')
        elif HBomb == 'No':
            print ('Military Advisor: My Apologises.')
        print ('1955')
        print ('Military Advisor: Sir, North Korea and The U.S.S.R have invaded the South!')
        Korea = input ('Will you get involved?: Yes or No')
        if Korea == 'Yes':
            ran = random.randint(1,100)
            if ran >40:
                print ('Diplomatic Advisor: North Korea has taken Control of the Korean area.')
                print ('Military Advisor: This is a Dark Day for The American Dream.')
            elif ran >40:
                print ('Diplomatic Advisor: The South Korean Goverment has won the war for Korea.')
                print ('INCOMING MESSAGE FROM The Democratic Korean Government: Thank You for the support we are forever greatful')
        if Korea == 'No':
            print ('INCOMING MESSAGE FROM The Soviet Union: South Korea Surrendered without much effot.')
        print ('1957')
        print ('NASA: Mr.Kenady, The USSR has sent a probe into space.')
        print ('1965')
        print ('Military Advisor: Sir, The Asian Nation of VIETNAM has recently had a comunist revoloution')
        Vietnam = input ('Will You begin the Vietnam war: Yes or No')
        if Vietnam == 'Yes':
            print ('Finacial Advisor: Sir, The War in Vietnam is draing our Money')
            print ('Finacial Advisor: The Annual GDP report has arrived')
            print ('Top GDPs')
            print ('1st USSR 12.3 Trillion')
            print ('2nd China 9.5 Trillion')
            print ('3rd Korea 2.2 Trillion')
            print ('4th Japan 1.2 Trillion')
            print ('5th USA 950 Billion')
            Viet = random.randint(1,100)
            if Viet >50:
                print ('Military Advisor: Unfortunatly Sir, The Damn Commies took Vietnam.')
                print ('Top GDPs')
                print ('1st China 22.8 Trillion')
                print ('2nd Korea 16.2 Trillion')
                print ('3rd USSR 13.0 Trillion')
                print ('4th Japan 11.9 Trillion')
                print ('5th ***** *** Trillion')
                print('6th ***** *** Trillion')
                print ('7th Vietnam 878.3 Billion')
                print ('8th USA 766.6 Billion')
                print('9th ***** *** Billion')
                print ('10th Canada 756.1 Billion')
            if Viet <50:
                print ('Military Advisor: Sir,Vietnam has been librated by the Us.')
                print ('Finacial Advisor: Mr.Nixon Due to the sucess of the war in Vietnam the Country is now 2nd Best GDP.')
                print ('Top GDPs')
                print ('1st China 22.8 Trillion')
                print ('2nd USA 18.9 Trillion')
                print ('3rd Korea 16.2 Trillion')
                print ('4th USSR 13.0 Trillion')
                print ('5th Vietnam 12.2 Trillion')
            print ('1966')
            print ('NASA: Mr. Johnson, We need to one up the USSR and land a man on the Moon.')
            Moon = input ('Will you fund the Space Race? Yes or No ')
            if Moon == 'Yes':
                print ('FBI: Our Special Branch has given us infomation that the USSR plans to land on the moon by 1970-75.')
            print ('1969')
            Space =  random.randint(1,100)
            if Space >45:
                print ('NASA: Sir... The USSR has landed the first man on the moon...')
            elif Space <45:
                ('INCOMING TRANSMISION FROM The Moon: Its One Small Step for man, One Giant Leap for mankind.')
            elif Moon == 'No':
                ('NASA: Thats A Shame...')
        print ('1990')
        print ('Diplomatic Advisor: Mr Bush Sir, Germany has been reunited after 45 years of separation.')
        print ('1991')
        print ('Capiltalism has won over comunism and the USSR has colapsed!!!')
        break
######################################################################################
    if country == 'Soviet Union':
        print ('1955')
        print ('Sir, We belive the Nation of Korea with its unstable government a comunist revolution may be a good idea.')
        Korea2 = ('Will you invoke a coupe in Korea: Yes/No')
        if Korea2 == 'Yes':
            Korea3 = random.randint(1,100)
            if Korea3  >50:
                print ('Sir, The Soivet State of Korea has been created')
                print ('Military Advisor: Our Power over korea has given us great holdings in the league of Nations.')
            elif Korea3  >10:
                print ('Diplomatic Advisor: The USA have called for a cease fire and they have split the Nation.')
            elif Korea3 <50:
                print ('Military Advisor: The US have taken control of the Korean area.')
        elif Korea2 == 'No':
            print ('Military Advisor: I see you have no intrests in Korea.')
        print ('1961')
        print ('Foriegn affairs Advisor: Our Section of Berlin needs protection')
        BWall = input('Will you build the berlin wall?: Yes/No')
        if BWall == 'Yes':
            print ('INCOMING MESSAGE FROM West Germany: I feel rather threated')
        elif BWall =='No':
            print ('Foriegn affairs advisor: Very Well...')
        print ('1965')
        print ('Military Advisor:')
        
    
        
