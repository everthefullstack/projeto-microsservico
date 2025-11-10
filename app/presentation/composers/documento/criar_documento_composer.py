from app.infra.configurations.settings import settings
from app.infra.engine.engine import EngineManager
from app.infra.session.session import SessionManager
from app.infra.repoositories.documento_repository import DocumentoRepository
from app.infra.unit_of_work.documento import DocumentoUnitOfWork
from app.application.use_cases.criar_documento import CriarDocumentoUseCase
from app.presentation.controllers.documento.criar_documento_controller import CriarDocumentoController


class CriarDocumentoControllerComposer:

    @staticmethod
    def compose():
        
        engine = EngineManager(settings=settings)
        session = SessionManager(engine=engine).get_session()
        repository = DocumentoRepository()
        unit_of_work = DocumentoUnitOfWork(session=session, documento_repository=repository)
        use_case = CriarDocumentoUseCase(unit_of_work=unit_of_work)
        controller = CriarDocumentoController(criar_documento_use_case=use_case)

        return controller
