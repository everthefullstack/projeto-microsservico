from dataclasses import dataclass
from app.infra.interfaces.session_interface import SessionInterface
from app.application.interfaces.unit_of_work_interface import UnitOfWorkInterface
from app.application.interfaces.documento_interface import DocumentoRepositoryInterface


@dataclass(slots=True)
class DocumentoUnitOfWork(UnitOfWorkInterface):

    session: SessionInterface
    documento_repository: DocumentoRepositoryInterface

    def __enter__(self) -> "UnitOfWorkInterface":

        self.documento_repository.session = self.session
       
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self.session.commit()

        else:
            self.session.rollback()

        self.session.close()
