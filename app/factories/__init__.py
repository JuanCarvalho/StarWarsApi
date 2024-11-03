from app.factories.domain_factory import DomainFactory
from app.factories.ports_factory import PortFactory
from app.factories.repository_factory import RepositoryFactory
from app.factories.rest_api_factory import ApiRestFactory

port_factory = PortFactory()
api_rest_factory = ApiRestFactory()
repository_factory = RepositoryFactory()
domain_factory = DomainFactory()
