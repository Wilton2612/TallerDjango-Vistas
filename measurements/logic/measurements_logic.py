from ..models import Measurement
from ..models import Variable

def get_measurements():
    medicion = Measurement.objects.all()
    return medicion

def get_measurement(var_pk):
    medicion = Measurement.objects.get(pk=var_pk)
    return medicion

def update_measurement(var_pk, new_var):
    medicion = get_measurement(var_pk)
    medicion.value = new_var["value"]
    medicion.save()
    return medicion

def create_measurement(var):
    variable = Variable(name=var["variable"])
    variable.save()
    medicion = Measurement(variable=variable,value=var["value"], unit=var["unit"], place=var["place"])
    medicion.save()
    return medicion

def delete_measurement(var_pk):
    medicion = Measurement.objects.get(pk=var_pk)
    medicion.delete()
    return  medicion