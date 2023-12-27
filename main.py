"""
Program to forecast radiance curve for Brazilian energy system, located in
Santo Andre. The data are retrieved from SEMASA meteorologic stations and UFABC
Solar Project.

Author: ofelippm (felippe.matheus@aluno.ufabc.edu.br)
"""
from ports.inbound.poller_use_case import PollerUseCase
from ports.inbound.forecast_use_case import ForecastUseCase
from dependency_injection import DependencyInjection

import dotenv
dotenv.load_dotenv()


class Main:
    def __init__(self, poller: PollerUseCase, service: ForecastUseCase):
        self.poller = poller
        self.service = service

    def run_forecast(self):
        while self.poller.have_job("queue"):
            job = self.poller.get_job("queue")
            print(f"Job: {job}")

            forecast = self.service.predict(features=job)
            print(f"Forecast: {forecast.as_dict()}")


if __name__ == "__main__":
    dep_inj = DependencyInjection()

    main = Main(poller=dep_inj.poller, service=dep_inj.service)
    main.run_forecast()
