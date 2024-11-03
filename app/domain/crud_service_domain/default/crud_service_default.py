from app.domain.crud_service_domain.crud_service_base import CrudServiceBase
from app.factories import domain_factory


@domain_factory.register("crud_default")
class CrudServiceDefault(CrudServiceBase):
    pass
