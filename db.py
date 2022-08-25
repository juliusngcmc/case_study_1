from models import SensorEODValue


def sensor_eod_value(**kwargs):
    SensorEODValue.create(
        sensor_ticker=kwargs['stock_ticker'],
        eod_date=kwargs['eod_date'],
        open_value=kwargs['open_value'],
        eod_value=kwargs['eod_value']
    )
    pass


class CreateRecord:
    pass


class UpdateRecord:
    def sensor_eod_value(self):
        pass


class DeleteRecord:
    def sensor_eod_value(self):
        pass


class ReadRecord:
    def sensor_eod_value(self):
        pass
