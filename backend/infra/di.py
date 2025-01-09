from dishka import Provider, Scope, provide

from .database import SqlChosenTariffRepo, SqlClientRepo, SqlPaymentRepo, SqlTariffRepo


class SqlProvider(Provider):
    scope = Scope.REQUEST

    def __init__(self, session) -> None:
        super().__init__()
        self.session = session()

    @provide
    def get_client_repo(self) -> SqlClientRepo:
        return SqlClientRepo(self.session)
    
    @provide
    def get_tariff_repo(self) -> SqlTariffRepo:
        return SqlTariffRepo(self.session)
    
    @provide
    def get_paymet_repo(self) -> SqlPaymentRepo:
        return SqlPaymentRepo(self.session)
    
    @provide
    def get_chosen_tariff_repo(self) -> SqlChosenTariffRepo:
        return SqlChosenTariffRepo(self.session)
