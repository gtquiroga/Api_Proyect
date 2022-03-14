# Api_Proyect

The API allows to get all cars information of a manufacturer and create new cars.

## Installing
After clonoing the repository
```
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## API

### Get /?name={manufacrurer name}
Given a manufacacturer name, return al car models and cars of that manufacturer.


    GET http://127.0.0.1:8000/?name=Mitsubishi

### POST /
It recived a json with manufacturer, car models and cars, creating the cars. If manufacturer or car model dont exist they are created and also the cars.

    POST http://127.0.0.1:8000/
      {
        "name": "Mitsubishi",
        "carmodel_set":[{
            "name": "L200",
            "production_year": 2011,
            "car_set":[{
                "manufacturing_date": "2020-02-02"
            }]
        },
        {
            "name": "Triton",
            "production_year": 2011,
             "car_set":[{
                "manufacturing_date": "2020-07-02"
            }]
        }]
    }
    
    
