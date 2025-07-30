from jinja2 import Environment, FileSystemLoader, Template
from weasyprint import HTML
from typing import Optional
import os


class PDFExport:
    def __init__(self, template_path: Optional[str] = None):
        """
        template_path: Ruta al archivo de plantilla HTML. Si no se especifica,
                       se usará una plantilla por defecto ubicada en ./templates/default_template.html
        """
        if template_path is None:
            base_path = os.path.dirname(__file__)
            self.template_path = os.path.join(
                base_path, "templates", "default_template.html"
            )
        else:
            self.template_path = template_path

        if not os.path.exists(self.template_path):
            raise FileNotFoundError(
                f"Plantilla HTML no encontrada: {self.template_path}"
            )

        self.env = Environment(
            loader=FileSystemLoader(os.path.dirname(self.template_path))
        )
        self.template = self.env.get_template(os.path.basename(self.template_path))

    def render(self, data: dict) -> bytes:
        """
        Renderiza la plantilla con los datos proporcionados y genera el PDF en memoria (como bytes).
        No lo guarda automáticamente.
        """
        html_content = self.template.render(data)
        pdf = HTML(string=html_content).write_pdf()
        return pdf  # tipo: bytes

    def save(self, pdf_bytes: bytes, output_path: str):
        """
        Guarda el PDF en disco.
        - pdf_bytes: contenido PDF generado por el método render()
        - output_path: ruta completa donde se guardará el archivo, incluyendo el nombre del archivo.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(pdf_bytes)
