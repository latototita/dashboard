from django import template

register = template.Library()

@register.filter(name='is_in_busket')
def is_in_busket(ads  , busket):
    keys = busket.keys()
    for id in keys:
        if int(id) == ads.id:
            return True
    return False;

 
@register.filter(name='busket_quantity')
def busket_quantity(ads  , busket):
    keys = busket.keys()
    for id in keys:
        if int(id) == ads.id:
            return busket.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(ads  , busket):
    try:
        if User.objects.filter(prime_user=True):
            return int(ads.prime_price_per_click) * int(busket_quantity(ads , busket))
        else:
            pass
    except:
        if User.objects.filter(advance_prime_user=True):
            return int(ads.advance_prime_price_per_click) * int(busket_quantity(ads , busket))
        else:
            pass

@register.filter(name='total_busket_price')
def total_busket_price(adses , busket):
    sum = 0 ;
    for ad in adses:
        sum += int(price_total(ad , busket))
    return sum

@register.filter(name='total_busket_price_grand')
def total_busket_price_grand(adses , busket):
    sum = 0 ;
    for ad in adses:
        sum += int(price_total(ad , busket))
    return sum
    