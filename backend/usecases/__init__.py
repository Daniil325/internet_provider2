from dishka import Provider, Scope, provide

from .client import CreateClientCommand, LoginClientCommand
from .tariff import CreateTariffCommand, UpdateTariffCommand, DeleteTariffCommand
from .payment import CreatePaymentCommand
from .chosen_tariff import CreateChosenTariffCommand


class CommandsProvider(Provider):
    scope = Scope.REQUEST
    
    create_client_command = provide(CreateClientCommand)
    login_client_command = provide(LoginClientCommand)
    
    create_tariff_command = provide(CreateTariffCommand)
    update_tariff_command = provide(UpdateTariffCommand)
    delete_tariff_command = provide(DeleteTariffCommand)
    
    create_payment_command = provide(CreatePaymentCommand)
    
    create_chosen_tariff_command = provide(CreateChosenTariffCommand)
