from location import Location
from place import Place

center = Location('Center')
Shev_d = Location('Shevchenkivskyi District')
Lych_d = Location('Lychakivskyi District')
Sykh_d = Location('Sykhiv District')
Fran_d = Location('Frankivskyi District')
Zali_d = Location('Zaliznychnyi District')

center.set_description('This area is full of different cafes, \
restaurants and peoples. Your friends like to spend time here. \
Try to visit "100 Rentgen" it is their favourite place!')
Shev_d.set_description("This area is full of your enemies. \
Also, your friend Ivan lost here in the last year, so you'd better be careful. ")
Lych_d.set_description('You always want to visit Lychakivskyi cemetery. \
Maybe you should try to do it today?')
Sykh_d.set_description('A lot of bullies live here. Also, there is market Shuvar and church \
where you can meet seminary student')
Fran_d.set_description('It is a beautiful and quiet district. \
UCU is located here, also, you may visit Stryiskyi park if you want. ')
Zali_d.set_description('Your main destination - the train station is located here')

ren = Place('100 Rentgen', 'pab')
po = Place('36po', 'restaurant')
piz = Place('Chelentano', 'restaurant')
ital = Place('Italian Courtyard', 'famous place')
center.set_places([ren, po, piz, ital])

club = Place("ADAM Gentlemen's Club", 'club')
house = Place('Abandoned house', 'house')
Shev_d.set_places([club, house])

cemetery = Place('Lychakivskyi cemetery', 'cemetery')
Lych_d.set_places([cemetery])

church = Place('Church', 'church')
market = Place('Shuvar', 'market')
Sykh_d.set_places([church, market])

ucu = Place('UCU', 'university')
park = Place('Stryiskyi park', 'park')
koleg = Place('Kolegium', 'home')
Fran_d.set_places([ucu, park, koleg])

station = Place('Vokzal', 'train station')
cafe = Place('Beer and varenyky', 'cheep cafe')
Zali_d.set_places([station, cafe])



