'''
covid.py - Phenny Coronavirus Module
'''

import web

@web.with_scraped_page_no_cache('https://www.worldometers.info/coronavirus/')
def scrape_stats(doc):
    elements = doc.find_class('maincounter-number')
    return ( i.text_content().strip() for i in elements )

def covid(phenny, input):
    phenny.say('Loading COVID-19 statistics...')
    cases, deaths, recovered = scrape_stats()
    current = format(int(cases.replace(',', '')) - ( int(deaths.replace(',', '')) + int(recovered.replace(',', '')) ), ',d')
    phenny.say('Cases: {}'.format(cases))
    phenny.say('Current: {}'.format(current))
    phenny.say('Deaths: {}'.format(deaths))
    phenny.say('Recovered: {}'.format(recovered))
    phenny.say('Recovery rate: {}%'.format(round(int(recovered.replace(',', ''))/int(cases.replace(',', '')) * 10000) / 100))
    phenny.say('Death rate: {}%'.format(round(int(deaths.replace(',', ''))/int(cases.replace(',', '')) * 10000) / 100))
    phenny.say('Recoveries/Deaths: {}'.format(round(int(recovered.replace(',', ''))/int(deaths.replace(',', '')) * 100 ) / 100 ))
    phenny.say('This is not medical advice.')

    
covid.commands = ['covid', 'covid19', 'coronavirus', '2019ncov', 'sarscov2', 'corona', 'pandemic']
covid.example = '.covid'
covid.priority = 'medium'
