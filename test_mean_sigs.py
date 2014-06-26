from mean_sightings import get_sighting

filename = 'sighting_tab_sm.csv'

'''all values take from data file sighting_tab_sm.csv'''

def test_water_is_correct():
	watrec,watmean = get_sighting(filename,'Water')
	assert watrec==2, 'Numer of records for water is wrong'
	assert watmean==17, 'Value of water mean is wrong'

def test_clay_is_correct():
        clayrec,claymean = get_sighting(filename,'Clay')
        assert clayrec==2, 'Numer of records for clay is wrong'
        assert claymean==25.5, 'Value of clay mean is wrong'
