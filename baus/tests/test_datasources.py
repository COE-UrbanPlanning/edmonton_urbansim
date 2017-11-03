from .. import datasources


def test_limits_settings():
    limits_settings = {
        "default": {
            "Residential": {
                "city1": 100,
                "city2": 200
            },
        }, "foo": {
            "Residential": {
                "city1": 50
            },
            "Office": {
                "city3": 12
            }
        }
    }
    out = datasources.limits_settings({"development_limits": limits_settings},
                                      "foo")
    assert out["Residential"]["city1"] == 50
    assert out["Residential"]["city2"] == 200
    assert out["Office"]["city3"] == 12


def test_inclusionary_housing_settings():
    inclusionary_housing_settings = {
        "foo": [{
            "amount": .2,
            "values": [
                "Edmonton"
            ]
        }, {
            "amount": .1,
            "values": [
                "Edmonton"
            ]
        }]
    }
    out = datasources.inclusionary_housing_settings({
        "inclusionary_housing_settings": inclusionary_housing_settings
    }, "foo")

    assert out["Edmonton"] == .2
