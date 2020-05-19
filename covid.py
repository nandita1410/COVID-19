from covid import Covid
covid= Covid()
"""
def covid_worldwdie():
    print(covid.get_total_active_cases())
    print(covid.get_total_confirmed_cases())
    print(covid.get_total_recovered())
    print(covid.get_total_deaths())
covid_worldwdie()
"""
#for particular country
india= covid.get_status_by_country_name("india")
data={ key: india[key]
       for key in india.keys() and {'confirmed', 'active', 'deaths', 'recovered'}
       
}
print(data)
