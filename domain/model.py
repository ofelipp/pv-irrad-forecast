from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from domain.data import Data


@dataclass
class Model(ABC):
    model: object
    name: str
    description: str = field(default=None)

    @abstractmethod
    def train(self, features: Data, labels: Data):
        raise NotImplementedError

    @abstractmethod
    def predict(self, features: Data) -> Data:
        raise NotImplementedError


@dataclass
class LinearRegressionModel(Model):

    def train(self, features: Data, labels: Data):
        self.model.fit(features, labels)

    def predict(self, features: Data) -> Data:
        return Data(
            data=self.model.predict(features.data),
            name=f"prediction_{self.name}",
            details=" ".join([
                    f"Predictions made by Linear Regression Model {self.name}",
                    f"using data {features.name}",
            ]),
        )


class TreeModel(Model):

    def train(self, features: Data, labels: Data):
        print(f"Model {self.name} was trained")

    def predict(self, features: Data) -> Data:
        return Data(
            data=self.model.predict(features.data),
            name=f"prediction_{self.name}",
            details=" ".join([
                    f"Predictions made by Linear Regression Model {self.name}",
                    f"using data {features.name}",
            ]),
        )


class DecisionTreeModel(Model):

    def train(self, features: Data, labels: Data):
        print(f"Model {self.name} was trained")

    def predict(self, features: Data) -> Data:
        return Data(
            data=self.model.predict(features.data),
            name=f"prediction_{self.name}",
            details=" ".join([
                    f"Predictions made by Linear Regression Model {self.name}",
                    f"using data {features.name}",
            ]),
        )


class RandomForestModel(Model):

    def train(self, features: Data, labels: Data):
        print(f"Model {self.name} was trained")

    def predict(self, features: Data) -> Data:
        return Data(
            data=self.model.predict(features.data),
            name=f"prediction_{self.name}",
            details=" ".join([
                    f"Predictions made by Linear Regression Model {self.name}",
                    f"using data {features.name}",
            ]),
        )


class NeuralNetworkModel(Model):

    def train(self, features: Data, labels: Data):
        print(f"Model {self.name} was trained")

    def predict(self, features: Data) -> Data:
        return Data(
            data=self.model.predict(features.data),
            name=f"prediction_{self.name}",
            details=" ".join([
                    f"Predictions made by Linear Regression Model {self.name}",
                    f"using data {features.name}",
            ]),
        )
