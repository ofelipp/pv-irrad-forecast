"""
Program to forecast radiance curve for Brazilian energy system, located in
Santo Andre. The data are retrieved from SEMASA meteorologic stations and UFABC
Solar Project.

Author: ofelippm (felippe.matheus@aluno.ufabc.edu.br)
"""

from ports.inbound.poller import Poller
from ports.inbound.forecast_use_case import ForecastUseCase
from dependency_injection import DependencyInjection


class Main:
    def __init__(self, poller: Poller, forecaster: ForecastUseCase):
        self.poller = poller
        self.forecaster = forecaster

    def run_forecast(self):
        while self.poller.have_job("queue"):
            job = self.poller.get_job("queue")
            print(f"Job: {job}")

            forecast = self.forecaster.predict(features=job)
            print(f"Forecast: {forecast}")


if __name__ == "__main__":
    dep_inj = DependencyInjection()

    main = Main(poller=dep_inj.poller, forecaster=dep_inj.forecaster)
    main.run_forecast()
