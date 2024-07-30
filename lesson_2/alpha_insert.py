def alpha_insert(list_of_countries, country):
    if country in list_of_countries:
        return list_of_countries

    if len(list_of_countries) == 0:
        list_of_countries.append(country)
        return list_of_countries

    list_of_countries.append(country)
    list_of_countries.sort()
    return list_of_countries

countries = ['Australia', 'Cuba', 'Scotland']

alpha_insert(countries, 'Brazil')
print(', '.join(countries))

alpha_insert(countries, 'Australia')
print(', '.join(countries))

countries = alpha_insert([], 'Brazil')
print(', '.join(countries))

countries = alpha_insert(['Australia', 'Cuba', 'Scotland'], 'Brazil')
print(', '.join(countries))